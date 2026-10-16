# 服务端路由类型缺失导致 CI 失败

## 现象与根因

项目详情与自动 sitemap 提交 `4b41799` 在本机通过，但 Cloudflare Build `8aff15af-0435-493c-9163-4c62cb1c1cd5` 在 `pnpm verify` 的类型检查阶段失败，尚未执行发布：

```text
src/routes/robots[.]txt.ts(4,3): error TS2353: ... 'server' does not exist ...
src/routes/sitemap[.]xml.ts(6,3): error TS2353: ... 'server' does not exist ...
```

`server.handlers` 依赖 TanStack Start 对 Router 的类型扩展。项目缺少显式类型入口；本机已有生成文件间接带入 Start 类型，掩盖了缺失。`tsr generate` 与 Start Vite 插件生成的路由树附带导入也不同，不能把已运行开发服务或构建后的本机结果视为首次检出的结果。

将失败提交导出到不含 `.cloudflare/` 等生成目录的临时目录，运行 `pnpm typecheck`，复现了 CI 的同两条错误。此复现复用了本机已安装依赖，验证的是生成文件差异，不是一次全新依赖安装。

## 修复与防复发

修复提交 `500883b` 新增受版本控制的 `src/start-env.d.ts`：

```ts
import '@tanstack/react-start'
```

这让首次类型检查显式载入 Start 的服务端路由扩展，没有关闭检查、修改生成类型或升级依赖。此前验证不足之处是没有覆盖无生成文件的首次检出，并且在首次推送后仅报告部署进行中，没有跟踪至最终结果。

后续遇到此类变更按 [部署手册](../operations/deployment.md#干净环境验证) 验证候选提交，并按“自动部署收尾”跟踪对应提交和新增线上入口。[AGENTS.md](../../AGENTS.md) 已要求此类故障修复时主动沉淀根因、遗漏原因、验证方法和防复发措施。

## 核验结果

- 隔离目录加入显式声明后，`pnpm verify` 通过：21 项 TypeScript/内容测试、19 项 Python 测试及生产构建通过。
- Cloudflare 修复构建 `9da941db-3ee7-4e3a-a86a-c6a6ace9c162` 完成，GitHub 检查结果 `success`，部署版本 `bbf696f1-261b-4bac-b9ec-b3fc7e6fe0a9`。
- 2026-10-16 公网通用 HTTP 检查 17 项通过；额外确认 `/projects/anan-iphone-use` 及其 `/zh`、`/ja` 版本的语言、摘要、canonical 与设备链接；`/sitemap.xml` 的 768 个规范地址及语言替代链接正确，`/robots.txt` 声明 sitemap。
- 验证范围为静态/构建和 HTTP；README 浏览器实时加载未因此得到实测证明。

本机补充证据位于 `.cache/project-pages-clean-before.log`、`.cache/project-pages-clean-after.log`、`.cache/project-pages-ci-retry.json` 与 `.cache/deployment/`，不提交日志或凭据；关键结论与标识已保留在本文，避免依赖临时缓存。
