import { readFileSync, mkdirSync, writeFileSync } from 'node:fs'
import { resolve, relative, dirname } from 'node:path'
import { markdownFiles, frontmatter } from './markdown.ts'
import { buildGuides } from './guides.ts'
import { buildTools } from './tools.ts'
import { z } from 'zod'
import { projectSchema, deviceSchema, repositoryMetricsSchema } from '../src/lib/content/schema.ts'
import type { Catalog } from '../src/lib/content/schema.ts'

/** Node-only build tooling. Workers consume the generated JSON, never the filesystem. */
export function buildCatalog(root = process.cwd(), write = false): Catalog {
  const projectFiles = markdownFiles(resolve(root, 'content/projects'))
  const deviceFiles = markdownFiles(resolve(root, 'content/devices'))
  const projects = projectFiles.map((file) => {
    const result = projectSchema.safeParse(frontmatter(file))
    if (!result.success) throw new Error(`${relative(root, file)}: ${result.error.message}`)
    return result.data
  })
  const devices = deviceFiles.map((file) => {
    const result = deviceSchema.safeParse(frontmatter(file))
    if (!result.success) throw new Error(`${relative(root, file)}: ${result.error.message}`)
    const manufacturerFolder = relative(resolve(root, 'content/devices'), file).split(/[\\/]/)[0]
    if (manufacturerFolder !== result.data.manufacturer.id) throw new Error(`${file}: manufacturer folder must match manufacturer.id`)
    return result.data
  })
  for (const [name, entries] of [['projects', projects], ['devices', devices]] as const) {
    const seen = new Set<string>()
    for (const entry of entries) {
      if (seen.has(entry.id)) throw new Error(`Duplicate ${name} ID: ${entry.id}`)
      seen.add(entry.id)
    }
  }
  const repositories = new Set<string>()
  const deviceIds = new Set(devices.map((device) => device.id))
  for (const project of projects) {
    const repository = project.repository.toLowerCase().replace(/\.git$/, '')
    if (repositories.has(repository)) throw new Error(`Duplicate repository: ${project.repository}`)
    repositories.add(repository)
    const references = new Set<string>()
    for (const device of project.devices) {
      if (!deviceIds.has(device.deviceId)) throw new Error(`${project.id}: unknown device ${device.deviceId}`)
      if (references.has(device.deviceId)) throw new Error(`${project.id}: duplicate device ${device.deviceId}`)
      references.add(device.deviceId)
    }
  }
  const catalog = { projects, devices }
  const metricsPath = resolve(root, 'data/repository-metrics.json')
  let snapshots: Record<string, unknown> = {}
  try { snapshots = JSON.parse(readFileSync(metricsPath, 'utf8')) } catch (error) {
    if (!(error instanceof Error && 'code' in error && error.code === 'ENOENT')) throw error
  }
  for (const project of projects) {
    if (snapshots[project.id] === undefined) continue
    const result = repositoryMetricsSchema.safeParse(snapshots[project.id])
    if (!result.success) throw new Error(`Metrics ${project.id}: ${result.error.message}`)
    if (result.data.repository.toLowerCase() !== project.repository.toLowerCase()) throw new Error(`Metrics ${project.id}: repository identity mismatch`)
    // The authoring Markdown stays unchanged; only the generated view gets metadata.
    Object.assign(project, { metrics: result.data })
  }
  const coversPath = resolve(root, 'data/repository-covers.json')
  let covers: Record<string, {repository: string; url: string}> = {}
  try { covers = JSON.parse(readFileSync(coversPath, 'utf8')) } catch (error) {
    if (!(error instanceof Error && 'code' in error && error.code === 'ENOENT')) throw error
  }
  for (const project of projects) {
    const discovered = covers[project.id]
    if (!project.cover && project.autoCover && discovered && discovered.repository.toLowerCase() === project.repository.toLowerCase()) {
      // Validate derived URLs with the same constraints as authored covers.
      const coverResult = projectSchema.shape.cover.safeParse(discovered.url)
      if (!coverResult.success) throw new Error(`Cover ${project.id}: invalid image URL`)
      project.cover = coverResult.data
    }
  }
  // Owner-selected repositories remain visible even after a later low-star refresh.
  let overrides: Record<string, { starThresholdExempt: true; approvedBy: 'site-owner'; approvedAt: string; reason: string }> = {}
  try {
    overrides = z.record(z.string().regex(/^[a-z0-9_.-]+\/[a-z0-9_.-]+$/), z.object({
      starThresholdExempt: z.literal(true), approvedBy: z.literal('site-owner'),
      approvedAt: z.iso.datetime({ offset: true }), reason: z.string().trim().min(1),
    }).strict()).parse(JSON.parse(readFileSync(resolve(root, 'data/project-intake-overrides.json'), 'utf8')))
  } catch (error) {
    if (!(error instanceof Error && 'code' in error && error.code === 'ENOENT')) throw error
  }

  catalog.projects = catalog.projects.filter((project) => overrides[project.repository.replace('https://github.com/', '').toLowerCase()]?.starThresholdExempt || !('metrics' in project) || (project.metrics as { stars: number }).stars >= 10)
  const tools = buildTools(root)
  const guides = buildGuides(root, catalog)
  if (write) {
    const guidesTarget = resolve(root, 'src/generated/guides.json')
    mkdirSync(dirname(guidesTarget), { recursive: true })
    const guidesOutput = JSON.stringify(guides, null, 2) + '\n'
    let existingGuides = ''
    try { existingGuides = readFileSync(guidesTarget, 'utf8') } catch { /* First build. */ }
    if (existingGuides !== guidesOutput) writeFileSync(guidesTarget, guidesOutput)
    const toolsTarget = resolve(root, 'src/generated/tools.json')
    mkdirSync(dirname(toolsTarget), { recursive: true })
    const toolsOutput = JSON.stringify(tools, null, 2) + '\n'
    let existingTools = ''
    try { existingTools = readFileSync(toolsTarget, 'utf8') } catch { /* First build. */ }
    if (existingTools !== toolsOutput) writeFileSync(toolsTarget, toolsOutput)
    const target = resolve(root, 'src/generated/catalog.json')
    const output = JSON.stringify(catalog, null, 2) + '\n'
    let existing = ''
    try { existing = readFileSync(target, 'utf8') } catch { /* First build. */ }
    if (existing !== output) {
      mkdirSync(dirname(target), { recursive: true })
      writeFileSync(target, output)
    }
  }
  return catalog
}
