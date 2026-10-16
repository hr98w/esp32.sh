# Cloudflare 部署记录

日期：2026-10-16。此次由用户明确授权部署及绑定域名，覆盖此前采集任务“仅本地”的工作范围限制；历史内容审阅报告保留原始事实。

## 部署结果

- CLI：`cf 1.0.0-beta.17`，本机已安装，项目亦固定该版本。
- 使用官方 OAuth 页面授权，凭据由 CLI 存储在用户配置目录，没有读取或复制 Token 到项目。
- Worker：`esp32-sh`。
- 自定义域名：`esp32.sh`。
- 已发布版本：`a8450009-25d0-47f8-90c9-f5deeb2ab8ac`。
- `cf deploy --prebuilt` 返回 `Deploy complete`，显示 `esp32.sh (custom domain)`。
- 域名 DNS API 确认根域名现为 Cloudflare 只读托管的代理 AAAA 记录，元数据包含 `origin_worker_id`。
- 未创建数据库、R2、定时采集或付费订阅；未访问个人 GitHub 身份。

## 本地配置变更

通过 `cf migrate --dry-run` 预览，再执行 `cf migrate`。生成 `cloudflare.config.ts`、加入项目级 `cf` 依赖，并按官方迁移要求使用支持该格式的 Cloudflare Vite 插件 beta。复用已有 Vite、TanStack Start 与内容处理插件。

`cloudflare.config.ts` 固定域名所在账户和 Worker 名称，保留原先的运行时兼容日期及 `nodejs_compat`，以 `domains: ["esp32.sh"]` 绑定根域名。

`pnpm build` 改为 `cf build`，`pnpm deploy` 改为 `cf deploy`。`.cloudflare/` 加入忽略规则；TypeScript 显式纳入生成的类型。成功部署后移除旧 `wrangler.jsonc`，避免两套发布配置。

## DNS 切换

首次发布已上传代码与静态资源，但自定义域名 API 返回 100117：根域名已有外部管理的 A 记录。

已在 `.cache/deploy-before-cf/root-dns-records.json` 保存原始两条根域名 A 记录；按用户部署与配域名的授权，仅移除这两条冲突记录，再执行相同的 `cf deploy --prebuilt`。第二次发布与域名绑定成功。没有变更其他 DNS 名称、邮件记录或域名注册设置。

迁移前的配置、依赖清单和锁文件也保存在 `.cache/deploy-before-cf/`。该目录在忽略规则中。

## 验证

- `pnpm check` 和生成类型后的 `pnpm exec tsc --noEmit` 通过。
- `cf build` 通过，输出构建规范目录至 `.cloudflare/output/v0/`。
- `cf deploy --dry-run --prebuilt` 通过，报告无资源绑定。
- 迁移后的本地生产 HTTP 检查通过：100 个项目、140 款设备，420 个设备语言页面，以及默认语言、筛选、重定向、404、外部设备图片和关联项目排序。
- 公网 HTTPS 检查通过：英文根页、中文首页、日文首页、140 款设备目录、StopWatch 中文详情、reTerminal E1002 日文详情、按 StopWatch 筛选的项目列表均返回 200，语言与卡片数量正确；主 JavaScript 和 CSS 均返回 200 及正确内容类型。TLS 检查未关闭。
- 公网检查结果保存在 `.cache/deployment/public-smoke-results.json`。本轮启动的本地生产预览已停止，原有开发服务未主动停止。

未运行 computer-use 或浏览器自动化。构建保留既有的大 chunk、CSS sourcemap 和路由工具链循环依赖警告。

## 以后更新

```sh
pnpm check
pnpm build
cf deploy --dry-run --prebuilt
cf deploy --prebuilt
```

`cf deploy --prebuilt` 发布最近一次构建，修改内容后应重新构建。快捷命令 `pnpm deploy` 会重新构建后发布。授权失效时重新运行 `cf auth login`，无需在聊天或配置文件里粘贴 Token。

官方参考：[迁移 Wrangler 项目](https://developers.cloudflare.com/cf/wrangler/migrate/)、[cf 配置](https://developers.cloudflare.com/cf/projects/cloudflare-config/)。
