---
id: heltec-wifi-lora-32-v2
name: WiFi LoRa 32 V2
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32
type: functional-board
summary:
  zh: 基于 ESP32 与 SX1276/SX1278 的 OLED LoRa 开发板；官方已逐步淘汰该版本。
  en: OLED LoRa board based on ESP32 and SX1276/SX1278; the manufacturer is phasing out this version.
  ja: ESP32とSX1276/SX1278を使うOLED付きLoRaボード。メーカーでは本バージョンを段階的に終了しています。
officialUrl: https://heltec.org/project/wifi-lora-32v2/
aliases:
  - Heltec WiFi LoRa 32(V2)
features:
  - display
  - lora
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/heltec-wifi-lora-32-v2/
    checkedAt: 2026-10-15T17:55:10+00:00
  - url: https://heltec.org/project/wifi-lora-32v2/
    checkedAt: 2026-10-15T19:36:30+00:00
cover: https://heltec.org/wp-content/uploads/2024/07/wifi-lora-32-v2-1.png
gallery:
  - image: https://heltec.org/wp-content/uploads/2024/07/wifi-lora-32-v2-1.png
    caption:
      zh: WiFi LoRa 32 V2 产品图
      en: WiFi LoRa 32 V2 product photo
      ja: WiFi LoRa 32 V2 製品画像
    sourceUrl: https://heltec.org/project/wifi-lora-32v2/
specifications:
  - label:
      zh: 无线芯片
      en: Radio IC
      ja: 無線IC
    value:
      zh: SX1276 / SX1278
      en: SX1276 / SX1278
      ja: SX1276 / SX1278
  - label:
      zh: 接口
      en: Interfaces
      ja: インターフェース
    value:
      zh: Micro USB / GPIO
      en: Micro USB / GPIO
      ja: Micro USB / GPIO
  - label:
      zh: 射频配置
      en: Radio configuration
      ja: 無線構成
    value:
      zh: 470–510MHz / 863–923MHz
      en: 470–510MHz / 863–923MHz
      ja: 470–510MHz / 863–923MHz
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://heltec.org/project/wifi-lora-32v2/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://heltec.org/project/wifi-lora-32v2/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
