---
id: heltec-wifi-lora-32-v4
name: WiFi LoRa 32 V4
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32-S3
type: functional-board
summary:
  zh: 结合 ESP32-S3 与 SX1262 的 LoRa 开发板，增加太阳能与 GNSS 扩展接口，含多个功率与硬件修订配置。
  en: ESP32-S3 and SX1262 LoRa board with solar and GNSS expansion connectors, offered in multiple power and hardware revisions.
  ja: ESP32-S3とSX1262を使うLoRaボード。ソーラー・GNSS拡張端子を備え、出力やハードウェア版に複数の構成があります。
officialUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/
aliases:
  - Heltec WiFi LoRa 32 V4
features:
  - display
  - lora
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/heltec-wifi-lora-32-v4/
    checkedAt: 2026-10-15T17:55:16+00:00
  - url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/
    checkedAt: 2026-10-15T19:36:32+00:00
cover: https://wiki.heltec.org/assets/images/v4-ae6cb435b4230bafa9b6516946f048ae.jpg
gallery:
  - image: https://wiki.heltec.org/assets/images/v4-ae6cb435b4230bafa9b6516946f048ae.jpg
    caption:
      zh: WiFi LoRa 32 V4 产品图
      en: WiFi LoRa 32 V4 product photo
      ja: WiFi LoRa 32 V4 製品画像
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32-S3R2
      en: ESP32-S3R2
      ja: ESP32-S3R2
  - label:
      zh: 存储
      en: Memory
      ja: メモリ
    value:
      zh: 16MB Flash / 2MB PSRAM
      en: 16MB Flash / 2MB PSRAM
      ja: 16MB Flash / 2MB PSRAM
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
      zh: USB-C / 40-pin GPIO
      en: USB-C / 40-pin GPIO
      ja: USB-C / 40-pin GPIO
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: 太阳能输入与外接锂电池充电
      en: Solar input and external lithium-battery charging
      ja: ソーラー入力・外付けリチウム電池充電
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
