---
id: physical-hermes
name: Physical Hermes
repository: https://github.com/RegeneratusLabs/physical-hermes
license: MIT
summary:
  zh: 把 SpotPear 1.28 英寸 ESP32-S3 语音机器人变成 Hermes Agent
    的实体终端：按键说话，屏幕显示回复并语音播放。通过局域网连接已有的 Hermes 主机，语音识别、合成与模型使用主机配置。
  en: Turn a SpotPear 1.28-inch ESP32-S3 robot into a physical Hermes Agent client
    with push-to-talk input, on-screen replies and speech playback. It connects
    over the LAN to an existing Hermes host and uses that host’s model and
    speech configuration.
  ja: SpotPearの1.28インチESP32-S3ロボットをHermes
    Agentの実体端末にするファームウェア。ボタンを押して話し、返信を画面と音声で受け取れます。LAN上のHermesホストに接続し、モデルと音声処理はホスト側の設定を利用します。
kind: firmware
tags:
  - ai
  - agent
  - audio
devices: []
addedAt: 2026-10-18
autoCover: true
sources:
  - url: https://github.com/RegeneratusLabs/physical-hermes#readme
    checkedAt: 2026-10-18T13:55:42+00:00
  - url: https://github.com/RegeneratusLabs/physical-hermes/blob/main/docs/1-the-device.md
    checkedAt: 2026-10-18T13:56:05+00:00
  - url: https://github.com/RegeneratusLabs/physical-hermes/blob/main/LICENSE
    checkedAt: 2026-10-18T13:56:03+00:00
compatibility: pending
---

Targets the SpotPear ESP32-S3-LCD-1.28-BOX robot; the touch variant is needed for swipe-to-cancel. The board port is documented as experimental. Its exact device is not yet in this catalog, so device links remain pending. No hardware validation by esp32.sh.
