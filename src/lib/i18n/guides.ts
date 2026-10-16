import type { Locale } from './index'
const messages = {
  zh: {
    title: '新手指南', intro: '先挑一个想玩的项目，再找适合的设备。', picks: '从这些玩法开始', device: '推荐设备', project: '开源项目',
    budget: { low: '低预算 · 基础开发板', medium: '中等预算 · 集成设备', high: '较高预算 · 成品机器人' },
    budgetNote: '预算为设备之间的相对参考；套装、配件和服务费用请以购买时为准。',
    tryTitle: '想先在浏览器里试试？', tryText: 'Wokwi 可以模拟部分 ESP32 项目，实际外设和固件支持以模拟器为准。', tools: '查看模拟与烧录工具 →',
    reading: '看看大家怎么入坑', readingNote: '原帖保留原语言，接近屏幕时加载。若未显示，可直接打开 X 原帖。',
  },
  en: {
    title: 'Start Here', intro: 'Find something you want to make. Then choose a device for it.', picks: 'Pick your first project', device: 'Suggested devices', project: 'Open-source projects',
    budget: { low: 'Lower budget · development board', medium: 'Mid budget · integrated device', high: 'Higher budget · complete robot' },
    budgetNote: 'Budget labels compare hardware options. Check current kit contents, accessories and service costs before buying.',
    tryTitle: 'Try something in your browser first?', tryText: 'Wokwi simulates selected ESP32 projects. Peripheral and firmware support depends on the simulator.', tools: 'Explore simulation and flashing tools →',
    reading: 'How others got started', readingNote: 'Posts stay in their original language and load near the screen. If an embed is unavailable, open the original on X.',
  },
  ja: {
    title: 'はじめて', intro: 'やってみたいことを見つけてから、デバイスを選ぼう。', picks: '最初のプロジェクトを選ぶ', device: 'おすすめデバイス', project: 'オープンソースプロジェクト',
    budget: { low: '低予算 · 開発ボード', medium: '中程度 · 一体型デバイス', high: '高め · 完成品ロボット' },
    budgetNote: '予算はハードウェア間の相対的な目安です。同梱品、周辺部品、サービス料金は購入時にご確認ください。',
    tryTitle: 'まずブラウザーで試してみる？', tryText: 'Wokwiは一部のESP32プロジェクトをシミュレーションできます。対応する周辺機器やファームウェアはシミュレーターに依存します。', tools: 'シミュレーション・書き込みツールへ →',
    reading: 'みんなの入門体験', readingNote: '投稿は原文のまま、画面に近づくと読み込みます。表示できない場合はXの原文を開けます。',
  },
}
export const guideText = (locale: Locale) => messages[locale]
