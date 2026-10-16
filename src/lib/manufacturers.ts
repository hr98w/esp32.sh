import type { Locale } from './i18n'

type Manufacturer = { id: string; name: string }

// Established Chinese names; other brands keep their original name.
const chineseNames: Record<string, string> = {
  lckfb: '立创', // https://wiki.lckfb.com/
  waveshare: '微雪', // https://www.waveshare.net/
  espressif: '乐鑫', // https://www.espressif.com/zh-hans/company/about-espressif
  'seeed-studio': '矽递', // https://wiki.seeedstudio.com/cn/Getting_Started/
  dfrobot: '智位', // https://www.dfrobot.cn/about
  'ai-thinker': '安信可', // https://ai-thinker.com/
}

export function manufacturerLabel(manufacturer: Manufacturer, locale: Locale) {
  const chinese = chineseNames[manufacturer.id]
  return locale === 'zh' && chinese ? `${chinese} ${manufacturer.name}` : manufacturer.name
}

export function manufacturerSearchNames(manufacturer: Manufacturer) {
  const chinese = chineseNames[manufacturer.id]
  return chinese ? [manufacturer.name, chinese, `${chinese} ${manufacturer.name}`] : [manufacturer.name]
}
