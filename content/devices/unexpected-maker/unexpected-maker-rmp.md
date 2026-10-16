---
id: unexpected-maker-rmp
name: Reflow Master Pro
manufacturer:
  id: unexpected-maker
  name: Unexpected Maker
chip: ESP32-S2
type: functional-board
summary:
  zh: 基于 ESP32-S2 的回流焊温控终端，配有彩色 TFT、热电偶输入与网页温度曲线管理。
  en: ESP32-S2 reflow-oven controller with a color TFT, thermocouple inputs, and browser-based profile management.
  ja: カラーTFT、熱電対入力、ブラウザーからの温度プロファイル管理を備えるESP32-S2リフロー炉コントローラー。
officialUrl: https://help.unexpectedmaker.com/docs/products/reflow-master-pro/
aliases:
  - UM RMP
features:
  - display
  - usb
sources:
  - url: https://www.espboards.dev/esp32/rmp/
    checkedAt: 2026-10-15T17:56:32+00:00
  - url: https://help.unexpectedmaker.com/docs/products/reflow-master-pro/
    checkedAt: 2026-10-15T17:58:02+00:00
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32-S2FN4R2
      en: ESP32-S2FN4R2
      ja: ESP32-S2FN4R2
  - label:
      zh: 屏幕
      en: Display
      ja: 画面
    value:
      zh: 2.4 英寸彩色 TFT
      en: 2.4-inch color TFT
      ja: 2.4インチカラーTFT
  - label:
      zh: 测温
      en: Temperature sensing
      ja: 温度計測
    value:
      zh: 2 × MAX31855 / K 型热电偶
      en: 2 × MAX31855 / K-type thermocouples
      ja: 2 × MAX31855 / K型熱電対
  - label:
      zh: 接口
      en: Interfaces
      ja: インターフェース
    value:
      zh: USB-C / STEMMA QT I2C / SSR / Auxiliary × 2
      en: USB-C / STEMMA QT I2C / SSR / Auxiliary × 2
      ja: USB-C / STEMMA QT I2C / SSR / Auxiliary × 2
  - label:
      zh: 供电与充电
      en: Power and charging
      ja: 給電・充電
    value:
      zh: USB-C 5V DC / DC Barrel Jack
      en: USB-C 5V DC / DC Barrel Jack
      ja: USB-C 5V DC / DC Barrel Jack
resources:
  - label:
      zh: 官方入门与硬件资料
      en: Official setup and hardware guide
      ja: 公式セットアップ・ハードウェア資料
    url: https://help.unexpectedmaker.com/docs/products/reflow-master-pro/
factoryFeatures:
  zh: 内置回流焊与烘烤模式、五种焊膏曲线，可通过网页管理曲线与设置。需要搭配外接 SSR 和烤箱使用。
  en: Built-in reflow and bake modes with five solder-paste profiles and browser-based profile/settings management. Requires an external SSR and oven.
  ja: リフロー・ベイクモード、5種類のはんだペーストプロファイル、ブラウザー設定を搭載。外付けSSRとオーブンが必要です。
---

Facts reviewed against the linked official documentation. Hardware revisions and lifecycle notes follow the source; no hardware tests performed here.
