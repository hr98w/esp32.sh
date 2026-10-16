---
id: espressif-esp32-s3-devkitc-1
name: ESP32-S3-DevKitC-1
manufacturer:
  id: espressif
  name: Espressif
chip: ESP32-S3
type: general-board
summary:
  zh: Espressif 官方 ESP32-S3 开发板，可用于连接外设和开发固件。
  en: Espressif's ESP32-S3 development board for firmware development and peripheral experiments.
  ja: ファームウェア開発や外付け機器の実験に使える、Espressif公式のESP32-S3開発ボード。
officialUrl: https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html
aliases:
  - DevKitC-1
  - 乐鑫 ESP32-S3 开发板
features:
  - gpio
  - usb
sources:
  - url: https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html
    checkedAt: 2026-10-15T17:32:28+00:00
  - url: https://www.espboards.dev/esp32/esp32-s3-devkitc-1/
  - url: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html
    checkedAt: 2026-10-16T00:13:43+00:00
specifications:
  - label:
      zh: 板载模组
      en: On-board module
      ja: 搭載モジュール
    value:
      zh: ESP32-S3-WROOM-1 / WROOM-1U / WROOM-2
      en: ESP32-S3-WROOM-1 / WROOM-1U / WROOM-2
      ja: ESP32-S3-WROOM-1 / WROOM-1U / WROOM-2
  - label:
      zh: USB
      en: USB
      ja: USB
    value:
      zh: USB OTG + USB-to-UART
      en: USB OTG + USB-to-UART
      ja: USB OTG + USB-to-UART
  - label:
      zh: 扩展
      en: Expansion
      ja: 拡張
    value:
      zh: GPIO / Boot / Reset
      en: GPIO / Boot / Reset
      ja: GPIO / Boot / Reset
resources:
  - label:
      zh: 官方用户指南与引脚表
      en: Official user guide and pinout
      ja: 公式ユーザーガイド・ピン配置
    url: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html
revisionNotes:
  - text:
      zh: 核对开发板版本、模组后缀和实际存储配置后再选择固件；同一开发板系列可能有不同 Flash、PSRAM 与天线选项。
      en: Check the board revision, module suffix, and actual memory configuration before selecting firmware. A board family may offer different Flash, PSRAM, and antenna options.
      ja: ファームウェアを選ぶ前に基板版・モジュール末尾記号・実際のメモリ構成を確認してください。同シリーズでもFlash・PSRAM・アンテナが異なる場合があります。
    sourceUrl: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html
cover: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32s3/_images/esp32-s3-devkitc-1-v1.1-isometric.png
gallery:
  - image: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32s3/_images/esp32-s3-devkitc-1-v1.1-isometric.png
    caption:
      zh: ESP32-S3-DevKitC-1 产品图
      en: ESP32-S3-DevKitC-1 product photo
      ja: ESP32-S3-DevKitC-1 製品画像
    sourceUrl: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html
---

同型号存在模块与存储配置差异。不假设某个 Flash 或 PSRAM 容量，也不根据相同芯片自动推断项目适配。
