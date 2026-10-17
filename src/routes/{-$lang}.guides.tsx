import { createFileRoute, Link } from '@tanstack/react-router'
import { catalog } from '../lib/content'
import { guides } from '../lib/guides'
import { localeParam, resolveLocale } from '../lib/i18n'
import { guideText } from '../lib/i18n/guides'
import { languageLinks, pageMeta } from '../lib/seo'
import { DeviceImage } from '../components/device-image'
import { XPostEmbed } from '../components/x-post-embed'

export const Route = createFileRoute('/{-$lang}/guides')({
  head: ({ params }) => {
    const locale = resolveLocale(params.lang), t = guideText(locale)
    return { meta: pageMeta({ title: `${t.title} — esp32.sh`, description: t.intro, path: '/guides', locale }), links: languageLinks('/guides', locale) }
  },
  component: Guides,
})
function Guides() {
  const locale = resolveLocale(Route.useParams().lang), t = guideText(locale)
  return <section className="content guide-directory">
    <h1>{t.title}</h1><p className="intro">{t.intro}</p>
    <h2>{t.picks}</h2>
    <div className="guide-picks">{guides.picks.map((pick, index) => {
      const devices = pick.deviceIds.map(id => catalog.devices.find(device => device.id === id)!)
      return <article className="guide-pick" key={pick.id} data-guide-pick={pick.id}>
        <div className="guide-pick-top"><span className="guide-number">0{index + 1}</span><span>{t.budget[pick.budget]}</span></div>
        <h3>{pick.title[locale]}</h3><p>{pick.summary[locale]}</p>
        <div className="guide-hardware"><DeviceImage src={devices[0].cover} name={devices[0].name} maker={devices[0].manufacturer.name} /><div><strong>{t.device}</strong>{devices.map(device => <Link key={device.id} to="/{-$lang}/devices/$deviceId" params={{ lang: localeParam(locale), deviceId: device.id }}>{locale === 'zh' && device.manufacturer.id === 'lckfb' ? '立创实战派 ESP32-S3' : device.name} →</Link>)}</div></div>
        <p className="guide-effort">{pick.effort[locale]}</p>
        <div className="guide-projects"><strong>{t.project}</strong>{pick.projectIds.map(id => { const project = catalog.projects.find(p => p.id === id)!; return <Link key={id} to="/{-$lang}/projects/$projectId" params={{ lang: localeParam(locale), projectId: id }}>{project.name} →</Link> })}</div>
        <a className="guide-start" href={pick.resource.url} target="_blank" rel="noopener noreferrer">{pick.resource.label[locale]}</a>
      </article>
    })}</div>
    <p className="guide-fineprint">{t.budgetNote}</p>
    <aside className="guide-try"><div><h3>{t.tryTitle}</h3><p>{t.tryText}</p></div><Link to="/{-$lang}/tools" params={{ lang: localeParam(locale) }} search={{ category: 'simulation' }}>{t.tools}</Link></aside>
    <div className="guide-reading"><h2>{t.reading}</h2><p>{t.readingNote}</p>
      <div className="guide-posts">{guides.posts.map(post => <XPostEmbed key={post.id} post={post} locale={locale} />)}</div>
    </div>
  </section>
}
