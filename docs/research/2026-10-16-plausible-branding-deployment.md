# Plausible 与品牌资源发布记录

日期：2026-10-16。用户明确要求“部署吧”，使用已有构建，通过项目内 cf CLI 发布。

## 发布范围

- 根布局统一加载 `https://plausible.haoran.cv/js/script.outbound-links.js`，`data-domain="esp32.sh"`，保留 defer。
- 页头芯片终端 Logo，以及独立绘制的 16px favicon、PNG 与 ICO 回退资源。
- 内容规模保持 100 个项目、140 款设备；技能与文档属于本地仓库维护资料。

## 执行结果与边界

- 上一轮 `pnpm verify`、完整本地生产 HTTP 检查通过。
- `pnpm deploy:check` 通过。
- 首次 `pnpm deploy:built` 提示没有认证凭据；`cf auth login` 与 `cf auth whoami` 随后确认现有 OAuth 授权有效，未强制登录、未读取或复制凭据。
- 重试 `pnpm deploy:built` 上传 12 个新/变更资源，随后输出 `Uploaded esp32-sh (85.90 sec)`、Worker 启动时间 12ms。
- CLI 提示服务/环境分组标签未应用，最终以 `fetch failed` 退出；不能将此次记录为 CLI 全流程成功。
- 随后通过 cf 查询部署列表也遇到连接失败。公开无凭据的 Node API 连通性探测报告 `UND_ERR_CONNECT_TIMEOUT`。本次未取得可靠的版本 ID，不借用历史版本号。
- 尽管 CLI 收尾报错，公网实际已在提供新版内容：9 项部署检查全部通过；另外检查英文、中文、日文首页、设备目录与中文 StopWatch 详情，均确认 head 中恰好一份指定 Plausible 脚本，domain/defer 正确，页头包含新 Logo。
- 证据：`.cache/deployment/public-smoke-results.json`。HTTPS 检查未关闭证书校验。未执行 DNS 修改，未手动发送统计事件，未进入 Plausible 后台，真实事件入库尚未验证。

新版已在生产域名生效。若需要 Cloudflare 版本 ID 或后台标签状态，待 API 网络恢复后用 cf 只读查询确认；不因收尾错误反复重复上传。
