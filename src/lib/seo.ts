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
