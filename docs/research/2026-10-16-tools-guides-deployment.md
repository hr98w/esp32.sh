# 2026-10-16 分页、工具与新手指南发布

- 站点：https://esp32.sh/
- Worker：`esp32-sh`
- 版本：`1edaa9b8-3a1d-437a-a348-bef9fac67fce`
- 发布方式：`pnpm deploy:built`（`cf deploy --prebuilt`），退出码 0，域名触发器部署成功。
- 内容：100 个项目、141 个设备、10 个工具；新手指南包含 4 张推荐和 10 条 X 嵌入。
- 新手指南：`/guides`、`/zh/guides`、`/ja/guides`；推文集中展示，桌面默认三列、平板两列、手机一列。新增立创实战派 S3 设备页；推荐设备均链接站内详情。

## 验证

`pnpm verify` 通过（15 个内容测试、19 个采集测试及生产构建）。`pnpm check:http` 通过，包含 423 个三语设备详情和三语新手指南。`pnpm deploy:check` 通过。

发布后 `pnpm check:deployment` 的 17 项公网检查全部通过，覆盖三语首页、分页、工具、新手指南、代表设备及 JS/CSS。另行核对线上 `/zh/guides` 含 10 条原帖链接、单一推文区域和桌面三列 CSS。结果保存在 `.cache/deployment/public-smoke-results.json` 和 `.cache/deployment/guide-layout-check.txt`。

这些是 HTTP、HTML 和样式规则检查，不代表浏览器水合、X iframe 实际渲染或硬件实测。

## 登录情况

第一次上传因凭据过期而未执行。默认设备授权流程网络请求失败，随后通过 `cf auth login --no-device` 完成官方 OAuth 登录，再发布成功。未修改 DNS，未使用 GitHub 身份或凭据。
