# 脚本索引与采集流程

所有命令从项目根目录运行。Node 工具通过 `node --import tsx` 执行，Python 工具使用标准库。常用命令已收口到 `package.json`；不要把某一轮临时操作当成每次都要重跑的流程。

## 日常入口

| 命令 | 作用 | 是否联网/发布 |
| --- | --- | --- |
| `pnpm check` | 内容与 TypeScript 检查 | 不采集、不发布 |
| `pnpm test` | 内容处理和采集工具的回归测试 | 使用本地 fixture，不采集、不发布 |
| `pnpm verify` | check + test + 生产构建 | 不采集、不发布 |
| `pnpm check:http` | 完整本地生产 HTTP 检查，预览默认需在 4317 端口运行 | 只读本地 HTTP |
| `pnpm check:deployment [origin]` | 少量页面和静态资源检查，默认线上域名 | 只读匿名 GET |
| `pnpm collect:report:all` | 生成目录、收录报告、设备补充报告和关联审阅线索 | 只读缓存，更新本地报告 |
| `pnpm deploy:check` / `pnpm deploy:built` | 检查/发布已构建产物 | 后者会发布，见部署手册 |

`check-deployment.py` 根据本地目录读取预期数量，不把项目数量写死。发布后的默认结果在 `.cache/deployment/public-smoke-results.json`；失败不会覆盖上次成功结果，应以时间和目标 URL 判断是哪次检查。检查本地可使用：

```sh
pnpm check:deployment http://localhost:4317 --delay 0 --output .cache/deployment/local-smoke-results.json
```

## 构建与编辑工具

- `content.ts`、`check-content.ts`：解析/校验 Markdown、合并 Star 与封面快照，生成目录。
- `content-plugin.ts`：构建时生成目录，开发时监听内容和快照。
- `test-content.ts`：目录身份、引用、快照、图片优先级等回归检查。
- `write-records.ts <reviewed.json>`：导入已审阅记录，默认跳过已有文件；`--replace` 会整条覆盖，不用于批量重放旧设备导入。
- `apply-device-enrichment.ts`：应用已审阅的参数计划与已验证图片；按 Markdown 内的 ID 找设备，保留正文，图片只在明确允许时替换。已有字段会按审阅计划更新，运行前必须对照 MD。
- `audit-collection.py`：核对收录规模、来源、许可/README/Star 依据与队列；`--min-projects`、`--min-devices` 可作为特定批次的门槛。
- `check-http.py`：完整本地生产检查。
- `check-deployment.py`：少量部署探测，不是浏览器或设备 E2E。
- `check-browser.mjs`：历史浏览器检查，保留作参考，不在默认检查流程中执行。

## 采集阶段

### 1. 从已有目录发现候选

```sh
pnpm collect:discover --online
pnpm collect:m5ware --online
pnpm collect:devices --online --manufacturer <maker-id> --max 10
```

对应 `discover.py`、`discover_m5ware.py`、`discover_devices.py`。`inventory_manufacturers.py` 记录所检查目录的厂商覆盖，`discover_cached_directory.py` 从已有目录缓存补候选。来源目录的总量不代表已正式收录量。

### 2. 核验源站，不自动批准

```sh
pnpm collect:projects --online --repo owner/repository
python3 scripts/collection/verify_devices.py --online --max 10
python3 scripts/collection/verify_license_files.py --online --repo owner/repository
python3 scripts/collection/enrich_devices.py --online --maker <maker-id> --max 10
```

项目核验检查公开源码、README、Star 和仓库身份；许可证不作为收录门槛，复杂代码/模型/资源许可如实记录，未声明时用 `Not specified`。`verify_devices.py`、`verify_device_overrides.py` 核对设备级来源，避免拿芯片 PDF 当开发板资料。`enrich_devices.py` 只采集详情与图片候选，不写正式 MD。`review_lilygo_sources.py` 是特定共享商品页的变体核验工具。

`verify_device_images.py --online` 只请求 `device-image-review.json` 中标为 `selected` 的图片，检查响应的实际格式；200 HTML、通用插画或错误型号照片都不能算合格产品图。型号和视觉审阅另由编辑完成。

### 3. 编辑后写入 Markdown

`curate_projects.py`、`curate_devices.py`、`curate_device_supplement.py` 保存早期批量导入的编辑记录，输出 `reviewed-*.json`。已有正式内容直接改 MD，不必为每次文案修订重放这些批次。

`curate_device_details.py` 会从缓存的 M5Stack 三语表格重建部分参数计划，可能覆盖后来人工修订的计划。它是批次工具，不纳入日常刷新命令；重跑前保留当前计划并逐项核对版本和测量口径。

审阅导入、参数补充、更新快照与生成报告是不同步骤；不要把抓到候选直接写成已收录。

### 4. 更新快照与进度

```sh
pnpm collect:metrics --online --refresh --max 20
pnpm collect:covers
pnpm collect:report:all
python3 scripts/audit-collection.py --min-projects 100 --min-devices 140
```

只有第一条联网刷新；失败保留旧 Star，不能写成 0。离线重建使用 `pnpm collect:metrics`，它只读已缓存响应。`collect:covers` 仅从已缓存且通过核验的 README 寻找可选图片，不保证每张都适合作为封面。

`resume_projects.py --online --target <count> --deadline <ISO-time>` 是显式启动的本机等待工具，会等待 GitHub 额度恢复，不是线上定时任务。不要因观察超时就重启仍在运行的采集进程。

## 网络约定

采集工具默认离线，联网必须显式 `--online`。`public_fetch.py` 统一使用不读取 `.curlrc` 的匿名 curl、HTTPS、同主机串行、缓存和限流重置时间。禁止个人 GitHub 凭据；Cloudflare 的部署 OAuth 不用于采集。

避免多个采集进程同时改写同一份整表 JSON。原始响应和请求冷却状态位于 `.cache/collection/`；正式审阅台账位于 `data/collection/`。更多字段与分类见 [数据说明](../data/README.md)。

## 工具目录

`scripts/tools.ts` 读取并校验 `content/tools/*.md`，由内容生成流程统一调用；`scripts/markdown.ts` 提供三类内容共用的 Frontmatter 读取。工具独立生成到 `src/generated/tools.json`，不会写入项目/设备的 `catalog.json` 或采集队列。编辑工具 Markdown 后运行 `pnpm check`；开发服务会监听内容变化。
