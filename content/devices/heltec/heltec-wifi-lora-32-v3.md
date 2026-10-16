---
id: heltec-wifi-lora-32-v3
name: WiFi LoRa 32 V3
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32-S3
type: functional-board
summary:
  zh: 结合 ESP32-S3、SX1262 与 0.96 英寸 OLED 的 LoRa 开发板，提供电池充电与保护电路。
  en: LoRa board combining ESP32-S3, SX1262, and a 0.96-inch OLED, with battery charging and protection circuitry.
  ja: ESP32-S3、SX1262、0.96インチOLEDを組み合わせたLoRaボード。電池充電・保護回路を備えます。
officialUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/
aliases:
  - Heltec WiFi LoRa 32 (V3)
features:
  - display
  - lora
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/heltec-wifi-lora-32-v3/
    checkedAt: 2026-10-15T17:55:13+00:00
  - url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/
    checkedAt: 2026-10-15T19:36:30+00:00
cover: https://heltec.org/wp-content/uploads/2023/09/LoRa-32-v3.jpg
gallery:
  - image: https://heltec.org/wp-content/uploads/2023/09/LoRa-32-v3.jpg
    caption:
      zh: WiFi LoRa 32 V3 产品图
      en: WiFi LoRa 32 V3 product photo
      ja: WiFi LoRa 32 V3 製品画像
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/
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
      zh: USB-C / CP2102 / GPIO
      en: USB-C / CP2102 / GPIO
      ja: USB-C / CP2102 / GPIO
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
