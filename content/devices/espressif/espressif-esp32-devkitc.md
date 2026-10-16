---
id: espressif-esp32-devkitc
name: ESP32-DevKitC
manufacturer:
  id: espressif
  name: Espressif
chip: ESP32
type: general-board
summary:
  zh: 通过两侧排针连接外设的通用开发板。
  en: General-purpose board with pin headers for connecting peripherals.
  ja: 両側のピンヘッダーから周辺機器を接続できる汎用開発ボード。
officialUrl: https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/index.html
aliases:
  - Espressif ESP32-DevKitC
features:
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/esp32-devkitc/
    checkedAt: 2026-10-15T17:39:16+00:00
  - url: https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/index.html
    checkedAt: 2026-10-15T17:41:30+00:00
  - url: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
    checkedAt: 2026-10-16T00:26:55+00:00
specifications:
  - label:
      zh: 板载模组
      en: On-board module
      ja: 搭載モジュール
    value:
      zh: ESP32-WROOM-32E（当前指南示例）
      en: ESP32-WROOM-32E (current guide example)
      ja: ESP32-WROOM-32E（現行ガイド例）
  - label:
      zh: USB
      en: USB
      ja: USB
    value:
      zh: Micro-USB / USB-to-UART
      en: Micro-USB / USB-to-UART
      ja: Micro-USB / USB-to-UART
  - label:
      zh: 扩展
      en: Expansion
      ja: 拡張
    value:
      zh: PWM / ADC / DAC / I2C / I2S / SPI / GPIO
      en: PWM / ADC / DAC / I2C / I2S / SPI / GPIO
      ja: PWM / ADC / DAC / I2C / I2S / SPI / GPIO
resources:
  - label:
      zh: 官方用户指南与引脚表
      en: Official user guide and pinout
      ja: 公式ユーザーガイド・ピン配置
    url: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
revisionNotes:
  - text:
      zh: 核对开发板版本、模组后缀和实际存储配置后再选择固件；同一开发板系列可能有不同 Flash、PSRAM 与天线选项。
      en: Check the board revision, module suffix, and actual memory configuration before selecting firmware. A board family may offer different Flash, PSRAM, and antenna options.
      ja: ファームウェアを選ぶ前に基板版・モジュール末尾記号・実際のメモリ構成を確認してください。同シリーズでもFlash・PSRAM・アンテナが異なる場合があります。
    sourceUrl: https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
