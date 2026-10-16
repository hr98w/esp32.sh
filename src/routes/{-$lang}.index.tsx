import { Pagination } from '../components/pagination'
import { paginate, parsePage } from '../lib/pagination'
import { selectProjects } from '../lib/directory'
import { manufacturerLabel } from '../lib/manufacturers'
import { matchesQuery, deviceSearchFields } from '../lib/search'
import { languageLinks } from '../lib/seo'
import { useState } from 'react'
import { createFileRoute, Link, redirect, stripSearchParams } from '@tanstack/react-router'
import { catalog, projectsForDevice } from '../lib/content'
import { resolveLocale, localeParam, text, tagLabel, formatPageCount } from '../lib/i18n'
import { ProjectCard } from '../components/project-card'

type ProjectSearch = { q?: string; device?: string; tag?: string; sort?: 'stars' | 'name' | 'newest'; page?: number }

export const Route = createFileRoute('/{-$lang}/')({
  validateSearch: (search: Record<string, unknown>): ProjectSearch => ({
    page: parsePage(search.page),
    q: typeof search.q === 'string' ? search.q : '',
    device: typeof search.device === 'string' && catalog.devices.some((device) => device.id === search.device) ? search.device : '',
    tag: typeof search.tag === 'string' && catalog.projects.some(project => project.tags.includes(search.tag as string)) ? search.tag : '',
    sort: search.sort === 'name' || search.sort === 'newest' ? search.sort : 'stars',
  }),
  search: {
    middlewares: [stripSearchParams({ q: '', device: '', tag: '', sort: 'stars', page: 1 })],
  },
  beforeLoad: ({ search, location, params }) => {
    const page = paginate(selectProjects(catalog, search), search.page).page
    const requestedPage = new URLSearchParams(location.searchStr).get('page')
    if (requestedPage !== null && (page === 1 || requestedPage !== String(page))) {
      throw redirect({ to: '/{-$lang}', params, search: { ...search, page }, replace: true })
    }
  },
  head: ({ params, match }) => { const t = text(resolveLocale(params.lang)); return { meta: [{ title: `${t.headline} — esp32.sh` }, { name: 'description', content: t.intro }], links: languageLinks('/', resolveLocale(params.lang), match.search.page) } },
  component: ProjectDirectory,
})

function ProjectDirectory() {
  const lang = resolveLocale(Route.useParams().lang)
  const search = Route.useSearch()
  const navigate = Route.useNavigate()
  const [deviceQuery, setDeviceQuery] = useState('')
  const [showDevices, setShowDevices] = useState(false)
  const t = text(lang)
  const update = (patch: Partial<typeof search>) => { void navigate({ search: (previous) => ({ ...previous, ...patch, page: 1 }), replace: true, resetScroll: false }) }
  const available = catalog.devices.filter((device) => projectsForDevice(device.id).length > 0)
  const models = available.filter((device) => matchesQuery(deviceQuery, deviceSearchFields(device)))
  const makers = [...new Map(models.map((device) => [device.manufacturer.id, device.manufacturer])).values()]
  const tags = [...new Set(catalog.projects.flatMap((project) => project.tags))]
  const projects = selectProjects(catalog, search)
  const pagination = paginate(projects, search.page)
  return <div className="workspace">
    <aside className="device-sidebar"><div className={`sidebar-disclosure ${showDevices ? 'expanded' : ''}`}><button className="mobile-device-toggle" aria-expanded={showDevices} onClick={() => setShowDevices(!showDevices)}>{search.device ? catalog.devices.find(device => device.id === search.device)?.name : t.myDevice} ▾</button><h2 className="desktop-device-heading">{t.myDevice}</h2><div className="sidebar-content">
      <input type="search" placeholder={t.deviceSearch} aria-label={t.deviceSearch} value={deviceQuery} onChange={(event) => setDeviceQuery(event.target.value)} />
      <button className={!search.device ? 'selected' : ''} onClick={() => { update({ device: '' }); setShowDevices(false) }}>{t.allDevices}<span>{catalog.projects.length}</span></button>
      {models.length === 0 && <p className="sidebar-hint">{t.noDevice}</p>}{makers.map((maker) => <details className="device-maker-group" key={maker.id} open={deviceQuery.trim().length > 0}><summary>{manufacturerLabel(maker, lang)}</summary>{models.filter((device) => device.manufacturer.id === maker.id).map((device) => <button key={device.id} className={search.device === device.id ? 'selected' : ''} onClick={() => { update({ device: device.id }); setShowDevices(false) }}>{device.name}<span>{projectsForDevice(device.id).length}</span></button>)}</details>)}
      <Link to="/{-$lang}/devices" params={{ lang: localeParam(lang) }}>{t.browseDevices}</Link>
    </div></div></aside>
    <section className="content"><h1>{t.headline}</h1><p className="intro">{t.intro}</p>
      <input className="project-search" type="search" placeholder={t.search} aria-label={t.search} value={search.q} onChange={(event) => update({ q: event.target.value })} />
      <div className="tags"><button aria-pressed={!search.tag} onClick={() => update({ tag: '' })}>{t.allTags}</button>{tags.map((tag) => <button key={tag} aria-pressed={search.tag === tag} onClick={() => update({ tag })}>{tagLabel(tag, lang)}</button>)}</div>
      <div className="results"><span role="status">{formatPageCount(projects.length, pagination.start, pagination.end, 'project', lang)}</span><select value={search.sort} aria-label={t.sort} onChange={(event) => update({ sort: event.target.value === 'newest' ? 'newest' : event.target.value === 'name' ? 'name' : 'stars' })}><option value="stars">{t.stars}</option><option value="name">A–Z</option><option value="newest">{t.newest}</option></select></div>
      {projects.length ? <div className="project-grid">{pagination.items.map((project) => <ProjectCard key={project.id} project={project} locale={lang} />)}</div> : <div className="empty"><p>{t.empty}</p><button onClick={() => update({ q: '', device: '', tag: '' })}>{t.clear}</button></div>}
      <Pagination page={pagination.page} pageCount={pagination.pageCount} locale={lang} directory="projects" />
    </section>
  </div>
}
