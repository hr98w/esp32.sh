---
id: adafruit-magtag29-esp32s2
name: MagTag 2.9
manufacturer:
  id: adafruit
  name: Adafruit
chip: ESP32-S2
type: functional-board
summary:
  zh: 带 2.9 英寸灰阶电子纸的 ESP32-S2 信息板；2025 版更换了屏幕驱动，固件需匹配版本。
  en: ESP32-S2 information board with 2.9-inch grayscale e-paper; the 2025 display-driver change requires matching firmware.
  ja: 2.9インチのグレースケール電子ペーパーを備えるESP32-S2情報ボード。2025年の表示ドライバー変更に対応するファームウェアが必要です。
officialUrl: https://learn.adafruit.com/adafruit-magtag
aliases:
  - Adafruit MagTag 2.9"
features:
  - epaper
  - imu
  - rgb
  - usb
sources:
  - url: https://www.espboards.dev/esp32/adafruit-magtag29-esp32s2/
    checkedAt: 2026-10-15T17:56:03+00:00
  - url: https://learn.adafruit.com/adafruit-magtag
    checkedAt: 2026-10-15T18:51:39+00:00
cover: https://cdn-learn.adafruit.com/guides/images/000/003/176/medium800thumb/MagTag_guide_image.gif
gallery:
  - image: https://cdn-learn.adafruit.com/guides/images/000/003/176/medium800thumb/MagTag_guide_image.gif
    caption:
      zh: MagTag 2.9 产品图
      en: MagTag 2.9 product photo
      ja: MagTag 2.9 製品画像
    sourceUrl: https://learn.adafruit.com/adafruit-magtag
specifications:
  - label:
      zh: 存储
      en: Memory
      ja: メモリ
    value:
      zh: 4MB Flash / 2MB PSRAM
      en: 4MB Flash / 2MB PSRAM
      ja: 4MB Flash / 2MB PSRAM
  - label:
      zh: 屏幕
      en: Display
      ja: 画面
    value:
      zh: 2.9 英寸灰阶电子纸 · 296 × 128
      en: 2.9-inch grayscale e-paper · 296 × 128
      ja: 2.9インチ階調電子ペーパー · 296 × 128
  - label:
      zh: 电池接口
      en: Battery connection
      ja: バッテリー接続
    value:
      zh: 外接 LiPo · USB-C 充电
      en: External LiPo · USB-C charging
      ja: 外付けLiPo · USB-C充電
  - label:
      zh: USB
      en: USB
      ja: USB
    value:
      zh: 原生 USB，具体设备模式取决于固件
      en: Native USB; device modes depend on firmware
      ja: ネイティブUSB、動作モードはファームウェア依存
resources:
  - label:
      zh: 官方入门、接线与开发指南
      en: Official setup, pinout, and development guide
      ja: 公式セットアップ・配線・開発ガイド
    url: https://learn.adafruit.com/adafruit-magtag
revisionNotes:
  - text:
      zh: 官方指南注明 2025 年出现显示驱动变更，刷写前需核对对应显示版本的配置。
      en: The official guide notes a display-driver change in 2025; use configuration for the actual display revision.
      ja: 公式ガイドに2025年のディスプレイドライバー変更が記載されています。実機の表示部に対応する設定を使用してください。
    sourceUrl: https://learn.adafruit.com/adafruit-magtag
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
