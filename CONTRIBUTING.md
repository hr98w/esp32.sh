# Contributing

To recommend an ESP32 project, [submit an issue](https://github.com/hr98w/esp32.sh/issues/new?template=submit-project.yml). Only the repository link is required; you do not need to write code or Markdown. Maintainers verify the project and prepare its listing.

Use pull requests for code changes, corrections, and direct content contributions. Ordinary issues remain available for questions and bug reports.

Contribute through a pull request to [hr98w/esp32.sh](https://github.com/hr98w/esp32.sh). Start with the [English README](README.md#contributing) or [中文 README](README.zh-CN.md#贡献内容). These are the content conventions for the directory; there is currently no automatic issue processing, AI approval, or auto-merge workflow.

1. Add one Markdown file per project under `content/projects/`, or one device under `content/devices/<manufacturer.id>/`. Start with a file in `templates/`.
2. Use a stable lowercase ID. Project folders do not depend on tags; a repository is listed once, even if it supports many boards.
3. Write a short summary in English, Chinese, and Japanese. Keep names, repository URLs, and hardware relations shared across languages. Original summaries are preferred to copying upstream paragraphs.
4. Projects need a substantive README, an explicit open-source license, and at least 10 GitHub stars at intake. A separate LICENSE file is not mandatory if the license is clearly declared elsewhere. Unclear licenses stay in the review queue.
5. Link a device only when upstream explicitly documents that model. Include the support source URL. Similar names, matching chips, M5Ware tags, and assumed pin compatibility are insufficient. List hardware revisions separately where they materially differ.
6. Use manufacturer sources for hardware facts. Unbranded boards use `generic`; unresolved manufacturers use `unknown`. Do not treat a marketplace seller as the manufacturer.
7. Covers are optional. Manual cover → cached README image candidate → project name. Use `autoCover: false` to disable discovery. Do not add third-party images without checking the relevant rights and attribution.
8. Add upstream URLs to `sources`; leave uncertain hardware details out. Project-device support belongs in the project file, and the device page finds it automatically.
9. Contributors can submit just the authored Markdown; maintainers update Star snapshots and review ledgers. Run `pnpm check` before review. Never commit personal tokens, cookies, `.cache/`, or generated build artifacts.

Stars and image candidates live in `data/` and do not require repeatedly editing each Markdown record. Website visits never call GitHub for Star updates. See `content/README.md` and `docs/research/collection-progress.md` for fields and review state.

# 内容投稿说明

推荐项目请[提交 Issue](https://github.com/hr98w/esp32.sh/issues/new?template=submit-project.yml)，只需填写 GitHub 仓库链接，不需要写代码或 Markdown。维护者负责核验和整理收录。修改网站代码、纠错或直接维护内容请提 PR；其他问题仍可提交普通 Issue。

项目、设备分别新增独立 Markdown 文件。项目文件平铺，设备按厂商分目录；摘要包含英文、中文和日文。项目需 README、明确的开源许可和入库时至少 10 个 Star。设备适配必须有上游明确依据，无法核实的先待定。封面可选。提交前运行 `pnpm check`，不要提交缓存、凭据或生成产物。

通过 [GitHub Pull Request](https://github.com/hr98w/esp32.sh/pulls) 提交维护改动，审核合并后发布。目前尚未启用自动处理 Issue、AI 自动批准或自动合并。维护与发布流程见 [文档索引](docs/README.md)。

## Tools / 工具

Tools use `content/tools/<id>.md` and [their own template](templates/tool.md). The [content guide](content/README.md#工具) explains the fields. Favor documented, useful ESP32 tools with distinct purposes. Hosted services and official vendor tools are allowed, but only verified source and license evidence warrants an open-source label; record pricing and usage requirements separately. Tools are curated rather than ranked by GitHub stars.

工具初版优先质量与实用性。每个工具各用一个 Markdown，补齐三语说明、适用条件、来源与核验时间；不把免费服务自动标成开源，也不把桌面浏览器支持推断成手机支持。
