import { manufacturerLabel } from '../lib/manufacturers'
import { languageLinks, pageMeta } from '../lib/seo'
import { createFileRoute, Link, notFound } from '@tanstack/react-router'
import { catalog, projectsForDevice } from '../lib/content'
import { resolveLocale, localeParam, text, featureLabel, formatCount } from '../lib/i18n'
import { deviceText, deviceTypeLabel } from '../lib/i18n/device'
import { ProjectCard } from '../components/project-card'
import { DeviceImage } from '../components/device-image'

export const Route = createFileRoute('/{-$lang}/devices/$deviceId')({
  loader: ({ params }) => {
    const device = catalog.devices.find((entry) => entry.id === params.deviceId)
    if (!device) throw notFound()
    return { device, projects: projectsForDevice(device.id).sort((a, b) => (b.metrics?.stars ?? -1) - (a.metrics?.stars ?? -1) || a.name.localeCompare(b.name)) }
  },
  head: ({ loaderData, params }) => ({ meta: pageMeta({ title: `${loaderData?.device.name ?? 'Device'} — esp32.sh`, description: loaderData?.device.summary[resolveLocale(params.lang)], path: `/devices/${params.deviceId}`, locale: resolveLocale(params.lang), image: loaderData?.device.cover }), links: languageLinks(`/devices/${params.deviceId}`, resolveLocale(params.lang)) }),
  component: DeviceDetail,
})
function DeviceDetail() {
  const lang = resolveLocale(Route.useParams().lang)
  const { device, projects } = Route.useLoaderData()
  const t = text(lang)
  const dt = deviceText(lang)
  const maker = manufacturerLabel(device.manufacturer, lang)
  const price = device.referencePrice
  const extraImages = device.gallery?.filter(image => image.image !== device.cover) ?? []
  const imageSource = device.gallery?.find(image => image.image === device.cover)?.sourceUrl
  return <section className="content device-detail">
    <Link to="/{-$lang}/devices" params={{ lang: localeParam(lang) }}>{t.back}</Link>
    <div className={`device-overview${device.cover ? ' has-image' : ''}`}>
      {device.cover && <figure className="device-hero-image">
        <DeviceImage src={device.cover} name={`${maker} ${device.name}`} maker={maker} eager />
        {imageSource && <figcaption><a href={imageSource} target="_blank" rel="noopener noreferrer">{dt.imageCredit} ↗</a></figcaption>}
      </figure>}
      <div className="device-hero-copy">
        <small>{maker} / {device.chip}{device.sku && ` / ${device.sku}`}</small>
        <span className="device-type-label">{deviceTypeLabel(device.type, lang)}</span>
        <h1>{device.name}</h1><p>{device.summary[lang]}</p>
        <div className="device-facts">{device.features.map(feature => <span key={feature}>{featureLabel(feature, lang)}</span>)}</div>
        <div className="device-official-links"><a href={device.officialUrl} target="_blank" rel="noopener noreferrer">{t.official}</a>{price && <a href={price.sourceUrl} target="_blank" rel="noopener noreferrer">{dt.store}</a>}</div>
        {price && <div className="device-price"><span>{dt.price} <strong>{new Intl.NumberFormat(lang, { style: 'currency', currency: price.currency, currencyDisplay: 'code' }).format(price.amount)}</strong></span><small>{t.checked}: {price.checkedAt} · {dt.priceNote}</small></div>}
      </div>
    </div>
    {device.specifications?.length ? <section className="device-section" aria-labelledby="hardware-specs">
      <h2 id="hardware-specs">{dt.specs}</h2><dl className="device-specs">{device.specifications.map((spec, index) => <div key={index}><dt>{spec.label[lang]}</dt><dd>{spec.value[lang]}</dd></div>)}</dl>
      {extraImages.length > 0 && <details className="device-gallery"><summary>{dt.images}</summary>{extraImages.map(image => <figure key={image.image}><DeviceImage src={image.image} name={image.caption[lang]} maker={maker} /><figcaption>{image.caption[lang]} · <a href={image.sourceUrl} target="_blank" rel="noopener noreferrer">{dt.gallerySource}</a></figcaption></figure>)}</details>}
    </section> : null}
    {(device.factoryFeatures || device.resources?.length) && <section className="device-section device-start" aria-labelledby="getting-started">
      <h2 id="getting-started">{dt.gettingStarted}</h2>
      {device.factoryFeatures && <div><h3>{dt.factory}</h3><p>{device.factoryFeatures[lang]}</p></div>}
      {device.resources?.length ? <ul className="device-resource-links">{device.resources.map(resource => <li key={resource.url}><a href={resource.url} target="_blank" rel="noopener noreferrer">{resource.label[lang]} ↗</a></li>)}</ul> : null}
    </section>}
    {device.revisionNotes?.length ? <section className="device-section device-revisions" aria-labelledby="revision-notes"><h2 id="revision-notes">{dt.revisions}</h2>{device.revisionNotes.map((note, index) => <p key={index}>{note.text[lang]} <a href={note.sourceUrl} target="_blank" rel="noopener noreferrer">{dt.source}</a></p>)}</section> : null}
    <p className="source-note">{t.sourceNote}</p>
    <details className="support-sources"><summary>{t.sources}</summary><ul>{device.sources.map(source => <li key={source.url}><a href={source.url} target="_blank" rel="noopener noreferrer">{new URL(source.url).hostname} ↗</a>{source.checkedAt && ` · ${t.checked}: ${source.checkedAt.slice(0, 10)}`}</li>)}</ul></details>
    <section className="device-section" aria-labelledby="related-projects">
      <div className="device-section-heading"><h2 id="related-projects">{t.related}</h2><small>{formatCount(projects.length, 'project', lang)}</small></div>
      {projects.length ? <div className="project-grid">{projects.map(project => <ProjectCard key={project.id} project={project} locale={lang} />)}</div> : <p className="empty">{t.missing}</p>}
      {projects.length > 0 && <details className="support-sources"><summary>{t.reference}</summary><ul>{projects.map(project => <li key={project.id}><a href={project.devices.find(entry => entry.deviceId === device.id)!.sourceUrl} target="_blank" rel="noopener noreferrer">{project.name} ↗</a></li>)}</ul></details>}
    </section>
  </section>
}
