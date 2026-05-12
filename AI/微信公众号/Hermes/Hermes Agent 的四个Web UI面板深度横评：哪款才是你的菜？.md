> 📎 来源: [DNOPC](https://mp.weixin.qq.com/s?__biz=MzY4ODE5Mjc0MQ==&mid=2247483827&idx=1&sn=5de510dce3d57747032cc4046227236e&chksm=f2d6fdeea64fc8c4b7f891ee29f54be4b60590c511ee52c18a15f092c8a2566bfbd1a5b963a1&mpshare=1&scene=1&srcid=04206w5lvqS8vILVxHI8UXMH&sharer_shareinfo=41f377ad09bae87f9ac15bf973eb9b23&sharer_shareinfo_first=41f377ad09bae87f9ac15bf973eb9b23) | 时间: 2026-04-22 00:16

---

## 前言：命令行虽好，但面板更香

很多朋友跑着 Hermes Agent，日常操作还是在终端里敲命令——黑底白字，一行一行读输出。

命令行固然很好，Hermes Agent 设计之初就是 terminal-first 的产品。但问题是：**当你需要管理多个会话、配置 Telegram Bot、查看 Token 消耗、设置定时任务时、更优秀的人机交互，终端的效率就开始拖后腿了。**

好消息是，开源社区已经跑出了几套非常成熟的 Web 面板方案。它们不是简陋的 demo，已经是功能覆盖完整、体验对标商业软件的成熟产品。

今天这篇，我们来一次深度横评，把目前 GitHub 上最主流的四套方案全部拆解：**EKKOLearnAI/hermes-web-ui、nesquena/hermes-webui、itq5/OpenClaw-Admin、open-webui/open-webui**。看完你就知道自己该选哪个了。

欢迎关注公众号或加入社区社群微信号:dnhopc，一起探索AI与OPC的更多可能性。

---

## 横向对比总览

在开始之前，先上一张全局对比表，建立整体认知：

| 维度 | EKKO Web UI | nesquena WebUI | OpenClaw-Admin | Open WebUI |
| --- | --- | --- | --- | --- |
| **定位** | 全能控制台 | 极简聊天面板 | 多智能体管理平台 | 通用 AI 平台 |
| **技术栈** | Vue 3 + Node.js BFF | Python + 原生 JS | Vue 3 + Express | Svelte + Python |
| **学习成本** | 中等 | 低 | 较高 | 低 |
| **配置 Telegram/Discord** | ✅ 原生支持 | ❌ 需手动 | ✅ 原生支持 | ❌ 需配置 |
| **数据看板** | ✅ Token/成本/趋势 | ⚠️ 仅当前会话 | ✅ 系统监控 | ✅ 用量统计 |
| **Web 终端** | ✅ node-pty | ❌ | ✅ node-pty | ❌ |
| **多网关支持** | ❌ 仅 Hermes | ❌ 仅 Hermes | ✅ OpenClaw + Hermes | ❌ |
| **上手难度** | 一键安装 | 零编译 | 需手动配置 | Docker 一键 |
| **适合人群** | 追求全面控制 | 纯聊天界面党 | 多智能体玩家 | 已有 Open WebUI |

---

## 方案一：EKKOLearnAI/hermes-web-ui —— 全能控制台

**GitHub**: https://github.com/EKKOLearnAI/hermes-web-ui**Star**: 社区活跃度高**技术栈**: Vue 3 + TypeScript + Vite + Naive UI（前端） + Koa 2 BFF（后端）

### 这是什么定位

如果用一个词来形容 EKKO Web UI，就是**全能管家**。它的设计目标非常明确：**你能在命令行做的所有事情，它都给你做了一个可视化的入口。**

它是四套方案里对 Hermes 平台渠道（Channel）集成最深的——8 个平台的机器人配置全部可以在一个页面里搞定。

### 核心功能拆解

**AI 对话**

- SSE 实时流式输出，支持异步运行
- 多会话管理：创建、重命名、删除、切换
- 按来源分组（Telegram、Discord、Slack 等），手风琴折叠
- 实时活跃会话指示器
- Markdown 渲染 + 语法高亮 + 代码复制
- Tool Call 详情展开（参数 / 结果）
- 文件上传支持
- 全局模型选择器：自动从 `~/.hermes/auth.json` 发现模型
- 每个会话显示模型 badge + Token 用量

**平台渠道配置**这是 EKKO 最亮眼的功能模块，一个页面统一配置 8 个平台：

| 平台 | 支持功能 |
| --- | --- |
| **Telegram** | Bot Token、@控制、反应、免费对话 |
| **Discord** | Bot Token、@、自动线程、反应、频道黑白名单 |
| **Slack** | Bot Token、@控制、机器人消息处理 |
| **WhatsApp** | 开关、@控制、@模式 |
| **Matrix** | Access Token、Homeserver、自动线程 |
| **飞书/Lark** | App ID / Secret、@控制 |
| **微信** | 扫码登录（浏览器内自动保存凭证） |
| **企业微信** | Bot ID / Secret |

凭证管理直接写入 `~/.hermes/.env`，频道行为设置写入 `~/.hermes/config.yaml`，配置变更后自动重启 Gateway。

**使用数据分析**

- Token 总消耗分解（输入 / 输出）
- 会话数量 + 日均统计
- 预估成本追踪 + 缓存命中率
- 模型使用分布图表
- 30 天每日趋势（柱状图 + 数据表）

**定时任务**

- 创建、编辑、暂停、恢复、删除 Cron 任务
- 立即触发执行
- Cron 表达式快捷预设

**模型管理**

- 从凭证池自动发现模型
- 从各 Provider 端点获取可用模型
- 添加、更新、删除 Provider（预设 + 自定义 OpenAI 兼容）
- OpenAI Codex OAuth 登录
- Provider 级模型分组 + 默认模型切换

**多 Profile 与 Gateway**

- 创建、重命名、删除、切换 Hermes Profiles
- 从现有 Profile 克隆或从归档（.tar.gz）导入
- 导出 Profile 用于备份或分享
- 多 Gateway 管理：启动、停止、监控每个 Profile 的 Gateway
- 自动端口冲突解决

**Web 终端**内置基于 node-pty 和 @xterm/xterm 的真实终端：

- 多会话支持：创建、切换、关闭终端会话
- 通过 WebSocket 实时传输键盘输入和 PTY 输出
- 窗口大小调整支持

### 安装方式

```
# npm 一键安装（推荐）npm install -g hermes-web-uihermes-web-ui start# 打开 http://localhost:8648# 一键安装脚本（自动检测 Node.js）bash <(curl -fsSL https://raw.githubusercontent.com/EKKOLearnAI/hermes-web-ui/main/scripts/setup.sh)# Docker Composedocker compose up -d --build hermes-agent hermes-webui# 打开 http://localhost:6060
```

### 谁适合用 EKKO

✅ **强烈推荐**：

- 需要同时管理多个消息平台（Telegram/Discord/Slack/微信）的用户
- 对 Token 消耗和成本控制有严格监控需求的团队
- 希望在 Web 界面直接操作 Gateway 配置的技术管理者
- 需要 Web 终端但不想开第二个 SSH 会话的人

❌ **不太适合**：

- 只想找个干净聊天界面、不想做任何配置的用户（功能过多反而是负担）
- Windows 原生用户（官方明确不支持）

---

## 方案二：nesquena/hermes-webui —— 极简聊天面板

**GitHub**: https://github.com/nesquena/hermes-webui**Star**: 社区活跃，有详尽的贡献者档案**技术栈**: Python + 原生 JavaScript + 无构建步骤

### 这是什么定位

nesquena 的方案主打一个**零门槛**。它用纯 Python 和原生 JS 写成，不需要 Node.js 环境，不需要 Webpack，不需要任何构建步骤。界面复刻了 Claude 的经典三栏布局，风格偏深色极简。

如果你追求的是**一个干净的聊天界面，不需要折腾复杂的配置**，这就是你的菜。

### 核心功能拆解

**三栏布局**

- 左侧边栏：会话列表 + 导航
- 中央聊天区：对话主体
- 右侧工作区：文件浏览

模型、Profile、Workspace 控制条始终固定在输入框 footer，一目了然。Token 用量用环形图显示，随时可见。

**聊天体验**

- SSE 流式响应（Token 生成时实时显示）
- 多 Provider 模型支持——任何 Hermes API Provider（OpenAI、Anthropic、Google、DeepSeek 等）都可以动态填充下拉菜单
- 发送消息时若有其他消息在处理中，自动排队
- 任意编辑历史用户消息并从该点重新生成
- 一键重试上一次助手响应
- 直接从 composer footer 取消正在运行的任务
- Tool Call 卡片内联显示：展开/折叠所有切换
- Mermaid 图表渲染（流程图、时序图、甘特图）
- 思考/推理展示：Claude 扩展思考和 o3 推理块的金色主题可折叠卡片
- 危险 Shell 命令审批卡（允许一次 / 本次会话 / 始终 / 拒绝）
- Markdown 渲染 + 代码块复制按钮
- 语法高亮（Python、JS、bash、JSON、SQL 等）

**语音输入**

- 浏览器原生语音识别（Web Speech API）
- 点击录音，再次点击或发送停止
- 实时转录显示在文本框
- 静默约 2 秒自动停止

**主题系统**内置 7 套主题：Dark（默认）、Light、Slate、Solarized Dark、Monokai、Nord、OLED。随时切换，即时预览，也可通过 `/theme` 命令切换。

**Docker 多容器编排**支持 Agent + Dashboard + WebUI 三容器协同：

- hermes-agent：Gateway API（端口 8642）
- hermes-dashboard：监控 UI（端口 9119）
- hermes-webui：浏览器聊天界面（端口 8787）

### 安装方式

```
# 方式一：克隆后引导git clone https://github.com/nesquena/hermes-webui.git hermes-webuicd hermes-webuipython3 bootstrap.py# 方式二：Shell 启动器./start.sh# Docker（推荐生产环境）docker compose up -d# 打开 http://localhost:8787
```

### 谁适合用 nesquena WebUI

✅ **强烈推荐**：

- 追求干净聊天体验、不想做复杂配置的用户
- 喜欢 Claude/ChatGPT 风格界面的用户
- macOS / Linux / WSL2 用户
- 需要 Docker 快速部署的用户

❌ **不太适合**：

- 需要配置 Telegram/Discord 机器人的用户（这些配置在 Hermes Agent 端单独处理）
- Windows 原生用户（不支持）
- 需要实时系统监控和 Token 成本分析的用户

---

## 方案三：itq5/OpenClaw-Admin ——多智能体管理平台

**GitHub**: https://github.com/itq5/OpenClaw-Admin**Star**: 社区活跃，中文文档完善**技术栈**: Vue 3 + TypeScript + Vite + Naive UI（前端） + Express + node-pty（后端）

### 这是什么定位

OpenClaw-Admin 的定位不是简单的聊天界面，是**多智能体管理平台**。它是四套方案里最"重"的一个，但功能也是最全的之一。

它的核心亮点是**同时支持 OpenClaw Gateway 和 Hermes Agent 两个平台**，一套界面管理两种智能体。此外它还提供了远程桌面、文件浏览器、系统监控等传统"运维工具"级别的功能。

**如果你手里跑着好几个 AI 代理，需要统一管控**，选这个。

### 核心功能拆解

**双网关支持**这是 OpenClaw-Admin 区别于其他方案的最大特点：

| 模块 | OpenClaw Gateway | Hermes Agent |
| --- | --- | --- |
| Dashboard | ✅ 完整 | ✅ 基础 |
| 在线对话 | ✅ | ✅ |
| 会话管理 | ✅ | ✅ |
| 记忆管理 | ✅ | ✅ |
| 任务计划 | ✅ | ✅ |
| 模型管理 | ✅ | ✅ |
| 频道管理 | ✅ (QQ/飞书/钉钉/企微) | ✅ (Telegram/Discord/Slack 等) |
| CLI 终端 | ✅ | ✅ |
| 系统监控 | ✅ | ❌ |
| 远程桌面 | ✅ | ❌ |

**OpenClaw Gateway 模块**

- 仪表盘：运行总览、Token 趋势图表、会话活跃度、实时事件流、Top 模型/渠道/工具分布
- 在线对话：SSE 实时聊天、斜杠命令、消息筛选、快捷回复、Token 统计
- 多智能体：创建管理多个 AI Agent、身份/模型/工具权限配置
- 智能体工坊：多 Agent 协作空间、场景创建向导、任务委派
- 虚拟公司：可视化办公场景、角色移动交互、区域功能
- 远程终端：SSE 协议、多节点支持、全屏模式
- 远程桌面：Linux/Windows 远程桌面、实时画面传输、剪贴板同步
- 系统监控：CPU/内存/磁盘、网络连接、实例状态、运行时间

**Hermes Agent 模块**除了覆盖基本功能外，亮点是 **Hermes CLI 终端**：

- 通过 node-pty 启动真实 CLI 进程，完整终端仿真
- 会话持久化：断开浏览器不中断 CLI 进程，支持断线重连 + 输出缓冲区回放
- 启动参数面板：可视化配置 model、provider、skills、toolsets、yolo 等
- 多会话管理：创建、切换、重连、分离、重命名、销毁
- 无 WebSocket：纯 SSE + HTTP POST 双通道，兼容严格网络策略

**Web Terminal 技术细节**

| 功能 | 支持情况 |
| --- | --- |
| 全屏模式 | ✅ |
| 右键粘贴 | ✅ |
| 选中复制 | ✅ |
| 自适应大小 | ✅ |
| 多会话 | ✅ |
| 断线重连 | ✅ |

### 安装方式

```
# 安装依赖npm install# 复制环境变量cp .env.example .env# 开发模式npm run dev:all# 打开 http://localhost:3001# 生产构建npm run buildnpm run start
```

**Hermes Agent 集成需要单独安装**：

```
# 一键安装 Hermes Agentcurl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash# 启动 Gatewayhermes gateway start# 启动 Dashboardhermes dashboard
```

### 谁适合用 OpenClaw-Admin

✅ **强烈推荐**：

- 同时使用 OpenClaw 和 Hermes 两个网关的用户
- 需要多智能体协作管理的团队
- 对系统监控（CPU/内存/网络）有硬需求的用户
- 需要远程桌面功能的技术管理者
- 中文用户（文档完善）

❌ **不太适合**：

- 只想找个聊天界面的轻量用户
- 单网关 + 简单需求（功能过多造成浪费）
- 追求秒级启动的极简主义者

---

## 方案四：open-webui/open-webui —— 通用AI平台

**GitHub**: https://github.com/open-webui/open-webui**Star**: 超大规模社区，极为活跃**技术栈**: Svelte（前端） + Python（后端）**安装方式**: Docker 一键部署

### 这是什么定位

Open WebUI 是一个**通用 AI 平台**，不是 Hermes 专属的面板。它的设计目标是成为一个功能完备的 self-hosted AI 平台，支持 Ollama、OpenAI 兼容 API 等多种后端。

它之所以在这篇文章里被提到，是因为 **Hermes Agent 可以被配置成 OpenAI 兼容的 API 格式**，从而"伪装"成 OpenAI 后端接入 Open WebUI。

如果你**已经在用 Open WebUI**，不需要再装新的面板，直接配置一下就能用 Hermes。

### 核心功能拆解

Open WebUI 的功能极为丰富，以下是亮点模块：

**多模型和多来源支持**

- 原生 Ollama 集成
- OpenAI 兼容 API 集成（LMStudio、GroqCloud、Mistral、OpenRouter、MiniMax、Z.AI 等）
- 多模型并行对话（同时使用多个模型）

**RAG 和知识库**

- 内置 RAG 推理引擎
- 支持 9 种向量数据库（ChromaDB、PGVector、Qdrant、Milvus、Elasticsearch、OpenSearch、Pinecone、S3Vector、Oracle 23ai）
- 多种文档提取引擎（Tika、Docling、Document Intelligence、Mistral OCR）
- `#`

  命令直接加载文件到对话

**Web 搜索和浏览**

- 15+ 搜索提供商（SearXNG、Google PSE、Brave Search、Kagi、Perplexity 等）
- Web 浏览能力：`#` + URL 直接注入网页内容到对话

**语音和视频**

- 多语音转文本提供商（本地 Whisper、OpenAI、Deepgram、Azure）
- 多语音合成引擎（Azure、ElevenLabs、OpenAI）
- 免手操作语音/视频通话

**企业级功能**

- LDAP / Active Directory 集成
- SCIM 2.0 自动供给
- SSO via OAuth
- 基于角色的访问控制（RBAC）
- 横向扩展：Redis + WebSocket 支持多节点部署
- OpenTelemetry 支持

**Pipeline 插件框架**支持自定义 Python 函数集成，实现函数调用、用户限流、实时翻译、有害信息过滤等。

### 与 Hermes 的集成方式

1. 在 Hermes Agent 端启用 API Server
2. 获取 API 地址和 Key
3. 在 Open WebUI 中添加 OpenAI 兼容的 Custom Provider，填入 Hermes 的 API 地址
4. 开始使用

```
# Hermes 端启用 API Server# 编辑 ~/.hermes/config.yamlapi_server:  enabled: true  key: "your-api-key"# 在 Open WebUI 中添加 Provider# URL: http://your-hermes-server:8642/v1# API Key: your-api-key
```

### 谁适合用 Open WebUI

✅ **强烈推荐**：

- 已经在使用 Open WebUI 的用户
- 需要 RAG 和知识库功能的用户
- 需要多模型并行对话的用户
- 企业环境，需要 LDAP/SCIM/RBAC 等安全功能

❌ **不太适合**：

- 追求 Hermes 原生体验的用户（毕竟不是亲生的）
- 需要深度集成 Hermes 特有功能（Channel 平台配置、Cron 任务管理等）的用户

---

## 深入对比：四个维度

### 1. 平台渠道集成深度

| 功能 | EKKO | nesquena | OpenClaw-Admin | Open WebUI |
| --- | --- | --- | --- | --- |
| Telegram Bot 配置 | ✅ 一键 | ❌ | ❌ | ❌ |
| Discord Bot 配置 | ✅ 一键 | ❌ | ❌ | ❌ |
| Slack Bot 配置 | ✅ 一键 | ❌ | ❌ | ❌ |
| 微信/企业微信 | ✅ | ❌ | ✅ (OpenClaw) | ❌ |
| 飞书/钉钉 | ✅ | ❌ | ✅ (OpenClaw) | ❌ |
| Matrix | ✅ | ❌ | ❌ | ❌ |

**结论**：EKKO 是渠道集成最全的；OpenClaw-Admin 在 OpenClaw 模式下渠道支持也很丰富。

### 2. 监控和数据分析

| 功能 | EKKO | nesquena | OpenClaw-Admin | Open WebUI |
| --- | --- | --- | --- | --- |
| Token 消耗追踪 | ✅ 完整 | ⚠️ 仅当前会话 | ✅ | ✅ |
| 成本估算 | ✅ | ❌ | ❌ | ✅ |
| 30天趋势图 | ✅ | ❌ | ❌ | ✅ |
| 模型分布 | ✅ | ❌ | ❌ | ✅ |
| 系统资源监控 | ❌ | ❌ | ✅ CPU/内存/磁盘 | ❌ |
| 实时事件流 | ❌ | ❌ | ✅ | ❌ |

**结论**：追求成本分析选 EKKO；追求系统监控选 OpenClaw-Admin。

### 3. 安装和维护门槛

| 方案 | 最低门槛 | 维护难度 |
| --- | --- | --- |
| EKKO | Node.js 18+ | 中等（npm 全局安装） |
| nesquena | Python 3.10+ / Docker | 低（Docker 一键） |
| OpenClaw-Admin | Node.js 18+ | 较高（多组件配置） |
| Open WebUI | Docker | 低（完全容器化） |

**结论**：纯小白用户首选 nesquena WebUI 或 Open WebUI 的 Docker 方案。

### 4. 扩展性和未来空间

| 方案 | 扩展性 | 社区活跃度 | 更新频率 |
| --- | --- | --- | --- |
| EKKO | 中等 | 社区驱动 | 持续更新 |
| nesquena | 高（架构清晰） | 活跃 + 详细贡献者档案 | Sprint 驱动 |
| OpenClaw-Admin | 高（双平台） | 中文社区 | 活跃 |
| Open WebUI | 极高（Pipeline 插件） | 巨型社区 | 高频更新 |

---

## 选择指南：找到你的方案

### 选 EKKOLearnAI/hermes-web-ui 如果：

- 你需要同时运营 Telegram/Discord/Slack 等多个平台的 Bot
- 你对 Token 消耗和成本控制有严格需求
- 你需要 Web 终端但不想开额外 SSH 窗口
- 你追求一站式控制台，所有配置都在一个界面

### 选 nesquena/hermes-webui 如果：

- 你只想要一个干净、好看的聊天界面
- 你是 Python 技术栈，不想碰 Node.js
- 你喜欢 Claude 的三栏布局风格
- 你追求零配置，Docker 一键启动

### 选 itq5/OpenClaw-Admin 如果：

- 你同时在用 OpenClaw 和 Hermes 两个平台
- 你需要管理多个 AI 智能体
- 你需要实时系统监控（CPU/内存/网络）
- 你需要远程桌面功能
- 你更喜欢中文文档和中文社区支持

### 选 open-webui/open-webui 如果：

- 你已经在用 Open WebUI，不想再装新的
- 你需要 RAG、知识库、多模型并行等高级功能
- 你的环境需要 LDAP/SCIM/RBAC 等企业安全功能
- 你希望享受超大规模社区的红利（海量插件、生态成熟）

---

## 实战建议：组合使用

这四套方案不是互斥的，实际上很多进阶用户会**组合使用**：

**推荐组合一**：nesquena WebUI（日常聊天）+ EKKO（渠道管理 + 成本监控）

- nesquena 给你最干净的聊天体验
- EKKO 的渠道配置和数据分析作为管理后台

**推荐组合二**：OpenClaw-Admin（统一管控）+ nesquena WebUI（各平台独立聊天）

- OpenClaw-Admin 负责全局监控和多 Agent 协调
- nesquena 给每个团队成员提供干净的聊天入口

**推荐组合三**：Open WebUI（RAG 能力）+ Hermes 直连（原生功能）

- 用 Open WebUI 的 RAG 和知识库功能
- 需要 Hermes 特有功能（Skill、Channel）时直接用终端

---

## 结语

开源社区很快肝出了四套方案，**Hermes Agent 的能力完全可以通过 Web 界面释放出来，而且体验不输商业软件。**

关键不是选"最好的"，而是选"最对的"。搞清楚自己的核心需求，对号入座：

- **全功能控制**

  → EKKO
- **极简聊天**

  → nesquena
- **多 Agent 运维**

  → OpenClaw-Admin
- **RAG + 企业功能**

  → Open WebUI

命令行是起点，Web 面板是终点。中间的距离，一行 npm install 就够了。

---

**相关仓库直达**：

- EKKOLearnAI/hermes-web-ui: https://github.com/EKKOLearnAI/hermes-web-ui
- nesquena/hermes-webui: https://github.com/nesquena/hermes-webui
- itq5/OpenClaw-Admin: https://github.com/itq5/OpenClaw-Admin
- open-webui/open-webui: https://github.com/open-webui/open-webui
