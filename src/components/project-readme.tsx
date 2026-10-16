import { lazy, Suspense, useEffect, useState } from 'react'
import { fetchProjectReadme, type ProjectReadme as Readme } from '../lib/project-readme'
import type { Locale } from '../lib/i18n'

const ReadmeMarkdown = lazy(() => import('./readme-markdown'))
const labels = {
  en: { original: 'View original ↗', loading: 'Loading README from GitHub…', error: 'README could not be loaded. You can read it on GitHub.', note: 'Original README · loaded directly from GitHub, in its original language.' },
  zh: { original: '查看原文 ↗', loading: '正在从 GitHub 加载 README…', error: 'README 暂时无法加载，你可以前往 GitHub 阅读。', note: '原始 README · 直接从 GitHub 加载，保留原文语言。' },
  ja: { original: '原文を見る ↗', loading: 'GitHubからREADMEを読み込み中…', error: 'READMEを読み込めませんでした。GitHubでご覧いただけます。', note: '元のREADME · GitHubから直接取得し、原文の言語で表示します。' },
}
export function ProjectReadme({ repository, locale }: { repository: string; locale: Locale }) {
  const [state, setState] = useState<{ repository: string; readme?: Readme; failed?: boolean }>()
  const t = labels[locale]
  useEffect(() => {
    let active = true
    const controller = new AbortController()
    const timeout = window.setTimeout(() => controller.abort(), 15000)
    fetchProjectReadme(repository, controller.signal).then(readme => {
      if (!controller.signal.aborted) setState({ repository, readme })
    }).catch(() => {
      if (active) setState({ repository, failed: true })
    }).finally(() => window.clearTimeout(timeout))
    return () => { active = false; window.clearTimeout(timeout); controller.abort() }
  }, [repository])
  const current = state?.repository === repository ? state : undefined
  const loading = <p className="readme-status" role="status">{t.loading}</p>
  return <section className="project-readme" aria-labelledby="project-readme-heading">
    <div className="readme-heading"><h2 id="project-readme-heading">README</h2><a href={current?.readme?.htmlUrl ?? `${repository}#readme`} target="_blank" rel="noopener noreferrer">{t.original}</a></div>
    <p className="readme-note">{t.note}</p>
    {current?.readme ? <Suspense fallback={loading}><ReadmeMarkdown readme={current.readme} /></Suspense>
      : current?.failed ? <p className="readme-status" role="status">{t.error} <a href={`${repository}#readme`} target="_blank" rel="noopener noreferrer">GitHub ↗</a></p> : loading}
  </section>
}
