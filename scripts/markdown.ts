import { readFileSync, readdirSync } from 'node:fs'
import { resolve } from 'node:path'
import { parseDocument } from 'yaml'

export function markdownFiles(directory: string): string[] {
  return readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const file = resolve(directory, entry.name)
    return entry.isDirectory() ? markdownFiles(file) : entry.isFile() && file.endsWith('.md') ? [file] : []
  }).sort()
}

export function frontmatter(file: string): unknown {
  const text = readFileSync(file, 'utf8').replace(/^\uFEFF/, '')
  const match = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/.exec(text)
  if (!match) throw new Error(`${file}: missing YAML frontmatter`)
  const document = parseDocument(match[1], { uniqueKeys: true })
  if (document.errors.length) throw new Error(`${file}: ${document.errors.map(error => error.message).join('; ')}`)
  return document.toJS()
}
