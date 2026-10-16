# Cloudflare 部署手册

生产站点为 **https://esp32.sh/**，Worker 名称为 `esp32-sh`。部署统一使用项目内的 `cf` CLI；配置唯一入口为根目录 `cloudflare.config.ts`。首次上线经过与版本号见 [上线记录](../research/2026-10-16-cloudflare-deployment.md)。

## 环境与登录

```sh
pnpm install --frozen-lockfile
pnpm exec cf --version
pnpm exec cf auth whoami
pnpm exec cf auth login
```

最后一条只在尚未登录或授权失效时运行，在 Cloudflare 官方网页完成授权。CLI 管理用户配置目录里的凭据；不要把 Token 复制到项目、命令参数、聊天或文档。Cloudflare 授权与 GitHub 采集身份是两回事，采集仍使用匿名请求。

`cf` 与适配的 Cloudflare Vite 插件目前使用 beta 版本；`cf` 固定版本，插件的安装版本由 `pnpm-lock.yaml` 锁定。换机器或 CI 使用冻结锁文件安装；升级这两个依赖应一起检查。

## Git 自动部署

代码仓库：[hr98w/esp32.sh](https://github.com/hr98w/esp32.sh)。Cloudflare Workers Builds 生产触发器监听 `main`，所有路径变更都会触发：

| 设置 | 值 |
| --- | --- |
| Worker | `esp32-sh` |
| 生产分支 | `main` |
| 根目录 | `/` |
| 构建命令 | `pnpm verify` |
| 部署命令 | `pnpm deploy:built` |
| 其他分支 / PR 预览部署 | 未配置 |

合并 Pull Request 或推送到 `main` 后，Cloudflare 安装锁文件依赖、检查并构建，通过后才发布。不会运行网络采集脚本。构建失败时查看 Workers Builds 日志；自动部署无需本机保持运行，也不需要把本机 OAuth 凭据放进 GitHub。

构建授权保存在 Cloudflare，限制到当前账户和 `esp32.sh` zone 所需的 Worker、路由及读取权限；临时明文凭据文件已删除。首次关联 GitHub 时，如 Cloudflare 提示授权，需在官方页面安装/授权 Cloudflare GitHub App 并允许访问此仓库。

未来迁移到组织时，转移现有 GitHub 仓库，更新本地 `origin`，并在 Cloudflare 的 Git 集成中核对新组织、仓库权限和 `main` 触发器。转移后用一次真实推送验证自动部署，不依赖旧仓库地址重定向来保证集成有效。

## 标准发布

新增服务端路由、调整类型声明、构建配置或依赖时，先按下节验证干净环境，再进行本地 HTTP 检查。运行过开发服务或构建的本机目录不能替代首次检出验证。

在项目根目录操作，依次执行：

```sh
pnpm verify
pnpm preview --port 4317
```

保持预览进程运行，在另一个终端检查：

```sh
pnpm check:http
```

通过后停止自己启动的预览进程，再发布这个构建：

```sh
pnpm deploy:check
pnpm deploy:built
pnpm check:deployment
```

- `verify` 执行内容与类型检查、两组测试、`cf build`；不会采集或上传。
- `deploy:check` 是 `cf deploy --dry-run --prebuilt`，只检查构建产物。
- `deploy:built` 是 `cf deploy --prebuilt`，发布最近一次构建，不重新构建。
- `check:deployment` 对公网发起少量匿名 GET，检查三语首页、设备目录、代表性详情、设备筛选和 JS/CSS。数量依据本地生成目录，因此应在刚完成发布且本地内容对应同一版本时运行。

构建后又修改内容、源码或部署配置，应重新运行构建与相应检查。`pnpm deploy` 是快捷命令，调用 `cf deploy` 自动构建后发布；它不会替代 `verify` 中的测试。

检查结果默认保存到 `.cache/deployment/public-smoke-results.json`，只在全部探测成功后更新。它不证明浏览器水合交互、所有外部图片长期可用或真实硬件运行。

发布后在新的有日期的部署记录中保存 Worker 版本 ID、发布范围和检查结果，不要覆盖首次上线记录。

## 干净环境验证

适用于服务端路由、类型/依赖/构建变更，以及“本机通过、CI 失败”的排查。对准备推送的本地提交运行以下命令：

```sh
# HEAD 必须已经包含本次候选改动；未提交文件不在归档中。
review_dir=$(mktemp -d "${TMPDIR:-/tmp}/esp32-clean.XXXXXX")
git archive HEAD | tar -x -C "$review_dir"
(
  cd "$review_dir" || exit 1
  pnpm install --frozen-lockfile || exit 1
  pnpm verify
)
```

此目录只含提交中的文件，不复制 `.cloudflare/`、`.tanstack/`、`src/generated/` 或本机 `node_modules/`。验证前不要启动开发服务，也不要先运行 `pnpm build` 来生成可能掩盖问题的类型。CI 同样先检查再构建，不应颠倒顺序来掩盖缺失声明。

如果仅为定位问题复用已安装的依赖，须明确这只能验证“缺少生成文件”的差异，不能证明冻结锁文件的全新安装；依赖安装故障应另做实际安装验证。不要清空主工作区、删除采集缓存或把凭据复制到隔离目录。检查后仅清理自己创建的临时目录。

`src/start-env.d.ts` 必须显式引用 `@tanstack/react-start`，让 `server.handlers` 类型在第一次 `tsc` 时可用。遇到 `TS2353`、`'server' does not exist`，先核对该声明、`tsconfig.json` 的包含范围及 Start 类型扩展是否加载，不直接改写生成文件、关闭类型检查或升级框架。完整案例见 [2026-10-16 排障记录](../research/2026-10-16-server-route-ci-failure.md)。

## 自动部署收尾

任务包含发布时，跟踪本次提交对应的 `Workers Builds: esp32-sh` 检查直到成功或失败。失败时先读取对应 Build ID 的完整日志，区分依赖安装、类型检查、测试、构建和上传阶段；发布修复后跟踪新的提交，不能只看到已触发就结束。读取日志使用 `cf`；先用匿名查询 `cf cli search "retrieve worker build logs"` 发现命令，再使用 `cf builds logs get <build-uuid>`，如日志截断按返回的 cursor 继续获取。

构建成功后运行 `pnpm check:deployment`，并额外探测本次新增或修改的线上入口。现有通用检查覆盖的是代表性页面，不自动证明新增路由已上线；例如本次项目详情、sitemap 和 robots.txt 需单独确认。无法取得最终状态或完成线上验证时，明确报告当前状态和未确认部分。

修复后按 [AGENTS.md](../../AGENTS.md) 的“故障修复后主动沉淀”更新维护规则和案例，不等待用户提醒。

## 域名与 DNS

`cloudflare.config.ts` 的 `accountId` 必须对应域名所在账户，`worker.domains` 当前包含 `esp32.sh`。日常内容发布不需要手工改 DNS。

需要排查时，可只读查看根域名记录：

```sh
pnpm exec cf dns records list --zone esp32.sh --name esp32.sh
```

Cloudflare 自定义域名目前使用带 `origin_worker_id` 的托管代理 AAAA 记录，地址 `100::`、`meta.read_only: true` 属于已核验的托管状态，不要把它当成错误的源站地址删除。

首次绑定曾遇到错误 **100117**：同名旧 A 记录阻止自定义域名接管。处理其他域名时先确认现有记录用途并备份；只处理与目标主机名冲突的记录，不套用首次上线的记录 ID，也不删除邮件记录。部署报错可能已上传了 Worker 或应用了部分触发器，不能根据非零退出码就认定远端完全没有改变。

新域名还需要 Cloudflare zone 为 Active、证书就绪。只有 HTTPS 页面实际可访问且内容正确，才把上线标为已验证。当前配置仅绑定根域名；没有额外配置 `www` 别名或跳转。

## 失败与回退

- 本地检查失败：先修复，不发布旧的 `.cloudflare/` 产物冒充新构建。
- 上传成功但域名失败：保留版本 ID，检查自定义域名与 DNS；修复后重新运行发布，不重新创建整个站点。
- 线上检查数量不一致：核对本地目录、构建时间和发布版本；检查是否遗漏重新构建。
- 需要回退代码或内容：恢复上次验证通过的源码、`content/` 和 `data/` 快照，再使用对应锁文件安装、构建、检查和发布。内容快照与代码一起回退，避免混合版本。
- 需要回退 DNS：使用当前变更前保存的记录；`.cache/deploy-before-cf/` 仅是首次迁移的本机备份，不是每次发布都会生成的通用备份。

`.cloudflare/` 可重新构建生成；`.cache/collection/` 含匿名采集原始依据及限流状态，清理前先看 [维护指南](maintenance.md)。

官方参考：[cf 项目迁移](https://developers.cloudflare.com/cf/wrangler/migrate/)、[cf 配置](https://developers.cloudflare.com/cf/projects/cloudflare-config/)。
