---
id: m5stack-stopwatch
name: StopWatch
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: 集成圆形 AMOLED 触摸屏、麦克风、扬声器和六轴运动传感器的便携 ESP32-S3 开发设备，内置电池，支持按键与振动反馈。
  en: A portable ESP32-S3 device with a round AMOLED touchscreen, microphone, speaker, six-axis motion sensor, built-in battery, buttons, and vibration feedback.
  ja: 円形AMOLEDタッチ画面、マイク、スピーカー、6軸モーションセンサーを搭載する携帯型ESP32-S3デバイス。バッテリー、ボタン、振動機能を備えています。
officialUrl: https://docs.m5stack.com/en/core/StopWatch
aliases:
  - M5Stack StopWatch
features:
  - display
  - touch
  - microphone
  - speaker
  - imu
  - battery
sources:
  - url: https://docs.m5stack.com/en/core/StopWatch
    checkedAt: 2026-10-16T00:00:00Z
  - url: https://docs.m5stack.com/en/guide/stopwatch/usage
    checkedAt: 2026-10-16T00:00:00Z
  - url: https://shop.m5stack.com/products/m5stack-stopwatch-dev-kit-esp32-s3
    checkedAt: 2026-10-16T00:00:00Z
sku: C152
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152_stopwatch_mainpictures_02.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152_stopwatch_mainpictures_02.webp
    caption:
      zh: 产品外观
      en: Product view
      ja: 製品外観
    sourceUrl: https://docs.m5stack.com/en/core/StopWatch
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152_stopwatch_mainpictures_01.webp
    caption:
      zh: 接口与硬件概览（官方英文标注）
      en: Hardware and interfaces (official English annotations)
      ja: 端子とハードウェア（公式英語表記）
    sourceUrl: https://docs.m5stack.com/en/core/StopWatch
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32-S3R8 · 双核，最高 240MHz
      en: ESP32-S3R8 · dual-core, up to 240MHz
      ja: ESP32-S3R8 · デュアルコア、最大240MHz
  - label:
      zh: 存储
      en: Memory
      ja: メモリ
    value:
      zh: 16MB Flash / 8MB PSRAM
      en: 16MB Flash / 8MB PSRAM
      ja: 16MB Flash / 8MB PSRAM
  - label:
      zh: 屏幕
      en: Display
      ja: 画面
    value:
      zh: 1.75 英寸圆形 AMOLED · 466 × 466 · 触摸
      en: 1.75-inch round AMOLED · 466 × 466 · touch
      ja: 1.75インチ円形AMOLED · 466 × 466 · タッチ対応
  - label:
      zh: 音频
      en: Audio
      ja: オーディオ
    value:
      zh: MEMS 麦克风 · ES8311 编解码器 · 1W 扬声器
      en: MEMS microphone · ES8311 codec · 1W speaker
      ja: MEMSマイク · ES8311コーデック · 1Wスピーカー
  - label:
      zh: 传感器
      en: Sensors
      ja: センサー
    value:
      zh: BMI270 六轴 IMU · RX8130CE 实时时钟
      en: BMI270 six-axis IMU · RX8130CE RTC
      ja: BMI270 6軸IMU · RX8130CE RTC
  - label:
      zh: 交互
      en: Controls
      ja: 操作
    value:
      zh: 2 个可编程按键 · 电源键 · 振动马达
      en: 2 programmable buttons · power button · vibration motor
      ja: プログラム可能なボタン×2 · 電源ボタン · 振動モーター
  - label:
      zh: 无线
      en: Wireless
      ja: 無線
    value:
      zh: 2.4GHz Wi-Fi
      en: 2.4GHz Wi-Fi
      ja: 2.4GHz Wi-Fi
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: 450mAh 内置电池 · USB-C 5V 输入
      en: 450mAh built-in battery · USB-C 5V input
      ja: 450mAh内蔵バッテリー · USB-C 5V入力
  - label:
      zh: 扩展
      en: Expansion
      ja: 拡張
    value:
      zh: HY2.0-4P Port.A · 背部 2.54mm 7-pin + 6-pin
      en: HY2.0-4P Port.A · rear 2.54mm 7-pin + 6-pin
      ja: HY2.0-4P Port.A · 背面2.54mm 7ピン＋6ピン
  - label:
      zh: 尺寸 / 重量
      en: Size / weight
      ja: 寸法・重量
    value:
      zh: 52 × 52 × 15.5mm / 39g
      en: 52 × 52 × 15.5mm / 39g
      ja: 52 × 52 × 15.5mm / 39g
factoryFeatures:
  zh: 出厂固件可体验图片徽章、表盘、闹钟、秒表、运动数据展示和音频频谱。图片徽章支持通过浏览器上传图片。
  en: The factory firmware includes a photo badge, watch faces, alarm clock, stopwatch, motion visualization, and audio spectrum. Upload badge images through a browser.
  ja: 出荷時ファームウェアで画像バッジ、文字盤、アラーム、ストップウォッチ、モーション表示、音声スペクトルを体験できます。バッジ画像はブラウザからアップロードできます。
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/stopwatch/program
  - label:
      zh: 出厂固件使用与恢复入口
      en: Factory firmware guide and restore links
      ja: 出荷時ファームウェアの使い方・復元リンク
    url: https://docs.m5stack.com/en/guide/stopwatch/usage
  - label:
      zh: 引脚、原理图与开发库
      en: Pinout, schematics, and development libraries
      ja: ピン配置・回路図・開発ライブラリ
    url: https://docs.m5stack.com/en/core/StopWatch
revisionNotes:
  - text:
      zh: v1.0 部分设备背部标为 BAT 的引脚实际为 5V 输入，不可连接锂电池。v1.0.1 才将该引脚调整为 BAT。请根据实物版本核对官方说明。
      en: "On some v1.0 units, the rear pin labeled BAT is actually a 5V input: do not connect a lithium battery. The pin changes to BAT in v1.0.1. Check the official notes for your hardware revision."
      ja: 一部のv1.0製品は背面のBAT表記ピンが実際には5V入力です。リチウム電池を接続しないでください。v1.0.1でBATピンに変更されています。実機の版に対応する公式説明をご確認ください。
    sourceUrl: https://docs.m5stack.com/en/core/StopWatch
referencePrice:
  amount: 45
  currency: USD
  sourceUrl: https://shop.m5stack.com/products/m5stack-stopwatch-dev-kit-esp32-s3
  checkedAt: 2026-10-16
---
