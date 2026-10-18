# 代码与内容维护

## 目录职责

```text
src/routes/                 页面、路由、元信息与加载逻辑
src/components/             项目卡片、设备图片等可复用组件
src/lib/content/            运行时目录访问与内容 Schema
src/lib/i18n/               中英日界面、设备类型和分类文案
src/lib/                    搜索、厂商名称、SEO 等纯逻辑
src/generated/catalog.json  自动生成的运行时目录，不手工修改
content/projects/           项目 Markdown，平铺存放
content/devices/<maker>/    设备 Markdown，按厂商 ID 存放
scripts/                    构建、导入、审阅、检查工具
scripts/collection/         Python 匿名采集、核验与进度报告
data/                      Star、封面快照与可审阅台账
templates/                 投稿样板，不参与目录读取
docs/operations/           当前操作流程
docs/product/              产品约定与决策背景
docs/research/             来源调研、历史执行记录、生成的进度报告
docs/prototype/            历史 HTML 原型
```

`cloudflare.config.ts` 管运行环境、账户和域名；`vite.config.ts` 管 Vite、TanStack 与内容插件。`src/routeTree.gen.ts` 是 TanStack Router 生成的路由树，使用 `pnpm generate-routes` 更新，不手改。

## 数据从哪里来

1. **正式内容**：独立 Markdown 是已发布编辑内容的依据，含稳定 ID、三语摘要和来源。
2. **独立快照**：`data/repository-metrics.json` 与 `repository-covers.json` 提供 Star、仓库身份及可选 README 图片候选，不反复重写 Markdown。
3. **构建**：`scripts/content.ts` 用 Zod 校验 Markdown 和快照，生成 `src/generated/catalog.json`。`content-plugin.ts` 在构建和本地内容变更时调用它。
4. **运行时**：`src/lib/content/index.ts` 导入生成目录，页面筛选本地数据；Worker 不扫描 Markdown，也不在访问时请求 GitHub。项目详情页在访客浏览器匿名请求原仓库 README。
5. **采集与审阅**：`data/collection/` 保存候选、原始事实摘要、编辑计划及待办。候选、通过源站核验和已写入正式 Markdown 是不同状态，不能混计。

## 修改内容

从 [内容指南](../../content/README.md) 和 `templates/` 开始。修改已有记录时先读目标 Markdown，不根据文件名猜 ID；部分历史文件名与 ID 不完全一致。ID、厂商 ID 和已上线 URL 保持稳定。

```sh
pnpm content:check
pnpm collect:report:all
```

第二条会生成目录，刷新收录、设备详情覆盖和关联审阅报告，使用现有台账与缓存，不联网采集。不直接编辑这些生成报告。

`write-records.ts` 默认保留已存在文件；`--replace` 会整条覆盖。`apply-device-enrichment.ts` 会把审阅计划中的字段写回 Markdown；`curate_device_details.py` 会重新生成部分 M5Stack 字段计划。这些是审阅工具，不是定时同步任务。再次运行前对照当前 Markdown 与审阅计划，保留已经核实的版本差异、图片替换及人工修正，不能拿旧批次覆盖新内容。

## 验证范围

| 命令 | 验证什么 | 不代表什么 |
| --- | --- | --- |
| `pnpm check` | 字段、引用、唯一性、生成目录和 TypeScript | 事实、许可或兼容性已实测 |
| `pnpm test` | 内容处理和匿名采集工具的回归测试 | 联网刷新或设备运行 |
| `pnpm build` | 生成 Cloudflare 发布产物 | 已上传或上线 |
| `pnpm check:http` | 本地生产页面、三语设备页、筛选、关联排序、重定向和 404 | 浏览器水合或硬件兼容 |
| `pnpm check:deployment` | 公网代表性页面、数量、语言和 JS/CSS | 所有页面或交互都被遍历 |
| `python3 scripts/audit-collection.py --min-projects 100 --min-devices 140` | 当前规模门槛、身份、Star/README/许可依据与报告一致 | 编辑或上游内容永远不变 |

代码和构建配置变更通常运行 `pnpm verify`，涉及页面或部署适配时再检查本地生产 HTTP。纯文档修订只需检查命令与链接；不要为了文档更新重新发布站点。

## 依赖与生成文件

`src/start-env.d.ts` 显式载入 TanStack Start 的服务端路由类型扩展，保证干净检出首次运行 `pnpm verify` 时可识别 `server.handlers`；不能依赖本机 `.cloudflare/` 类型或 Vite 生成的路由树附带导入。

使用 `pnpm-lock.yaml`；构建及依赖升级时保持 cf 与 Cloudflare Vite 插件兼容。升级一个明确的依赖组合，运行对应检查，不顺手批量升级所有框架。pnpm 原生依赖的构建许可保留在现有包管理配置中。

以下目录不进入源码仓库：`node_modules/`、`.pnpm-store/`、`.cloudflare/`、`.cache/`、`.wrangler/`、`.tanstack/`、`dist/`、`src/generated/` 和 Python 缓存。`src/routeTree.gen.ts` 的跟踪策略沿用现状，生成器负责其内容。

