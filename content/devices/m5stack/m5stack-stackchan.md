---
id: m5stack-stackchan
name: StackChan (CoreS3)
manufacturer:
  id: m5stack
  name: M5Stack
chip: ESP32-S3
type: integrated-device
summary:
  zh: 基于 CoreS3 的桌面机器人，集成触控屏、摄像头、音频和舵机运动机构。
  en: A CoreS3-based desktop robot with a touchscreen, camera, audio, and servo motion.
  ja: タッチ画面、カメラ、オーディオ、サーボ駆動部を備える、CoreS3ベースの卓上ロボット。
officialUrl: https://docs.m5stack.com/en/StackChan
aliases:
  - M5StackChan
  - M5Stack StackChan
  - K151
  - K151-R
features:
  - display
  - touch
  - camera
  - audio
  - imu
  - battery
  - servo
sources:
  - url: https://github.com/stack-chan/stack-chan#readme
  - url: https://docs.m5stack.com/en/StackChan
    checkedAt: 2026-10-15T18:29:21+00:00
cover: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/K151_stack_chan_main_pictures_03.webp
gallery:
  - image: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/K151_stack_chan_main_pictures_03.webp
    caption:
      zh: StackChan (CoreS3) 产品图
      en: StackChan (CoreS3) product photo
      ja: StackChan (CoreS3) 製品画像
    sourceUrl: https://docs.m5stack.com/en/StackChan
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32-S3 · 240MHz
      en: ESP32-S3 · 240MHz
      ja: ESP32-S3 · 240MHz
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
      zh: 2 英寸 IPS 触摸屏 · 320 × 240
      en: 2-inch IPS touchscreen · 320 × 240
      ja: 2インチIPSタッチ画面 · 320 × 240
  - label:
      zh: 音频
      en: Audio
      ja: オーディオ
    value:
      zh: 双麦克风 ES7210 · 1W 扬声器
      en: ES7210 dual microphones · 1W speaker
      ja: ES7210デュアルマイク · 1Wスピーカー
  - label:
      zh: 传感器
      en: Sensors
      ja: センサー
    value:
      zh: BMI270 + BMM150 / LTR-553ALS-WA / ST25R3916
      en: BMI270 + BMM150 / LTR-553ALS-WA / ST25R3916
      ja: BMI270 + BMM150 / LTR-553ALS-WA / ST25R3916
  - label:
      zh: 运动机构
      en: Motion
      ja: 駆動機構
    value:
      zh: 水平 360°、垂直 90°反馈舵机
      en: 360° pan and 90° tilt feedback servos
      ja: 水平360°・垂直90°フィードバックサーボ
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: 550mAh 电池 · USB-C
      en: 550mAh battery · USB-C
      ja: 550mAhバッテリー · USB-C
  - label:
      zh: 接口
      en: Interfaces
      ja: インターフェース
    value:
      zh: microSD / Grove × 3 / USB OTG
      en: microSD / Grove × 3 / USB OTG
      ja: microSD / Grove × 3 / USB OTG
  - label:
      zh: 尺寸
      en: Dimensions
      ja: 寸法
    value:
      zh: 54.0 × 70.5 × 61.5mm
      en: 54.0 × 70.5 × 61.5mm
      ja: 54.0 × 70.5 × 61.5mm
resources:
  - label:
      zh: Arduino 入门
      en: Arduino quick start
      ja: Arduino入門
    url: https://docs.m5stack.com/en/arduino/stackchan/program
  - label:
      zh: 出厂固件说明
      en: Factory firmware guide
      ja: 出荷時ファームウェア資料
    url: https://docs.m5stack.com/en/StackChan#factory-firmware
sku: K151 / K151-R
revisionNotes:
  - text:
      zh: K151 与带遥控器的 K151-R 套装内容不同；项目针对其他 Stack-chan 自组装版本的支持不能直接视为适配本机。
      en: K151 and the K151-R remote-control kit have different contents. Support for other DIY Stack-chan builds does not automatically cover this device.
      ja: K151とリモコン付きK151-Rは同梱品が異なります。他の自作Stack-chan構成向けプロジェクトが本製品に対応するとは限りません。
    sourceUrl: https://docs.m5stack.com/en/StackChan
---

This is the complete StackChan CoreS3 robot (K151 family), not a bare CoreS3 or a Stack-chan RT. The manufacturer documents controller-specific app support.
