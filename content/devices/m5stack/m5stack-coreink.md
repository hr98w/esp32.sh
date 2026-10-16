---
id: m5stack-coreink
name: CoreInk
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32
type: integrated-device
summary:
  zh: M5Stack 的低功耗信息显示设备，采用 ESP32，配有电子纸屏幕、电池供电、GPIO 扩展。
  en: M5Stack low-power information display based on ESP32, with e-paper display, battery power, GPIO expansion.
  ja: ESP32を搭載したM5Stackの低消費電力の情報表示デバイス。電子ペーパーディスプレイ、バッテリー電源、GPIO拡張を備えています。
officialUrl: https://docs.m5stack.com/en/core/coreink
aliases:
  - M5Stack-CoreInk
features:
  - epaper
  - battery
  - gpio
sources:
  - url: https://www.espboards.dev/esp32/m5stack-coreink/
    checkedAt: 2026-10-15T17:23:35+00:00
  - url: https://docs.m5stack.com/en/core/coreink
    checkedAt: 2026-10-15T17:27:23+00:00
  - url: https://docs.m5stack.com/zh_CN/core/coreink
    checkedAt: 2026-10-16T00:05:44+00:00
  - url: https://docs.m5stack.com/ja/core/coreink
    checkedAt: 2026-10-16T00:05:46+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-PICO-D4 @ Xtensa® 32-bit LX6 dual-core processor, clock frequency up to 240MHz
      zh: ESP32-PICO-D4 @ Xtensa® 32 位 LX6 双核处理器，主频 240MHz
      ja: ESP32-PICO-D4 @ Xtensa® 32ビット LX6 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 4MB
      zh: 4MB
      ja: 4MB
  - label:
      en: E-Ink Display
      zh: 墨水屏
      ja: 電子ペーパーディスプレイ
    value:
      zh: 1.54 英寸电子纸 · 200 × 200 · GDEW0154M09
      en: 1.54-inch e-paper · 200 × 200 · GDEW0154M09
      ja: 1.54インチ電子ペーパー · 200 × 200 · GDEW0154M09
  - label:
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: 390mAh@3.7V
      zh: 390mAh@3.7V
      ja: 390mAh@3.7V
  - label:
      en: Input Voltage
      zh: 输入电压
      ja: 入力電圧
    value:
      en: 5V @ 500mA
      zh: 5V @ 500mA
      ja: 5V @ 500mA
  - label:
      en: Interface
      zh: 接口
      ja: インターフェース
    value:
      en: USB Type-C x 1, HY2.0-4P x 1, M5-Bus female socket, top HAT expansion interface
      zh: USB Type-C x 1，HY2.0-4P x 1 ，M5-Bus 总线母座，顶部 HAT 拓展接口
      ja: USB Type-C x 1、HY2.0-4P x 1、M5-Bus バスソケット、上部 HAT 拡張インターフェース
  - label:
      en: Physical Buttons
      zh: 物理按键
      ja: 物理ボタン
    value:
      en: Programmable button x1, reset button x1, power button x1
      zh: 可编程按键 x1 ，复位按键 x1，电源按键 x1
      ja: プログラマブルボタン x1 、リセットボタン x1、電源ボタン x1
  - label:
      en: RTC
      zh: RTC
      ja: RTC
    value:
      en: BM8563
      zh: BM8563
      ja: BM8563
  - label:
      en: Wi-Fi
      zh: Wi-Fi
      ja: Wi-Fi
    value:
      en: 2.4 GHz Wi-Fi
      zh: 2.4 GHz Wi-Fi
      ja: 2.4 GHz Wi-Fi
  - label:
      en: Product Size
      zh: 产品尺寸
      ja: 製品サイズ
    value:
      en: 56.0 x 40.0 x 16.0mm
      zh: 56.0 x 40.0 x 16.0mm
      ja: 56.0 x 40.0 x 16.0mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 31.5g
      zh: 31.5g
      ja: 31.5g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5coreink/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5coreink/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/coreink/coreink_sch.pdf
sku: K048
cover: https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_02.webp
gallery:
  - image: https://static-cdn.m5stack.com/resource/docs/products/core/coreink/coreink_02.webp
    caption:
      zh: CoreInk 产品图
      en: CoreInk product photo
      ja: CoreInk 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/coreink
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
