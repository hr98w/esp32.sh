---
id: m5stack-cardputer
name: Cardputer
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的掌上键盘设备，集成屏幕、扬声器等外设。
  en: A handheld M5Stack keyboard device with a display, speaker, and other integrated peripherals.
  ja: ディスプレイやスピーカーを搭載した、M5Stackの小型キーボードデバイス。
officialUrl: https://docs.m5stack.com/en/core/Cardputer
aliases:
  - M5Cardputer
  - M5Stack Cardputer
features:
  - display
  - keyboard
  - audio
sources:
  - url: https://docs.m5stack.com/en/core/Cardputer
    checkedAt: 2026-10-15T17:32:13+00:00
  - url: https://docs.m5stack.com/zh_CN/core/Cardputer
    checkedAt: 2026-10-16T00:05:32+00:00
  - url: https://docs.m5stack.com/ja/core/Cardputer
    checkedAt: 2026-10-16T00:05:34+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-S3FN8 @ Xtensa® 32-bit LX7 dual-core processor, clock frequency 240MHz
      zh: ESP32-S3FN8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz
      ja: ESP32-S3FN8 @ Xtensa® 32ビット LX7 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 8MB
      zh: 8MB
      ja: 8MB
  - label:
      en: Screen
      zh: 屏幕
      ja: 画面
    value:
      en: ST7789V2 @ 1.14 inch, 240 x 135 px
      zh: ST7789V2@1.14 Inch, 240 x 135px
      ja: ST7789V2@1.14 インチ，240 x 135px
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: MEMS microphone @ SPM1423
      zh: MEMS 麦克风 @SPM1423
      ja: MEMS マイク @SPM1423
  - label:
      en: Speaker
      zh: 腔体喇叭
      ja: スピーカー
    value:
      en: 8 Ω @ 1 W I2S @ NS4168
      zh: 8Ω@1W / I2S@NS4168
      ja: 8 Ω@1W I2S@NS4168
  - label:
      en: Keyboard
      zh: 键盘
      ja: キーボード
    value:
      en: 56 keys (4 x 14)
      zh: 56 按键 (4 x 14)
      ja: 56 キー (4 x 14)
  - label:
      en: Battery Capacity
      zh: 电池容量
      ja: バッテリー容量
    value:
      en: 120 mAh + 1400 mAh (in base)
      zh: 120mAh+1400mAh（底座中）
      ja: 120 mAh + 1400 mAh（ベース部）
  - label:
      en: USB
      zh: USB
      ja: USB
    value:
      en: USB OTG, USB Serial/JTAG
      zh: USB OTG, USB Serial/JTAG
      ja: USB OTG, USB Serial/JTAG
  - label:
      en: Buttons
      zh: 按键
      ja: ボタン
    value:
      en: 1 x Reset button + 1 x User button
      zh: 1 x 复位按键 + 1 x 用户按键
      ja: 1 x リセットボタン + 1 x ユーザボタン
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
      en: 84.0 x 54.0 x 19.7 mm
      zh: 84.0 x 54.0 x 19.7mm
      ja: 84.0 x 54.0 x 19.7 mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 92.3 g
      zh: 92.3g
      ja: 92.3 g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5cardputer/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/cardputer/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/481/Sch_M5Cardputer.pdf
sku: K132
cover: https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-60261bcd-a23f-40e6-994d-ad97477dcec4.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/Cardputer/img-60261bcd-a23f-40e6-994d-ad97477dcec4.webp
    caption:
      zh: Cardputer 产品图
      en: Cardputer product photo
      ja: Cardputer 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/Cardputer
---

本记录指原版 Cardputer，不包含 Cardputer ADV。硬件版本与规格以官方文档为准。
