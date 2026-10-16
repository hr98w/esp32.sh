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
