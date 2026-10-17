import { locales, localizedPath } from './i18n'
import type { Locale } from './i18n'

/** Content pages share one stable identity across language variants. */
export function languageLinks(path: string, locale: Locale, page = 1) {
  const site = 'https://esp32.sh'
  const suffix = page > 1 ? `?page=${page}` : ''
  return [
    { rel: 'canonical', href: site + localizedPath(path, locale) + suffix },
    ...locales.map(language => ({ rel: 'alternate', hrefLang: language === 'zh' ? 'zh-CN' : language, href: site + localizedPath(path, language) + suffix })),
    { rel: 'alternate', hrefLang: 'x-default', href: site + localizedPath(path, 'en') + suffix },
  ]
}

export const defaultSocialImage = 'https://esp32.sh/social-card.png'

/** Emit sharing metadata in server HTML; crawlers do not need client-side JS. */
export function pageMeta({ title, description, path, locale, page = 1, image }: {
  title: string; description?: string; path: string; locale: Locale; page?: number; image?: string
}) {
  let shareImage = defaultSocialImage
  try {
    const candidate = new URL(image ?? '')
    if (candidate.protocol === 'https:' && !candidate.pathname.toLowerCase().endsWith('.svg')) shareImage = candidate.href
  } catch { /* Missing or unsuitable cover uses our raster brand card. */ }
  const summary = description ?? ''
  const url = languageLinks(path, locale, page)[0].href
  return [
    { title }, { name: 'description', content: summary },
    { property: 'og:type', content: 'website' },
    { property: 'og:site_name', content: 'esp32.sh' },
    { property: 'og:title', content: title },
    { property: 'og:description', content: summary },
    { property: 'og:url', content: url },
    { property: 'og:locale', content: { en: 'en_US', zh: 'zh_CN', ja: 'ja_JP' }[locale] },
    { property: 'og:image', content: shareImage },
    { property: 'og:image:alt', content: shareImage === defaultSocialImage ? 'esp32.sh — Find your next ESP32 project' : title },
    ...(shareImage === defaultSocialImage ? [
      { property: 'og:image:type', content: 'image/png' },
      { property: 'og:image:width', content: '1200' },
      { property: 'og:image:height', content: '630' },
    ] : []),
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: title },
    { name: 'twitter:description', content: summary },
    { name: 'twitter:image', content: shareImage },
    { name: 'twitter:image:alt', content: shareImage === defaultSocialImage ? 'esp32.sh — Find your next ESP32 project' : title },
  ]
}
