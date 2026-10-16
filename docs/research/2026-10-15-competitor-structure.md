# ESPboards 与 ESPHome Devices 网站结构分析

记录日期：2026-10-15。用途：为 esp32.sh 的信息组织提供参考，并保留后续流量竞争研究的入口。

ESPboards 围绕硬件知识和开发任务组织内容，ESPHome Devices 围绕可运行 ESPHome 的具体设备组织内容。前者值得参考厂商、芯片、板型、用途之间的关联；后者值得参考简洁的设备列表、统一元数据和 GitHub 贡献入口。

两站是用户选定的重点竞品。流量规模、来源占比和主要获客页面尚待独立研究；内容数量、GitHub 活跃度和网站成熟度不能替代访问数据。本次依据公开页面、返回的 HTML 和 ESPHome Devices 公开源码分析结构；未执行浏览器交互，交互逻辑以所见控件及源码为依据。

## 两站的组织方式

| 维度 | ESPboards | ESPHome Devices |
| --- | --- | --- |
| 核心内容 | 开发板、芯片、传感器资料，以及教程、排障、工具 | 具体设备的 ESPHome 配置与说明 |
| 首页任务 | 引导用户进入多种资源栏目 | 说明目录用途、展示新设备、提供贡献入口 |
| 导航方式 | 顶部栏目与资源聚合页 | 文档侧栏、站内搜索、分类列表 |
| 主要分类 | 芯片、厂商、板型、用途；传感器另按类别和协议分类 | 设备类型、地区电气标准、微控制器平台 |
| 列表呈现 | 硬件条目带名称、厂商、价格等；不同聚合页承担不同任务 | 紧凑的设备名称与可点击分类标签 |
| 排序与榜单 | 热门设备榜与用途推荐分开 | 名称 A–Z、发布日期 |
| 详情页侧重 | 参数、引脚、文档、购买入口及相关资源 | 设备信息、配置、刷写或使用说明 |
| 内容维护入口 | 首页有社交渠道和项目展示邀请；未确认与 ESPHome 相同的统一设备投稿机制 | 明确的 GitHub 文件贡献流程，详情页可直接编辑 |