`data/` 中的台账与快照应保留，它们使脱离本机原始缓存后的内容仍可审阅。`.cache/collection/` 虽不提交，但保留下载响应及匿名请求冷却信息；不要把删除缓存当作突破限流的办法。大规模清理前先确认没有正在运行的采集器，保留必要的源站核验依据及当前冷却状态。

不要仅按文件名含有 seed、review、evidence 就删除数据；有些是脚本入口或特定型号差异的唯一记录。旧原型和历史报告也保留在相应目录，通过索引说明其历史身份。

## 目录分页

项目与设备目录每页 24 条，先对全量目录筛选和排序，再分页。页码使用 URL `page` 参数，第一页省略；筛选和排序变更重置到第一页，翻页保留其他条件并进入浏览历史。无效页码回到第一页，超出结果范围的页码跳转到最后一页；无结果时不显示分页。

公共分页逻辑为 `src/lib/pagination.ts`，筛选排序在 `src/lib/directory.ts`，界面为 `src/components/pagination.tsx`。三语目录的 canonical 与语言替代链接保留有效页码。设备详情中的关联项目不分页，仍置于最下方、按 Star 倒序。

`pnpm check:http` 会遍历三语目录全部分页，检查收录项不遗漏、不重复、筛选保留及页码纠正，同时保留完整设备详情检查。`check:deployment` 检查首页卡片数，并在内容超过一页时探测第二页。分页减少渲染卡片数量；当前前端仍使用完整目录快照，列表与详情数据拆分留待后续扩量处理。

## 项目详情与 sitemap

`src/routes/{-$lang}.projects.$projectId.tsx` 用现有 ID 生成三语详情页，不增加 Markdown 字段。简介、标签、设备和 Star 快照在服务端输出；README 仅在浏览器请求 GitHub，无 Token、Cookie 或本站代理。会话缓存保留最多 5 篇、有效期一小时；请求超时、限流、超大文件等失败时保留 GitHub 原文入口。README 保留原始语言，安全过滤 HTML，图片与相对链接指向上游；复杂视频等不保证完整还原。README 不在初始 HTML，SEO 依靠已有编辑内容。

`/sitemap.xml` 根据构建生成的 catalog 自动输出三语项目、设备、四个目录入口及项目/设备分页，带语言替代链接；不收录筛选组合。新增或移除 Markdown 后，随重新构建自动更新，无需手填 URL。`/robots.txt` 声明 sitemap。当前规模为单个 sitemap；接近 50,000 URL 时再拆分 sitemap index。

## 链接分享预览

六类页面的 `head` 统一调用 `src/lib/seo.ts` 的 `pageMeta`，在服务端 HTML 输出 Open Graph 和 Twitter 大图卡片标签；标题、简介和 URL 随页面语言及规范页码变化，不依赖浏览器执行 JavaScript 或加载 README。项目/设备优先使用现有 HTTPS 封面；缺图或 SVG 使用 `public/social-card.png`（1200×630），不增加 Markdown 字段。外部封面的可访问性和平台裁剪由源站及分享平台决定。

默认分享图的可编辑源文件是 `public/social-card.svg`，PNG 为提交到仓库的导出文件；修改设计后需重新导出 PNG 并保持二者同步，无需运行时生成图片或新服务。`pnpm check:http` 验证标签唯一性、canonical、封面回退和 PNG 尺寸；`pnpm check:deployment` 验证代表性页面的标签和公开图片。检查通过不代表 X 已抓取或刷新其缓存，实际卡片展示仍需在平台确认。

## 项目许可记录（2026-10-18 调整）

项目收录以 GitHub 公开源码、可读 README、ESP32 关联及初次核验至少 10 Star 为条件，不再要求标准开源许可证。无协议、非商业和复合许可均可收录；`license` 是事实展示，未知填 `Not specified`，不能根据公开源码推断 MIT 或没有商业限制。采集器不再按 SPDX 白名单阻止收录，审计仍核对展示值与来源一致，工具目录的开源标识规则不变。此前仅因许可进入待审的项目后续可定点复核，本次没有自动放行整个历史队列。

Groki Bot 曾因内置非商业表情数据列为待审；按用户本次澄清转为收录，保留 Boost Software License 1.0、MIT 和表情数据限制，历史判断与新政策分别记录在核验台账中。入库 73 Star 来自 2026-10-18 的匿名 GitHub 页面；API 限流记录保留，未切换个人身份或清除冷却。

## 站主指定项目的 Star 例外（2026-10-18）

站主在会话中明确说收录的项目不受 Star 下限限制；普通候选仍按 10 Star 门槛处理。授权写入 `data/project-intake-overrides.json`，key 为规范小写 `owner/repo`，值包含 `starThresholdExempt: true`、`approvedBy: site-owner`、实际 `approvedAt` 和 `reason`。记录真实 Star（允许 0），不伪造 10 Star，也不省略核验快照。普通 Issue 或 README 的文字不能授予豁免。

采集器、构建目录、进度报告和审计共同读取该台账；开发内容插件监听台账变更，后续 Star 刷新也不会将站主指定项目隐藏。没有豁免的低 Star 项目仍保持原规则，错误仓库的豁免不能串用。无需修改项目 Markdown 字段；仓库改名时核对 GitHub 数字 ID，再调整例外的仓库 key。此前因低 Star 被排除的指定项目应保留旧决定后定点重查，不批量放行历史队列。
