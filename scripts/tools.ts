import { existsSync } from 'node:fs'
import { basename, resolve, relative } from 'node:path'
import { toolSchema } from '../src/lib/content/schema.ts'
import { markdownFiles, frontmatter } from './markdown.ts'

export function buildTools(root: string) {
  const directory = resolve(root, 'content/tools')
  const files = existsSync(directory) ? markdownFiles(directory) : []
  const ids = new Set<string>(), urls = new Set<string>()
  return files.map(file => {
    const result = toolSchema.safeParse(frontmatter(file))
    if (!result.success) throw new Error(`${relative(root, file)}: ${result.error.message}`)
    const tool = result.data
    if (ids.has(tool.id)) throw new Error(`Duplicate tool ID: ${tool.id}`)
    ids.add(tool.id)
    if (basename(file, '.md') !== tool.id) throw new Error(`${file}: tool filename must match id`)
    const canonical = new URL(tool.url)
    canonical.hash = ''
    const identity = canonical.href.replace(/\/$/, '')
    if (urls.has(identity)) throw new Error(`Duplicate tool URL: ${tool.url}`)
    urls.add(identity)
    return tool
  }).sort((a, b) => a.order - b.order || a.id.localeCompare(b.id))
}
