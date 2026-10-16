# 内容指南

应用内容放在本目录，产品文档和设计原型留在 `docs/`。`projects/**/*.md` 与 `devices/**/*.md` 会被读取，其余文件不会作为项目或设备记录。

每条内容包含 YAML Frontmatter 和可选 Markdown 正文。字段目前采用第一版约定，详见 `src/lib/content/schema.ts` 与 `templates/`。运行 `pnpm content:check` 检查提交。

## 项目

- 必填：`id`、`name`、`repository`、`license`、`kind`、`summary`、`addedAt`。
- `summary` 中保存 `zh`、`en`、`ja` 三个版本；仓库、许可、设备关联共用。
- `kind`：`firmware`、`application`、`library` 或 `framework`，方便区分可体验固件与开发依赖。
- `tags`：多个稳定标签，调整标签不需要移动文件。
- `devices`：`deviceId` 与 `sourceUrl` 的列表，记录上游适配依据。不根据相同芯片自动关联。
- `cover`：可选 HTTPS 图片地址或 `/images/...` 本站资源路径。不要填空字符串，不填写即可。
- `autoCover`：可选，默认 `true`，用于控制 README 自动取图；候选来自独立数据快照，缺图或加载失败显示项目名。
- `sources`：来源 URL 与核验时间；记录来源不代替适配依据。
- `compatibility`：`documented`（有明确型号关联）、`pending`（具体型号待核验）或 `custom-hardware`（自定义硬件组合）。
- `addedAt`：目录收录日期，使用带引号的 `YYYY-MM-DD`；不等同于仓库创建日期或代码更新时间。

`id` 使用小写字母、数字和连字符，记录创建后保持稳定；文件名建议与 ID 一致。每个 GitHub 仓库只收录一次。许可证字段仍需核对上游许可声明（LICENSE 文件或 README 中的明确授权），格式校验无法证明它确实开源。

## 设备

- 必填：`id`、`name`、`manufacturer`、`chip`、`type`、`summary`、`officialUrl`。
- `type` 是人工确认的硬件形态，不根据芯片或厂商自动推断：
  - `integrated-device`：集成设备，已组成便携终端、控制器等整体形态，例如 StopWatch；不保证每个项目都无需额外硬件。
  - `functional-board`：功能开发板，围绕屏幕、摄像头、LoRa、以太网等外设开发，可能需要安装外壳或连接其他部件。
  - `general-board`：通用开发板，以主控和扩展引脚为主；电池接口、RGB 灯、存储卡槽本身不改变此分类。
  - `module`：需载板或焊接集成的模组，不能当作可直接连接电脑使用的开发板。
- `type` 与 `chip`、`features` 独立；按收录的具体型号与套装配置分类，不因厂商使用 Dev Kit 一词就判为通用板。
- `manufacturer` 包含稳定 `id` 和显示 `name`；其 ID 必须与厂商文件夹一致。
- `sources` 保存目录与官方资料 URL，以及核验时间。
- `aliases` 保存别名；`features` 保存板载功能标签；`cover` 可选。
- 项目关联只在项目中填写，设备页会自动反向查询。
- 以下详情字段均可选，有来源再填写，完整样板见 [StopWatch](devices/m5stack/m5stack-stopwatch.md)：
  - `sku`：明确的厂商产品编号，不用商家自定义编号替代。
  - `cover`、`gallery`：外部产品图片；图库各项含 `image`、三语 `caption` 和 `sourceUrl`。优先官方 CDN，当前不新增 R2 或本站图片代理。
  - `specifications`：参数表，每项含三语 `label` 与 `value`；分别核对主控、无线协处理器、模组、Flash/PSRAM 和硬件版本。
  - `factoryFeatures`：三语出厂功能说明，与可刷写的社区项目分开。
  - `resources`：三语 `label` 与 HTTPS `url`，用于文档、固件、入门、原理图和引脚等资料。
  - `revisionNotes`：三语 `text` 与 `sourceUrl`，说明版本、套件和测量口径差异。
  - `referencePrice`：`amount`、三字母 `currency`、`sourceUrl`、`checkedAt`（日期）。只记录核实过的参考价，不承诺实时价格或库存。

不要因为同系列产品页面共用一张参数表就合并取值；电池接口不等于随附电池，开发板名里的屏幕尺寸也不能替代具体套件核验。正式内容优先保存在 MD，补充计划与采集台账见 [维护指南](../docs/operations/maintenance.md)。

## 自动数据

生成的目录在 `src/generated/catalog.json`，由脚本维护且不进入版本控制。Star、README 封面候选与采集日期放在 `data/`，避免自动任务反复修改人工 MD。

收录来源与规则的完整讨论见 [产品文档](../docs/product/2026-10-16-content-records.md)。
