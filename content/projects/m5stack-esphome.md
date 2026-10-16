---
id: m5stack-esphome
name: M5Stack ESPHome Integrations
repository: https://github.com/m5stack/esphome-yaml
license: MIT
summary:
  zh: M5Stack 官方 ESPHome 配置与外部组件，包含 CoreS3 语音助手和 Tab5 家居控制面板。
  en: Official M5Stack ESPHome configurations and external components, including a
    CoreS3 voice assistant and Tab5 home-control panel.
  ja: CoreS3音声アシスタントやTab5ホーム操作画面などを含む、M5Stack公式ESPHome設定・外部コンポーネント集。
kind: firmware
tags:
  - home
  - automation
devices:
  - deviceId: m5stack-cores3
    sourceUrl: https://github.com/m5stack/esphome-yaml#readme
  - deviceId: m5stack-tab5
    sourceUrl: https://github.com/m5stack/esphome-yaml#readme
addedAt: 2026-10-16
autoCover: true
sources:
  - url: https://github.com/m5stack/esphome-yaml#readme
    checkedAt: 2026-10-16T00:05:55+00:00
compatibility: documented
---

Short editorial summary based on the upstream README. Hardware support is documented upstream; no device testing was performed by esp32.sh.
