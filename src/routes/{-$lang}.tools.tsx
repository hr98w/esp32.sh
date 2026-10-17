import { createFileRoute, stripSearchParams } from '@tanstack/react-router'
import { ToolCard } from '../components/tool-card'
import { tools } from '../lib/tools'
import { selectTools } from '../lib/directory'
import { resolveLocale } from '../lib/i18n'
import { toolText, formatToolCount } from '../lib/i18n/tools'
import { toolCategories, type ToolCategory } from '../lib/tool-types'
import { languageLinks, pageMeta } from '../lib/seo'

type ToolSearch = { q?: string; category?: ToolCategory | '' }
export const Route = createFileRoute('/{-$lang}/tools')({
  validateSearch: (search: Record<string, unknown>): ToolSearch => ({
    q: typeof search.q === 'string' ? search.q : '',
    category: toolCategories.includes(search.category as ToolCategory) ? search.category as ToolCategory : '',
  }),
  search: { middlewares: [stripSearchParams({ q: '', category: '' })] },
  head: ({ params }) => {
    const locale = resolveLocale(params.lang), t = toolText(locale)
    return { meta: pageMeta({ title: `${t.title} — esp32.sh`, description: t.intro, path: '/tools', locale }), links: languageLinks('/tools', locale) }
  },
  component: ToolDirectory,
})

function ToolDirectory() {
  const locale = resolveLocale(Route.useParams().lang), t = toolText(locale)
  const search = Route.useSearch(), navigate = Route.useNavigate()
  const update = (patch: Partial<ToolSearch>) => { void navigate({ search: previous => ({ ...previous, ...patch }), replace: true, resetScroll: false }) }
  const filtered = selectTools(tools, search)
  return <section className="content tool-directory">
    <h1>{t.title}</h1><p className="intro">{t.intro}</p>
    <input className="project-search" type="search" placeholder={t.search} aria-label={t.search} value={search.q} onChange={event => update({ q: event.target.value })} />
    <div className="tags"><button aria-pressed={!search.category} onClick={() => update({ category: '' })}>{t.all}</button>{toolCategories.map(category => <button key={category} aria-pressed={search.category === category} onClick={() => update({ category })}>{t.category[category]}</button>)}</div>
    <div className="results"><span role="status">{formatToolCount(filtered.length, locale)}</span>{(search.q || search.category) && <button onClick={() => update({ q: '', category: '' })}>{t.clear}</button>}</div>
    {filtered.length ? <div className="tool-grid">{filtered.map(tool => <ToolCard key={tool.id} tool={tool} locale={locale} />)}</div> : <div className="empty"><p>{t.empty}</p></div>}
    <p className="tool-note">{t.note}</p>
  </section>
}
