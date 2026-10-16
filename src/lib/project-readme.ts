/** Browser-only transport. No server proxy, credentials, or repository fields needed. */
export interface ProjectReadme { content: string; htmlUrl: string; rawUrl: string; path: string }
const cacheKey = 'esp32.sh:readmes:v1'
const ttl = 60 * 60 * 1000
const maxBytes = 512 * 1024

type CacheEntry = { repository: string; expires: number; readme: ProjectReadme }
export async function fetchProjectReadme(repository: string, signal: AbortSignal): Promise<ProjectReadme> {
  if (typeof window === 'undefined') throw new Error('README requests are browser-only')
  let cache: CacheEntry[] = []
  try {
    const saved: unknown = JSON.parse(sessionStorage.getItem(cacheKey) ?? '[]')
    if (Array.isArray(saved)) cache = saved.filter(entry => entry && entry.expires > Date.now() && typeof entry.readme?.content === 'string')
  } catch { /* Storage can be blocked or full; loading still works. */ }
  const cached = cache.find(entry => entry.repository === repository)
  if (cached) return cached.readme
  const repo = new URL(repository).pathname.replace(/^\//, '')
  const response = await fetch(`https://api.github.com/repos/${repo}/readme`, {
    headers: { Accept: 'application/vnd.github+json' }, credentials: 'omit', signal,
  })
  if (!response.ok) throw new Error(`GitHub ${response.status}`)
  const value: unknown = await response.json()
  if (!value || typeof value !== 'object') throw new Error('Unsupported README')
  const data = value as Record<string, unknown>
  if (data.encoding !== 'base64' || typeof data.content !== 'string' || typeof data.size !== 'number' || data.size > maxBytes || typeof data.path !== 'string' || typeof data.html_url !== 'string' || typeof data.download_url !== 'string') throw new Error('Unsupported README')
  if (new URL(data.html_url).origin !== 'https://github.com' || new URL(data.download_url).origin !== 'https://raw.githubusercontent.com') throw new Error('Unexpected README source')
  const bytes = Uint8Array.from(atob(data.content.replace(/\s/g, '')), char => char.charCodeAt(0))
  if (bytes.length > maxBytes) throw new Error('README too large')
  const readme = { content: new TextDecoder().decode(bytes), htmlUrl: data.html_url, rawUrl: data.download_url, path: data.path }
  try {
    sessionStorage.setItem(cacheKey, JSON.stringify([{ repository, expires: Date.now() + ttl, readme }, ...cache.filter(entry => entry.repository !== repository)].slice(0, 5)))
  } catch { /* A full cache must never hide the README. */ }
  return readme
}

/** Resolve repository-relative links without sending images through esp32.sh. */
export function readmeUrl(value: string, image: boolean, readme: ProjectReadme): string {
  try {
    const base = image ? readme.rawUrl : readme.htmlUrl
    let result: URL
    if (value.startsWith('/') && !value.startsWith('//')) {
      const encodedPath = readme.path.split('/').map(encodeURIComponent).join('/')
      const root = base.slice(0, base.length - encodedPath.length)
      result = new URL(value.slice(1), root)
    } else result = new URL(value, base)
    return (image ? ['https:', 'http:'] : ['https:', 'http:', 'mailto:']).includes(result.protocol) ? result.href : ''
  } catch { return '' }
}
