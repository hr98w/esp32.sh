import { createFileRoute } from '@tanstack/react-router'
import { catalog } from '../lib/content'
import { buildSitemap } from '../lib/sitemap'

export const Route = createFileRoute('/sitemap.xml')({
  server: { handlers: { GET: () => new Response(buildSitemap(catalog), { headers: {
    'Content-Type': 'application/xml; charset=utf-8',
    'Cache-Control': 'public, max-age=300',
  } }) } },
})
