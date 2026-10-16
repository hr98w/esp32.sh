---
id: anan-iphone-use
name: Anan iPhone Use
repository: https://github.com/ananhq/anan-iphone-use
license: GPL-3.0-only AND AGPL-3.0-or-later
summary:
  zh: 为 M5Stack StopWatch 提供 iPhone 控制的 MCP 固件，通过 USB 或实验性的 BLE
    执行鼠标、键盘操作；画面观察与智能体逻辑由客户端负责。
  en: MCP firmware for M5Stack StopWatch with USB and experimental BLE
    mouse/keyboard input for iPhone; screen observation and agent logic stay in
    the client.
  ja: StopWatch向けMCPファームウェア。USBまたは実験段階のBLEでiPhoneにマウス・キーボード入力を送り、画面観察とエージェント処理はクライアント側が担当。
kind: firmware
tags:
  - ai
  - agent
  - tools
devices:
  - deviceId: m5stack-stopwatch
    sourceUrl: https://github.com/ananhq/anan-iphone-use#readme
addedAt: 2026-10-16
autoCover: true
sources:
  - url: https://github.com/ananhq/anan-iphone-use#readme
    checkedAt: 2026-10-16T15:02:45+00:00
  - url: https://github.com/ananhq/anan-iphone-use#license
    checkedAt: 2026-10-16T15:02:45+00:00
compatibility: documented
---

Upstream documents the named board. Agent/client and device-firmware responsibilities are distinct; no hardware testing was performed by esp32.sh.
