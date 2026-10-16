# esp32.sh

[English](README.md) | **简体中文**

为你手里的 ESP32 设备寻找开源项目。

ESP32 开源项目与设备目录：[esp32.sh](https://esp32.sh/)。英文默认根路径，中文 `/zh`，日文 `/ja`。项目和设备各用独立 Markdown 保存；设备按厂商分目录，项目按标签筛选。TanStack Start + React + Cloudflare Workers，部署使用 `cf`。

## 开发与检查

需要 Node.js 22.12+、pnpm 10、Python 3.10+ 和 curl。Python 工具只使用标准库。

```sh
pnpm install --frozen-lockfile
pnpm dev                 # http://localhost:3000/
pnpm verify              # 内容、类型、测试、生产构建；不采集或发布
```

检查本地生产构建，在两个终端分别运行：

```sh
pnpm preview --port 4317
pnpm check:http          # 完整设备页面与筛选检查，默认检查 localhost:4317
```

## 贡献项目与设备

每个条目各用一个独立 Markdown 文件。普通内容投稿不需要修改应用代码或配置数据库。先查看已有内容，避免重复收录同一个 GitHub 仓库或设备型号。

克隆仓库后（公开仓库开放后也可先 Fork），创建分支并安装依赖：

```sh
git switch -c content/add-entry
pnpm install --frozen-lockfile
```

### 新增项目

复制[项目模板](templates/project.md)，放到项目目录，项目不按标签分文件夹：

```sh
cp templates/project.md content/projects/my-project.md
```

修改新文件：

- 填写唯一、稳定的小写连字符 `id`（如 `my-project`）、上游 `name` 和规范的 `repository` 地址（`https://github.com/owner/repository`）。一个仓库只收录一次，可关联多个设备和标签。
- 确认项目有可读 README、明确开源许可、收录时至少 **10 个 GitHub Star**，并与 ESP32 有实际关联。`license` 填实际核实的许可，不能直接沿用模板中的 MIT。
- `summary.en`、`summary.zh`、`summary.ja` 分别填写事实一致的简短介绍。`kind` 选 `firmware`、`application`、`library` 或 `framework`；`tags` 优先复用已有标签。`addedAt` 使用实际目录收录日期（`'YYYY-MM-DD'`），不要沿用模板日期。
- 在 `sources` 中填写上游依据，例如 `sources: [{ url: https://github.com/owner/repository#readme }]`。`checkedAt` 可选，填写时使用实际核验时间的 ISO 时间戳。
- 关联已有设备时，填写其内部 `deviceId` 和明确支持该型号的上游 `sourceUrl`，并设 `compatibility: documented`。相同芯片不代表兼容；无法确认时保留 `devices: []` 和 `compatibility: pending`，明确为自组硬件时用 `custom-hardware`。
- `cover` 可选，没有就省略。优先使用官方或上游 HTTPS 图片地址；没有可用图片时展示项目名称。

不要在 Markdown 中填写 Star 数量，也不需要修改生成文件。Star 快照、核验依据和审核台账由维护者补充。也可以使用[项目收录技能](skills/esp32-project-intake/SKILL.md)，从 GitHub 链接和简单介绍生成记录。

### 新增设备

复制[设备模板](templates/device.md)，放到对应厂商的目录：

```sh
mkdir -p content/devices/my-maker
cp templates/device.md content/devices/my-maker/my-maker-model.md
```

- 填写唯一、稳定的设备 `id`、`name`、`manufacturer.id`、`manufacturer.name`、`chip` 和 `type`。**文件夹名必须与 `manufacturer.id` 一致**；已有厂商请复用其目录，新条目的文件名建议与 ID 相同。
- 按实际硬件形态选择：`integrated-device`（StopWatch 这样的集成设备）、`functional-board`（围绕特定外设的功能开发板）、`general-board`（通用开发板）、`module`（需集成到载板的模组）。芯片型号单独填在 `chip` 中。
- 补齐三语 `summary`、`officialUrl`，并在 `sources` 中提供厂商资料。无品牌产品使用厂商 ID `generic`，无法确认厂商的使用 `unknown`，不要把经销商直接当成制造商。
- `aliases`、`features`、外部封面、详细参数、资料链接、版本说明和有来源的参考价均可选；只填写能够核实的信息，分清硬件版本和套件附件。完整示例见 [StopWatch](content/devices/m5stack/m5stack-stopwatch.md)。
- 项目适配关系写在对应的**项目 Markdown** 中，不写进设备文件；设备页面会自动反向查询。关联新设备时，将设备和项目文件放在同一次投稿中。

### 检查与提交

```sh
pnpm check
```

该命令检查字段、重复 ID/仓库、设备引用及 TypeScript，不代表已经核实许可或实测硬件。运行它不需要 GitHub 凭据或 Cloudflare 登录。纯内容投稿不需要部署网站或运行采集脚本。

检查改动后，仅提交本次需要的内容文件；公开仓库开放后，通过 Pull Request 投稿，并附上上游链接和仍待确认的适配、许可问题。目前公开仓库地址尚未公布，可先在本地准备和审阅内容。通过审核的 Markdown 会在下次网站部署后展示。

完整字段见[内容指南](content/README.md)，收录规则见[贡献约定](CONTRIBUTING.md)。不要提交凭据、缓存或生成的构建产物。

## 发布

```sh
pnpm exec cf auth login  # 首次使用或授权失效时，在官方页面登录
pnpm verify
pnpm deploy:check        # 检查刚刚构建的产物，不上传
pnpm deploy:built        # 发布刚刚验证的产物
pnpm check:deployment    # 少量只读 HTTPS 检查，对照本地目录核对线上
```

快捷发布可用 `pnpm deploy`，会重新构建并发布。配置入口是 [cloudflare.config.ts](cloudflare.config.ts)。完整流程、域名维护和回退方法见 [部署手册](docs/operations/deployment.md)。

## 维护入口

| 要做什么 | 从哪里开始 |
| --- | --- |
| 用 Codex 从文字或 GitHub 链接收录项目 | [ESP32 项目收录技能](skills/esp32-project-intake/SKILL.md) |
| 新增或修改项目、设备 | [内容指南](content/README.md)、[投稿模板](templates/)、[贡献约定](CONTRIBUTING.md) |
| 了解数据流、目录职责和检查范围 | [维护指南](docs/operations/maintenance.md) |
| 扩充内容、更新 Star、刷新待办 | [采集工具说明](scripts/README.md)、[数据台账说明](data/README.md) |
| 查看已收录与待审核状态 | [收录进度](docs/research/collection-progress.md)、[设备补充进度](docs/research/device-enrichment-progress.md) |
| 回看产品决策、调研和上线记录 | [文档索引](docs/README.md) |
| 让编码代理接手 | [AGENTS.md](AGENTS.md) |

## 内容原则

- 中英同等重要；目前界面及摘要支持中、英、日三语。
- 项目首次收录需 README、明确开源许可和至少 10 Star；许可不清楚的留待审核。
- 设备适配必须有上游明确依据，相同芯片不代表型号兼容；本站没有硬件实测背书。
- 图片优先使用官方外部地址，缺图或加载失败显示名称；未配置 R2 图片托管。
- Star 与 README 封面候选存为快照，访问网页不会请求 GitHub。
- 当前项目卡片直达 GitHub，设备有独立页面。源码仓库与投稿入口尚未公布；没有数据库、登录、支付、收藏或 AI 自动合并。
