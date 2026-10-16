# GitHub 与 Workers Builds

- 公开仓库：https://github.com/hr98w/esp32.sh
- 本地 `origin` 与 `main` 上游已设置，保留原本提交历史。
- Cloudflare Worker：`esp32-sh`；生产域名：`esp32.sh`。
- Workers Builds 生产触发器：`7c336a0d-a794-4bfd-b6b5-4859cc9b75e6`。
- 监听 `main` 的全部路径；构建 `pnpm verify`，通过后部署 `pnpm deploy:built`。构建缓存已启用，其他分支未配置部署。
- 触发验证：提交 `ce616f8d44545b8ae5b7a5bbfb9a0c4c6f48a113`，来源 `push_event`。
- 首次构建 `67bd4809-ae6d-426a-a7a6-a53112d6dacc` 成功，GitHub 检查成功，部署版本 `00a50605-31fa-4496-9f35-bbcfc3104100`。
- 自动发布后 17 项公网 HTTP 检查通过。未验证浏览器水合、X iframe 或硬件运行。

构建授权在 Cloudflare 中管理，限制为当前账户和 esp32.sh zone 所需权限；临时明文文件已删除，没有提交到 GitHub。本地 CLI 未自动读取 macOS 系统代理；本次 Git / cf 命令显式使用已配置的本地代理后连接成功，未把代理地址写入项目配置。

日常操作与未来迁移组织时的检查项见[部署手册](../operations/deployment.md)。官方说明：[Workers Builds 配置](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/)、[GitHub 仓库转移](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)。
