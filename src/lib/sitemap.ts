import { locales, localizedPath } from './i18n'
import { PAGE_SIZE } from './pagination'

const site = 'https://esp32.sh'
const escapeXml = (value: string) => value.replace(/[<>&"']/g, char => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&apos;' })[char]!)
export function buildSitemap(catalog: { projects: { id: string }[]; devices: { id: string }[] }) {
  const paths = ['/', '/devices', '/tools', '/guides', ...catalog.projects.map(project => `/projects/${project.id}`), ...catalog.devices.map(device => `/devices/${device.id}`)]
  for (const [path, count] of [['/', catalog.projects.length], ['/devices', catalog.devices.length]] as const) {
    for (let page = 2; page <= Math.ceil(count / PAGE_SIZE); page++) paths.push(`${path}?page=${page}`)
  }
  const entries = paths.flatMap(path => {
    const [pathname, query] = path.split('?')
    const href = (locale: typeof locales[number]) => site + localizedPath(pathname, locale) + (query ? `?${query}` : '')
    const alternatives = [...locales.map(locale => `<xhtml:link rel="alternate" hreflang="${locale === 'zh' ? 'zh-CN' : locale}" href="${escapeXml(href(locale))}"/>`), `<xhtml:link rel="alternate" hreflang="x-default" href="${escapeXml(href('en'))}"/>`].join('')
    return locales.map(locale => `<url><loc>${escapeXml(href(locale))}</loc>${alternatives}</url>`)
  })
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n${entries.join('\n')}\n</urlset>`
}
