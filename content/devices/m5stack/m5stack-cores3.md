---
id: m5stack-cores3
name: CoreS3
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的集成多种交互外设的控制器，采用 ESP32-S3，配有屏幕、触摸输入、摄像头、音频输入输出。
  en: M5Stack controller with integrated interactive peripherals based on ESP32-S3, with display, touch input, camera, audio I/O.
  ja: ESP32-S3を搭載したM5Stackの複数の操作機能を搭載したコントローラー。ディスプレイ、タッチ入力、カメラ、オーディオ入出力を備えています。
officialUrl: https://docs.m5stack.com/en/core/coreS3
aliases:
  - M5Stack CoreS3
features:
  - display
  - touch
  - camera
  - audio
sources:
  - url: https://www.espboards.dev/esp32/m5stack-cores3/
    checkedAt: 2026-10-15T17:23:38+00:00
  - url: https://docs.m5stack.com/en/core/coreS3
    checkedAt: 2026-10-15T17:27:25+00:00
  - url: https://docs.m5stack.com/zh_CN/core/coreS3
    checkedAt: 2026-10-16T00:05:48+00:00
  - url: https://docs.m5stack.com/ja/core/coreS3
    checkedAt: 2026-10-16T00:05:50+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-S3 @ Xtensa® 32-bit LX7 dual-core processor, clock frequency 240MHz
      zh: ESP32-S3 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz
      ja: ESP32-S3 @ Xtensa® 32ビット LX7 デュアルコアプロセッサ、動作周波数 240MHz
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
      en: Touch IPS LCD
      zh: 触摸 IPS LCD 屏幕
      ja: 静電容量タッチ IPS 液晶
    value:
      en: 2.0" @320 × 240 ILI9342C / ILI9342E
      zh: 2.0"@320 x 240 ILI9342C / ILI9342E
      ja: 2.0"@320 x 240 ILI9342C / ILI9342E
  - label:
      en: Camera
      zh: 摄像头
      ja: カメラ
    value:
      en: GC0308 0.3MP
      zh: GC0308@ 0.3MP
      ja: GC0308@0.3MP
  - label:
      en: 6-axis IMU
      zh: 六轴姿态传感器
      ja: 6 軸 IMU
    value:
      en: BMI270
      zh: BMI270
      ja: BMI270
  - label:
      en: 3-axis Magnetometer
      zh: 三轴磁力计
      ja: 3 軸磁気センサー
    value:
      en: BMM150
      zh: BMM150
      ja: BMM150
  - label:
      en: Speaker
      zh: 扬声器
      ja: スピーカー
    value:
      en: 16-bit I2S amplifier AW88298 @1W
      zh: 16bits-I2S 功放芯片 AW88298@1W
      ja: 16bits-I2S アンプ AW88298@1W
  - label:
      en: Audio Codec
      zh: 音频编码芯片
      ja: オーディオコーデック
    value:
      en: ES7210, dual-microphone input
      zh: ES7210，双麦克风输入
      ja: ES7210、デュアルマイク入力
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
      en: "Whole set (CoreS3+DinBase): 69.0 × 54.0 × 31.5mm / Main unit (CoreS3): 54.0 × 54.0 × 15.5mm"
      zh: 整机套件（CoreS3+DinBase）：69.0 x 54.0 x 31.5mm / 主机部分（CoreS3）：54.0 x 54.0 x 15.5mm
      ja: 完成品セット（CoreS3+DinBase）：69.0 x 54.0 x 31.5mm 本体（CoreS3）：54.0 x 54.0 x 15.5mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 72.7g
      zh: 72.7g
      ja: 72.7g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5cores3/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5cores3/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0.pdf
  - label:
      zh: 出厂固件资料
      en: Factory firmware resources
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/guide/cores3/restore_factory
sku: K128
cover: https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-96063e2a-637a-4d11-ac47-1ce4f1cdfd3e.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-96063e2a-637a-4d11-ac47-1ce4f1cdfd3e.webp
    caption:
      zh: CoreS3 产品图
      en: CoreS3 product photo
      ja: CoreS3 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/coreS3
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
