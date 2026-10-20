---
type: integrated-device
id: waveshare-esp32-s3-touch-amoled-2-16
name: ESP32-S3-Touch-AMOLED-2.16
manufacturer:
  id: waveshare
  name: Waveshare
chip: ESP32-S3
summary:
  zh: 带外壳和实体按键的 ESP32-S3 桌面显示与语音开发终端，配备 2.16 英寸 480×480 AMOLED 触摸屏、双麦克风、音频输出、IMU 和
    RTC，可用于状态看板和交互项目。
  en: An enclosed ESP32-S3 display and audio development terminal with physical
    buttons, a 2.16-inch 480×480 AMOLED touchscreen, dual microphones, audio
    output, an IMU and RTC for dashboards and interactive projects.
  ja: ケースと物理ボタンを備えたESP32-S3の表示・音声開発端末。2.16インチ480×480
    AMOLEDタッチ画面、デュアルマイク、音声出力、IMU、RTCを搭載し、ダッシュボードや対話型プロジェクトに利用できます。
officialUrl: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16
aliases:
  - Waveshare ESP32-S3-Touch-AMOLED-2.16
  - 微雪 ESP32-S3 2.16 英寸 AMOLED
  - ESP32-S3-Touch-AMOLED-2.16-EN
features:
  - display
  - touch
  - audio
  - microphone
  - speaker
  - imu
  - battery
  - usb
  - sd
cover: https://docs.waveshare.com/assets/images/ESP32-S3-Touch-AMOLED-2.16-showcase-174b30e4b87190a8ea342215849d233f.webp
gallery:
  - image: https://docs.waveshare.com/assets/images/ESP32-S3-Touch-AMOLED-2.16-showcase-174b30e4b87190a8ea342215849d233f.webp
    caption:
      zh: 带外壳的 ESP32-S3-Touch-AMOLED-2.16 官方产品图
      en: Official ESP32-S3-Touch-AMOLED-2.16 photo with enclosure
      ja: ESP32-S3-Touch-AMOLED-2.16のケース付き公式製品画像
    sourceUrl: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16
specifications:
  - label:
      zh: 主控
      en: Processor
      ja: プロセッサ
    value:
      zh: ESP32-S3R8 · 双核 Xtensa LX7 · 最高 240MHz
      en: ESP32-S3R8 · dual-core Xtensa LX7 · up to 240MHz
      ja: ESP32-S3R8 · デュアルコアXtensa LX7 · 最大240MHz
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
      zh: 2.16 英寸 AMOLED · 480 × 480 · 1670 万色 · CO5300 · QSPI
      en: 2.16-inch AMOLED · 480 × 480 · 16.7M colors · CO5300 · QSPI
      ja: 2.16インチAMOLED · 480 × 480 · 1670万色 · CO5300 · QSPI
  - label:
      zh: 触摸
      en: Touch
      ja: タッチ
    value:
      zh: CST9220 电容触摸 · I²C
      en: CST9220 capacitive touch · I²C
      ja: CST9220静電容量式タッチ · I²C
  - label:
      zh: 无线
      en: Wireless
      ja: 無線
    value:
      zh: 2.4GHz Wi-Fi 802.11 b/g/n / Bluetooth 5 LE
      en: 2.4GHz Wi-Fi 802.11 b/g/n / Bluetooth 5 LE
      ja: 2.4GHz Wi-Fi 802.11 b/g/n / Bluetooth 5 LE
  - label:
      zh: 音频
      en: Audio
      ja: 音声
    value:
      zh: 双麦克风 · ES7210 麦克风 ADC · ES8311 音频编解码器
      en: Dual microphones · ES7210 microphone ADC · ES8311 audio codec
      ja: デュアルマイク · ES7210マイクADC · ES8311オーディオコーデック
  - label:
      zh: 传感器与时钟
      en: Sensors and clock
      ja: センサー・時計
    value:
      zh: QMI8658 六轴 IMU / PCF85063ATL RTC
      en: QMI8658 6-axis IMU / PCF85063ATL RTC
      ja: QMI8658 6軸IMU / PCF85063ATL RTC
  - label:
      zh: 供电
      en: Power
      ja: 電源
    value:
      zh: USB-C / 3.7V 锂电池 MX1.25 2PIN 接口 · AXP2101 电源管理
      en: USB-C / 3.7V Li-ion battery via MX1.25 2-pin connector · AXP2101 power
        management
      ja: USB-C / MX1.25 2ピン経由の3.7Vリチウム電池 · AXP2101電源管理
  - label:
      zh: 按键与扩展
      en: Controls and expansion
      ja: ボタン・拡張
    value:
      zh: BOOT、PWR、GPIO18 按键 · TF 卡槽 · GPIO 焊盘
      en: BOOT, PWR and GPIO18 buttons · TF card slot · GPIO pads
      ja: BOOT・PWR・GPIO18ボタン · TFカードスロット · GPIOパッド
