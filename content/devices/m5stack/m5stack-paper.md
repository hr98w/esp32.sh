---
id: m5stack-paper
name: M5Paper
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: 带触摸输入的 4.7 英寸电子纸终端。
  en: 4.7-inch e-paper terminal with touch input.
  ja: タッチ操作に対応する4.7インチ電子ペーパー端末。
officialUrl: https://docs.m5stack.com/en/core/m5paper
aliases:
  - M5Stack M5Paper
features:
  - epaper
  - touch
  - battery
  - sd
sources:
  - url: https://m5ware.com/projects/23
  - url: https://docs.m5stack.com/en/core/m5paper
    checkedAt: 2026-10-15T17:58:58+00:00
  - url: https://docs.m5stack.com/zh_CN/core/m5paper
    checkedAt: 2026-10-16T00:06:00+00:00
  - url: https://docs.m5stack.com/ja/core/m5paper
    checkedAt: 2026-10-16T00:06:02+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-D0WDQ6-V3 @ Xtensa® 32-bit LX6 dual-core processor, clock frequency 240MHz
      zh: ESP32-D0WDQ6-V3 @ Xtensa® 32 位 LX6 双核处理器，主频 240MHz
      ja: ESP32-D0WDQ6-V3 @ Xtensa® 32ビット LX6 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 16MB
      zh: 16MB
      ja: 16MB
  - label:
      en: PSRAM
      zh: PSRAM
      ja: PSRAM
    value:
      en: 8MB Quad
      zh: 8MB Quad
      ja: 8MB Quad
  - label:
      en: E-ink Screen
      zh: 墨水屏
      ja: 電子ペーパー
    value:
      en: 'Model: EPD*ED047TC1 / 540 x 960@4.7" / Grayscale: 16 levels / Display area: 58.32 x 103.68mm / Display driver IC: IT8951E'
      zh: '型号：EPD*ED047TC1 / 540 x 960@4.7" / 灰度 : 16 级 / 显示区域 : 58.32 x 103.68mm / 显示驱动芯片 : IT8951E'
      ja: '型番：EPD*ED047TC1 / 540 x 960@4.7" / グレースケール : 16 階調 / 表示領域 : 58.32 x 103.68mm / 表示ドライバ IC : IT8951E'
  - label:
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: 1150mAh@3.7V
      zh: 1150mAh@3.7V
      ja: 1150mAh@3.7V
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: 5V@500mA
      zh: 5V@500mA
      ja: 5V@500mA
  - label:
      en: Interfaces
      zh: 接口
      ja: インターフェース
    value:
      en: USB Type-C x 1, HY2.0-4P x 3, TF-card (microSD) slot
      zh: USB Type-C x 1，HY2.0-4P x 3 ，TF-card (microSD) 卡槽
      ja: USB Type-C x 1、HY2.0-4P x 3、TF カード (microSD) スロット
  - label:
      en: Physical Buttons
      zh: 物理按键
      ja: 物理ボタン
    value:
      en: Rotary switch x 1, reset button x 1
      zh: 拨轮开关 *1 ，复位按键 *1
      ja: ホイッチスイッチ *1、リセットボタン *1
  - label:
      en: RTC
      zh: RTC
      ja: RTC
    value:
      en: BM8563
      zh: BM8563
      ja: BM8563
  - label:
      en: Wi-Fi
      zh: Wi-Fi
      ja: Wi-Fi
    value:
      en: 2.4 GHz Wi-Fi
      zh: 2.4 GHz Wi-Fi
      ja: 2.4 GHz Wi-Fi
  - label:
      en: Product Size
      zh: 产品尺寸
      ja: 製品サイズ
    value:
      en: 118.6 x 67.0 x 10.0mm
      zh: 118.6 x 67.0 x 10.0mm
      ja: 118.6 x 67.0 x 10.0mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 87.1g
      zh: 87.1g
      ja: 87.1g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5paper/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5paper/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/m5paper/M5_PAPER_SCH.pdf
sku: K049
cover: https://static-cdn.m5stack.com/resource/docs/products/core/m5paper/m5paper_02.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/m5paper/m5paper_02.webp
    caption:
      zh: M5Paper 产品图
      en: M5Paper product photo
      ja: M5Paper 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/m5paper
---

Exact model and peripherals reviewed against official M5Stack product documentation.
