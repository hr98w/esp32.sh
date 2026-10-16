import type { DeviceType } from '../device-types'
import type { Locale } from './index'

const messages = {
  zh: { type: '设备类型', allTypes: '全部', specs: '关键硬件', gettingStarted: '开始使用', factory: '开箱可以体验', revisions: '版本与注意事项', images: '更多设备图片', imageCredit: '图片来源', price: '官方参考价', priceNote: '采集时的价格；运费、税费及当前售价以商店为准。', store: '官方商店 ↗', source: '查看原始资料 ↗', gallerySource: '查看图片来源 ↗' },
  en: { type: 'Device type', allTypes: 'All', specs: 'Key hardware', gettingStarted: 'Getting started', factory: 'Try it out of the box', revisions: 'Hardware revisions & notes', images: 'More device images', imageCredit: 'Image source', price: 'Official reference price', priceNote: 'A dated price snapshot. Check the store for current pricing, shipping, and taxes.', store: 'Official store ↗', source: 'View source ↗', gallerySource: 'View image source ↗' },
  ja: { type: 'デバイスの種類', allTypes: 'すべて', specs: '主なハードウェア', gettingStarted: 'はじめに', factory: '開封して体験できること', revisions: 'ハードウェアの版と注意事項', images: 'その他の製品画像', imageCredit: '画像の出典', price: '公式参考価格', priceNote: '取得時点の価格です。現在の価格、送料、税金はストアでご確認ください。', store: '公式ストア ↗', source: '元の資料を見る ↗', gallerySource: '画像の出典を見る ↗' },
}
export const deviceText = (locale: Locale) => messages[locale]

const typeNames: Record<DeviceType, Record<Locale, string>> = {
  'integrated-device': { zh: '集成设备', en: 'Integrated devices', ja: '一体型デバイス' },
  'functional-board': { zh: '功能开发板', en: 'Specialized boards', ja: '機能特化ボード' },
  'general-board': { zh: '通用开发板', en: 'General-purpose boards', ja: '汎用開発ボード' },
  module: { zh: '模组', en: 'Modules', ja: 'モジュール' },
}
export const deviceTypeLabel = (type: DeviceType, locale: Locale) => typeNames[type][locale]
