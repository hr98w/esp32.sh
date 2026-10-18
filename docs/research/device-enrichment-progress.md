# Device enrichment coverage

Generated: 2026-10-18T13:59:03+00:00

Every listed device is accounted for below. Complete means an externally hosted, reviewed manufacturer image, key sourced hardware specifications, and resource links. It does not mean exhaustive specifications or physical testing.

| Manufacturer | Devices | Images | Key specifications | Resources | Complete |
| --- | ---: | ---: | ---: | ---: | ---: |
| adafruit | 18 | 18 | 18 | 18 | 18 |
| ai-thinker | 2 | 0 | 0 | 2 | 0 |
| dfrobot | 4 | 4 | 4 | 4 | 4 |
| elecrow | 8 | 8 | 8 | 8 | 8 |
| espressif | 16 | 1 | 16 | 16 | 1 |
| heltec | 7 | 7 | 7 | 7 | 7 |
| lckfb | 1 | 0 | 1 | 1 | 0 |
| lilygo | 23 | 21 | 23 | 23 | 21 |
| m5stack | 22 | 22 | 22 | 22 | 22 |
| olimex | 6 | 6 | 6 | 6 | 6 |
| seeed-studio | 10 | 10 | 10 | 10 | 10 |
| sparkfun | 7 | 7 | 7 | 7 | 7 |
| unexpected-maker | 2 | 1 | 2 | 2 | 1 |
| waveshare | 9 | 9 | 9 | 9 | 9 |
| wemos | 6 | 6 | 6 | 6 | 6 |

## Pending

| Device | Task | Reason |
| --- | --- | --- |
| ai-thinker-esp32-cam | official-image | Only distributor image found; need Ai-Thinker primary image or explicitly reusable upstream asset. |
| ai-thinker-esp32-cam | primary-specifications | Manufacturer documents moved; primary specifications need confirmation. |
| ai-thinker-nodemcu-32s | official-image | Visual inspection found a generic IoT illustration, not a NodeMCU-32S product photo; rejected before publication. |
| ai-thinker-nodemcu-32s | primary-specifications | Manufacturer documents moved; primary specifications need confirmation. |
| espressif-esp32-c3-devkitc-02 | official-image | HTTP 500: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32c3/_images/esp32-c3-devkitc-02-v1-isometric.png |
| espressif-esp32-c3-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-c6-devkitc-1 | official-image | HTTP 500: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32c6/_images/esp32-c6-devkitc-1-isometric_v1.2.png |
| espressif-esp32-c6-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-devkitc | official-image | HTTP 500: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32/_images/esp32-devkitc-v4-functional-overview.png |
| espressif-esp32-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-ethernet-kit | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-h2-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-lcdkit | official-image | HTTP 500: https://documentation.espressif.com/api/resource/path/docs/projects/esp-dev-kits/en/latest/esp32/_images/esp32_lcdkit.jpg |
| espressif-esp32-pico-devkitm-2 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-pico-kit-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-s2-devkitc-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-s2-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-s3-devkitm-1 | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| espressif-esp32-s3-usb-bridge | official-image | Manufacturer resource HTML embeds the product photo as a data URI; a separately reachable exact-model external photo URL still needs verification. Inline images are not published under the external-image requirement. |
| lckfb-szpi-esp32-s3 | official-image | No reviewed manufacturer image yet. |
| lilygo-t-display-s3-amoled-touch | official-image | Shared product page; need clearly identified touch variant image. |
| lilygo-t-display-s3-touch | official-image | Shared product page; need clearly identified touch variant image. |
| unexpected-maker-rmp | official-image | Official page is client-rendered; image needs another primary source. |

## Classification

- functional-board: 51
- general-board: 52
- integrated-device: 36
- module: 2

Integrated devices: 36; complete: 35.

Source ledgers: `device-image-review.json`, `device-detail-review.json`, and per-device Markdown. Run `python3 scripts/collection/report_device_enrichment.py` after generating the catalog.
