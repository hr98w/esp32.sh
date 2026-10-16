import type { Locale } from './i18n'

export const repositoryUrl = 'https://github.com/hr98w/esp32.sh'
export const projectSubmissionLabel = 'submission:project'
export const submissionTemplates: Record<Locale, string> = {
  en: 'submit-project.yml', zh: 'submit-project.zh-CN.yml', ja: 'submit-project.ja.yml',
}
export function projectSubmissionUrl(locale: Locale) {
  return `${repositoryUrl}/issues/new?template=${submissionTemplates[locale]}`
}
