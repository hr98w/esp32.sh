import type { Locale } from './index'

const messages = {
  en: {
    title: 'ESP32 toolbox', intro: 'Flash firmware, simulate circuits, debug devices, and create display assets.',
    search: 'Search tools or tasks…', all: 'All tools', empty: 'No matching tools.', clear: 'Clear filters',
    open: 'Open tool ↗', visit: 'Get tool ↗', source: 'Sources', reviewed: 'Reviewed', openSource: 'Open source',
    note: 'Check each tool’s documentation for supported hardware, connection requirements, and current plans.',
    category: { flashing: 'Flashing & management', simulation: 'Simulation', 'coding-debugging': 'Coding & debugging', 'display-assets': 'Displays & assets' },
    runtime: { browser: 'Browser', desktop: 'Desktop app', cli: 'Command line' },
    pricing: { free: 'Free', freemium: 'Free + paid', paid: 'Paid', unspecified: 'See pricing' },
    sourceType: { 'open-source': 'Open source', 'hosted-service': 'Online service', 'official-tool': 'Official tool' },
  },
  zh: {
    title: 'ESP32 工具箱', intro: '烧录固件、模拟电路、调试设备，制作屏幕界面与素材。',
    search: '搜索工具或用途…', all: '全部工具', empty: '没有匹配的工具。', clear: '清除筛选',
    open: '打开工具 ↗', visit: '获取工具 ↗', source: '资料来源', reviewed: '核验', openSource: '开源',
    note: '具体硬件支持、连接要求和最新收费方案，请查看工具官方说明。',
    category: { flashing: '烧录与管理', simulation: '模拟仿真', 'coding-debugging': '编程调试', 'display-assets': '屏幕与素材' },
    runtime: { browser: '浏览器', desktop: '桌面应用', cli: '命令行' },
    pricing: { free: '免费', freemium: '免费 + 付费', paid: '付费', unspecified: '费用见官网' },
    sourceType: { 'open-source': '开源', 'hosted-service': '在线服务', 'official-tool': '官方工具' },
  },
  ja: {
    title: 'ESP32 ツールボックス', intro: 'ファームウェアの書き込み、回路のシミュレーション、デバッグ、画面素材の作成に。',
    search: 'ツールや用途を検索…', all: 'すべて', empty: '一致するツールがありません。', clear: '絞り込みを解除',
    open: 'ツールを開く ↗', visit: 'ツールを入手 ↗', source: '情報源', reviewed: '確認日', openSource: 'オープンソース',
    note: '対応ハードウェア、接続条件、最新の料金プランは各ツールの公式資料をご確認ください。',
    category: { flashing: '書き込み・管理', simulation: 'シミュレーション', 'coding-debugging': '開発・デバッグ', 'display-assets': '画面・素材' },
    runtime: { browser: 'ブラウザー', desktop: 'デスクトップ', cli: 'コマンドライン' },
    pricing: { free: '無料', freemium: '無料・有料', paid: '有料', unspecified: '料金は公式へ' },
    sourceType: { 'open-source': 'オープンソース', 'hosted-service': 'オンラインサービス', 'official-tool': '公式ツール' },
  },
}
export const toolText = (locale: Locale) => messages[locale]
export function formatToolCount(count: number, locale: Locale) {
  const n = count.toLocaleString(locale)
  return locale === 'zh' ? `${n} 个工具` : locale === 'ja' ? `${n} ツール` : `${n} ${count === 1 ? 'tool' : 'tools'}`
}
