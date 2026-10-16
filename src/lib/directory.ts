import type { Catalog } from './content/schema'
import { matchesQuery, deviceSearchFields } from './search'

export type ProjectFilters = { q?: string; device?: string; tag?: string; sort?: 'stars' | 'name' | 'newest' }
export type DeviceFilters = { type?: string; q?: string; maker?: string; chip?: string; feature?: string }

export function selectProjects(catalog: Catalog, search: ProjectFilters) {
  return catalog.projects.filter(project =>
    (!search.device || project.devices.some(device => device.deviceId === search.device)) &&
    (!search.tag || project.tags.includes(search.tag)) &&
    (!search.q || matchesQuery(search.q, [project.name, ...Object.values(project.summary), project.repository]))
  ).sort((a, b) => search.sort === 'newest'
    ? b.addedAt.localeCompare(a.addedAt) || a.name.localeCompare(b.name) || a.id.localeCompare(b.id)
    : search.sort === 'name' ? a.name.localeCompare(b.name) || a.id.localeCompare(b.id)
    : (b.metrics?.stars ?? -1) - (a.metrics?.stars ?? -1) || a.name.localeCompare(b.name) || a.id.localeCompare(b.id))
}

export function selectDevices(catalog: Catalog, search: DeviceFilters) {
  return catalog.devices.filter(d =>
    (!search.type || d.type === search.type) && (!search.maker || d.manufacturer.id === search.maker) &&
    (!search.chip || d.chip === search.chip) &&
    (!search.feature || d.features.includes(search.feature) ||
      (search.feature === 'display' && d.features.includes('epaper')) ||
      (search.feature === 'audio' && d.features.some(f => f === 'microphone' || f === 'speaker'))) &&
    matchesQuery(search.q ?? '', [...deviceSearchFields(d), ...Object.values(d.summary)])
  ).sort((a, b) => a.manufacturer.name.localeCompare(b.manufacturer.name) || a.name.localeCompare(b.name) || a.id.localeCompare(b.id))
}
