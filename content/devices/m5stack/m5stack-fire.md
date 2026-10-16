---
id: m5stack-fire
name: FIRE
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的模块化传感与显示控制器，采用 ESP32，配有屏幕、音频输入输出、运动传感器。
  en: M5Stack modular sensing and display controller based on ESP32, with display, audio I/O, motion sensor.
  ja: ESP32を搭載したM5Stackのモジュール型のセンサー・表示コントローラー。ディスプレイ、オーディオ入出力、モーションセンサーを備えています。
officialUrl: https://docs.m5stack.com/en/core/fire
aliases:
  - M5Stack-FIRE
features:
  - display
  - audio
  - imu
sources:
  - url: https://www.espboards.dev/esp32/m5stack-fire/
    checkedAt: 2026-10-15T17:23:43+00:00
  - url: https://docs.m5stack.com/en/core/fire
    checkedAt: 2026-10-15T17:27:29+00:00
  - url: https://docs.m5stack.com/zh_CN/core/fire
    checkedAt: 2026-10-16T00:05:56+00:00
  - url: https://docs.m5stack.com/ja/core/fire
    checkedAt: 2026-10-16T00:05:58+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-D0WDQ6 @ Xtensa® 32-bit LX6 dual-core processor, clock frequency 240MHz
      zh: ESP32-D0WDQ6 @ Xtensa® 32 位 LX6 双核处理器，主频 240MHz
      ja: ESP32-D0WDQ6 @ Xtensa® 32ビット LX6 デュアルコアプロセッサ、動作周波数 240MHz
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
      en: IPS Screen
      zh: IPS 屏幕
      ja: IPS ディスプレイ
    value:
      en: 2 inch, 320x240 Colorful TFT LCD, ILI9342C, Max brightness 853nit
      zh: 2 inch，320x240 Colorful TFT LCD，ILI9342C，最高亮度 853nit
      ja: 2 インチ、320x240 カラー TFT LCD、ILI9342C、最大輝度 853nit
  - label:
      en: MEMS
      zh: MEMS
      ja: MEMS
    value:
      en: BMM150 + SH200Q/MPU6886
      zh: BMM150 + SH200Q/MPU6886
      ja: BMM150 + SH200Q/MPU6886
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: MEMS Analog BSE3729 Microphone
      zh: MEMS Analog BSE3729 Microphone
      ja: MEMS アナログ BSE3729 マイクロフォン
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
      zh: 电池
      ja: バッテリー
    value:
      en: 500mAh@3.7V, inside vb
      zh: 500 mAh @ 3.7V，inside vb
      ja: 500 mAh @ 3.7V、inside vb
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: 5V@500mA
      zh: 5V@500mA
      ja: 5V@500mA
  - label:
      en: Host Interface
      zh: 主机接口
      ja: ホストインターフェース
    value:
      en: USB Type-C x 1, GROVE (I2C+I/O+UART) x 1
      zh: USB Type-C x 1，GROVE (I2C+I/O+UART) x 1
      ja: USB Type-C x 1、GROVE (I2C+I/O+UART) x 1
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
      en: 54.0 x 54.0 x 28.6mm
      zh: 54.0 x 54.0 x 28.6mm
      ja: 54.0 x 54.0 x 28.6mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 62.6g
      zh: 62.6g
      ja: 62.6g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5fire/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5fire/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/480/M5-Core-Schematic_20171206.pdf
sku: K007
cover: https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_07.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/fire/fire_07.webp
    caption:
      zh: FIRE 产品图
      en: FIRE product photo
      ja: FIRE 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/fire
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
