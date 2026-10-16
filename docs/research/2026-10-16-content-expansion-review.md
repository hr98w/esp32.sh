# 设备详情与项目扩充审阅报告

本轮目标：最多两小时；优先补现有设备的官方图片与详情，再把有 README、明确开源许可且至少 10 Star 的项目尽量扩充到 100 个。仅本地审阅。

## 当前结果

| 项目 | 数量 | 说明 |
| --- | ---: | --- |
| 已收录项目 | 100 | 从本轮开始时的 67 个增加 33 个，每个项目独立 Markdown |
| 已收录设备 | 140 | 保持设备规模，按 14 个厂商完善已有记录 |
| 有官方外部产品图的设备 | 120 | 核对实际图片响应及型号，逐张查看；没有把图片加入网站静态资源 |
| 有关键硬件参数的设备 | 138 | 对照厂商资料，区分型号、版本和套件；两款 Ai-Thinker 留待官方资料核验 |
| 有资料入口的设备 | 140 | 包括官方文档、入门、引脚、原理图或明确标注的型号参考 |
| 集成设备 | 35 | 全部具有图片、关键参数和资料入口 |
| 有来源的项目与设备关联 | 164 | 44 款设备有已确认项目关联；其余 96 款仍缺明确型号支持依据 |
| 项目 README 封面候选 | 64 | 启发式候选，不视为经过编辑挑选的官方产品图；加载失败回退名称 |

所有项目与设备均保留中、英、日摘要。设备参数、版本说明和资料标签也按三语保存。没有补写未核实的价格、库存或购买清单。

## 设备内容

按 M5Stack、LILYGO、Waveshare、Seeed、Elecrow 等厂商分批核对，再补开发板厂商。详情保留概述、关键参数、出厂功能（有依据时）、资料入口、版本说明及来源；相关项目仍位于最下面，按 Star 倒序。

五款具有成品形态的设备从功能板调整为集成设备：

- `waveshare-esp32-s3-touch-amoled-1-8`
- `waveshare-esp32-s3-touch-amoled-2-06`
- `waveshare-esp32-s3-touch-lcd-4b`
- `elecrow-crowpanel-rotary-2-1`
- `lilygo-t-embed`

最终分类为 35 款集成设备、51 款功能开发板、52 款通用开发板、2 款模组。没有把芯片裸片和可以直接使用的成品混为一类。

审阅中处理的具体问题：

- Timer Camera 的电池接口不等于内置电池，已修正简介与标签。
- Tab5 主机和含电池套件分别说明，避免把套件配件写成所有版本标配。
- CrowPanel P4 的主控存储与无线协处理器存储分开核对。
- XIAO ESP32S3 Plus、基础版和 Sense 分别取值，记录相机版本差异。
- PaperS3 的三语尺寸口径不一致，核对官方机械图后明确“机身尺寸”测量范围，保留来源与内部判定依据。
- LILYGO T-Call 商品页混有 SIM800 和 A7670 变体图片，采用明确对应 SIM800 的图片。
- Heltec WiFi Kit 32 文档中的图片标有 SX1262/LoRa，已弃用并替换为其官方 WiFi Kit32 V3 商品页照片。
- M5Dial 参数和照片明确对应 V1.1（K130-V11），补充版本说明。
- 官方当前订购表将 ESP32-C3-DevKitC-02 标为 EOL，页面新增带来源的说明。

图片使用原厂 CDN、原厂文档域名或原厂明确使用的外部存储地址。保留原始格式，部分为 WebP，部分为 JPEG/PNG/GIF；没有为转换格式新增本站图片流量，没有配置或上传 R2。

## 项目收录与适配

从既有 M5Ware、awesome-esp32、Awesome M5Stack Cardputer 等候选台账继续核验，没有为凑数进行全网盲搜。新增项目包括 StopWatch 互动表情、PaperS3 EPUB 阅读器、Cardputer 键鼠和 SSH、Tab5 官方演示、AREA512、ESPHome、MicroPython 等。

Star 是带日期的匿名 API 快照，不是实时数值。README、许可证标识与 GitHub 仓库 ID 一并保留；API 无法识别但人工可确认的许可，另存声明来源和判定说明。

涉及复杂许可的处理：

- ESPHome 按上游声明记录 `MIT AND GPL-3.0-only`，没有把整个项目笼统写成 MIT。
- sanoTTS-jp 的代码与模型条款不同，模型有用途限制和下游义务，留待审核。
- 带专有声明、非商业模型或许可相互冲突的候选不进入公开列表。
- 旧版已弃用 SDK、非 ESP32 的 Linux 基础设施及说明不足的候选保留明确排除或待审原因。

适配依据来自上游 README 或对应的官方支持文档，不依据芯片相同自动推断。特别处理了这些情况：

