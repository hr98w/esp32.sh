---
id: m5stack-sticks3
name: StickS3
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: M5Stack 的便携式语音与传感开发设备，采用 ESP32-S3，配有屏幕、运动传感器、麦克风、电池供电。
  en: M5Stack portable voice and sensing development device based on ESP32-S3, with display, motion sensor, microphone, battery power.
  ja: ESP32-S3を搭載したM5Stackの携帯型の音声・センサー開発デバイス。ディスプレイ、モーションセンサー、マイク、バッテリー電源を備えています。
officialUrl: https://docs.m5stack.com/en/core/StickS3
aliases:
  - M5Stack StickS3
features:
  - display
  - imu
  - microphone
  - speaker
  - battery
sources:
  - url: https://github.com/s0lness/awesome-esp32
  - url: https://docs.m5stack.com/en/core/StickS3
    checkedAt: 2026-10-15T17:27:01+00:00
  - url: https://docs.m5stack.com/zh_CN/core/StickS3
    checkedAt: 2026-10-16T00:06:28+00:00
  - url: https://docs.m5stack.com/ja/core/StickS3
    checkedAt: 2026-10-16T00:06:30+00:00
specifications:
  - label:
      en: SoC
      zh: SoC
      ja: SoC
    value:
      en: ESP32-S3-PICO-1-N8R8 @ Xtensa® 32-bit LX7 dual-core processor, clock frequency 240MHz
      zh: ESP32-S3-PICO-1-N8R8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz
      ja: ESP32-S3-PICO-1-N8R8 @ Xtensa® 32ビット LX7 デュアルコアプロセッサ、動作周波数 240MHz
  - label:
      en: Flash
      zh: Flash
      ja: Flash
    value:
      en: 8MB
      zh: 8MB
      ja: 8MB
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
      zh: 屏幕
      ja: ディスプレイ
    value:
      en: "Model: ST7789P3 / Resolution: 135x240"
      zh: 型号：ST7789P3 / 分辨率：135x240
      ja: 型番：ST7789P3 / 解像度：135x240
  - label:
      en: IMU
      zh: IMU
      ja: IMU
    value:
      en: BMI270
      zh: BMI270
      ja: BMI270
  - label:
      en: Microphone
      zh: 麦克风
      ja: マイク
    value:
      en: "MEMS microphone, Signal-to-Noise Ratio (SNR): 65 dB"
      zh: MEMS 麦克风，信噪比 (SNR)：65 dB
      ja: MEMS マイク、SNR：65 dB
  - label:
      en: Speaker
      zh: 扬声器
      ja: スピーカー
    value:
      en: AW8737 power amplifier + 8Ω@1W 2011 cavity speaker
      zh: AW8737 功放芯片 + 8Ω@1W 2011 型腔体喇叭
      ja: AW8737 アンプチップ + 8Ω@1W 2011 型エンクロージャスピーカー
  - label:
      en: Audio Codec
      zh: 音频编解码器
      ja: オーディオコーデック
    value:
      en: "ES8311: 24-bit resolution, I2S protocol"
      zh: ES8311：24 位分辨率，采用 I2S 协议
      ja: ES8311：24 ビット分解能、I2S プロトコル採用
  - label:
      en: Battery Capacity
      zh: 电池容量
      ja: バッテリー容量
    value:
      en: 250mAh
      zh: 250mAh
      ja: 250mAh
  - label:
      en: Input Power
      zh: 输入电源
      ja: 入力電源
    value:
      en: USB Type-C DC 5V
      zh: USB Type-C DC 5V
      ja: USB Type-C DC 5V
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
      en: 48.0 x 24.0 x 15.0mm
      zh: 48.0 x 24.0 x 15.0mm
      ja: 48.0 x 24.0 x 15.0mm
  - label:
      en: Product Weight
      zh: 产品重量
      ja: 製品重量
    value:
      en: 20.0g
      zh: 20.0g
      ja: 20.0g
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/m5sticks3/program
  - label:
      zh: UIFlow2 入门
      en: UIFlow2 quick start
      ja: UIFlow2入門
    url: https://docs.m5stack.com/en/uiflow2/sticks3/program
  - label:
      zh: 官方原理图
      en: Official schematic
      ja: 公式回路図
    url: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24.pdf
sku: K150
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_02.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_02.webp
    caption:
      zh: StickS3 产品图
      en: StickS3 product photo
      ja: StickS3 製品画像
    sourceUrl: https://docs.m5stack.com/en/core/StickS3
revisionNotes:
  - text:
      zh: 官方建议仅用电池供电时将扬声器音量保持在 75% 以下，以避免功耗过大引发重启。
      en: The official guide recommends keeping speaker volume below 75% on battery power to avoid resets from excessive power draw.
      ja: 公式ガイドでは、電池駆動時の消費電力による再起動を避けるため、スピーカー音量を75%未満にすることを推奨しています。
    sourceUrl: https://docs.m5stack.com/en/core/StickS3
---

Do not infer firmware compatibility solely from the ESP32 chip family. Hardware revisions and peripherals must match the upstream project.
