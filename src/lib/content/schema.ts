import { toolCategories } from '../tool-types.ts'
import { deviceTypes } from '../device-types.ts'
import { z } from 'zod'

const id = z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)
const url = z.url().refine((value) => value.startsWith('https://'), 'Use an HTTPS URL')
const localizedText = z.object({ zh: z.string().min(1), en: z.string().min(1), ja: z.string().min(1) }).strict()
const cover = z.union([url, z.string().regex(/^\/images\//)]).optional()
const source = z.object({ url, checkedAt: z.iso.datetime({ offset: true }).optional() }).strict()

export const projectSchema = z.object({
  id,
  name: z.string().min(1),
  repository: url.regex(/^https:\/\/github\.com\/[\w.-]+\/[\w.-]+$/),
  license: z.string().min(1),
  summary: localizedText,
  kind: z.enum(['firmware', 'application', 'library', 'framework']),
  tags: z.array(id).default([]),
  devices: z.array(z.object({ deviceId: id, sourceUrl: url }).strict()).default([]),
  addedAt: z.iso.date(),
  cover,
  autoCover: z.boolean().default(true),
  sources: z.array(source).default([]),
  compatibility: z.enum(['documented', 'pending', 'custom-hardware']).default('pending'),
}).strict()

export const deviceSchema = z.object({
  type: z.enum(deviceTypes),
  id,
  name: z.string().min(1),
  manufacturer: z.object({ id, name: z.string().min(1) }).strict(),
  chip: z.string().min(1),
  summary: localizedText,
  officialUrl: url,
  aliases: z.array(z.string()).default([]),
  features: z.array(z.string()).default([]),
  cover,
  sku: z.string().min(1).optional(),
  gallery: z.array(z.object({ image: z.union([url, z.string().regex(/^\/images\//)]), caption: localizedText, sourceUrl: url }).strict()).optional(),
  specifications: z.array(z.object({ label: localizedText, value: localizedText }).strict()).optional(),
  factoryFeatures: localizedText.optional(),
  resources: z.array(z.object({ label: localizedText, url }).strict()).optional(),
  revisionNotes: z.array(z.object({ text: localizedText, sourceUrl: url }).strict()).optional(),
  referencePrice: z.object({ amount: z.number().positive(), currency: z.string().regex(/^[A-Z]{3}$/), sourceUrl: url, checkedAt: z.iso.date() }).strict().optional(),
  sources: z.array(source).default([]),
}).strict()

export const toolSchema = z.object({
  id,
  name: z.string().min(1),
  url,
  icon: url.optional(),
  repository: projectSchema.shape.repository.optional(),
  category: z.enum(toolCategories),
  summary: localizedText,
  requirements: localizedText,
  runtime: z.enum(['browser', 'desktop', 'cli']),
  sourceType: z.enum(['open-source', 'hosted-service', 'official-tool']),
  license: z.string().min(1).optional(),
  pricing: z.enum(['free', 'freemium', 'paid', 'unspecified']),
  order: z.number().int().min(0),
  sources: z.array(source.extend({ checkedAt: z.iso.datetime({ offset: true }) })).min(1),
  addedAt: z.iso.date(),
}).strict().superRefine((tool, context) => {
  if (tool.sourceType === 'open-source' && (!tool.license || !tool.repository)) {
    context.addIssue({ code: 'custom', message: 'Open-source tools need an explicit license and repository', path: ['sourceType'] })
  }
})
export type Tool = z.infer<typeof toolSchema>

export const repositoryMetricsSchema = z.object({
  repository: url,
  githubId: z.number().int().positive(),
  stars: z.number().int().min(0),
  checkedAt: z.iso.datetime({ offset: true }),
  pushedAt: z.iso.datetime({ offset: true }).nullable(),
  archived: z.boolean(),
  sourceUrl: url,
}).strict()
export type RepositoryMetrics = z.infer<typeof repositoryMetricsSchema>
export type Project = z.infer<typeof projectSchema> & { metrics?: RepositoryMetrics }
export type Device = z.infer<typeof deviceSchema>
export type Catalog = { projects: Project[]; devices: Device[] }

export const guidePostSchema = z.object({
  id, title: localizedText,
  url: z.string().regex(/^https:\/\/(?:x\.com|twitter\.com)\/[A-Za-z0-9_]+\/status\/[0-9]+$/),
  order: z.number().int().min(0),
}).strict()
export const guidePickSchema = z.object({
  id, title: localizedText, summary: localizedText, effort: localizedText,
  budget: z.enum(['low', 'medium', 'high']),
  deviceIds: z.array(id).min(1), projectIds: z.array(id).min(1),
  resource: z.object({ label: localizedText, url }).strict(),
  sources: z.array(url).min(1), order: z.number().int().min(0),
}).strict()
export type GuidePost = z.infer<typeof guidePostSchema>
export type GuidePick = z.infer<typeof guidePickSchema>
