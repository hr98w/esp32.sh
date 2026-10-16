---
id: m5stack-basic
name: BASIC
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的可堆叠的模块化控制器，采用 ESP32，配有屏幕、扬声器、GPIO 扩展。
  en: M5Stack stackable modular controller based on ESP32, with display, speaker, GPIO expansion.
  ja: ESP32を搭載したM5Stackの積み重ね式のモジュール型コントローラー。ディスプレイ、スピーカー、GPIO拡張を備えています。
officialUrl: https://docs.m5stack.com/en/core/basic
aliases:
  - M5Stack-Core-ESP32
features:
  - display
  - speaker
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/m5stack-core-esp32/
    checkedAt: 2026-10-15T17:23:32+00:00
  - url: https://docs.m5stack.com/en/core/basic
    checkedAt: 2026-10-15T17:27:19+00:00
  - url: https://docs.m5stack.com/zh_CN/core/basic
    checkedAt: 2026-10-16T00:05:28+00:00
  - url: https://docs.m5stack.com/ja/core/basic
    checkedAt: 2026-10-16T00:05:30+00:00
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
      en: IPS Display
      zh: IPS 屏幕
      ja: IPS ディスプレイ
    value:
      en: 2-inch, 320 × 240 Color TFT LCD, ILI9342C, max brightness 853 nit
      zh: 2 inch，320x240 Colorful TFT LCD，ILI9342C，最高亮度 853nit
      ja: 2 inch，320x240 カラフル TFT LCD，ILI9342C，最大輝度 853nit
  - label:
      en: Speaker
      zh: 扬声器
      ja: スピーカー
    value:
      en: 1W-0928
      zh: 1W-0928
      ja: 1W-0928
  - label:
      en: Battery
      zh: 锂电池
      ja: リチウム電池
    value:
      en: 110 mAh @ 3.7 V
      zh: 110mAh @ 3.7V
      ja: 110mAh @ 3.7V
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: 5V@500 mA
      zh: 5V@500mA
      ja: 5V@500mA
  - label:
      en: Host Interface
      zh: 主机接口
      ja: ホストインターフェース
    value:
      en: USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1
      zh: USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1
      ja: USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1
  - label:
      en: Buttons
      zh: 按键
      ja: ボタン
    value:
      en: Custom buttons × 3
      zh: 自定义按键 x 3
      ja: カスタムボタン x 3
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
      en: 54.0 × 54.0 × 17.0 mm
      zh: 54.0 x 54.0 x 17.0mm
      ja: 54.0 x 54.0 x 17.0mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 49.5 g
      zh: 49.5g
      ja: 49.5g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5core/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5core/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206.pdf
  - label:
      zh: 出厂固件资料
      en: Factory firmware resources
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/guide/m5core/restore_factory
sku: K001
cover: https://static-cdn.m5stack.com/resource/docs/products/core/basic/basic_02.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/basic/basic_02.webp
    caption:
      zh: BASIC 产品图
      en: BASIC product photo
      ja: BASIC 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/basic
---
