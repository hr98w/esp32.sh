---
id: m5stack-station-485
name: Station-485
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的盒式工业与桌面控制器，采用 ESP32，配有屏幕、RS-485 接口、GPIO 扩展。
  en: M5Stack enclosed industrial and desktop controller based on ESP32, with display, RS-485 interface, GPIO expansion.
  ja: ESP32を搭載したM5Stackのケース入りの産業・デスク用コントローラー。ディスプレイ、RS-485インターフェース、GPIO拡張を備えています。
officialUrl: https://docs.m5stack.com/en/core/station_485
aliases:
  - M5Stack-Station
features:
  - display
  - rs485
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/m5stack-station/
    checkedAt: 2026-10-15T17:23:46+00:00
  - url: https://docs.m5stack.com/en/core/station_485
    checkedAt: 2026-10-15T17:27:31+00:00
  - url: https://docs.m5stack.com/zh_CN/core/station_485
    checkedAt: 2026-10-16T00:06:12+00:00
  - url: https://docs.m5stack.com/ja/core/station_485
    checkedAt: 2026-10-16T00:06:14+00:00
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
      en: IPS LCD Screen
      zh: IPS LCD 屏幕
      ja: IPS 液晶画面
    value:
      en: 1.14"@240 x 135 ST7789V2
      zh: 1.14"@240 x 135 ST7789V2
      ja: 1.14"＠240*135 ST7789V2
  - label:
      en: USB Power
      zh: USB 供电
      ja: USB 給電
    value:
      en: 5V@1A
      zh: 5V@1A
      ja: 5V@1A
  - label:
      en: RS485 Power
      zh: RS485 供电
      ja: RS485 給電
    value:
      en: 9 ~ 24V@1A
      zh: 9~24V@1A
      ja: 9~24V@1A
  - label:
      en: Host Ports
      zh: 主机接口
      ja: ホストインターフェース
    value:
      en: USB Type-C x 1, HY2.0-4P (I2C+I/O+UART) x 6, Full-Size USB Type-A (OUTPUT), PWR485
      zh: USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 6，Full-Size USB Type-A (OUTPUT)，PWR485
      ja: USB Type-C x 1、HY2.0-4P (I2C+I/O+UART) x 6、フルサイズ USB Type-A (出力)、PWR485
  - label:
      en: Buttons
      zh: 按键
      ja: プッシュボタン
    value:
      en: Power button, physical buttons x 3
      zh: 电源键、物理按键 * 3
      ja: 電源ボタン、物理ボタン * 3
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
      en: 88.0 x 65.0 x 35.0mm
      zh: 88.0 x 65.0 x 35.0mm
      ja: 88.0 x 65.0 x 35.0mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 63.6g
      zh: 63.6g
      ja: 63.6g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5station/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5station/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3.pdf
sku: K123
cover: https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_02.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_02.webp
    caption:
      zh: Station-485 产品图
      en: Station-485 product photo
      ja: Station-485 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/station_485
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
