import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { resolve, dirname } from 'node:path'
import { stringify } from 'yaml'
import { deviceSchema, projectSchema } from '../src/lib/content/schema.ts'

const filename = process.argv[2]
if (!filename) throw new Error('Usage: node --import tsx scripts/write-records.ts <reviewed-records.json> [--replace]')
const records = JSON.parse(readFileSync(filename, 'utf8')) as { kind: 'project' | 'device'; data: unknown; note?: string }[]
let written = 0
for (const entry of records) {
  const record = entry.kind === 'project' ? projectSchema.parse(entry.data) : deviceSchema.parse(entry.data)
  const path = entry.kind === 'device' && 'manufacturer' in record
    ? `content/devices/${record.manufacturer.id}/${record.id}.md`
    : `content/projects/${record.id}.md`
  if (existsSync(path) && !process.argv.includes('--replace')) continue
  mkdirSync(dirname(resolve(path)), { recursive: true })
  const output = '---\n' + stringify(record) + '---\n\n' + (entry.note ?? '') + '\n'
  if (existsSync(path) && readFileSync(path, 'utf8') === output) continue
  writeFileSync(path, output)
  written++
}
console.log(`Wrote ${written} reviewed content records. Existing records are preserved unless --replace is explicit.`)
