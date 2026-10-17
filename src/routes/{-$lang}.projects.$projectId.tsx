import { createFileRoute, Link, notFound } from '@tanstack/react-router'
import { catalog } from '../lib/content'
import { languageLinks, pageMeta } from '../lib/seo'
import { localeParam, resolveLocale, tagLabel, text } from '../lib/i18n'
import { ProjectReadme } from '../components/project-readme'

export const Route = createFileRoute('/{-$lang}/projects/$projectId')({
  loader: ({ params }) => {
    const project = catalog.projects.find(entry => entry.id === params.projectId)
    if (!project) throw notFound()
    return { project }
  },
  head: ({ loaderData, params }) => ({
    meta: pageMeta({ title: `${loaderData?.project.name ?? 'Project'} — esp32.sh`, description: loaderData?.project.summary[resolveLocale(params.lang)], path: `/projects/${params.projectId}`, locale: resolveLocale(params.lang), image: loaderData?.project.cover }),
    links: languageLinks(`/projects/${params.projectId}`, resolveLocale(params.lang)),
  }),
  component: ProjectDetail,
})
function ProjectDetail() {
  const locale = resolveLocale(Route.useParams().lang)
  const { project } = Route.useLoaderData()
  const t = text(locale)
  return <section className="content project-detail">
    <Link to="/{-$lang}" params={{ lang: localeParam(locale) }}>← {t.projects}</Link>
    <div className="project-detail-heading"><h1>{project.name}</h1><a className="project-github" href={project.repository} target="_blank" rel="noopener noreferrer">{t.open}</a></div>
    <p className="project-summary">{project.summary[locale]}</p>
    <div className="project-facts"><span title={project.metrics ? `${t.checked}: ${project.metrics.checkedAt.slice(0, 10)}` : undefined}>{project.metrics ? `★ ${project.metrics.stars.toLocaleString(locale)}` : t.metricsPending}{project.metrics?.archived ? ` · ${t.archived}` : ''}</span><span>{project.license}</span>{project.tags.map(tag => <Link key={tag} to="/{-$lang}" params={{ lang: localeParam(locale) }} search={{ tag }}>{tagLabel(tag, locale)}</Link>)}</div>
    <div className="project-devices"><strong>{t.devices}</strong><div className="device-tags">{project.devices.map(({ deviceId }) => <Link key={deviceId} to="/{-$lang}/devices/$deviceId" params={{ lang: localeParam(locale), deviceId }}>{catalog.devices.find(device => device.id === deviceId)?.name}</Link>)}</div>{!project.devices.length && <small>{project.compatibility === 'custom-hardware' ? t.customHardware : t.compatibilityPending}</small>}</div>
    <ProjectReadme key={project.id} repository={project.repository} locale={locale} />
  </section>
}
