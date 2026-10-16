---
id: m5stack-papers3
name: PaperS3
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的电子纸触控开发终端，采用 ESP32-S3，配有电子纸屏幕、触摸输入、电池供电。
  en: M5Stack touchscreen e-paper development terminal based on ESP32-S3, with e-paper display, touch input, battery power.
  ja: ESP32-S3を搭載したM5Stackのタッチ式電子ペーパー開発端末。電子ペーパーディスプレイ、タッチ入力、バッテリー電源を備えています。
officialUrl: https://docs.m5stack.com/en/core/PaperS3
aliases:
  - M5Stack PaperS3
features:
  - epaper
  - touch
  - battery
sources:
  - url: https://github.com/s0lness/awesome-esp32
  - url: https://docs.m5stack.com/en/core/PaperS3
    checkedAt: 2026-10-15T17:27:07+00:00
  - url: https://docs.m5stack.com/zh_CN/core/PaperS3
    checkedAt: 2026-10-16T00:06:04+00:00
  - url: https://docs.m5stack.com/ja/core/PaperS3
    checkedAt: 2026-10-16T00:06:06+00:00
  - url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139.pdf
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-S3R8 @ Xtensa® 32-bit LX7 dual-core processor, clock frequency 240MHz
      zh: ESP32-S3R8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz
      ja: ESP32-S3R8 @ Xtensa® 32ビット LX7 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 16MB
      zh: 16MB
      ja: 16MB
  - label:
      en: PSRAM
      zh: PSRAM
      ja: PSRAM
    value:
      en: 8MB Octal
      zh: 8MB Octal
      ja: 8MB Octal
  - label:
      en: Display
      zh: 显示屏
      ja: ディスプレイ
    value:
      en: '4.7" touch e-ink screen (full screen) @EPD_ED047TC1 / Resolution: 960x540 pixels / 16-level grayscale display'
      zh: 4.7" 触控电子墨水屏（全面屏）@EPD_ED047TC1 / 分辨率：960x540 像素 / 16 级灰度显示
      ja: 4.7" タッチ電子ペーパーフルスクリーン @EPD_ED047TC1、解像度：960×540、16 階調グレースケール
  - label:
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: "3.7V@1800mAh lithium battery @ charging chip: LGS4056H"
      zh: 3.7V@1800mAh 锂电池 @充电芯片：LGS4056H
      ja: 3.7 V @ 1800 mAh リチウムバッテリー（充電 IC：LGS4056H）
  - label:
      en: Power Input
      zh: 电源输入
      ja: 入力電源
    value:
      en: 5V@500mA
      zh: 5V@500mA
      ja: 5 V @ 500 mA
  - label:
      en: Button
      zh: 按键
      ja: ボタン
    value:
      en: 1x physical button (for device control, power on/off, reset, download mode)
      zh: 1x 物理按键（用于设备控制，开关机，复位，下载模式）
      ja: 物理ボタン ×1（電源、リセット、ダウンロードモード）
  - label:
      en: Wi-Fi
      zh: Wi-Fi
      ja: Wi-Fi
    value:
      en: 2.4 GHz Wi-Fi
      zh: 2.4 GHz Wi-Fi
      ja: 2.4 GHz Wi-Fi
  - label:
      zh: 机身尺寸
      en: Body dimensions
      ja: 本体寸法
    value:
      zh: 121.5 × 67 × 7.7mm（不含挂耳和侧键突出部分）
      en: 121.5 × 67 × 7.7mm (excluding the hanging tab and side-button protrusion)
      ja: 121.5 × 67 × 7.7mm（吊り下げ部・側面ボタンの突出部を除く）
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 89.0g
      zh: 89.0g
      ja: 89.0g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5papers3/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/m5papers3/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/sch_papers3_V1.0.pdf
  - label:
      zh: 官方尺寸图
      en: Official mechanical drawing
      ja: 公式寸法図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/C139.pdf
sku: C139
cover: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/12.webp
gallery:
  - image: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/12.webp
    caption:
      zh: PaperS3 产品图
      en: PaperS3 product photo
      ja: PaperS3 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/PaperS3
---

Do not infer firmware compatibility solely from the ESP32 chip family. Hardware revisions and peripherals must match the upstream project.
