export const locales = ['zh', 'en', 'ja'] as const
export type Locale = (typeof locales)[number]
export const languageNames: Record<Locale, string> = { zh: '中文', en: 'English', ja: '日本語' }
export function isLocale(value: unknown): value is Locale { return locales.includes(value as Locale) }
export const localeParam = (locale: Locale) => locale === 'en' ? undefined : locale
export const resolveLocale = (value: unknown): Locale => isLocale(value) ? value : 'en'
export function localizedPath(pathname: string, locale: Locale): string {
  const parts = pathname.split('/').filter(Boolean)
  if (isLocale(parts[0])) parts.shift()
  return '/' + (locale === 'en' ? parts : [locale, ...parts]).join('/')
}
export const htmlLang = (locale: Locale) => locale === 'zh' ? 'zh-CN' : locale

const messages = {
  zh: {
    tools: '工具', guides: '新手指南', submitProject: '提交项目', githubContribute: '在 GitHub 点 Star 或参与贡献',
    pagination: '分页', previousPage: '上一页', nextPage: '下一页', pageLabel: '第', showing: '当前',
    sort: '排序', checked: '采集日期', metricsPending: 'Star 待更新', archived: '已归档', noDevice: '未找到型号。侧栏仅列出已有相关项目的设备。', customHardware: '自定义硬件 · 配置参考仓库', compatibilityPending: '具体型号适配待核验', deviceCount: '个设备', allChips: '所有芯片', allFeatures: '所有特征', deviceEmpty: '没有匹配的设备。', contribute: '提交项目 / 设备', contributeText: '推荐项目请点右上角“提交项目”，填写 Issue，无需写代码。修改网站或维护内容请提交 Pull Request。', sources: '资料来源', sourceNote: '信息据公开资料整理，未进行硬件实测；硬件版本与支持范围请查看上游。', policy: '项目初次收录需有 README、明确的开源许可及至少 10 个 GitHub Star。Star 为采集快照；本站介绍为编辑摘要，详情以上游为准。',
    projects: '项目', devices: '设备', headline: '发现好玩的开源项目', intro: '选一台你手里的设备，看看它还能玩什么。', myDevice: '我的设备', allDevices: '所有设备', deviceSearch: '搜索型号或厂商…', search: '搜索项目、用途或作者…', allTags: '全部项目', stars: 'Star 最多', newest: '最新收录', empty: '暂时没有匹配的项目。', clear: '清除筛选', browseDevices: '浏览设备目录 →', hardwareIntro: '从开发板到带屏幕、键盘的集成设备。', related: '这台设备能玩什么？', maker: '厂商', chip: '芯片', official: '设备资料 ↗', back: '← 设备目录', open: 'GitHub ↗', projectCount: '个项目', about: '关于 / 收录说明', aboutText: '根据手里的具体设备寻找开源项目。项目需要有明确的开源许可证，适配关系参考上游资料，相同芯片不代表兼容。', missing: '暂未收录相关项目。', reference: '适配依据', language: '选择语言', manufacturer: '所有厂商', imageAlt: '项目封面', notFound: '页面不存在。', home: '返回项目目录',
  },
  en: {
    tools: 'Tools', guides: 'Start Here', submitProject: 'Submit Project', githubContribute: 'Star or contribute to esp32.sh on GitHub',
    pagination: 'Pagination', previousPage: 'Previous', nextPage: 'Next', pageLabel: 'Page', showing: 'Showing',
    sort: 'Sort', checked: 'Collected', metricsPending: 'Stars pending', archived: 'Archived', noDevice: 'No matching model. Only devices with listed projects appear here.', customHardware: 'Custom hardware · see repository', compatibilityPending: 'Exact device support under review', deviceCount: 'devices', allChips: 'All chips', allFeatures: 'All features', deviceEmpty: 'No matching devices.', contribute: 'Submit a project / device', contributeText: 'Recommend a project through Submit Project: open an issue, no code required. Use a pull request for website or content changes.', sources: 'Sources', sourceNote: 'Information is compiled from public documentation and has not been hardware-tested here. Check upstream for revisions and support details.', policy: 'New projects need a README, an explicit open-source license, and at least 10 GitHub stars. Stars are dated snapshots. Descriptions are editorial summaries; refer to upstream for details.',
    projects: 'Projects', devices: 'Devices', headline: 'Find your next ESP32 project', intro: 'Pick a device you own. See what else it can do.', myDevice: 'My device', allDevices: 'All devices', deviceSearch: 'Search a model or maker…', search: 'Search projects, ideas, or authors…', allTags: 'All projects', stars: 'Most starred', newest: 'Newly added', empty: 'No matching projects yet.', clear: 'Clear filters', browseDevices: 'Browse device directory →', hardwareIntro: 'Development boards and devices with displays, keyboards, and more.', related: 'What can this device do?', maker: 'Manufacturer', chip: 'Chip', official: 'Device documentation ↗', back: '← Device directory', open: 'GitHub ↗', projectCount: 'projects', about: 'About / Listing policy', aboutText: 'Find open-source projects for the device you own. Projects need an explicit open-source license. Hardware support follows upstream documentation; a shared chip does not guarantee compatibility.', missing: 'No related projects listed yet.', reference: 'Support source', language: 'Select language', manufacturer: 'All manufacturers', imageAlt: 'Project cover', notFound: 'Page not found.', home: 'Browse projects',
  },
  ja: {
    tools: 'ツール', guides: 'はじめて', submitProject: 'プロジェクトを推薦', githubContribute: 'GitHubでStarやコントリビューション',
    pagination: 'ページ送り', previousPage: '前へ', nextPage: '次へ', pageLabel: 'ページ', showing: '表示',
    sort: '並び順', checked: '取得日', metricsPending: 'Star確認待ち', archived: 'アーカイブ済み', noDevice: '該当モデルはありません。関連プロジェクトがあるデバイスのみ表示しています。', customHardware: '独自ハードウェア · 詳細はリポジトリへ', compatibilityPending: '対応モデルは確認中', deviceCount: 'デバイス', allChips: 'すべてのチップ', allFeatures: 'すべての機能', deviceEmpty: '一致するデバイスがありません。', contribute: 'プロジェクト・デバイスを投稿', contributeText: 'プロジェクトの推薦は右上のボタンからIssueを投稿してください。コードの作成は不要です。サイトや掲載内容の変更はプルリクエストでお願いします。', sources: '情報源', sourceNote: '公開資料に基づく情報です。当サイトでは実機検証を行っていません。ハードウェアの版や対応範囲は開発元でご確認ください。', policy: 'プロジェクトの新規掲載にはREADME、明示的なオープンソースライセンス、10以上のGitHub Starが必要です。Star数は取得時点の値です。紹介文は編集した要約であり、詳細は開発元の資料をご覧ください。',
    projects: 'プロジェクト', devices: 'デバイス', headline: 'ESP32で、次は何を作ろう？', intro: '手元のデバイスを選んで、新しい使い道を見つけよう。', myDevice: '手元のデバイス', allDevices: 'すべてのデバイス', deviceSearch: 'モデル名やメーカーを検索…', search: 'プロジェクトや用途を検索…', allTags: 'すべて', stars: 'Starが多い順', newest: '掲載が新しい順', empty: '一致するプロジェクトがありません。', clear: '絞り込みを解除', browseDevices: 'デバイス一覧を見る →', hardwareIntro: '開発ボードから画面・キーボード付きのデバイスまで。', related: 'このデバイスで何ができる？', maker: 'メーカー', chip: 'チップ', official: 'デバイス資料 ↗', back: '← デバイス一覧', open: 'GitHub ↗', projectCount: '件', about: 'このサイト・掲載方針', aboutText: '手元のデバイスからオープンソースプロジェクトを探せます。明示的なオープンソースライセンスが必要です。対応関係は開発元の資料に基づき、同じチップでも互換性は保証されません。', missing: '関連プロジェクトはまだ登録されていません。', reference: '対応情報の出典', language: '言語を選択', manufacturer: 'すべてのメーカー', imageAlt: 'プロジェクト画像', notFound: 'ページが見つかりません。', home: 'プロジェクト一覧へ',
  },
}
export const text = (locale: Locale) => messages[locale]

