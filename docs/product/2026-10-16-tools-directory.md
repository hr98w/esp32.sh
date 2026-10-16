# 工具目录首版

日期：2026-10-16。用户确认新增工具页，并强调首批质量。当前为本地实现，尚未部署。

## 结构与收录规则

导航增加「工具 / Tools / ツール」，对应 `/tools`、`/zh/tools`、`/ja/tools`。沿用现有复古风格，直接展示搜索、用途分类和紧凑卡片；使用小尺寸的官方真实图标，没有侧边栏、大图、收藏或按 Star 排序。默认按人工 `order` 展示，每个工具各用 `content/tools/<id>.md` 保存。首批共 10 个。

按用户任务分为烧录与管理、模拟仿真、编程调试、屏幕与素材。工具需有明确 ESP32 用途、官方或作者文档、可追溯来源；同类项需要可解释的使用差异。不为扩充数字收录无文档的小型克隆，也不把普通 Arduino 模拟器当作 ESP32 模拟器。

工具允许在线服务与官方工具入口；只有核实源码及许可后才标记开源。免费不等于开源；费用采用分类而非具体金额，未证实费用则显示「费用见官网」。不对未测试的手机/浏览器/板型承诺兼容。

## 首批选择

| 工具 | 首选场景与依据 |
| --- | --- |
| ESPConnect | 浏览器中集中管理、备份和烧录，依据作者 README 与 MIT 许可 |
| Wokwi | 浏览器 ESP32 仿真，依据官方芯片/外设支持表和价格页；作为在线服务展示，不标记整个模拟器开源 |
| ViperIDE | MicroPython/CircuitPython 编辑、REPL 与文件管理，依据作者文档与 MIT 许可；手机连接按文档区分 |
| ESP Launchpad | 乐鑫预置示例和 DIY 固件入口，依据官方工具与仓库的 Apache-2.0 声明 |
| Espressif ESP Tool | 已知烧录地址的固件操作，依据 esptool-js 官方文档的 Apache-2.0、浏览器及 Android 兼容层说明 |
| M5Burner | M5Stack 设备固件与 Demo，依据官方文档；不推断开源许可或费用承诺 |
| MQTTX Web | MQTT 消息调试，依据官方文档与 Apache-2.0 许可；使用文档给出的 `/web-client` 实际客户端入口，注明在线版要求 wss:// |
| LVGL Font Converter | 中日文字体子集与字库生成，依据官方页面和 lv_font_conv 的 MIT 许可 |
| LVGL Image Converter | LVGL 图片资源生成，依据官方 v8/v9 页面；不从旧转换库推断整个新版网站的许可 |
| EEZ Studio | 桌面 LVGL 可视化界面设计，依据作者仓库与 GPL v3 许可；不声称任意开发板开箱即用 |

具体来源和核验时间保存在各工具 MD，不重复复制完整上游说明。ESPHome Web、ESP Web Tools 和 Espressif QEMU 留作后续候选：分别是生态专用入口、面向项目作者的安装组件、偏进阶的本地仿真；暂不为数量扩充首批列表。

## 数据与验证

`scripts/tools.ts` 校验 ID、唯一入口、文件名、三语、分类、开源标识与核验来源，工具独立生成到 `src/generated/tools.json`。现有项目/设备 `catalog.json` 与采集队列结构保持现状，工具数据在独立工具路由 chunk 中加载。

工具页为外部链接目录，不在本站嵌入烧录器、模拟器、编译后端或代理第三方资源。来源阅读不是硬件实测；本轮没有执行烧录、串口连接、固件安装、MQTT 连接或浏览器自动化。部分本机 raw.githubusercontent.com 请求遇到连接重置，采用匿名公开网页中的官方文档/许可核验，没有使用个人 GitHub 身份或绕过限流。

质量回归覆盖内容校验、错误标签与重复链接拦截、三语工具页、类别/关键词组合筛选、链接与导航。完整项目/设备分页及设备详情 HTTP 回归一并保留。

## 官方图标

首批 10 个工具均设置可选的 `icon` HTTPS 地址，优先官网 favicon/Logo。ESPConnect、Wokwi、ViperIDE、LVGL 与乐鑫使用各自官网资源；M5Burner 使用 M5Stack 官方文档站图标；MQTTX 使用官方静态资源 CDN 的 favicon；EEZ Studio 使用官方 GitHub 仓库中的 icon.png。两个 LVGL 转换器共用官方 LVGL 图标。

9 个图标直链已通过匿名 GET 和 PNG/ICO/SVG 文件签名验证。EEZ 图标通过匿名 GitHub Contents API 确认路径及 PNG 原始字节，但本机 raw/CDN 直链连接不稳定，尚不能确认此网络下的浏览器可达性。未使用个人身份，也未绕过限流。相关来源页及核验时间保存在各 MD；本机核验图片只留在忽略的 `.cache/tool-icons/` 中，不新增 public 资源。

页面直接加载外部图标，固定显示尺寸并保持原始长宽比；缺少 icon、加载错误或水合前已有缓存失败时回退到原分类 SVG。来源失效不会导致卡片保留破图。
