---
id: magpie-usage-display
name: Magpie Usage Display
repository: https://github.com/peterroe/magpie-usage-display
license: MIT
summary:
  zh: 把 Magpie 网关的额度、请求状态、Token 用量、会话和缓存统计放到微雪 2.16 英寸 AMOLED 屏幕上。macOS Companion
    从本机网关读取数据，通过加密 BLE 推送到 ESP32-S3，支持滑动切换四个页面。
  en: Show Magpie gateway quotas, request status, token usage, sessions and cache
    statistics on a Waveshare 2.16-inch AMOLED board. A macOS companion reads
    the local gateway and sends updates to the ESP32-S3 over encrypted BLE, with
    four swipeable views.
  ja: Magpieゲートウェイの利用枠、リクエスト状況、トークン使用量、セッション、キャッシュ統計をWaveshareの2.16インチAMOLEDボードに表示します。macOSのCompanionがローカルゲートウェイから取得したデータを暗号化BLEでESP32-S3へ送り、4画面をスワイプで切り替えられます。
kind: firmware
tags:
  - ai
  - display
  - tools
devices:
  - deviceId: waveshare-esp32-s3-touch-amoled-2-16
    sourceUrl: https://github.com/peterroe/magpie-usage-display#硬件与系统要求
addedAt: 2026-10-20
cover: https://raw.githubusercontent.com/peterroe/magpie-usage-display/main/docs/photos/overview.jpg
autoCover: true
sources:
  - url: https://github.com/peterroe/magpie-usage-display#readme
    checkedAt: 2026-10-20T03:59:09+00:00
  - url: https://github.com/peterroe/magpie-usage-display/blob/main/LICENSE
    checkedAt: 2026-10-20T03:59:25+00:00
  - url: https://github.com/peterroe/magpie-usage-display/blob/main/THIRD_PARTY_NOTICES.md
    checkedAt: 2026-10-20T03:59:27+00:00
compatibility: documented
---

Community project, not an official Magpie product. Upstream only documents Waveshare ESP32-S3-Touch-AMOLED-2.16 with macOS; the exact board is linked in this catalog. Firmware updates require USB (no OTA). No hardware testing by esp32.sh.
