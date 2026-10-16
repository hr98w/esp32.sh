import { existsSync } from 'node:fs'
import { basename, resolve } from 'node:path'
import { guidePostSchema, guidePickSchema, type Catalog } from '../src/lib/content/schema.ts'
import { markdownFiles, frontmatter } from './markdown.ts'

export function buildGuides(root: string, catalog: Catalog) {
  function load<T extends { id: string; order: number }>(folder: string, parse: (data: unknown) => T): T[] {
    const directory = resolve(root, 'content/guides', folder)
    const ids = new Set<string>()
    return (existsSync(directory) ? markdownFiles(directory) : []).map(file => {
      const entry = parse(frontmatter(file))
      if (ids.has(entry.id)) throw new Error(`Duplicate guide ID: ${entry.id}`)
      if (basename(file, '.md') !== entry.id) throw new Error(`${file}: guide filename must match id`)
      ids.add(entry.id)
      return entry
    }).sort((a, b) => a.order - b.order || a.id.localeCompare(b.id))
  }
  const posts = load('posts', data => guidePostSchema.parse(data))
  const tweetIds = new Set<string>()
  for (const post of posts) {
    const identity = new URL(post.url).pathname.split('/').pop()!
    if (tweetIds.has(identity)) throw new Error(`Duplicate X post: ${post.url}`)
    tweetIds.add(identity)
  }
  const picks = load('picks', data => guidePickSchema.parse(data))
  for (const pick of picks) {
    for (const device of pick.deviceIds) if (!catalog.devices.some(d => d.id === device)) throw new Error(`${pick.id}: unknown guide device ${device}`)
    for (const project of pick.projectIds) if (!catalog.projects.some(p => p.id === project)) throw new Error(`${pick.id}: unknown guide project ${project}`)
  }
  return { posts, picks }
}
