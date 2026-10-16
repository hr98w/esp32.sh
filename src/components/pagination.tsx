import { Link } from '@tanstack/react-router'
import { localeParam, text, type Locale } from '../lib/i18n'
import { pageNumbers } from '../lib/pagination'

export function Pagination({ page, pageCount, locale, directory }: { page: number; pageCount: number; locale: Locale; directory: 'projects' | 'devices' }) {
  if (pageCount <= 1) return null
  const t = text(locale)
  const to = directory === 'projects' ? '/{-$lang}' : '/{-$lang}/devices'
  const target = (next: number) => ({ to, params: { lang: localeParam(locale) }, search: (previous: Record<string, unknown>) => ({ ...previous, page: next }) })
  return <nav className="pagination" aria-label={t.pagination}>
    {page > 1 ? <Link {...target(page - 1)} rel="prev">← {t.previousPage}</Link> : <span aria-disabled="true">← {t.previousPage}</span>}
    <div className="pagination-pages">{pageNumbers(page, pageCount).map((n, i) => n === 'gap'
      ? <span className="pagination-gap" key={`gap-${i}`}>…</span>
      : n === page ? <span key={n} aria-current="page" aria-label={`${t.pageLabel} ${n}`}>{n}</span>
      : <Link {...target(n)} key={n} aria-label={`${t.pageLabel} ${n}`}>{n}</Link>)}</div>
    {page < pageCount ? <Link {...target(page + 1)} rel="next">{t.nextPage} →</Link> : <span aria-disabled="true">{t.nextPage} →</span>}
  </nav>
}
