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

## 标准发布

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
