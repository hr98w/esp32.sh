import { manufacturerSearchNames } from './manufacturers'
import type { Device } from './content/schema'

const normalize = (value: string) => value.normalize('NFKC').toLowerCase().replace(/[\s_.-]+/g, '')

/** Match separate keywords while tolerating common model punctuation. */
export function matchesQuery(query: string, fields: readonly string[]) {
  const tokens = query.trim().split(/\s+/).map(normalize).filter(Boolean)
  const searchable = fields.map(normalize)
  return tokens.every(token => searchable.some(field => field.includes(token)))
}

export function deviceSearchFields(device: Device) {
  return [device.name, device.id, device.chip, ...manufacturerSearchNames(device.manufacturer).flatMap(name => [name, name + ' ' + device.name]), ...device.aliases,
    // M5Core2 / M5Cardputer are common search spellings of M5Stack products.
    ...(device.manufacturer.id === 'm5stack' ? ['M5' + device.name.replace(/^M5/i, '')] : []),
  ]
}