const tagNames: Record<string, Record<Locale, string>> = {
  agent: {zh:'智能体', en:'Agents', ja:'AIエージェント'},
  security: {zh:'安全测试', en:'Security', ja:'セキュリティ'},
  demo: {zh:'演示', en:'Demos', ja:'デモ'},
  tools: {zh:'工具', en:'Tools', ja:'ツール'}, home: {zh:'智能家居', en:'Smart home', ja:'スマートホーム'},
  display: {zh:'显示', en:'Displays', ja:'ディスプレイ'}, audio: {zh:'音频', en:'Audio', ja:'オーディオ'},
  ai: {zh:'AI', en:'AI', ja:'AI'}, games: {zh:'游戏', en:'Games', ja:'ゲーム'},
  radio: {zh:'无线通信', en:'Radio', ja:'無線通信'}, camera: {zh:'摄像头', en:'Cameras', ja:'カメラ'},
  learning: {zh:'学习', en:'Learning', ja:'学習'}, wearable: {zh:'穿戴', en:'Wearables', ja:'ウェアラブル'},
  graphics: {zh:'图形', en:'Graphics', ja:'グラフィックス'}, music: {zh:'音乐', en:'Music', ja:'音楽'},
  automation: {zh:'自动化', en:'Automation', ja:'自動化'}, networking: {zh:'网络', en:'Networking', ja:'ネットワーク'},
}
export const tagLabel = (tag: string, locale: Locale) => tagNames[tag]?.[locale] ?? tag
const featureNames: Record<string, Record<Locale, string>> = {
  servo:{zh:'舵机',en:'Servo',ja:'サーボ'},
  display:{zh:'屏幕',en:'Display',ja:'画面'}, touch:{zh:'触摸',en:'Touch',ja:'タッチ'}, keyboard:{zh:'键盘',en:'Keyboard',ja:'キーボード'},
  audio:{zh:'音频',en:'Audio',ja:'オーディオ'}, microphone:{zh:'麦克风',en:'Microphone',ja:'マイク'}, speaker:{zh:'扬声器',en:'Speaker',ja:'スピーカー'},
  imu:{zh:'运动传感器',en:'Motion sensor',ja:'モーションセンサー'}, battery:{zh:'电池供电',en:'Battery power',ja:'バッテリー'},
  epaper:{zh:'电子纸',en:'E-paper',ja:'電子ペーパー'}, usb:{zh:'USB',en:'USB',ja:'USB'}, gpio:{zh:'GPIO',en:'GPIO',ja:'GPIO'},
  ethernet:{zh:'以太网',en:'Ethernet',ja:'Ethernet'}, camera:{zh:'摄像头',en:'Camera',ja:'カメラ'}, lora:{zh:'LoRa',en:'LoRa',ja:'LoRa'},
  gps:{zh:'定位',en:'GNSS',ja:'GNSS'}, encoder:{zh:'旋转编码器',en:'Rotary encoder',ja:'ロータリーエンコーダー'},
  rfid:{zh:'RFID',en:'RFID',ja:'RFID'}, subghz:{zh:'Sub-GHz',en:'Sub-GHz',ja:'Sub-GHz'}, sd:{zh:'存储卡',en:'Memory card',ja:'メモリーカード'},
  rs485:{zh:'RS-485',en:'RS-485',ja:'RS-485'}, rgb:{zh:'RGB 灯',en:'RGB light',ja:'RGBライト'},
}
export const featureLabel = (feature: string, locale: Locale) => featureNames[feature]?.[locale] ?? feature

export function formatCount(count: number, unit: 'project' | 'device', locale: Locale) {
  const t = text(locale)
  const label = locale === 'en' && count === 1 ? unit : unit === 'project' ? t.projectCount : t.deviceCount
  return `${count.toLocaleString(locale)} ${label}`
}

export function formatPageCount(total: number, start: number, end: number, unit: 'project' | 'device', locale: Locale) {
  const count = formatCount(total, unit, locale)
  return total ? `${count} · ${text(locale).showing} ${start.toLocaleString(locale)}–${end.toLocaleString(locale)}` : count
}
