---
id: lilygo-t-watch-2020
name: T-Watch 2020
manufacturer:
  id: lilygo
  name: LILYGO
chip: ESP32
type: integrated-device
summary:
  zh: LILYGO 的可编程穿戴设备，采用 ESP32，配有屏幕、触摸输入、运动传感器、电池供电。
  en: LILYGO programmable wearable device based on ESP32, with display, touch input, motion sensor, battery power.
  ja: ESP32を搭載したLILYGOのプログラム可能なウェアラブルデバイス。ディスプレイ、タッチ入力、モーションセンサー、バッテリー電源を備えています。
officialUrl: https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html
aliases:
  - TTGO T-Watch
features:
  - display
  - touch
  - imu
  - battery
sources:
  - url: https://www.espboards.dev/esp32/twatch/
    checkedAt: 2026-10-15T17:25:01+00:00
  - url: https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html
    checkedAt: 2026-10-15T17:28:14+00:00
cover: https://t-watch-document-en.readthedocs.io/en/latest/_images/t201.png
gallery:
  - image: https://t-watch-document-en.readthedocs.io/en/latest/_images/t201.png
    caption:
      zh: T-Watch 2020 产品图
      en: T-Watch 2020 product photo
      ja: T-Watch 2020 製品画像
    sourceUrl: https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサー
    value:
      zh: ESP32
      en: ESP32
      ja: ESP32
  - label:
      zh: 屏幕
      en: Display
      ja: 画面
    value:
      zh: 1.54 英寸 LCD 电容触摸屏
      en: 1.54-inch capacitive-touch LCD
      ja: 1.54インチ静電容量式タッチLCD
  - label:
      zh: 传感器
      en: Sensors
      ja: センサー
    value:
      zh: BMA423 三轴加速度计 · RTC
      en: BMA423 three-axis accelerometer · RTC
      ja: BMA423 3軸加速度センサー · RTC
  - label:
      zh: 音频
      en: Audio
      ja: オーディオ
    value:
      zh: MAX98357A I2S
      en: MAX98357A I2S
      ja: MAX98357A I2S
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: AXP202 PMU
      en: AXP202 PMU
      ja: AXP202 PMU
  - label:
      zh: 交互
      en: Controls
      ja: 操作
    value:
      zh: 红外发射 · 振动马达
      en: IR transmitter · vibration motor
      ja: 赤外線送信 · 振動モーター
resources:
  - label:
      zh: 官方入门与硬件资料
      en: Official setup and hardware guide
      ja: 公式セットアップ・ハードウェア資料
    url: https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html
revisionNotes:
  - text:
      zh: T-Watch 2020 存在多个硬件版本，音频和引脚配置需核对对应版本；本页不推定各版本通用。
      en: T-Watch 2020 has multiple hardware revisions. Match audio and pin configurations to the specific revision; this record does not imply cross-revision compatibility.
      ja: T-Watch 2020には複数のハードウェア版があります。音声・ピン設定は実機の版に合わせてください。版をまたぐ互換性は前提にしていません。
    sourceUrl: https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html
---

Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.
