# esp32.sh

[English](README.md) | **简体中文**

为你手里的 ESP32 设备寻找开源项目：**[esp32.sh](https://esp32.sh/zh)**。

收录开源项目、设备、实用工具和新手推荐，支持中英日三语。使用 TanStack Start、React 和 Cloudflare Workers，内容以 Markdown 保存，无需数据库。

## 本地开发

需要 Node.js 22.12+、pnpm 10、Python 3.10+ 和 curl。

```sh
pnpm install --frozen-lockfile
pnpm dev                     # http://localhost:3000
pnpm verify                  # 内容、类型、测试和生产构建
```

检查生产构建时，在两个终端分别运行 `pnpm preview --port 4317` 和 `pnpm check:http`。

## 贡献内容

推荐项目请[提交 Issue](https://github.com/hr98w/esp32.sh/issues/new?template=submit-project.yml)，只需提供 GitHub 链接。修改网站或维护内容请提 PR。

每个条目一个 Markdown，从[模板](templates/)开始：

| 内容 | 目录 |
| --- | --- |
| 项目 | `content/projects/` |
| 设备 | `content/devices/<manufacturer.id>/` |
| 工具 | `content/tools/` |
| 新手推荐 | `content/guides/picks/` |
| X 推文嵌入 | `content/guides/posts/` |

简介需包含中英日三语。项目须在 GitHub 公开源码、有 README、与 ESP32 相关，且收录时至少 10 Star。许可证不作为收录门槛；无协议或有非商业限制均可收录，但须如实注明。设备适配需有上游明确依据，相同芯片不代表兼容。封面可选。

运行 `pnpm check` 后，向 [hr98w/esp32.sh](https://github.com/hr98w/esp32.sh) 提交 Pull Request。字段和审核规则见[内容指南](content/README.md)与[贡献约定](CONTRIBUTING.md)。

## 部署

Cloudflare Workers Builds 监听 `main`，通过 `pnpm verify` 后自动部署。Git 集成与手动发布见[部署手册](docs/operations/deployment.md)。

```sh
pnpm exec cf auth login      # 需要登录时使用
pnpm verify
pnpm deploy:check            # 预检查，不上传
pnpm deploy:built
pnpm check:deployment
```

项目详情页复用现有 Markdown 信息，由访客浏览器直接从 GitHub 加载原始 README。`/sitemap.xml` 和 `/robots.txt` 根据目录自动更新。

配置入口：[cloudflare.config.ts](cloudflare.config.ts)。完整流程见[部署手册](docs/operations/deployment.md)。

## 文档

- [维护手册](docs/operations/maintenance.md) · [采集工具](scripts/README.md) · [收录进度](docs/research/collection-progress.md)
- [项目收录技能](skills/esp32-project-intake/SKILL.md) · [文档索引](docs/README.md)
