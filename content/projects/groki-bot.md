---
id: groki-bot
name: Groki Bot
repository: https://github.com/JosssphZhou/groki-bot
license: BSL-1.0 / MIT / Emotion Ball (non-commercial assets)
summary:
  zh: 带表情动画的 ESP32 桌面机器人固件，可在 CoreS3 搭配底座或 StopWatch 上进行 AI 语音交互，并通过电脑网关连接 Grok
    Bot 智能体。部分表情数据仅限非商业使用。
  en: ESP32 desktop robot firmware with animated expressions and AI voice
    interaction on CoreS3 with a robot base or StopWatch, plus a computer
    gateway for Grok Bot agents. Some expression data is restricted to
    non-commercial use.
  ja: CoreS3とロボット用ベース、またはStopWatchで表情アニメーションとAI音声対話を楽しめるESP32ファームウェア。PCゲートウェイからGrok
    Botエージェントに接続でき、一部の表情データは非商用利用に限定されます。
kind: firmware
tags:
  - ai
  - agent
  - audio
  - graphics
devices:
  - deviceId: m5stack-cores3
    sourceUrl: https://github.com/JosssphZhou/groki-bot#hardware
  - deviceId: m5stack-stopwatch
    sourceUrl: https://github.com/JosssphZhou/groki-bot#hardware
addedAt: 2026-10-18
cover: https://raw.githubusercontent.com/JosssphZhou/groki-bot/main/docs/images/banner.png
autoCover: true
sources:
  - url: https://github.com/JosssphZhou/groki-bot#readme
    checkedAt: 2026-10-18T13:05:34+00:00
  - url: https://github.com/JosssphZhou/groki-bot/blob/main/third_party/emotion-ball/LICENSE
    checkedAt: 2026-10-18T13:05:57+00:00
compatibility: documented
---

CoreS3 needs a Stack-chan or Takao base. AtomS3 profiles are documented upstream with reduced features and have not been rebuilt in the described release; only the documented CoreS3 and StopWatch profiles are linked here. No hardware testing by esp32.sh.
