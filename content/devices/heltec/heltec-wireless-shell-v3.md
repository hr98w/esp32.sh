---
id: heltec-wireless-shell-v3
name: Wireless Shell V3
manufacturer:
  id: heltec
  name: Heltec
chip: ESP32-S3
type: module
summary:
  zh: 将 ESP32-S3 与 SX1262 集成在邮票孔模块中，适合嵌入自定义电路板的 LoRa 项目。
  en: ESP32-S3 and SX1262 castellated module for integrating LoRa into custom circuit boards.
  ja: ESP32-S3とSX1262を集積したキャステレーション端子モジュール。自作基板へLoRa機能を組み込む用途向け。
officialUrl: https://heltec.org/project/wireless-shell-v3/
aliases:
  - Heltec Wireless Shell (V3)
features:
  - lora
sources:
  - url: https://www.espboards.dev/esp32/heltec-wireless-shell-v3/
    checkedAt: 2026-10-15T17:55:21+00:00
  - url: https://heltec.org/project/wireless-shell-v3/
    checkedAt: 2026-10-15T19:36:33+00:00
cover: https://heltec.org/wp-content/uploads/2023/09/wireless-shell-frt.png
gallery:
  - image: https://heltec.org/wp-content/uploads/2023/09/wireless-shell-frt.png
    caption:
      zh: Wireless Shell V3 产品图
      en: Wireless Shell V3 product photo
      ja: Wireless Shell V3 製品画像
    sourceUrl: https://heltec.org/project/wireless-shell-v3/
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
      zh: IPEX1.0 / 1.27mm 焊接接口
      en: IPEX1.0 / 1.27mm castellated interface
      ja: IPEX1.0 / 1.27mmキャスタレーション端子
  - label:
      zh: 尺寸
      en: Dimensions
      ja: 寸法
    value:
      zh: 38.4 × 16.1 × 2.8mm
      en: 38.4 × 16.1 × 2.8mm
      ja: 38.4 × 16.1 × 2.8mm
resources:
  - label:
      zh: 官方入门、示例与引脚资料
      en: Official setup, examples, and pinout
      ja: 公式セットアップ・サンプル・ピン配置
    url: https://heltec.org/project/wireless-shell-v3/
revisionNotes:
  - text:
      zh: 按具体硬件版本与射频频段选择固件。带电池接口不代表套装附带电池；Tracker 的 GNSS 与 LoRa 芯片功能不同。
      en: Match firmware to the hardware revision and radio band. A battery connector does not mean a battery is included; GNSS and LoRa are separate functions on Tracker.
      ja: ハードウェア版と無線周波数帯に合うファームウェアを使用してください。電池端子があっても電池同梱とは限りません。TrackerのGNSSとLoRaは別機能です。
    sourceUrl: https://heltec.org/project/wireless-shell-v3/
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
