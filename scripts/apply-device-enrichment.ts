/** Apply reviewed facts and verified external images; preserve IDs, prose, and existing covers. */
import { readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { parse, stringify } from 'yaml'
import { deviceSchema } from '../src/lib/content/schema.ts'

const details = JSON.parse(readFileSync('data/collection/device-detail-review.json', 'utf8'))
const images = JSON.parse(readFileSync('data/collection/device-image-review.json', 'utf8'))
let updated = 0
for (const maker of readdirSync('content/devices', { withFileTypes: true }).filter(e => e.isDirectory())) {
  for (const file of readdirSync(`content/devices/${maker.name}`).filter(f => f.endsWith('.md'))) {
    const path = `content/devices/${maker.name}/${file}`
    const raw = readFileSync(path, 'utf8')
    const match = /^---\n([\s\S]*?)\n---([\s\S]*)$/.exec(raw)!
    const device = parse(match[1])
    const reviewed = details[device.id]
    if (reviewed) {
      for (const field of ['specifications', 'resources', 'sku', 'summary', 'features', 'revisionNotes', 'factoryFeatures', 'type']) {
        if (reviewed[field] !== undefined) device[field] = reviewed[field]
      }
      device.sources = [...(device.sources ?? []).filter((s: {url: string}) => !reviewed.sources?.some((r: {url: string}) => r.url === s.url)), ...(reviewed.sources ?? [])]
    }
    const image = images[device.id]
    if (image?.status === 'verified' && (!device.cover || device.cover === image.imageUrl || image.replaceCover === true)) {
      device.cover = image.imageUrl
      if (image.replaceCover && !device.gallery?.some((entry: {image: string}) => entry.image === image.imageUrl)) device.gallery = undefined
      device.gallery ??= [{ image: image.imageUrl, caption: {zh: `${device.name} 产品图`, en: `${device.name} product photo`, ja: `${device.name} 製品画像`}, sourceUrl: image.sourceUrl }]
    }
    deviceSchema.parse(device)
    const output = '---\n' + stringify(device, {lineWidth: 0}) + '---' + match[2]
    if (output !== raw) { writeFileSync(path, output); updated++ }
  }
}
console.log(`Updated ${updated} device Markdown files from reviewed evidence.`)
