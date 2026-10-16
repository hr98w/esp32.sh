---
id: m5stack-core2
name: Core2
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的触控物联网终端，采用 ESP32，配有屏幕、触摸输入、音频输入输出、运动传感器。
  en: M5Stack touchscreen IoT terminal based on ESP32, with display, touch input, audio I/O, motion sensor.
  ja: ESP32を搭載したM5Stackのタッチ式のIoT端末。ディスプレイ、タッチ入力、オーディオ入出力、モーションセンサーを備えています。
officialUrl: https://docs.m5stack.com/en/core/core2
aliases:
  - M5Stack-Core2
features:
  - display
  - touch
  - audio
  - imu
sources:
  - url: https://www.espboards.dev/esp32/m5stack-core2/
    checkedAt: 2026-10-15T17:23:32+00:00
  - url: https://docs.m5stack.com/en/core/core2
    checkedAt: 2026-10-15T17:27:21+00:00
  - url: https://docs.m5stack.com/zh_CN/core/core2
    checkedAt: 2026-10-16T00:05:40+00:00
  - url: https://docs.m5stack.com/ja/core/core2
    checkedAt: 2026-10-16T00:05:42+00:00
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
      en: IPS LCD Screen
      zh: IPS LCD 屏幕
      ja: IPS LCD スクリーン
    value:
      en: 2.0"@320 x 240 ILI9342C / ILI9342E
      zh: 2.0"@320 x 240 ，屏幕型号： ILI9342C / ILI9342E
      ja: 2.0"@320 x 240 ILI9342C / ILI9342E
  - label:
      en: Capacitive Touch IC
      zh: 电容式触摸屏 IC
      ja: 静電容量式タッチスクリーン IC
    value:
      en: FT6336U
      zh: FT6336U
      ja: FT6336U
  - label:
      en: IMU
      zh: IMU
      ja: IMU
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
      en: Lithium Battery
      zh: 锂电池
      ja: リチウムバッテリー
    value:
      en: 500mAh@3.7V
      zh: 500mAh@3.7V
      ja: 500mAh@3.7V
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
      en: Button
      zh: 按键
      ja: ボタン
    value:
      en: Power button, RST button, screen virtual buttons x 3
      zh: 电源键、RST 键、屏幕虚拟按键 x 3
      ja: 電源ボタン、RST ボタン、スクリーン仮想ボタン x 3
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
      en: 54.0 x 54.0 x 16.5mm
      zh: 54.0 x 54.0 x 16.5mm
      ja: 54.0 x 54.0 x 16.5mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 54.9g
      zh: 54.9g
      ja: 54.9g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5core2/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5core2/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH.pdf
  - label:
      zh: 出厂固件资料
      en: Factory firmware resources
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/guide/core2/restore_factory
sku: K010
cover: https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_04.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_04.webp
    caption:
      zh: Core2 产品图
      en: Core2 product photo
      ja: Core2 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/core2
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
