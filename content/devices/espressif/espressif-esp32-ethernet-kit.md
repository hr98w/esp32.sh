---
id: espressif-esp32-ethernet-kit
name: ESP32-Ethernet-Kit
manufacturer:
  id: espressif
  name: Espressif
chip: ESP32
type: functional-board
summary:
  zh: 用于以太网与 Wi-Fi 互连实验的开发套件。
  en: Development kit for Ethernet-to-Wi-Fi connectivity experiments.
  ja: EthernetとWi-Fiの相互接続を試すための開発キット。
officialUrl: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html
aliases:
  - Espressif ESP32-Ethernet-Kit
features:
  - ethernet
sources:
  - url: https://www.espboards.dev/esp32/esp32-ethernet-kit/
    checkedAt: 2026-10-15T17:39:21+00:00
  - url: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-ethernet-kit.html
    checkedAt: 2026-10-15T17:41:34+00:00
  - url: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32/esp32-ethernet-kit/user_guide.html
    checkedAt: 2026-10-16T00:27:18+00:00
specifications:
  - label:
      zh: 板载模组
      en: On-board module
      ja: 搭載モジュール
    value:
      zh: ESP32-WROVER-E
      en: ESP32-WROVER-E
      ja: ESP32-WROVER-E
  - label:
      zh: 以太网
      en: Ethernet
      ja: Ethernet
    value:
      zh: IP101GRI PHY / RMII
      en: IP101GRI PHY / RMII
      ja: IP101GRI PHY / RMII
  - label:
      zh: USB
      en: USB
      ja: USB
    value:
      zh: FT2232H USB-to-serial / JTAG
      en: FT2232H USB-to-serial / JTAG
      ja: FT2232H USB-to-serial / JTAG
  - label:
      zh: 存储
      en: Memory
      ja: メモリ
    value:
      zh: 8MB PSRAM
      en: 8MB PSRAM
      ja: 8MB PSRAM
resources:
  - label:
      zh: 官方用户指南与引脚表
      en: Official user guide and pinout
      ja: 公式ユーザーガイド・ピン配置
    url: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-ethernet-kit/user_guide.html
revisionNotes:
  - text:
      zh: 核对开发板版本、模组后缀和实际存储配置后再选择固件；同一开发板系列可能有不同 Flash、PSRAM 与天线选项。
      en: Check the board revision, module suffix, and actual memory configuration before selecting firmware. A board family may offer different Flash, PSRAM, and antenna options.
      ja: ファームウェアを選ぶ前に基板版・モジュール末尾記号・実際のメモリ構成を確認してください。同シリーズでもFlash・PSRAM・アンテナが異なる場合があります。
    sourceUrl: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-ethernet-kit/user_guide.html
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
