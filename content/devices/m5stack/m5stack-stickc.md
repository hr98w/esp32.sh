---
id: m5stack-stickc
name: M5StickC
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的便携式传感开发设备，采用 ESP32，配有屏幕、运动传感器、电池供电。
  en: M5Stack portable sensing development device based on ESP32, with display, motion sensor, battery power.
  ja: ESP32を搭載したM5Stackの携帯型のセンサー開発デバイス。ディスプレイ、モーションセンサー、バッテリー電源を備えています。
officialUrl: https://docs.m5stack.com/en/core/m5stickc
aliases:
  - M5Stick-C
features:
  - display
  - imu
  - battery
sources:
  - url: https://www.espboards.dev/esp32/m5stick-c/
    checkedAt: 2026-10-15T17:23:54+00:00
  - url: https://docs.m5stack.com/en/core/m5stickc
    checkedAt: 2026-10-15T17:27:37+00:00
  - url: https://docs.m5stack.com/zh_CN/core/m5stickc
    checkedAt: 2026-10-16T00:06:16+00:00
  - url: https://docs.m5stack.com/ja/core/m5stickc
    checkedAt: 2026-10-16T00:06:18+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-PICO-D4 @ Xtensa® 32-bit LX6 dual-core processor, clock frequency up to 240MHz
      zh: ESP32-PICO-D4 @ Xtensa® 32 位 LX6 双核处理器，主频 240MHz
      ja: ESP32-PICO-D4 @ Xtensa® 32ビット LX6 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 4MB
      zh: 4MB
      ja: 4MB
  - label:
      en: LCD Screen
      zh: LCD 屏幕
      ja: LCD スクリーン
    value:
      en: 0.96 inch, 80 x 160 Colorful TFT LCD, ST7735SV
      zh: 0.96 inch，80 x 160 Colorful TFT LCD，ST7735SV
      ja: 0.96 インチ、80 x 160 カラー TFT LCD、ST7735SV
  - label:
      en: MEMS
      zh: MEMS
      ja: MEMS
    value:
      en: MPU6886
      zh: MPU6886
      ja: MPU6886
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: SPM1423
      zh: SPM1423
      ja: SPM1423
  - label:
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: 95mAh@3.7V, inside vb
      zh: 95 mAh @ 3.7V，inside vb
      ja: 95 mAh @ 3.7V、内部 vb
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: 5V@500mA
      zh: 5V@500mA
      ja: 5V@500mA
  - label:
      en: Interface
      zh: 接口
      ja: インターフェース
    value:
      en: USB Type-C x 1, GROVE (I2C+I/O+UART) x 1
      zh: USB Type-C x 1，GROVE (I2C+I/O+UART) x 1
      ja: USB Type-C x 1、GROVE (I2C+I/O+UART) x 1
  - label:
      en: Button
      zh: 按键
      ja: ボタン
    value:
      en: Custom Button x 2
      zh: 自定义按键 x 2
      ja: カスタムボタン x 2
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
      en: 48.2 x 25.5 x 13.7mm
      zh: 48.2 x 25.5 x 13.7mm
      ja: 48.2 x 25.5 x 13.7mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 15.1g
      zh: 15.1g
      ja: 15.1g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5stickc/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5stickc/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/M5StickC/20191118__StickC_A04_3110_Schematic_Rebuild_PinMap.pdf
sku: K016-C
cover: https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_01.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/m5stickc_01.webp
    caption:
      zh: M5StickC 产品图
      en: M5StickC product photo
      ja: M5StickC 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/m5stickc
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
