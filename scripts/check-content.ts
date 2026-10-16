import { buildCatalog } from './content.ts'

try {
  const catalog = buildCatalog(process.cwd(), process.argv.includes('--write'))
  console.log(`Content valid: ${catalog.projects.length} projects, ${catalog.devices.length} devices.`)
} catch (error) {
  console.error(error instanceof Error ? error.message : error)
  process.exitCode = 1
}
