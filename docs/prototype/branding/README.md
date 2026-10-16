# 方案 A：芯片终端（草图）

[打开预览](index.html) · [整页预览图](preview.png)

- `chip-terminal.svg`：32 × 32 坐标的主图；深蓝芯片、浅色引脚、青绿亮边、米黄色 `>_`。
- `chip-terminal-16.svg`：独立绘制的 16 × 16 小图版。每边由三个引脚减少到两个，简化边框，符号落在整数像素上。
- `chip-terminal-{16,32,48}.png`：透明背景导出，用于浅色/深色背景的原尺寸预览。
- `preview.svg` / `preview.png`：标志与字标组合、大小对照、模拟浏览器标签页。字标在提案中使用系统等宽字体；图标本身由纯 SVG 路径组成，无字体与外部资源依赖。

方案已确认，已接入网站页头与 favicon，并于 2026-10-16 在生产域名验证生效；发布经过见 [发布记录](../../research/2026-10-16-plausible-branding-deployment.md)。正式资源位于 `public/logo.svg`、`public/favicon.svg`、`public/favicon-{16,32}.png` 和 `public/favicon.ico`，此目录保留提案与预览。调整正式资源时以 public 中的文件为准。

主色：深蓝 `#000080`、青绿亮边 `#66C5B1`、米黄 `#FFF3B0`。搭配网站已有的 `#008080` 背景。

本机导出工具为 `rsvg-convert`，不作为网站构建依赖：

```sh
rsvg-convert -w 16 -h 16 docs/prototype/branding/chip-terminal-16.svg -o docs/prototype/branding/chip-terminal-16.png
rsvg-convert -w 32 -h 32 docs/prototype/branding/chip-terminal.svg -o docs/prototype/branding/chip-terminal-32.png
rsvg-convert -w 48 -h 48 docs/prototype/branding/chip-terminal.svg -o docs/prototype/branding/chip-terminal-48.png
rsvg-convert docs/prototype/branding/preview.svg -o docs/prototype/branding/preview.png
```
