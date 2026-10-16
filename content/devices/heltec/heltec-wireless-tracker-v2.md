---
id: heltec-wireless-tracker-v2
name: Wireless Tracker V2
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32-S3
type: functional-board
summary:
  zh: 集成 ESP32-S3、SX1262 和 UC6580 GNSS 的无线定位开发板，配备 TFT 并支持太阳能充电。
  en: Wireless tracking board with ESP32-S3, SX1262, UC6580 GNSS, a TFT, and solar charging support.
  ja: ESP32-S3、SX1262、UC6580 GNSS、TFTを備え、ソーラー充電にも対応する無線追跡開発ボード。
officialUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wireless-tracker-v2/
aliases:
  - Heltec Wireless Tracker V2
features:
  - lora
  - gps
  - display
sources:
  - url: https://www.espboards.dev/esp32/heltec-wireless-tracker-v2/
    checkedAt: 2026-10-15T17:55:32+00:00
  - url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wireless-tracker-v2/
    checkedAt: 2026-10-15T19:36:36+00:00
cover: https://wiki.heltec.org/assets/images/1-6973aadd7789ec08f8a35c9f2f3d8237.jpg
gallery:
  - image: https://wiki.heltec.org/assets/images/1-6973aadd7789ec08f8a35c9f2f3d8237.jpg
    caption:
      zh: Wireless Tracker V2 产品图
      en: Wireless Tracker V2 product photo
      ja: Wireless Tracker V2 製品画像
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wireless-tracker-v2/
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
      zh: 传感器
      en: Sensors
      ja: センサー
    value:
      zh: UC6580 GNSS
      en: UC6580 GNSS
      ja: UC6580 GNSS
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: CN3165 · 支持外接电池与太阳能充电
      en: CN3165 · external battery and solar charging supported
      ja: CN3165 · 外付け電池・ソーラー充電に対応
  - label:
      zh: 尺寸
      en: Dimensions
      ja: 寸法
    value:
      zh: 53.00 × 25.40 × 9.37mm
      en: 53.00 × 25.40 × 9.37mm
      ja: 53.00 × 25.40 × 9.37mm
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wireless-tracker-v2/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wireless-tracker-v2/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
