---
id: m5stack-tab5
name: Tab5
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-P4
type: integrated-device
summary:
  zh: M5Stack 的平板形态交互终端，采用 ESP32-P4，配有屏幕、触摸输入、摄像头、RS-485 接口。
  en: M5Stack tablet-style interaction terminal based on ESP32-P4, with display, touch input, camera, RS-485 interface.
  ja: ESP32-P4を搭載したM5Stackのタブレット型の操作端末。ディスプレイ、タッチ入力、カメラ、RS-485インターフェースを備えています。
officialUrl: https://docs.m5stack.com/en/core/Tab5
aliases:
  - M5Stack Tab5
features:
  - display
  - touch
  - camera
  - rs485
sources:
  - url: https://www.espboards.dev/esp32/m5stack-tab5/
    checkedAt: 2026-10-15T17:23:49+00:00
  - url: https://docs.m5stack.com/en/core/Tab5
    checkedAt: 2026-10-15T17:27:33+00:00
  - url: https://docs.m5stack.com/zh_CN/core/Tab5
    checkedAt: 2026-10-16T00:06:32+00:00
  - url: https://docs.m5stack.com/ja/core/Tab5
    checkedAt: 2026-10-16T00:06:34+00:00
specifications:
  - label:
      en: Main Controller SoC
      zh: 主控制器 SoC
      ja: メインコントローラ SoC
    value:
      en: ESP32-P4NRW32@RISC-V 32-bit Dual-core 360MHz + LP Single-core 40MHz
      zh: ESP32-P4NRW32@RISC-V 32 位双核 360MHz + LP 单核 40MHz
      ja: ESP32-P4NRW32@RISC-V 32 ビットデュアルコア 360MHz + LP シングルコア 40MHz
  - label:
      en: Wireless Module SoC
      zh: 无线模块 SoC
      ja: ワイヤレスモジュール SoC
    value:
      en: ESP32-C6-MINI-1U
      zh: ESP32-C6-MINI-1U
      ja: ESP32-C6-MINI-1U
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
      en: 32MB Octal
      zh: 32MB Octal
      ja: 32MB Octal
  - label:
      en: Display
      zh: 显示
      ja: ディスプレイ
    value:
      zh: 5 英寸 IPS 触摸屏 · 1280 × 720 · ST7123 / ST7121
      en: 5-inch IPS touchscreen · 1280 × 720 · ST7123 / ST7121
      ja: 5インチIPSタッチ画面 · 1280 × 720 · ST7123 / ST7121
  - label:
      en: Camera
      zh: 摄像头
      ja: カメラ
    value:
      en: SC2356 @ 2MP (1600×1200), via MIPI‑CSI interface
      zh: SC2356 @ 2MP（1600×1200），通过 MIPI‑CSI 接口
      ja: SC2356 @ 2MP（1600×1200）、MIPI‑CSI インターフェース経由
  - label:
      en: Motion Sensor
      zh: 运动传感器
      ja: モーションセンサー
    value:
      en: BMI270 six-axis (accelerometer + gyroscope, support interrupt wake-up)
      zh: BMI270 六轴（加速度计 + 陀螺仪，支持中断唤醒）
      ja: BMI270 六軸（加速度計 + ジャイロ、割込みによるウェイクアップ対応）
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: Dual microphone system (AEC echo cancellation)
      zh: 双麦克风系统（AEC 回声消除）
      ja: デュアルマイクシステム（AEC エコーキャンセル）
  - label:
      en: Speaker
      zh: 扬声器
      ja: スピーカー
    value:
      en: 1W@8Ω NS4150B
      zh: 1W@8Ω NS4150B
      ja: 1W@8Ω NS4150B
  - label:
      en: Audio Chip
      zh: 音频芯片
      ja: オーディオチップ
    value:
      en: ES8388 codec, ES7210 AEC front end
      zh: ES8388 编解码，ES7210 AEC 前端
      ja: ES8388 コーデック、ES7210 AEC フロントエンド
  - label:
      en: Battery
      zh: 电池
      ja: バッテリー
    value:
      en: NP-F550 removable lithium battery, 7.4V@2000mAh (14.8 Wh)
      zh: NP-F550 可拆卸锂电池，7.4V@2000mAh（14.8 Wh）
      ja: NP-F550 着脱式リチウムバッテリー、7.4V@2000mAh（14.8 Wh）
  - label:
      en: Expansion Interface
      zh: 扩展接口
      ja: 拡張インターフェース
    value:
      en: 1× HY2.0-4P, 1× M5-Bus, GPIO_EXT expansion bus
      zh: 1× HY2.0-4P，1× M5-Bus，GPIO_EXT 拓展总线
      ja: 1× HY2.0-4P、1× M5-Bus、GPIO_EXT 拡張バス
  - label:
      en: USB Ports
      zh: USB 端口
      ja: USB ポート
    value:
      en: USB Type-A (Host), USB Type-C (USB 2.0 OTG)
      zh: USB Type-A（Host），USB Type-C（USB 2.0 OTG）
      ja: USB Type-A（ホスト）、USB Type-C（USB 2.0 OTG）
  - label:
      en: Product Size
      zh: 产品尺寸
      ja: 製品サイズ
    value:
      en: "Tab5: 128.0 x 80.0 x 12.0mm / Tab5 Kit: 128.0 x 80.0 x 26.7mm"
      zh: Tab5：128.0 x 80.0 x 12.0mm / Tab5 Kit：128.0 x 80.0 x 26.7mm
      ja: Tab5：128.0 x 80.0 x 12.0mm / Tab5 Kit：128.0 x 80.0 x 26.7mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: "Tab5: 120.9g / Tab5 Kit: 217.6g / Battery: 96.7g"
      zh: Tab5：120.9g / Tab5 Kit：217.6g / 电池：96.7g
      ja: Tab5：120.9g / Tab5 Kit：217.6g / 電池：96.7g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5tab5/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/Tab5/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Schematics_PDF.pdf
  - label:
      zh: 出厂固件资料
      en: Factory firmware resources
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/esp_idf/m5tab5/userdemo
sku: C145/K145
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_03.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_03.webp
    caption:
      zh: Tab5 产品图
      en: Tab5 product photo
      ja: Tab5 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/Tab5
revisionNotes:
  - text:
      zh: C145 是 Tab5 主机，K145 是带 NP-F550 电池的套装。电池、厚度和重量应按具体 SKU 核对。
      en: C145 is the Tab5 main unit; K145 is the kit with an NP-F550 battery. Check the exact SKU for included battery, thickness, and weight.
      ja: C145はTab5本体、K145はNP-F550バッテリー付きキットです。電池の同梱、厚さ、重量はSKUごとに確認してください。
    sourceUrl: https://docs.m5stack.com/en/core/Tab5
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
