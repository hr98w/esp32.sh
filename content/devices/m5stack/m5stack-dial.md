---
id: m5stack-dial
name: Dial V1.1
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的旋钮式控制终端，采用 ESP32-S3，配有屏幕、触摸输入、旋转编码器、RFID 读取。
  en: M5Stack rotary control terminal based on ESP32-S3, with display, touch input, rotary encoder, RFID reader.
  ja: ESP32-S3を搭載したM5Stackのダイヤル式の操作端末。ディスプレイ、タッチ入力、ロータリーエンコーダー、RFIDリーダーを備えています。
officialUrl: https://docs.m5stack.com/en/core/M5Dial%20V1.1
aliases:
  - M5Stack Dial V1.1
features:
  - display
  - touch
  - encoder
  - rfid
sources:
  - url: https://www.espboards.dev/esp32/m5stack-dial/
    checkedAt: 2026-10-15T17:23:40+00:00
  - url: https://docs.m5stack.com/en/core/M5Dial%20V1.1
    checkedAt: 2026-10-15T17:27:27+00:00
  - url: https://docs.m5stack.com/zh_CN/core/M5Dial%20V1.1
    checkedAt: 2026-10-16T00:05:52+00:00
  - url: https://docs.m5stack.com/ja/core/M5Dial%20V1.1
    checkedAt: 2026-10-16T00:05:54+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-S3FN8 @ Xtensa® 32-bit LX7 dual-core processor, clock frequency 240MHz
      zh: ESP32-S3FN8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz
      ja: ESP32-S3FN8 @ Xtensa® 32ビット LX7 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 8MB
      zh: 8MB
      ja: 8MB
  - label:
      en: Screen Driver
      zh: 屏幕驱动
      ja: ディスプレイドライバ
    value:
      en: GC9A01 / 1.28 Inch 240 x 240px
      zh: GC9A01 / 1.28 Inch 240 x 240px
      ja: GC9A01 / 1.28 インチ 240 x 240px
  - label:
      en: Touch Driver
      zh: 触摸驱动
      ja: タッチドライバ
    value:
      en: FT3267
      zh: FT3267
      ja: FT3267
  - label:
      en: Encoder
      zh: 编码器
      ja: エンコーダ
    value:
      en: "Resolution: 16 positions, 64 pulses/rev"
      zh: 分辨率：16 定位，64 脉冲 / 圈
      ja: 解像度：16 位置、64 パルス / 回転
  - label:
      en: RFID
      zh: RFID
      ja: RFID
    value:
      en: "WS1850S @ Tag operating frequency: 13.56 MHz, ISO/IEC 14443 Type A/Type B protocol"
      zh: "WS1850S @标签工作频率: 13.56 MHz ,ISO/IEC 14443 Type A/Type B 协议"
      ja: "WS1850S @タグ動作周波数: 13.56 MHz、ISO/IEC 14443 Type A/Type B プロトコル"
  - label:
      en: Wide Voltage Input Range
      zh: 宽电压输入范围
      ja: 広電圧入力範囲
    value:
      en: DC 6 ~ 36V
      zh: DC 6~36V
      ja: DC 6~36V
  - label:
      en: USB
      zh: USB
      ja: USB
    value:
      en: USB OTG, USB Serial/JTAG
      zh: USB OTG, USB Serial/JTAG
      ja: USB OTG, USB Serial/JTAG
  - label:
      en: Battery Socket Specification
      zh: 电池座子规格
      ja: バッテリーソケット仕様
    value:
      en: 1.25mm-2P
      zh: 1.25mm-2P
      ja: 1.25mm-2P
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
      en: 51.0 x 51.0 x 32.3mm
      zh: 51.0 x 51.0 x 32.3mm
      ja: 51.0 x 51.0 x 32.3mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 46.2g
      zh: 46.2g
      ja: 46.2g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5dial/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5dial/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial.pdf
sku: K130-V11
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_02.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_02.webp
    caption:
      zh: Dial V1.1 产品图
      en: Dial V1.1 product photo
      ja: Dial V1.1 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/M5Dial%20V1.1
revisionNotes:
  - text:
      zh: 本页参数和产品图对应 M5Dial V1.1（K130-V11）。刷写前请核对上游项目所支持的硬件版本。
      en: Specifications and product images on this page refer to M5Dial V1.1 (K130-V11). Check the hardware revisions supported by the upstream project before flashing.
      ja: 本ページの仕様と製品画像はM5Dial V1.1（K130-V11）のものです。書き込み前に上流プロジェクトが対応するハードウェア版を確認してください。
    sourceUrl: https://docs.m5stack.com/en/core/M5Dial%20V1.1
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
