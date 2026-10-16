---
id: olimex-esp32-poe-iso
name: ESP32-PoE-ISO
manufacturer:
  id: olimex
  name: Olimex
chip: ESP32
type: functional-board
summary:
  zh: 提供以太网供电与电气隔离的 ESP32 开发板，带 MicroSD 和 LiPo 充电接口。
  en: ESP32 board with galvanically isolated Power over Ethernet, MicroSD, and LiPo charging connectors.
  ja: 絶縁型PoE給電、MicroSD、LiPo充電端子を備えるESP32ボード。
officialUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-PoE-ISO/open-source-hardware
aliases:
  - OLIMEX ESP32-PoE-ISO
features:
  - ethernet
  - sd
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/esp32-poe-iso/
    checkedAt: 2026-10-15T19:28:57+00:00
  - url: https://www.olimex.com/Products/IoT/ESP32/ESP32-PoE-ISO/open-source-hardware
    checkedAt: 2026-10-15T19:31:05+00:00
cover: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/images/thumbs/310x230/ESP32-POE-ISO-1.jpg
gallery:
  - image: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE-ISO/images/thumbs/310x230/ESP32-POE-ISO-1.jpg
    caption:
      zh: ESP32-PoE-ISO 产品图
      en: ESP32-PoE-ISO product photo
      ja: ESP32-PoE-ISO 製品画像
    sourceUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-PoE-ISO/open-source-hardware
specifications:
  - label:
      zh: 接口
      en: Interfaces
      ja: インターフェース
    value:
      zh: 100Mbps Ethernet / USB / GPIO
      en: 100Mbps Ethernet / USB / GPIO
      ja: 100Mbps Ethernet / USB / GPIO
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: 隔离 PoE / 外接 LiPo 电池接口与充电
      en: Isolated PoE / external LiPo connector and charging
      ja: 絶縁PoE / 外付けLiPo端子・充電
  - label:
      zh: 模组配置
      en: Module options
      ja: モジュール構成
    value:
      zh: WROOM / WROVER 及不同天线配置
      en: WROOM / WROVER and antenna variants
      ja: WROOM / WROVER・アンテナ構成違い
resources:
  - label:
      zh: 官方入门与硬件资料
      en: Official setup and hardware guide
      ja: 公式セットアップ・ハードウェア資料
    url: https://www.olimex.com/Products/IoT/ESP32/ESP32-PoE-ISO/open-source-hardware
revisionNotes:
  - text:
      zh: 该系列存在不同天线、存储、温度等级和硬件修订配置。引脚与固件需按实际后缀型号和板上版本核对；充电接口不表示附带电池。
      en: The family has antenna, memory, temperature-grade, and board-revision variants. Match pin assignments and firmware to the full suffix and board revision; a charging connector does not imply an included battery.
      ja: アンテナ、メモリ、温度グレード、基板版の異なる構成があります。末尾記号と基板版に合うピン設定・ファームウェアを使用し、充電端子があっても電池同梱とは限らない点をご確認ください。
    sourceUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-PoE-ISO/open-source-hardware
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
