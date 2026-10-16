import { useEffect, useRef, useState } from 'react'
import type { Tool } from '../lib/content/schema'
import type { Locale } from '../lib/i18n'
import type { ToolCategory } from '../lib/tool-types'
import { toolText } from '../lib/i18n/tools'

const iconPaths: Record<ToolCategory, string> = {
  flashing: 'M13 2 5 13h6l-1 9 9-12h-6l1-8Z',
  simulation: 'M6 6h12v12H6zM9 2v4m6-4v4M9 18v4m6-4v4M2 9h4m-4 6h4m12-6h4m-4 6h4',
  'coding-debugging': 'm5 7 5 5-5 5m8 0h6',
  'display-assets': 'M3 4h18v13H3zM8 21h8m-4-4v4',
}

export function ToolCard({ tool, locale }: { tool: Tool; locale: Locale }) {
  const t = toolText(locale)
  const imageRef = useRef<HTMLImageElement>(null)
  const [failedIcon, setFailedIcon] = useState<string | null>(null)
  useEffect(() => {
    const image = imageRef.current
    if (image?.complete && image.naturalWidth === 0 && tool.icon) setFailedIcon(tool.icon)
  }, [tool.icon])
  const showIcon = Boolean(tool.icon && tool.icon !== failedIcon)
  return <article className="tool-card" data-tool-id={tool.id}>
    <div className="tool-heading"><span className={`tool-icon ${showIcon ? 'has-image' : ''}`} aria-hidden="true">{showIcon ? <img ref={imageRef} src={tool.icon} width="30" height="30" alt="" loading="lazy" decoding="async" referrerPolicy="no-referrer" onError={() => setFailedIcon(tool.icon ?? null)} /> : <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="miter"><path d={iconPaths[tool.category]} /></svg>}</span><div><small>{t.category[tool.category]}</small><h2><a href={tool.url} target="_blank" rel="noopener noreferrer">{tool.name}</a></h2></div></div>
    <p className="tool-summary">{tool.summary[locale]}</p>
    <div className="tool-badges"><span>{t.runtime[tool.runtime]}</span><span>{t.sourceType[tool.sourceType]}</span><span>{t.pricing[tool.pricing]}</span></div>
    <p className="tool-requirements">{tool.requirements[locale]}</p>
    <div className="tool-actions"><a className="tool-open" href={tool.url} target="_blank" rel="noopener noreferrer">{tool.runtime === 'browser' ? t.open : t.visit}</a>{tool.repository && tool.repository !== tool.url && <a href={tool.repository} target="_blank" rel="noopener noreferrer" title={tool.license}>GitHub ↗</a>}</div>
    <div className="tool-provenance"><a href={tool.sources[0].url} target="_blank" rel="noopener noreferrer">{t.source}</a><span>{tool.license ? `${tool.license} · ` : ''}{t.reviewed} {tool.sources[0].checkedAt.slice(0, 10)}</span></div>
  </article>
}