依据：[ESPboards 首页](https://www.espboards.dev/)、[开发板目录](https://www.espboards.dev/esp32/)、[ESPHome Devices 首页](https://devices.esphome.io/)、[ESP32 分类](https://devices.esphome.io/board/esp32/)。

## ESPboards 的页面结构

主要入口可以按以下层次理解。这是页面关系的概括，不是完整站点地图。

```text
首页
├─ Blog：教程、评测、项目文章
├─ Boards：硬件入口
│  ├─ 按芯片：ESP32-S3 等
│  ├─ 按厂商：M5Stack、Waveshare、LILYGO 等
│  ├─ 按板型：CYD、Super Mini、Zero 等
│  ├─ Popular：热门设备榜
│  ├─ Best：按用途推荐
│  └─ 具体开发板或集成设备
├─ Sensors：传感器资料
│  ├─ 按类别
│  ├─ 按通信协议
│  └─ 具体传感器
├─ Troubleshooting：分类、具体故障、向导、FAQ
├─ Tools：计算器、烧录、像素图案与音频工具等
└─ LVGL Designer：独立子域名的界面设计工具
```

首页有全局搜索入口，主要内容区将用户导向不同任务，再展示最新文章。由此可见，它服务的需求包括查设备、学习、解决故障和使用工具。[首页](https://www.espboards.dev/)

硬件目录通过多个聚合页重复利用设备资料。例如，同一台 M5Stack 设备可以从厂商页、芯片页和用途推荐进入；这些入口都有独立 URL，可以分别分享和被搜索引擎发现。芯片页还连接模块变体与开发板，厂商页介绍品牌并列出产品。[M5Stack 厂商页](https://www.espboards.dev/esp32/manufacturer/m5stack/)、[ESP32-S3 页](https://www.espboards.dev/esp32/microcontroller/esp32s3/)、[CYD 板型页](https://www.espboards.dev/esp32/type/cyd/)

设备范围已经包含下游厂商的集成产品。以 M5Stack Tab5 为例，页面介绍屏幕、相机等集成功能，并以整台设备为资料单元。该页的内容模块包括短介绍、图片、价格入口、主要规格、引脚、入门、注意事项、下载、FAQ、相关资源和相似设备。资源链接还指向 ESPHome 对应设备配置及厂商固件。[Tab5 详情页](https://www.espboards.dev/esp32/m5stack-tab5/)

对 esp32.sh 的启发是：具体商品型号应有稳定身份，厂商、芯片和板型则作为可交叉浏览的分类。无需在早期把芯片参数和引脚资料都复制过来。

用途推荐将需求分成触摸屏、电子纸、摄像头、LoRa 等，并为不同预算安排选项；热门榜则另设页面。热门榜自述依据 Google Search 的曝光与点击排序，但公开页未给出可独立复核的完整统计明细、时间窗或总体访问量。因此它可作为后续关键词研究的线索，不能用来证明该站总流量及来源占比。[用途推荐](https://www.espboards.dev/esp32/best/)、[热门榜](https://www.espboards.dev/esp32/popular/)

传感器有单独的类别、协议和详情结构，排障按错误类型组织，工具页集中提供浏览器工具。产品推断：这些栏目覆盖多种搜索意图，并与硬件资料形成内链；它们实际各自带来多少访问，需要后续数据验证。[传感器目录](https://www.espboards.dev/sensors/)、[排障入口](https://www.espboards.dev/troubleshooting/)、[工具页](https://www.espboards.dev/tools/)

## ESPHome Devices 的页面结构

```text
首页：用途说明、新增设备、贡献入口
├─ Made for ESPHome
├─ Device Type
│  └─ dimmer / light / misc / plug / relay / sensor / switch
├─ Electrical Standard
│  └─ au / br / eu / global / in / uk / us
├─ Microcontroller
│  └─ ESP32 / ESP8266 / BK72xx / RP2040 / RTL87xx 等
├─ Guides：添加设备、转换设备等
└─ Device：具体产品资料与配置
```

它的分类对应 ESPHome 的使用场景：用户需要知道设备做什么、适用哪个地区、使用什么微控制器。ESP32 在这里是平台分类；它还收录其他芯片平台，不能把整个站当成 ESP32 开发板目录。[首页](https://devices.esphome.io/)

分类列表以名称和标签为主，提供按名称或发布日期排序。标签链接到类型、平台和地区的独立分类页。检查的 `DeviceListing.astro` 负责客户端重新排序；所见列表没有厂商、价格、Star 或多条件组合筛选控件。这一观察限于检查的页面及组件，不扩展成全站不存在其他交互的断言。[ESP32 列表](https://devices.esphome.io/board/esp32/)、[传感器列表](https://devices.esphome.io/type/sensor/)、[列表组件](https://github.com/esphome/devices.esphome.io/blob/main/src/components/DeviceListing.astro)

设备页的顶部展示统一分类，正文允许不同贡献者按设备需要组织。KinCony B2 页面包括资源、基础配置和高级配置；Apollo AIR-1 页面包括介绍、快速开始、上游配置和相关链接。它们共同提供设备与可用配置之间的联系，但正文并非所有设备都完全一致。[KinCony B2](https://devices.esphome.io/devices/kincony-b2/)、[Apollo AIR-1](https://devices.esphome.io/devices/apollo-automation-air-1/)

Made for ESPHome 是有要求的生态项目入口，页面说明设备按相应要求设计并预装固件。普通设备收录与该项目资格需区分；这不是 esp32.sh 仅凭兼容信息即可照搬的认证标签。[Made for ESPHome](https://devices.esphome.io/made-for-esphome/)

## ESPHome Devices 的贡献与维护

公开贡献页要求每台设备建立目录和 Markdown 文件，元数据包含标题、日期、类型、地区等；微控制器、项目链接、难度等可补充。贡献入口还提供填写用户名和设备名后生成 GitHub 新文件链接的功能。[贡献指南](https://devices.esphome.io/devices/adding-devices/)

值得借鉴的是“单个设备记录 + 标准字段 + 原位纠错”的组织方式。详情页的 Edit page 链接指向 GitHub 对应内容文件，用户不必另行描述要改哪个页面。[页面示例](https://devices.esphome.io/devices/apollo-automation-air-1/)

源码补充确认：

| 文件 | 与本次分析相关的内容 |
| --- | --- |
| [`astro.config.mjs`](https://github.com/esphome/devices.esphome.io/blob/main/astro.config.mjs) | 使用 Astro、Starlight；配置侧栏、站点地图、GitHub 编辑入口和设备资源集成 |
| [`package.json`](https://github.com/esphome/devices.esphome.io/blob/main/package.json) | 构建前执行设备与 YAML 校验，另有链接检查脚本 |
| [`DeviceListing.astro`](https://github.com/esphome/devices.esphome.io/blob/main/src/components/DeviceListing.astro) | 静态输出列表，浏览器按名称或日期重排；别名行不增加设备总数 |
| [`.github/workflows/ci.yaml`](https://github.com/esphome/devices.esphome.io/blob/main/.github/workflows/ci.yaml) | PR 包括 Markdown、YAML、元数据及外链检查 |

源码取样依据为 GitHub tree `232bac526f06237daabba9111cee7910ac282f9c`，这是 tree SHA，不是 commit SHA。上述链接指向可变的 main；今后复查实现时应重新核对。没有依据将其所有审核流程概括成 AI 审核或自动合并。

## 对 esp32.sh 的产品含义

用户已明确的范围另存于 [产品约束](../product/2026-10-15-product-direction.md)。以下是待讨论的结构建议：

| 参考对象 | 适合借鉴 | 与当前范围的关系 |
| --- | --- | --- |
| ESPboards 的厂商与产品结构 | 原厂板、第三方集成板、成品设备统一收录；按厂商、芯片和板载功能浏览 | 符合下游产品收录需求 |
| ESPboards 的分类聚合页 | 有内容支撑的芯片、厂商、用途页面 | 为后续搜索获客留下清晰页面结构 |
| ESPHome 的简洁列表 | 名称、标签、独立详情页、统一排序控件 | 可以增加仓库 Star 与具体设备筛选 |
| ESPHome 的贡献入口 | 文件化内容、统一元数据、页面纠错链接 | 符合 GitHub 投稿与低维护目标 |
| 两站的丰富详情 | 保留短说明、必要元数据及原始链接 | 项目页以 AI 摘要为主，制作细节由原仓库承载 |

项目和设备应是独立记录，建立多对多关系：一个项目支持多台设备，一台设备对应多个项目。具体设备型号与芯片系列应分开筛选；同芯片不自动建立固件兼容关系。一个通用项目可以只标支持的芯片系列，不强行指定商品型号。

硬件记录可覆盖普通开发板、带屏幕或麦克风等外设的一体板、带外壳的完整设备。硬件本身是否开放设计单独记录；用户明确要求开源的是收录的项目，不能据此擅自排除所有非开源硬件商品。

Star 排序属于项目仓库热度。设备页可列出相关项目并按 Star 排序；不能把某项目的 Star 冒充设备自己的热度。最先提供总 Star 和新增时间即可；若以后加入一周增长，需要积累带时间的快照。

## 后续流量研究清单

当前先保留研究问题，不填写未经核实的流量数字。后续应对两站采用相同统计月份、地区、设备口径，并区分主域与子域。

| 研究对象 | 要查的问题 | 现有线索 |
| --- | --- | --- |
| 域名及子域 | 两站月访问量及趋势如何？工具子域是否被并入？ | ESPboards 有独立 LVGL 子域；devices.esphome.io 是 ESPHome 的子域 |
| 自然搜索 | 非品牌关键词是什么？流量落在哪类页面？ | ESPboards 的型号、引脚、选型、故障页面；ESPHome 的产品型号与配置页面 |
| 热门落地页 | 哪些页面贡献主要流量，内容是否集中？ | ESPboards 的 Popular 页可作为候选型号清单，不作为访问量证明 |
| 外链与引荐 | 官方文档、GitHub、硬件厂商、社区分别带来什么？ | Tab5 页实际链接到 ESPHome 配置；其他引荐方向及数量待查 |
| 社交 | X、Reddit、YouTube、Pinterest 等渠道有何作用？ | ESPboards 公开社交入口；入口存在不代表渠道流量大 |
| 受众地区 | 中文与英文市场的关键词、竞争强度是否不同？ | esp32.sh 已确定中英文同等重要 |
| 内容缺口 | 有搜索需求但竞品缺少哪些项目或设备关联？ | 聚焦具体设备能运行的开源项目、项目 demo 和仓库排序 |

比较时记录工具名、采样日期、统计区间与估算口径。SEO 工具的自然搜索估算不等于总访问量，公开页面也无法提供竞争对手的真实 Search Console 数据。最终竞争方向应由具体关键词和落地页证据决定。
