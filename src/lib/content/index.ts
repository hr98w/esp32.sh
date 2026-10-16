import data from '../../generated/catalog.json'
import type { Catalog } from './schema'

export const catalog: Catalog = data as Catalog
export const projectsForDevice = (id: string) => catalog.projects.filter((project) => project.devices.some((device) => device.deviceId === id))
