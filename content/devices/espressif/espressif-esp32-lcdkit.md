---
id: espressif-esp32-lcdkit
name: ESP32-LCDKit
manufacturer:
  id: espressif
  name: Espressif
chip: ESP32
type: functional-board
summary:
  zh: 需搭配 ESP32-DevKitC 使用的人机界面扩展板，可连接外部显示屏。
  en: HMI expansion board used with ESP32-DevKitC and an external display.
  ja: ESP32-DevKitCと外部ディスプレイを組み合わせて使うHMI拡張ボード。
officialUrl: https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32/esp32-lcdkit/user_guide.html
aliases:
  - Espressif ESP32-LCDKit
features:
  - audio
  - sd
sources:
  - url: https://www.espboards.dev/esp32/esp32-lcdkit/
    checkedAt: 2026-10-15T17:39:28+00:00
  - url: https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32/esp32-lcdkit/user_guide.html
    checkedAt: 2026-10-15T17:41:38+00:00
specifications:
  - label:
      zh: 扩展
      en: Expansion
      ja: 拡張
    value:
      zh: 串行或 8/16-bit 并行 LCD 接口
      en: Serial or 8/16-bit parallel LCD interface
      ja: シリアル・8/16-bitパラレルLCD端子
  - label:
      zh: 音频
      en: Audio
      ja: オーディオ
    value:
      zh: 音频放大器与双扬声器输出
      en: Audio amplifier and two speaker outputs
      ja: オーディオアンプ・スピーカー出力2系統
  - label:
      zh: 存储扩展
      en: Storage expansion
      ja: ストレージ拡張
    value:
      zh: SD 卡槽
      en: SD card slot
      ja: SDカードスロット
resources:
  - label:
      zh: 官方用户指南与引脚表
      en: Official user guide and pinout
      ja: 公式ユーザーガイド・ピン配置
    url: https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32/esp32-lcdkit/user_guide.html
revisionNotes:
  - text:
      zh: LCDKit 是搭配 ESP32-DevKitC 和外接显示屏使用的扩展平台；不把扩展板本身当作内置主控与屏幕的独立终端。
      en: LCDKit is an expansion platform used with ESP32-DevKitC and an external display, not a standalone terminal with an integrated MCU and screen.
      ja: LCDKitはESP32-DevKitCと外付け画面を組み合わせる拡張基板であり、主制御・画面を内蔵した独立端末ではありません。
    sourceUrl: https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/esp32/esp32-lcdkit/user_guide.html
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