- chat-stick 的 StackChan 目标仅完成硬件接入，已移除完整语音项目关联；StopWatch 有完整客户端说明，已补入。
- Stack-chan、StackChan MCP 与正式 K151 机器人套件分别核对。
- Avatar Mic 的 Dial 示例需要外接 PDMUnit，不表述为 Dial 内置麦克风。
- AREA512 只关联已明确匹配的 ADV；没有把 Cardputer v1.1 自动当成所有初代 Cardputer。
- DualPID 的 Core2 仍在上游计划清单中，只关联明确列出的 BASIC。
- PathShield 简介只描述扫描与持续出现情况，不承诺能可靠判定跟踪行为。

本站没有进行设备刷写或硬件实测。型号文本命中只是审阅线索，特殊上下文的人工结论单独保存在 `device-compatibility-review.json`。

## 待办与可重复执行

20 款设备仍缺可接受的外部官方图片，2 款仍缺可确认的官方关键参数。逐型号原因见 [设备补充进度](device-enrichment-progress.md)：

- 15 款 Espressif：迁移后的资料 HTML 内嵌图片，部分资源接口返回 500，原始文档图片域名从匿名采集环境连接超时；不发布未经验证的替代图或内嵌 data URI。
- 两款 LILYGO 触摸变体：同一商品页混合多个版本，需要明确对应触摸型号的图。
- 两款 Ai-Thinker：旧官方文档迁移；通用物联网插图、经销商图没有冒充官方型号照片。
- Reflow Master Pro：旧商品链接转到通用商店，未采用通用店铺图。

这些条目保留设备名称回退。已有规格仅在有依据时补充；缺失信息没有使用相近型号代填。

持久化资料：

- [全部收录与候选进度](collection-progress.md)、[逐设备收录队列](device-intake-queue.md)。
- `data/collection/device-enrichment-queue.json`：所有 140 款设备的详情、图片、资料完成状态。
- `data/collection/device-detail-review.json`：人工审阅的字段补充计划。
- `data/collection/device-image-review.json`：型号图片选择、格式/字节验证、视觉审阅及弃用原因。
- `data/collection/repository-evidence.json`、`project-editorial-review.json`：项目核验与三语编辑依据。
- `data/collection/device-relation-audit.json`、`device-compatibility-review.json`：全部关联线索与特殊上下文判定。

常用离线命令：

```sh
pnpm content:generate
python3 scripts/collection/report.py
python3 scripts/collection/report_device_enrichment.py
python3 scripts/collection/audit_device_relations.py
python3 scripts/audit-collection.py --min-projects 100 --min-devices 140
```

`enrich_devices.py` 只保存来源候选；审阅后的详情与验证过的图片由 `apply-device-enrichment.ts` 写回独立 Markdown。它按文件内设备 ID 定位，保留正文和现有封面，只有明确标注替换时才换图。不要对旧设备导入 JSON 使用 `--replace` 覆盖已经丰富的 Markdown。

匿名 GitHub API 在额度耗尽时按服务器重置时间等待；第二次额度耗尽后，下一次恢复时间晚于本轮任务截止时间，已停止等待进程，保留全部进度。没有切换身份、使用个人 Token 或绕过限流。

## 验证记录

2026-10-16 收尾检查通过：

- `pnpm check`：100 个项目、140 个设备的内容规则及 TypeScript 校验通过。
- `pnpm test:content`：9 项内容回归检查通过。
- `pnpm test:collection`：19 项匿名采集、缓存、限流、解析及图片格式检查通过。
- `pnpm build`：客户端及 Cloudflare Worker 生产构建通过。
- `python3 scripts/audit-collection.py --min-projects 100 --min-devices 140`：Markdown、三语摘要、来源、README、许可、Star 和队列计数一致。
- `python3 scripts/collection/audit_device_relations.py`：164 条关联全部有型号文本线索或已记录的人工上下文判定，没有未处理的词法缺口。这不是运行或硬件兼容性证明。
- `python3 scripts/check-http.py http://localhost:4317`：本地生产 Worker 返回的 420 个设备语言页面全部通过，同时验证默认英文根路径、筛选、重定向、404、外部图片地址、摘要语言，以及关联项目的范围、位于最后和 Star 倒序。
- 另行核对 140 个设备 ID 均在补充队列中；35 款集成设备的图片、关键参数和资料入口齐全；120 个设备封面均匹配实际格式检查与视觉审阅记录；`public/images/` 只有原有 `.gitkeep`。

构建仍有工具链循环依赖、较大客户端 chunk 和 CSS sourcemap 警告，未影响退出状态。目录数据随内容规模增长，后续可单独评估按路由拆分与首屏传输量。本轮没有为消除警告扩展技术改造。

HTTP 检查不验证浏览器水合交互；图片网络结果仅代表检查时的可用性，外部域名后续仍可能变化。没有真实硬件运行验证。

没有使用 computer-use、浏览器自动化、`gh`、个人凭据、Cloudflare 账户、R2 上传或部署命令；没有发布、推送仓库、创建外部 Issue/PR 或联系作者。变更仅在本地工作区。
