# 文档索引

日常操作查 `operations/`；字段规则查 `content/README.md`；`product/` 和 `research/` 保留当时的决策、来源与执行记录。历史报告中的数量和“尚未部署”等描述只代表当时状态。

## 日常维护

- [部署手册](operations/deployment.md)：cf 登录、构建、发布、线上检查、域名与回退。
- [维护指南](operations/maintenance.md)：目录职责、数据流、验证与依赖更新。
- [内容指南](../content/README.md)、[贡献约定](../CONTRIBUTING.md)：Markdown 字段与审阅要求。
- [采集工具说明](../scripts/README.md)、[数据台账说明](../data/README.md)：脚本入口、网络行为与审阅阶段。

## 当前进度（脚本生成）

- [收录进度](research/collection-progress.md)、[逐设备收录队列](research/device-intake-queue.md)。
- [设备图片与详情覆盖](research/device-enrichment-progress.md)。
- 刷新这些文件运行 `pnpm collect:report:all`，不要直接修改生成的报告。

- [项目投稿与贡献](operations/submissions.md)：双语表单、专用标签及未来 AI 处理边界。

## 产品约定与历史依据

- [Agent 标签与指定项目收录](research/2026-10-16-agent-tags-intake.md)：标签边界、设备关联与组合许可。

- [GitHub 与 Workers Builds](research/2026-10-16-github-workers-builds.md)：个人仓库、main 自动部署和首次推送验证。

- [新手指南](product/2026-10-16-beginner-guide.md)：推荐设备与玩法、独立推文 Markdown、嵌入和删减方式。

- [产品方向](product/2026-10-15-product-direction.md)、[功能结构](product/2026-10-15-site-functional-structure.md)。
- [工具目录首版](product/2026-10-16-tools-directory.md)：页面组织、首批 10 个工具与质量规则。
- [内容记录约定](product/2026-10-16-content-records.md)、[首轮采集计划](product/2026-10-16-data-collection-plan.md)。
- [竞品结构调研](research/2026-10-15-competitor-structure.md)、[按设备找项目调研](research/2026-10-15-device-to-project-discovery.md)。
- [内容扩充审阅报告](research/2026-10-16-content-expansion-review.md)。
- [分页、工具与新手指南发布](research/2026-10-16-tools-guides-deployment.md)：版本与 17 项公网检查。
- [Plausible 与 Logo 发布记录](research/2026-10-16-plausible-branding-deployment.md)：线上检查与 CLI 收尾网络错误的边界。
- [首次 Cloudflare 上线记录](research/2026-10-16-cloudflare-deployment.md)：已发布版本和 DNS 切换依据。
- [历次工作日志](research/overnight-work-log.md)、[早期 HTML 原型](prototype/index.html)。

新增操作规则写入相应维护手册；一次性的核验结论写进有日期的研究记录或 `data/collection/` 台账，避免把操作入口埋进长日志。
