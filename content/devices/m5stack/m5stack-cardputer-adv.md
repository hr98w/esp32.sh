---
id: m5stack-cardputer-adv
name: Cardputer ADV
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的带键盘的掌上开发终端，采用 ESP32-S3，配有屏幕、键盘、音频输入输出、运动传感器。
  en: M5Stack handheld keyboard development terminal based on ESP32-S3, with display, keyboard, audio I/O, motion sensor.
  ja: ESP32-S3を搭載したM5Stackのキーボード付き携帯開発端末。ディスプレイ、キーボード、オーディオ入出力、モーションセンサーを備えています。
officialUrl: https://docs.m5stack.com/en/core/Cardputer-Adv
aliases:
  - M5Stack Cardputer ADV
features:
  - display
  - keyboard
  - audio
  - imu
sources:
  - url: https://github.com/s0lness/awesome-esp32
  - url: https://docs.m5stack.com/en/core/Cardputer-Adv
    checkedAt: 2026-10-15T17:27:05+00:00
  - url: https://docs.m5stack.com/zh_CN/core/Cardputer-Adv
    checkedAt: 2026-10-16T00:05:36+00:00
  - url: https://docs.m5stack.com/ja/core/Cardputer-Adv
    checkedAt: 2026-10-16T00:05:38+00:00
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
      en: Display
      zh: 屏幕
      ja: スクリーン
    value:
      en: ST7789V2@1.14", 240 x 135px
      zh: ST7789V2@1.14", 240 x 135px
      ja: ST7789V2@1.14 インチ，240 x 135px
  - label:
      en: IMU
      zh: 姿态传感器
      ja: 姿勢センサー
    value:
      en: BMI270
      zh: BMI270
      ja: BMI270
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: "MEMS microphone, SNR: 65 dB"
      zh: MEMS 麦克风，信噪比 (SNR)：65 dB
      ja: MEMS マイク（S/N 比：65dB）
  - label:
      en: Speaker
      zh: 扬声器
      ja: スピーカー
    value:
      en: NS4150B amplifier + 8Ω@1W speaker
      zh: NS4150B 功放芯片 + 8Ω@1W 扬声器
      ja: NS4150B アンプチップ + 8Ω@1W スピーカー
  - label:
      en: Audio Codec
      zh: 音频编解码芯片
      ja: オーディオコーデック
    value:
      en: ES8311
      zh: ES8311
      ja: ES8311
  - label:
      en: Keyboard
      zh: 键盘
      ja: キーボード
    value:
      en: 56 keys (4 x 14)
      zh: 56 按键 (4 x 14)
      ja: 56 キー（4 x 14）
  - label:
      en: Battery Capacity
      zh: 电池容量
      ja: バッテリー容量
    value:
      en: 1500mAh
      zh: 1500mAh
      ja: 1500mAh
  - label:
      en: Expansion Ports
      zh: 拓展接口
      ja: 拡張インターフェース
    value:
      en: HY2.0-4P + EXT 2.54-14P
      zh: HY2.0-4P + EXT 2.54-14P
      ja: HY2.0-4P + EXT 2.54-14P
  - label:
      en: Product Size
      zh: 产品尺寸
      ja: 製品サイズ
    value:
      en: 84.0 x 54.0 x 19.6mm
      zh: 84.0 x 54.0 x 19.6mm
      ja: 84.0 x 54.0 x 19.6mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 81.0g
      zh: 81.0g
      ja: 81.0g
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
    url: https://docs.m5stack.com/en/uiflow2/cardputer-adv/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58.pdf
sku: K132-Adv
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_02.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_02.webp
    caption:
      zh: Cardputer ADV 产品图
      en: Cardputer ADV product photo
      ja: Cardputer ADV 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/Cardputer-Adv
---

Do not infer firmware compatibility solely from the ESP32 chip family. Hardware revisions and peripherals must match the upstream project.
