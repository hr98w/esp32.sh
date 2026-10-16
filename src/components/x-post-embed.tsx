import { useEffect, useRef, useState } from 'react'
import type { GuidePost } from '../lib/content/schema'
import type { Locale } from '../lib/i18n'

type Widgets = { createTweet: (id: string, target: HTMLElement, options: Record<string, unknown>) => Promise<HTMLElement | undefined> }
declare global { interface Window { twttr?: { widgets?: Widgets } } }
let widgetPromise: Promise<Widgets> | undefined
function loadWidgets(): Promise<Widgets> {
  if (window.twttr?.widgets) return Promise.resolve(window.twttr.widgets)
  if (widgetPromise) return widgetPromise
  widgetPromise = new Promise<Widgets>((resolve, reject) => {
    const script = document.createElement('script')
    const timeout = window.setTimeout(() => fail(), 15000)
    const fail = () => { window.clearTimeout(timeout); script.remove(); reject(new Error('X widgets unavailable')) }
    script.src = 'https://platform.twitter.com/widgets.js'
    script.async = true
    script.onload = () => {
      window.clearTimeout(timeout)
      if (window.twttr?.widgets) resolve(window.twttr.widgets)
      else fail()
    }
    script.onerror = fail
    document.head.appendChild(script)
  }).catch(error => { widgetPromise = undefined; throw error })
  return widgetPromise
}

export function XPostEmbed({ post, locale }: { post: GuidePost; locale: Locale }) {
  const frame = useRef<HTMLDivElement>(null)
  const [loaded, setLoaded] = useState(false)
  useEffect(() => {
    const container = frame.current!
    let cancelled = false
    setLoaded(false)
    // An isolated target prevents a late widget response from touching a newer render.
    const target = document.createElement('div')
    container.replaceChildren(target)
    const render = async () => {
      try {
        const widgets = await loadWidgets()
        if (cancelled) return
        const tweet = await widgets.createTweet(post.url.split('/').pop()!, target, {
          lang: locale === 'zh' ? 'zh-cn' : locale, theme: 'light', dnt: true, conversation: 'none', align: 'center',
        })
        if (!cancelled && tweet) setLoaded(true)
      } catch { /* The original-post link remains usable when X cannot load. */ }
    }
    const observer = typeof IntersectionObserver !== 'undefined' ? new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) { observer!.disconnect(); void render() }
    }, { rootMargin: '400px' }) : undefined
    if (observer) observer.observe(container)
    else void render()
    return () => { cancelled = true; observer?.disconnect(); target.remove() }
  }, [post.url, locale])
  const open = { zh: '在 X 查看原帖 ↗', en: 'Read original on X ↗', ja: 'Xで原文を読む ↗' }[locale]
  return <article className="guide-post" data-guide-post={post.id}>
    <h3>{post.title[locale]}</h3>
    <div ref={frame} className={`x-post-frame${loaded ? ' is-loaded' : ''}`} />
    <a className="x-original" href={post.url} target="_blank" rel="noopener noreferrer">{open}</a>
  </article>
}
