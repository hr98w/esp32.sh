---
id: heltec-wireless-stick-lite-v3
name: Wireless Stick Lite V3
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32-S3
type: functional-board
summary:
  zh: 不带 OLED 的 ESP32-S3 与 SX1262 LoRa 开发板，带 USB-C 与锂电池管理接口。
  en: ESP32-S3 and SX1262 LoRa board without an OLED, with USB-C and lithium-battery management.
  ja: OLEDを省いたESP32-S3・SX1262 LoRaボード。USB-Cとリチウム電池管理端子を備えます。
officialUrl: https://heltec.org/project/wireless-stick-lite-v2/
aliases:
  - Heltec Wireless Stick Lite (V3)
features:
  - lora
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/heltec-wireless-stick-lite-v3/
    checkedAt: 2026-10-15T17:55:24+00:00
  - url: https://heltec.org/project/wireless-stick-lite-v2/
    checkedAt: 2026-10-15T19:36:36+00:00
cover: https://heltec.org/wp-content/uploads/2023/09/wireless-stickLite-front.png
gallery:
  - image: https://heltec.org/wp-content/uploads/2023/09/wireless-stickLite-front.png
    caption:
      zh: Wireless Stick Lite V3 产品图
      en: Wireless Stick Lite V3 product photo
      ja: Wireless Stick Lite V3 製品画像
    sourceUrl: https://heltec.org/project/wireless-stick-lite-v2/
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32-S3FN8
      en: ESP32-S3FN8
      ja: ESP32-S3FN8
  - label:
      zh: 存储
      en: Memory
      ja: メモリ
    value:
      zh: 8MB Flash
      en: 8MB Flash
      ja: 8MB Flash
  - label:
      zh: 无线芯片
      en: Radio IC
      ja: 無線IC
    value:
      zh: SX1262
      en: SX1262
      ja: SX1262
  - label:
      zh: 接口
      en: Interfaces
      ja: インターフェース
    value:
      zh: USB-C / IPEX1.0 / GPIO
      en: USB-C / IPEX1.0 / GPIO
      ja: USB-C / IPEX1.0 / GPIO
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: 支持外接 3.7V 锂电池供电与充电
      en: External 3.7V lithium-battery power and charging supported
      ja: 外付け3.7Vリチウム電池の給電・充電に対応
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://heltec.org/project/wireless-stick-lite-v2/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://heltec.org/project/wireless-stick-lite-v2/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