factoryFeatures:
  zh: 官方出厂固件提供基于 Brookesia 的应用界面，可体验绘图、计算器、音频频谱、重力球及小智 AI 等示例；视频/TF 示例需另备相应文件或 TF
    卡，网络语音功能需按官方资料配置。
  en: Factory firmware offers a Brookesia app interface with drawing, calculator,
    audio-spectrum, gravity-ball and XiaoZhi AI demos. Video/TF examples need
    suitable files or a TF card; network voice features require the official
    setup.
  ja: 出荷時ファームウェアはBrookesiaのアプリ画面で描画、電卓、音声スペクトラム、重力ボール、XiaoZhi
    AIなどを提供します。動画・TFの例には対応ファイルやTFカードが必要で、ネットワーク音声機能は公式手順で設定します。
resources:
  - label:
      zh: 官方文档与引脚说明
      en: Official documentation and pinout
      ja: 公式ドキュメント・ピン配置
    url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16
  - label:
      zh: 官方示例、原理图与资料下载
      en: Official examples, schematics and downloads
      ja: 公式サンプル・回路図・ダウンロード
    url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16/Resources-And-Documents
  - label:
      zh: 出厂固件与恢复步骤
      en: Factory firmware and recovery
      ja: 出荷時ファームウェア・復元手順
    url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16/Instructions-For-Use
  - label:
      zh: Arduino 开发教程
      en: Arduino development guide
      ja: Arduino開発ガイド
    url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16/Arduino
  - label:
      zh: ESP-IDF 开发教程
      en: ESP-IDF development guide
      ja: ESP-IDF開発ガイド
    url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16/ESP-IDF
revisionNotes:
  - text:
      zh: 官方商品页当前标价为 29.99–31.99 美元，提供含电池和不含电池选项；本页参考价记录区间低价，电池是否随附及 SKU 以所选套餐为准。
      en: The official listing shows USD 29.99–31.99 with battery-included and
        battery-excluded options. The reference price records the lower end;
        check the selected bundle for its battery and SKU.
      ja: 公式価格は29.99～31.99米ドルで、電池付き・電池なしを選択できます。参考価格は下限を記録しており、電池の同梱とSKUは選択したセットで確認してください。
    sourceUrl: https://www.waveshare.com/esp32-s3-touch-amoled-2.16.htm
  - text:
      zh: 本条目为 ESP32-S3 版 2.16 英寸型号，不与 ESP32-C6 版、2.06 英寸或其他 AMOLED 板混用固件。
      en: This entry covers the 2.16-inch ESP32-S3 model. Do not interchange firmware
        with the ESP32-C6 version, 2.06-inch models or other AMOLED boards.
      ja: 本項目は2.16インチESP32-S3版です。ESP32-C6版、2.06インチ版、ほかのAMOLEDボードのファームウェアを流用しないでください。
    sourceUrl: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16
referencePrice:
  amount: 29.99
  currency: USD
  sourceUrl: https://www.waveshare.com/esp32-s3-touch-amoled-2.16.htm
  checkedAt: 2026-10-20
sources:
  - url: https://www.waveshare.com/esp32-s3-touch-amoled-2.16.htm
    checkedAt: 2026-10-20T04:01:37+00:00
  - url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16
    checkedAt: 2026-10-20T04:01:37+00:00
  - url: https://docs.waveshare.com/ESP32-S3-Touch-AMOLED-2.16/Instructions-For-Use
    checkedAt: 2026-10-20T04:02:37+00:00
---

Manufacturer specifications and photos reviewed; no device testing by esp32.sh. Firmware compatibility follows explicit upstream project documentation.
