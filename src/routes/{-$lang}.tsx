import { createFileRoute, Link, Outlet, notFound, redirect, useLocation } from '@tanstack/react-router'
import { projectSubmissionUrl, repositoryUrl } from '../lib/submissions'
import { isLocale, locales, languageNames, text, resolveLocale, localeParam, localizedPath } from '../lib/i18n'

export const Route = createFileRoute('/{-$lang}')({
  beforeLoad: ({ params, location }) => {
    if (params.lang !== undefined && !isLocale(params.lang)) throw notFound()
    if (params.lang === 'en') throw redirect({ href: localizedPath(location.pathname, 'en') + location.searchStr, statusCode: 301, replace: true })
  },
  component: LocaleLayout,
})

function LocaleLayout() {
  const lang = resolveLocale(Route.useParams().lang)
  const t = text(lang)
  const location = useLocation()
  return <div className="desktop">
    <header className="masthead"><Link className="logo" to="/{-$lang}" params={{ lang: localeParam(lang) }}><img className="logo-icon" src="/logo.svg" width="32" height="32" alt="" aria-hidden="true" /><span className="logo-wordmark">esp32<span>.sh</span></span></Link>
      <nav><Link to="/{-$lang}" params={{ lang: localeParam(lang) }} activeOptions={{ exact: true }}>{t.projects}</Link><Link to="/{-$lang}/devices" params={{ lang: localeParam(lang) }}>{t.devices}</Link><Link to="/{-$lang}/tools" params={{ lang: localeParam(lang) }}>{t.tools}</Link><Link to="/{-$lang}/guides" params={{ lang: localeParam(lang) }}>{t.guides}</Link></nav>
      <div className="masthead-actions"><select className="language" aria-label={t.language} value={lang} onChange={(event) => {
        const path = localizedPath(location.pathname, resolveLocale(event.target.value))
        window.location.assign(path + location.searchStr)
      }}>{locales.map((locale) => <option key={locale} value={locale}>{languageNames[locale]}</option>)}</select><a className="submit-project" href={projectSubmissionUrl(lang)} target="_blank" rel="noopener noreferrer">{t.submitProject}</a></div>
    </header>
    <main className="window"><div className="titlebar">esp32.sh</div><Outlet /></main>
    <footer><details><summary>{t.about}</summary><p>{t.aboutText}</p><p>{t.policy}</p><h3>{t.contribute}</h3><p>{t.contributeText} <a href={repositoryUrl} target="_blank" rel="noopener noreferrer">GitHub ↗</a></p></details><span>SMALL CHIPS. BIG POSSIBILITIES.</span></footer>
  </div>
}
