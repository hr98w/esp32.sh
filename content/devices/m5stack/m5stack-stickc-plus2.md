---
id: m5stack-stickc-plus2
name: M5StickC PLUS2
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的便携式传感开发设备，采用 ESP32，配有屏幕、运动传感器、麦克风、电池供电。
  en: M5Stack portable sensing development device based on ESP32, with display, motion sensor, microphone, battery power.
  ja: ESP32を搭載したM5Stackの携帯型のセンサー開発デバイス。ディスプレイ、モーションセンサー、マイク、バッテリー電源を備えています。
officialUrl: https://docs.m5stack.com/en/core/M5StickC%20PLUS2
aliases:
  - M5Stack M5StickC PLUS2
features:
  - display
  - imu
  - microphone
  - battery
sources:
  - url: https://github.com/s0lness/awesome-esp32
  - url: https://docs.m5stack.com/en/core/M5StickC%20PLUS2
    checkedAt: 2026-10-15T17:27:03+00:00
  - url: https://docs.m5stack.com/zh_CN/core/M5StickC%20PLUS2
    checkedAt: 2026-10-16T00:06:24+00:00
  - url: https://docs.m5stack.com/ja/core/M5StickC%20PLUS2
    checkedAt: 2026-10-16T00:06:26+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-PICO-V3-02@Dual-Core Processor, up to 240MHz
      zh: ESP32-PICO-V3-02@双核处理器，主频 240MHz
      ja: ESP32-PICO-V3-02@デュアルコアプロセッサ、最大 240MHz 動作周波数
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 8MB
      zh: 8MB
      ja: 8MB
  - label:
      en: PSRAM
      zh: PSRAM
      ja: PSRAM
    value:
      en: 2MB Quad
      zh: 2MB Quad
      ja: 2MB Quad
  - label:
      en: LCD Screen
      zh: LCD 屏幕
      ja: LCD スクリーン
    value:
      en: 1.14-inch, 135 x 240 Colorful TFT LCD, ST7789v2
      zh: 1.14-inch，135*240 Colorful TFT LCD，ST7789v2
      ja: 1.14 インチ、135*240 カラー TFT LCD、ST7789v2
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
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: 200mAh@3.7V, inside
      zh: 200mAh@3.7V，inside
      ja: 200mAh@3.7V、内部
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
      en: USB Type-C x 1, HY2.0-4P (I2C+I/O+UART) x 1
      zh: USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1
      ja: USB Type-C x 1、HY2.0-4P (I2C+I/O+UART) x 1
  - label:
      en: Button
      zh: 按键
      ja: ボタン
    value:
      en: Custom Button x 3
      zh: 自定义按键 x 3
      ja: カスタムボタン x 3
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
      en: 48.0 x 24.0 x 13.5mm
      zh: 48.0 x 24.0 x 13.5mm
      ja: 48.0 x 24.0 x 13.5mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 16.7g
      zh: 16.7g
      ja: 16.7g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5stickc_plus2/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5stickcplus2/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5.pdf
  - label:
      zh: 出厂固件资料
      en: Factory firmware resources
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/guide/stickc_plus2/restore_factory
sku: K016-P2
cover: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/6.webp
gallery:
  - image: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/6.webp
    caption:
      zh: M5StickC PLUS2 产品图
      en: M5StickC PLUS2 product photo
      ja: M5StickC PLUS2 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/M5StickC%20PLUS2
---

Do not infer firmware compatibility solely from the ESP32 chip family. Hardware revisions and peripherals must match the upstream project.
