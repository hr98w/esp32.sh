---
id: meshtastic
name: Meshtastic
repository: https://github.com/meshtastic/firmware
license: GPL-3.0
summary:
  zh: 通过低功耗 LoRa 无线电构建离网消息网络，支持多种微控制器平台。
  en: Build off-grid messaging networks over low-power LoRa radios, with firmware
    for multiple hardware platforms.
  ja: 低消費電力のLoRa無線を使ってオフグリッドのメッセージネットワークを構築する、複数機種対応のファームウェア。
kind: firmware
tags:
  - radio
  - networking
devices:
  - deviceId: lilygo-t-beam-supreme
    sourceUrl: https://meshtastic.org/docs/hardware/devices/lilygo/tbeam/
  - deviceId: lilygo-t3s3-v1-0
    sourceUrl: https://meshtastic.org/docs/hardware/devices/lilygo/lora/
  - deviceId: lilygo-t-watch-s3
    sourceUrl: https://meshtastic.org/docs/hardware/devices/lilygo/twatch/
  - deviceId: lilygo-t-deck-plus
    sourceUrl: https://meshtastic.org/docs/hardware/devices/lilygo/tdeck/
addedAt: 2026-10-16
autoCover: true
sources:
  - url: https://github.com/meshtastic/firmware#readme
    checkedAt: 2026-10-15T17:23:41+00:00
  - url: https://meshtastic.org/docs/hardware/devices/lilygo/tbeam/
    checkedAt: 2026-10-15T17:53:00+00:00
  - url: https://meshtastic.org/docs/hardware/devices/lilygo/lora/
    checkedAt: 2026-10-15T17:53:02+00:00
  - url: https://meshtastic.org/docs/hardware/devices/lilygo/tdeck/
    checkedAt: 2026-10-15T17:53:05+00:00
  - url: https://meshtastic.org/docs/hardware/devices/lilygo/twatch/
    checkedAt: 2026-10-15T17:53:07+00:00
compatibility: documented
---

Short editorial summary based on the upstream README. Hardware support is documented upstream; no device testing was performed by esp32.sh.
