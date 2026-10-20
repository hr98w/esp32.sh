---
id: ivy-ai
name: Ivy AI
repository: https://github.com/iamankushpandit/esp_ai
license: GPL-3.0-or-later (Espressif SDK linking exception)
summary:
  zh: 在 Freenove FNK0104B 上运行的 ESP32-S3 语音助手，支持“Hey
    Ivy”唤醒、本地语音识别、小型语言模型和英文语音合成。模型资源存于 microSD，语音识别与模型推理分阶段运行以适应内存限制。
  en: An ESP32-S3 voice assistant for the Freenove FNK0104B with “Hey Ivy”
    wake-word detection, local speech recognition, a small language model and
    English speech synthesis. Models live on microSD, with recognition and
    inference running in separate phases to fit memory.
  ja: Freenove FNK0104B向けのESP32-S3音声アシスタント。「Hey
    Ivy」による起動、ローカル音声認識、小型言語モデル、英語音声合成に対応します。モデルをmicroSDに保存し、メモリに収まるよう音声認識と推論を段階的に実行します。
kind: firmware
tags:
  - ai
  - audio
  - demo
devices: []
addedAt: 2026-10-20
autoCover: true
sources:
  - url: https://github.com/iamankushpandit/esp_ai/blob/main/README.md
    checkedAt: 2026-10-20T04:45:33+00:00
  - url: https://github.com/iamankushpandit/esp_ai/blob/main/LICENSE
    checkedAt: 2026-10-20T04:45:52+00:00
  - url: https://github.com/iamankushpandit/esp_ai/blob/main/NOTICE.md
    checkedAt: 2026-10-20T04:45:54+00:00
  - url: https://github.com/iamankushpandit/esp_ai/blob/main/LICENSE.exception
    checkedAt: 2026-10-20T04:46:34+00:00
  - url: https://github.com/iamankushpandit/esp_ai/blob/main/THIRD_PARTY.md
    checkedAt: 2026-10-20T04:46:36+00:00
compatibility: pending
---

Targets the Freenove FNK0104B; its exact device is not yet in this catalog. Model weights have separate terms, including non-commercial dataset restrictions. No hardware validation by esp32.sh.
