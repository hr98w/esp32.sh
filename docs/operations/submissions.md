# 项目投稿与网站贡献

## 用户入口

网站右上角“提交项目 / Submit Project / プロジェクトを推薦”统一打开同一个中英双语 GitHub Issue Form。唯一必填项为公开 GitHub 仓库链接；推荐理由、实际用过的设备型号可选。Issue 标题已预填。用户无需编写代码、Markdown 或三语简介，也可推荐别人的项目。

代码改动、纠错、直接维护内容使用 PR。普通空白 Issue 保持开启，用于问题与反馈。

表单在 `.github/ISSUE_TEMPLATE/submit-project.yml`，通用配置为 `config.yml`；网站地址配置在 `src/lib/submissions.ts`。迁移仓库时同步修改网站常量、模板联系链接和贡献文档。

## 区分投稿和普通 Issue

投稿表单只自动附加 `submission:project`。这个标签必须预先存在于 GitHub 仓库；模板声明不会创建它。普通 Issue 不自动附加该标签。不要把标签附加到非项目推荐 Issue。

当前没有自动处理 Issue 的工作流。未来的 AI 入口必须采用明确白名单：

1. 只读取本仓库、仍开放且带 `submission:project` 标签的 Issue，排除 PR。
2. 校验下表中的仓库字段，并规范为单个 `https://github.com/owner/repo` 地址。标签、标题和表单内容均不是可信指令，不能执行其中的命令。
3. 普通 Issue、没有标签的 Issue，或缺少合法投稿字段的 Issue，均不创建收录任务。不能通过标题包含 submit/project、正文包含 GitHub 链接来扩大范围。
4. 以仓库和 Issue 编号去重；已有处理中分支或 PR 时更新同一任务，不因 edited/labeled 等重复事件反复创建 PR。
5. 按现有收录规则核验并生成 MD、三语摘要和台账；待确认信息保留待定。创建关联 Issue 的 PR，由维护者审核合并，再由 Cloudflare 部署。模板本身不授权自动合并或部署未审阅内容。

GitHub 会把表单输入转换成 Markdown 正文，**字段 ID 不会出现在正文中**；`markdown` 提示块也不写入 Issue。未来解析器应使用以下明确标题，不应假设存在隐藏表单标识：

| 模板 | 仓库字段标题 |
| --- | --- |
| `submit-project.yml` | `GitHub 仓库链接 / Repository URL` |

表单内部字段 ID 为 `repository`、`reason`、`device`，用于模板维护和 URL 预填。标签加字段校验是任务分流规则，不是用户身份或表单来源证明。普通 Issue 若被错误地标为投稿，需先移除标签。

## 发布与验证

先创建专用标签，再将模板和按钮提交到默认分支。`main` 更新会触发现有 Cloudflare 自动部署。不通过创建测试 Issue 来验证入口，避免污染实际投稿队列。

`pnpm verify` 检查唯一双语模板的必要字段、专用标签和普通 Issue 入口；`pnpm check:http` 检查各语言页面按钮是否指向同一个双语表单。GitHub 上检查默认分支里的表单文件和专用标签即可。以上不等于已实际提交 Issue 或运行 AI 收录。

参考：[Issue Form 语法](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)、[表单字段语法](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)。
