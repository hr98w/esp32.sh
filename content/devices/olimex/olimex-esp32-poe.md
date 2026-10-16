---
id: olimex-esp32-poe
name: ESP32-PoE
manufacturer:
  id: olimex
  name: Olimex
chip: ESP32
type: functional-board
summary:
  zh: 支持以太网供电的 ESP32 开发板；本型号没有 PoE 电气隔离，接线与供电按官方说明操作。
  en: ESP32 board with Power over Ethernet; this model lacks galvanic PoE isolation, so follow official wiring and power instructions.
  ja: PoE給電対応のESP32ボード。本モデルにはPoEの電気的絶縁がないため、接続と給電は公式の手順に従ってください。
officialUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
aliases:
  - OLIMEX ESP32-PoE
features:
  - ethernet
  - sd
  - usb
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/esp32-poe/
    checkedAt: 2026-10-15T19:29:00+00:00
  - url: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
    checkedAt: 2026-10-15T19:31:46+00:00
cover: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/images/thumbs/310x230/ESP32-POE.jpg
gallery:
  - image: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/images/thumbs/310x230/ESP32-POE.jpg
    caption:
      zh: ESP32-PoE 产品图
      en: ESP32-PoE product photo
      ja: ESP32-PoE 製品画像
    sourceUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
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
      zh: PoE / 外接 LiPo 电池接口与充电
      en: PoE / external LiPo connector and charging
      ja: PoE / 外付けLiPo端子・充電
  - label:
      zh: 隔离
      en: Isolation
      ja: 絶縁
    value:
      zh: PoE 电源不隔离
      en: PoE power is not galvanically isolated
      ja: PoE電源は非絶縁
resources:
  - label:
      zh: 官方入门与硬件资料
      en: Official setup and hardware guide
      ja: 公式セットアップ・ハードウェア資料
    url: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
revisionNotes:
  - text:
      zh: 该系列存在不同天线、存储、温度等级和硬件修订配置。引脚与固件需按实际后缀型号和板上版本核对；充电接口不表示附带电池。
      en: The family has antenna, memory, temperature-grade, and board-revision variants. Match pin assignments and firmware to the full suffix and board revision; a charging connector does not imply an included battery.
      ja: アンテナ、メモリ、温度グレード、基板版の異なる構成があります。末尾記号と基板版に合うピン設定・ファームウェアを使用し、充電端子があっても電池同梱とは限らない点をご確認ください。
    sourceUrl: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
