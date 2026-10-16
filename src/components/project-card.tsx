import { useEffect, useRef, useState } from 'react'
import { Link } from '@tanstack/react-router'
import type { Project } from '../lib/content/schema'
import { catalog } from '../lib/content'
import { text, localeParam } from '../lib/i18n'
import type { Locale } from '../lib/i18n'

export function ProjectCard({ project, locale }: { project: Project; locale: Locale }) {
  const [failedCover, setFailedCover] = useState<string | null>(null)
  const imageRef = useRef<HTMLImageElement>(null)
  // A cached or blocked image may fail before React hydrates the SSR markup.
  useEffect(() => {
    const image = imageRef.current
    if (image?.complete && image.naturalWidth === 0 && project.cover) setFailedCover(project.cover)
  }, [project.cover])
  const t = text(locale)
  return <article className="project-card">
    <a className="cover" href={project.repository} target="_blank" rel="noopener noreferrer">
      {project.cover && project.cover !== failedCover
        ? <img ref={imageRef} src={project.cover} alt={`${project.name} — ${t.imageAlt}`} loading="lazy" onError={() => setFailedCover(project.cover ?? null)} />
        : <span className="name-cover"><small>ESP32.SH</small><strong>{project.name}</strong></span>}
    </a>
    <div className="card-body">
      <h2><a href={project.repository} target="_blank" rel="noopener noreferrer">{project.name}</a></h2>
      <p>{project.summary[locale]}</p>
      {project.devices.length === 0 && <small className="compatibility">{project.compatibility === 'custom-hardware' ? t.customHardware : t.compatibilityPending}</small>}<div className="device-tags">{project.devices.map(({ deviceId }) => <Link key={deviceId} to="/{-$lang}/devices/$deviceId" params={{ lang: localeParam(locale), deviceId }}>{catalog.devices.find((device) => device.id === deviceId)?.name}</Link>)}</div>
      <div className="card-meta"><span title={project.metrics ? `${t.checked}: ${project.metrics.checkedAt.slice(0, 10)}` : t.metricsPending}>{project.metrics ? `★ ${project.metrics.stars.toLocaleString(locale)}` : t.metricsPending}{project.metrics?.archived ? ` · ${t.archived}` : ''}</span><span>{project.license}</span><a href={project.repository} target="_blank" rel="noopener noreferrer">{t.open}</a></div>
    </div>
  </article>
}
