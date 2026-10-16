# Agent 标签与指定项目收录

`agent` 的展示名称为智能体 / Agents / AIエージェント。它与 `ai` 可同时使用，面向实际智能体流程、模型工具调用、智能体可调用的 MCP 设备能力，以及智能体操作终端；不是“ESP32 上运行大模型”的承诺。

## 标签审阅

| 项目 | 加入 agent 的依据 |
| --- | --- |
| ESP32 iPhone Agent（新增） | iPhone 应用负责视觉智能体，ESP32 中继 AirPlay 画面并执行 USB HID 输入 |
| Anan iPhone Use（新增） | 为外部智能体提供 iPhone HID 操作的 MCP 固件，观察和决策留在客户端 |
| M5Claw | 实际 Agent 流程、工具调用、记忆与定时任务 |
| ClawPuter | 面向外部 OpenClaw Gateway 的硬件终端 |
| stackchan-mcp | 供 MCP 客户端调用的机器人动作、相机与语音工具 |
| chat-stick | 语音交互，并能调用设备和服务端工具 |
| XiaoZhi | 设备侧与云端 MCP 工具控制 |
| AI Stack-chan Ex | README 明确说明已实现实时语音与 MCP 扩展 |
| Vibe Watch | 智能体会话选择、批准/拒绝与语音输入的硬件界面 |
| VibeStick for Mac | 编程智能体的状态显示及按键语音输入终端 |

没有替换原有 `ai` 标签。普通 Stack-chan 是通用机器人与 MOD 平台；AI Monitor 当前主要显示用量，Claude 审批窗口标为开发中，两者暂不加入 agent。

KK StopWatch Avatar 已存在于 `content/projects/stopwatch-avatar.md`，保留 graphics/demo，不重复收录。它是程序绘制的互动表情，不具备智能体流程；将许可按 README 的明确声明细化为 AGPL-3.0-or-later。

## 来源与边界

三个指定仓库均完整阅读了缓存的上游 README。两个新增仓库的元信息及 README 于 2026-10-16 匿名获取；Star 快照分别为 2785 和 113，GitHub ID 未与现有条目重复。Avatar 使用现有 2026-10-16 核验快照（63 Star）。现有标签审阅使用上次匿名抓取的完整 README 缓存，具体来源时间保存在 `project-editorial-review.json` 的 `tagReview` 中。

ESP32 iPhone Agent 当前 README 已改为手机端应用编排流程，不再沿用旧的 Mac/Python 运行架构。明确适配 XIAO ESP32S3 普通版，不推导到 Sense、Plus 或其他 ESP32-S3 设备。Anan iPhone Use 明确支持 StopWatch，BLE 输入仍为实验功能，没有在本站实测硬件。

许可按完整 README 的 License 段核实：

- ESP32 iPhone Agent：MIT 主体与 GPL-3.0 的 AirPlay 代码；README 说明组合固件按 GPL-3.0 分发，记录为 `MIT AND GPL-3.0`。
- Anan iPhone Use：原有 `GPL-3.0-only` 与集成 Avatar 引擎的 `AGPL-3.0-or-later`，保留两个声明。

单独请求许可证文件时遇到匿名 GitHub API 403，已停止追加请求并保留限流状态；没有切换到个人身份或绕过冷却。没有声称独立读取了许可证文件。正文许可声明与核验依据已定点写入证据台账。
