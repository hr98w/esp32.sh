# Contributing content

The public repository and submission flow have not been announced yet. Start with the step-by-step [English README](README.md#contributing-projects-and-devices) or [中文 README](README.zh-CN.md#贡献项目与设备). These are the content conventions for the directory; there is no automated AI approval or auto-merge workflow.

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

项目、设备分别新增独立 Markdown 文件。项目文件平铺，设备按厂商分目录；摘要包含英文、中文和日文。项目需 README、明确的开源许可和入库时至少 10 个 Star。设备适配必须有上游明确依据，无法核实的先待定。封面可选。提交前运行 `pnpm check`，不要提交缓存、凭据或生成产物。

站点已上线；公开源码仓库与投稿入口尚未公布。内容先在本地审阅，再由维护者发布，没有 AI 自动批准或自动合并。维护与发布流程见 [文档索引](docs/README.md)。
