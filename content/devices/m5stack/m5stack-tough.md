---
id: m5stack-tough
name: Tough
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: 带封闭外壳和触控屏的工业控制开发终端。
  en: Industrial-control development terminal with an enclosed case and touchscreen.
  ja: ケースとタッチ画面を備えた産業制御用の開発端末。
officialUrl: https://docs.m5stack.com/en/core/tough
aliases:
  - M5Stack Tough
features:
  - display
  - touch
  - speaker
  - sd
sources:
  - url: https://m5ware.com/projects/453
  - url: https://docs.m5stack.com/en/core/tough
    checkedAt: 2026-10-15T17:59:01+00:00
  - url: https://docs.m5stack.com/zh_CN/core/tough
    checkedAt: 2026-10-16T00:06:36+00:00
  - url: https://docs.m5stack.com/ja/core/tough
    checkedAt: 2026-10-16T00:06:38+00:00
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
      en: IPS LCD
      zh: IPS LCD
      ja: IPS LCD
    value:
      en: 2.0" 320 x 240 ILI9342C full-color display, max brightness 853 nits
      zh: 2.0" 320 x 240 ILI9342C 全彩显示屏，最大亮度 853nit
      ja: 2.0" 320 × 240 ILI9342C フルカラー、最大輝度 853 nit
  - label:
      en: Touch Controller
      zh: 触控面板驱动芯片
      ja: タッチ IC
    value:
      en: CHSC6540
      zh: CHSC6540
      ja: CHSC6540
  - label:
      en: Speaker Setup
      zh: 扬声器配置
      ja: スピーカー
    value:
      en: NS4168 16-bit I2S amplifier + 1W speaker
      zh: NS4168 16bit I2S 功放 + 1W 扬声器
      ja: NS4168 16-bit I2S アンプ + 1 W スピーカー
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: USB (5V@500mA) / RS485 interface power input (6 ~ 24V@1A)
      zh: USB (5V @ 500mA) / RS485 接口输入电源 (6 ~ 24V @ 1A)
      ja: USB（5V @ 500mA） / RS485 インターフェース入力電源（6 ~ 24V @ 1A）
  - label:
      en: Interfaces
      zh: 接口
      ja: インターフェース
    value:
      en: USB Type-C x 1, HY2.0-4P x 4 (RS485 / I2C / GPIO / UART interfaces)
      zh: USB Type-C x 1, HY2.0-4P x 4 (RS485 / I2C / GPIO / UART 接口)
      ja: USB Type-C x 1、HY2.0-4P x 4（RS485 / I2C / GPIO / UART インターフェース）
  - label:
      en: RTC Clock Chip
      zh: RTC 时钟芯片
      ja: RTC チップ
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
      en: 76.0 x 58.0 x 41.6 mm
      zh: 76.0 x 58.0 x 41.6mm
      ja: 76.0 × 58.0 × 41.6 mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 117.5 g
      zh: 117.5g
      ja: 117.5 g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5tough/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5tough/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough-Schematics-PDF.pdf
sku: K034
cover: https://static-cdn.m5stack.com/resource/docs/products/core/tough/tough_06.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/tough/tough_06.webp
    caption:
      zh: Tough 产品图
      en: Tough product photo
      ja: Tough 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/tough
---

Exact model and peripherals reviewed against official M5Stack product documentation.
