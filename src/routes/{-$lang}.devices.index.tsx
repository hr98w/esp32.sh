import { Pagination } from '../components/pagination'
import { paginate, parsePage } from '../lib/pagination'
import { selectDevices } from '../lib/directory'
import { deviceTypes, type DeviceType } from '../lib/device-types'
import { deviceText, deviceTypeLabel } from '../lib/i18n/device'
import { DeviceImage } from '../components/device-image'
import { manufacturerLabel } from '../lib/manufacturers'
import { languageLinks, pageMeta } from '../lib/seo'
import { createFileRoute, Link, redirect, stripSearchParams } from '@tanstack/react-router'
import { catalog, projectsForDevice } from '../lib/content'
import { resolveLocale, localeParam, text, featureLabel, formatCount, formatPageCount } from '../lib/i18n'

type DeviceSearch = { type?: DeviceType | ''; q?: string; maker?: string; chip?: string; feature?: string; page?: number }

export const Route = createFileRoute('/{-$lang}/devices/')({
  validateSearch: (search: Record<string, unknown>): DeviceSearch => ({
    type: deviceTypes.includes(search.type as DeviceType) ? search.type as DeviceType : '',
    page: parsePage(search.page),
    q: typeof search.q === 'string' ? search.q : '',
    maker: typeof search.maker === 'string' && catalog.devices.some(d => d.manufacturer.id === search.maker) ? search.maker : '',
    chip: typeof search.chip === 'string' && catalog.devices.some(d => d.chip === search.chip) ? search.chip : '',
    feature: typeof search.feature === 'string' && catalog.devices.some(d => d.features.includes(search.feature as string)) ? search.feature : '',
  }),
  search: { middlewares: [stripSearchParams({type:'',q:'',maker:'',chip:'',feature:'',page:1})] },
  beforeLoad: ({ search, location, params }) => {
    const page = paginate(selectDevices(catalog, search), search.page).page
    const requestedPage = new URLSearchParams(location.searchStr).get('page')
    if (requestedPage !== null && (page === 1 || requestedPage !== String(page))) {
      throw redirect({ to: '/{-$lang}/devices', params, search: { ...search, page }, replace: true })
    }
  },
  head: ({params, match}) => { const t = text(resolveLocale(params.lang)); return {meta:pageMeta({title:`${t.devices} — esp32.sh`,description:t.hardwareIntro,path:'/devices',locale:resolveLocale(params.lang),page:match.search.page}),links:languageLinks('/devices',resolveLocale(params.lang), match.search.page)} },
  component: DeviceDirectory,
})
function DeviceDirectory() {
  const lang = resolveLocale(Route.useParams().lang)
  const t = text(lang)
  const dt = deviceText(lang)
  const search = Route.useSearch()
  const navigate = Route.useNavigate()
  const update = (patch: Partial<typeof search>) => { void navigate({search: previous => ({...previous,...patch,page:1}), replace:true, resetScroll:false}) }
  const makers = [...new Map(catalog.devices.map(d => [d.manufacturer.id,d.manufacturer])).values()].sort((a,b)=>a.name.localeCompare(b.name))
  const chips = [...new Set(catalog.devices.map(d => d.chip))].sort()
  const features = [...new Set(catalog.devices.flatMap(d => d.features))].sort()
  const devices = selectDevices(catalog, search)
  const pagination = paginate(devices, search.page)
  return <section className="content"><h1>{t.devices}</h1><p className="intro">{t.hardwareIntro}</p>
    <div className="tags device-type-tabs" role="group" aria-label={dt.type}>
      <button aria-pressed={!search.type} onClick={() => update({type:''})}>{dt.allTypes}</button>
      {deviceTypes.map(type => <button key={type} aria-pressed={search.type === type} onClick={() => update({type})}>{deviceTypeLabel(type, lang)}</button>)}
    </div>
    <div className="device-toolbar">
      <input type="search" aria-label={t.deviceSearch} placeholder={t.deviceSearch} value={search.q} onChange={event=>update({q:event.target.value})}/>
      <select aria-label={t.maker} value={search.maker} onChange={event=>update({maker:event.target.value})}><option value="">{t.manufacturer}</option>{makers.map(m=><option key={m.id} value={m.id}>{manufacturerLabel(m, lang)}</option>)}</select>
      <select aria-label={t.chip} value={search.chip} onChange={event=>update({chip:event.target.value})}><option value="">{t.allChips}</option>{chips.map(chip=><option key={chip}>{chip}</option>)}</select>
      <select aria-label={t.allFeatures} value={search.feature} onChange={event=>update({feature:event.target.value})}><option value="">{t.allFeatures}</option>{features.map(feature=><option key={feature} value={feature}>{featureLabel(feature,lang)}</option>)}</select>
    </div>
    <div className="results"><span role="status">{formatPageCount(devices.length, pagination.start, pagination.end, 'device', lang)}</span>{Object.entries(search).some(([key, value]) => key !== 'page' && Boolean(value))&&<button onClick={()=>update({type:'',q:'',maker:'',chip:'',feature:'',page:1})}>{t.clear}</button>}</div>
    {devices.length ? <div className="project-grid">{pagination.items.map((device) => <article className="project-card" key={device.id}>
    <Link className="cover device-cover" to="/{-$lang}/devices/$deviceId" params={{ lang: localeParam(lang), deviceId: device.id }}><DeviceImage src={device.cover} name={device.name} maker={manufacturerLabel(device.manufacturer, lang)} /></Link>
    <div className="card-body"><small className="device-type-label">{deviceTypeLabel(device.type, lang)}</small><h2><Link to="/{-$lang}/devices/$deviceId" params={{ lang: localeParam(lang), deviceId: device.id }}>{device.name}</Link></h2><p>{device.summary[lang]}</p><div className="device-facts card-features">{device.features.slice(0, 4).map(feature => <span key={feature}>{featureLabel(feature, lang)}</span>)}</div><div className="card-meta"><span>{device.chip}</span><span>{formatCount(projectsForDevice(device.id).length, 'project', lang)}</span></div></div>
  </article>)}</div>:<p className="empty">{t.deviceEmpty}</p>}<Pagination page={pagination.page} pageCount={pagination.pageCount} locale={lang} directory="devices" /></section>
}
