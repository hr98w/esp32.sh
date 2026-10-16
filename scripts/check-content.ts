import { buildGuides } from './guides.ts'
import { buildTools } from './tools.ts'
import { buildCatalog } from './content.ts'

try {
  const catalog = buildCatalog(process.cwd(), process.argv.includes('--write'))
  const guides = buildGuides(process.cwd(), catalog)
  console.log(`Content valid: ${catalog.projects.length} projects, ${catalog.devices.length} devices, ${buildTools(process.cwd()).length} tools, ${guides.picks.length} guide picks, ${guides.posts.length} X posts.`)
} catch (error) {
  console.error(error instanceof Error ? error.message : error)
  process.exitCode = 1
}
