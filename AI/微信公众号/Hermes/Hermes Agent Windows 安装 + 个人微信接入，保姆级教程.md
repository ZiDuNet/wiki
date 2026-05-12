> 📎 来源: [极智AI智能体研究](https://mp.weixin.qq.com/s?__biz=MzIxODQxNDc4NQ==&mid=2247483993&idx=1&sn=4857cb18d5aa0d83801e66c632c09aac&chksm=96f5cd7c3424357af1a1dacf65294188e05bb4e9f36ff4e4db8bef516899474e91ae97ec9d2b&mpshare=1&scene=1&srcid=0423PsRMUiKsaJWCZH594K5Z&sharer_shareinfo=20201b851345a7822152c6fb70cbeb77&sharer_shareinfo_first=20201b851345a7822152c6fb70cbeb77) | 时间: 2026-04-23 21:47

---

> 最近 GitHub 上爆火的开源 AI Agent——**Hermes Agent**，凭借"自我进化、自带长期记忆、自动沉淀技能"三大核心能力，直接对标 OpenClaw。更关键的是，它原生支持接入个人微信，让你的 AI 助手真正变成随时可用的微信机器人。

> 今天手把手教你在 Windows 上从零安装，并接入个人微信，实现 AI 自动回复。

---

## 一、Hermes Agent 是什么？

Hermes Agent 是一款**开源、自托管的 AI Agent**，采用 MIT 许可证，核心目标是打造一个**越用越懂你的私人 AI 员工**。它不是简单的聊天机器人，而是一个具备长期记忆、自动学习、工具调用能力的智能体框架。

**GitHub 仓库**：

```
NousResearch/hermes-agent
```

与 OpenClaw 等同类产品相比，Hermes 的独特优势在于：

| 对比项 | Hermes Agent 优势 |
| --- | --- |
| Token 消耗 | 上下文组织更紧凑，比 OpenClaw 低约 **30%** |
| 过程透明度 | 任务推进步骤清晰可见，用户全程可感知 |
| 自我进化 | 将执行经验自动沉淀为长期记忆和可复用技能 |
| 迁移便利 | 提供   ``` hermes claw migrate ```   一键从 OpenClaw 迁移 |
| 环境隔离 | 支持   ``` hermes profile ```   做工作/个人/测试多环境切换 |

---

## 二、核心功能详解

### 2.1 长期记忆与自我进化

这是 Hermes 区别于普通 AI 聊天工具的最大亮点。

**长期记忆（Persistent Memory）**

- 所有历史会话存储在本地 SQLite 数据库中，支持全文检索
- 跨会话记住你的项目结构、代码习惯、偏好设置
- 不像普通聊天窗口，关掉就全忘了

**自动沉淀技能（Auto Skills）**

- 当 Hermes 成功完成一个复杂任务后，会自动将解决经验固化为 **Skill 文件**
- 下次遇到类似任务，直接复用已有技能，效率指数级提升
- 越用越懂你，真正做到"经验积累"

**举个实际例子**：你让 Hermes 帮你写一份财报分析报告，它第一次可能要摸索格式和数据来源；第二次你再提类似需求，它会直接调用上次沉淀的技能，几分钟搞定。

### 2.2 多模型灵活切换

Hermes 支持 **200+ 种大模型**，不绑定任何一家厂商，随时切换：

| 类别 | 支持的模型 |
| --- | --- |
| 国内模型 | 通义千问（Qwen）、智谱（GLM）、Kimi（Moonshot）、MiniMax、DeepSeek |
| 海外模型 | Claude、GPT、Gemini、Codex |
| 其他 | OpenRouter 中转站、本地 Ollama 部署模型、任何 OpenAI 兼容接口 |

切换模型只需一条命令：

**bash**

**hermes model**

交互式选择即可，零门槛。

### 2.3 消息平台接入

这是 Hermes 最受欢迎的功能之一——**让你的 AI 助手住进你常用的聊天工具里**。

| 类别 | 支持的平台 |
| --- | --- |
| 即时通讯 | **Telegram** 、Discord、Slack、WhatsApp、Signal |
| 国内平台 | **个人微信** 、企业微信、飞书、钉钉 |
| 其他 | Email |

接入后你可以随时随地通过微信、飞书、Telegram 等跟你的 AI 助手对话，它依然具备完整的记忆和能力，不受平台限制。

### 2.4 内置 40+ 工具

Hermes 不是只会"说话"的 AI，它自带丰富的工具集，可以真正"做事"：

| 工具类别 | 具体能力 |
| --- | --- |
| 终端操作 | 执行 Shell 命令、安装软件、管理文件 |
| 文件系统 | 读写文件、搜索代码、批量操作 |
| 浏览器控制 | 自动填表、抓取网页、截图、数据提取 |
| 图片与视觉 | 图片生成、截图分析、OCR |
| TTS 语音 | 文本转语音（依赖 ffmpeg） |
| 代码开发 | 编写、调试、重构代码 |

### 2.5 MCP 协议支持

MCP（Model Context Protocol）是 AI 工具调用的标准化协议。Hermes 原生支持 MCP，意味着你可以接入海量第三方工具：

- 接入数据库工具（查询 MySQL、PostgreSQL）
- 接入 API 工具（调用外部服务）
- 接入文件工具（操作 Google Drive、Notion 等）
- 接入专业领域工具（金融数据、法律检索等）

MCP 让 Hermes 的能力边界几乎无限扩展。

### 2.6 定时自动化（Cron）

内置 Cron 调度器，支持设置定时任务，让 AI 主动干活：

| 场景 | 示例 |
| --- | --- |
| 日报生成 | 每天早上 9 点自动汇总行业新闻 |
| 文件备份 | 每周自动备份指定目录 |
| 网站监控 | 每小时检查目标网站是否更新 |
| 信息抓取 | 定时采集竞品价格、社交媒体舆情 |
| 提醒服务 | 定时发送会议提醒、待办事项 |

配置文件位于 

```
~/.hermes/cron/
```

 目录。

### 2.7 沙箱与安全隔离

| 特性 | 说明 |
| --- | --- |
| 容器隔离 | 工具执行可在沙箱容器中运行，保护宿主系统 |
| 命令审批 | 敏感操作需用户确认后才执行 |
| 自托管 | 所有数据存储在本地，隐私完全可控 |
| Web 管理界面 | 通过   ``` http://127.0.0.1:9119 ```   可视化管理一切 |

### 2.8 研究与训练支持

Hermes 还面向 AI 研究者提供了高级功能：

- **批量轨迹生成与压缩**

  ：自动记录 Agent 执行轨迹，可用于训练下一代 tool-calling 模型
- **Atropos RL 环境**

  ：内置强化学习训练环境
- **多模型推理**

  ：同一任务可调用多个模型协同推理

---

## 三、实际使用场景

理解了功能，来看看 Hermes 能在你的工作和生活中做什么：

| 场景 | 具体用法 |
| --- | --- |
| **个人 AI 编程助手** | 记住你的代码风格和项目结构，自动调用常用函数库 |
| **微信智能客服** | 接入个人微信，自动回复消息、处理常见咨询 |
| **远程操控助手** | 通过微信/Telegram 随时随地发指令，AI 帮你执行 |
| **定时信息监控** | 每天自动抓取行业新闻、竞品动态、股价变动 |
| **团队共享助手** | 接入 Slack/Discord 群组，整个团队共用一个 AI 助手 |
| **网页自动化** | 自动填表、批量抓取数据、监控价格变动 |
| **文档与报告** | 自动生成周报、财报分析、行业研究报告 |
| **学习研究** | 保存任务执行轨迹，形成个人知识库 |

---

## 四、环境准备

### 4.1 前置要求

| 项目 | 要求 |
| --- | --- |
| 操作系统 | Windows 10 / 11 |
| Python | 无需预装，安装脚本自动处理 |
| Node.js | 无需预装，安装脚本自动处理 |
| 模型 API | 至少一个 64K 上下文的模型 API Key |
| 费用预估 | 3.99 美元即可上手 |

### 4.2 两种安装方式

| 方案 | 适用人群 | 优点 | 缺点 |
| --- | --- | --- | --- |
| **方案 A：PowerShell 原生安装** | 快速体验、简单上手 | 无需装 WSL，一条命令搞定 | 部分高级功能可能受限 |
| **方案 B：WSL2 安装（推荐）** | 长期使用、功能完整 | 完整 Linux 环境，功能 100% 兼容 | 需先配置 WSL2 |

---

## 五、方案 A：PowerShell 一键安装

**适合想快速体验的用户。**

打开 Windows PowerShell（管理员），执行：

**powershell**

**irm https://res1.hermesagent.org.cn/install.ps1 | iex**

安装完成后，直接跳到 **第六部分：配置模型**。

---

## 六、方案 B：WSL2 完整安装（推荐长期使用）

### 6.1 启用 WSL2

以**管理员身份**打开 PowerShell，依次执行：

**powershell**

**# 启用 Windows 子系统 Linux 功能
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 启用虚拟机平台功能（WSL 2 必需）
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart**

> ⚠️ 执行完成后，**必须重启计算机**。

### 6.2 设置 WSL2 为默认版本

重启后，打开 PowerShell 执行：

**powershell**

**wsl --set-default-version 2**

### 6.3 安装 Ubuntu 发行版

**powershell**

**wsl --install -d Ubuntu-24.04**

> 安装完成后会弹出 Ubuntu 窗口，设置用户名和密码（记住密码，后续 sudo 会用到）。

### 6.4 更新系统并安装 Git

进入 Ubuntu 终端，执行：

**bash**

**sudo apt update && sudo apt upgrade -y
sudo apt install git -y**

### 6.5 一键安装 Hermes Agent

**bash**

**curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash**

安装脚本会自动处理以下依赖：

| 依赖项 | 说明 |
| --- | --- |
| uv | 快速 Python 包管理器 |
| Python 3.11 | 通过 uv 安装，无需 sudo |
| Node.js v22 | 浏览器自动化所需 |
| ripgrep | 快速文件搜索 |
| ffmpeg | TTS 音频格式转换 |

### 6.6 验证安装

**bash**

**# 重新加载 Shell 配置
source ~/.bashrc

# 验证版本
hermes --version**

看到 

```
Hermes Agent v0.x.x
```

 字样即安装成功 ✅

---

## 七、配置 AI 模型

### 7.1 运行配置向导

**bash**

**hermes setup**

### 7.2 配置步骤

按引导提示操作：

1. **选择 LLM 提供商**

   — 推荐选择 

   ```
   Custom endpoint (OpenAI compatible)
   ```

    或 

   ```
   OpenRouter
   ```
2. **输入 API Base URL**

   — 填入对应平台的 API 地址（见下方列表）
3. **输入 API Key**

   — 粘贴你的 Key（

   ```
   sk-
   ```

    开头）
4. **选择默认模型**

   — 选一个性价比高的模型

**常用 API 地址速查：**

| 提供商 | API Base URL | 推荐模型 |
| --- | --- | --- |
| 智谱 GLM | ``` https://open.bigmodel.cn/api/paas/v4 ``` | glm-5.1 |
| 通义千问 | ``` https://dashscope.aliyuncs.com/compatible-mode/v1 ``` | qwen-max |
| DeepSeek | ``` https://api.deepseek.com/v1 ``` | deepseek-chat |
| Kimi | ``` https://api.moonshot.cn/v1 ``` | moonshot-v1-128k |
| MiniMax | ``` https://api.minimax.chat/v1 ``` | abab7 |
| OpenRouter | ``` https://openrouter.ai/api/v1 ``` | 按需选择 |

### 7.3 手动编辑配置（可选）

**bash**

**nano ~/.hermes/config.yaml**

**yaml**

**model:
provider:custom
base\_url:https://open.bigmodel.cn/api/paas/v4
api\_key:sk-xxxxxxx
default:glm-5.1**

> ⚠️ URL 和 API Key 不能有多余空格，必须完整复制。

### 7.4 随时切换模型

**bash**

**hermes model**

### 7.5 测试对话

**bash**

**hermes**

进入欢迎界面后发一条消息测试，能正常回复即配置成功 ✅

---

## 八、接入个人微信

> Hermes Agent 通过腾讯官方 iLink Bot API 接入微信，**非第三方破解协议**，安全性有保障。

### 8.1 安装微信相关依赖

**bash**

**pip install aiohttp cryptography
pip install qrcode**

> - ```
>   aiohttp
>   ```

>   + 

>   ```
>   cryptography
>   ```

>   ：**必装**，微信 CDN 使用 AES-128-ECB 加密，缺了会导致图片收发失败
> - ```
>   qrcode
>   ```

>   ：推荐安装，让二维码直接显示在终端

### 8.2 运行微信网关配置向导

**bash**

**hermes gateway setup**

### 8.3 配置步骤

**① 选择平台** — 选择 

```
Weixin
```

**② 扫码登录** — 终端自动显示二维码，用手机微信扫码确认

> 如果终端二维码渲染失败，系统会提示一个链接，在浏览器中打开即可获取二维码。

**③ 私聊授权方式**

| 选项 | 说明 |
| --- | --- |
| ✅ 推荐 | ``` Use DM pairing approval ```   — 私聊配对审批 |
| 其他 | 允许所有私聊 / 仅允许列出的用户ID / 禁用私聊 |

**④ 群聊处理方式**

| 选项 | 说明 |
| --- | --- |
| ✅ 推荐 | ``` Disable group chats ```   — 禁用群聊 |
| 其他 | 允许所有群聊 / 仅允许列出的群聊ID |

**⑤ 确认并重启** — 输入 

```
Y
```

，系统自动重启网关服务

成功后终端提示：

```
微信连接成功，account_id=your-account-id
```

 ✅

账号凭证自动保存在 

```
~/.hermes/weixin/accounts/
```

 目录。

### 8.4 环境变量配置（可选）

如需精细权限控制，编辑 

```
~/.hermes/.env
```

：

**env**

**# 基础配置（必填）
WEIXIN\_ACCOUNT\_ID=your-account-id

# 限定只有特定用户能私聊 Bot
WEIXIN\_DM\_POLICY=allowlist
WEIXIN\_ALLOWED\_USERS=user\_id\_1,user\_id\_2

# 开启群消息（默认关闭）
WEIXIN\_GROUP\_POLICY=allowlist
WEIXIN\_GROUP\_ALLOWED\_USERS=group\_id\_1**

### 8.5 启动微信网关

**bash**

**hermes gateway**

启动后，在手机微信给 Bot 发消息，几秒内即可收到 AI 回复 ✅

---

## 九、日常使用与管理

### 9.1 常用命令速查

| 命令 | 功能 |
| --- | --- |
| ``` hermes ``` | 启动 TUI 对话界面 |
| ``` hermes model ``` | 切换 AI 模型 |
| ``` hermes setup ``` | 重新运行配置向导 |
| ``` hermes gateway setup ``` | 配置消息网关 |
| ``` hermes gateway ``` | 启动消息网关 |
| ``` hermes update ``` | 更新到最新版本 |
| ``` hermes doctor ``` | 检查安装和配置状态 |
| ``` hermes dashboard ``` | 启动 Web 管理界面 |
| ``` hermes claw migrate ``` | 从 OpenClaw 一键迁移 |
| ``` hermes profile ``` | 多环境配置隔离 |

### 9.2 Web 管理界面

**bash**

**hermes update
hermes dashboard**

浏览器访问 

```
http://127.0.0.1:9119
```

，可以：

- 📊 管理 Agent 运行状态
- 💬 查看所有会话历史
- 📈 分析 Token 用量和费用
- ⏰ 管理定时任务
- 🔧 技能开关管理
- 🔑 可视化配置 API Key

---

## 十、常见问题排查

| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 二维码不显示 | 缺少 qrcode 库 | ``` pip install qrcode ``` |
| 图片收发失败 | 缺少 cryptography 库 | ``` pip install aiohttp cryptography ``` |
| 掉线（错误码 -14） | Session 过期 | 重新执行   ``` hermes gateway setup ```   扫码 |
| Token 冲突报错 | 一个 token 运行了多个 poller | 先停掉另一个进程 |
| AI 不回复 | 模型未响应 / 网关未启动 | 检查 API Key、运行   ``` hermes doctor ``` |
| 长消息截断 | 微信单条上限 4000 token | 正常分段，系统自动处理 |
| 空响应 | Base URL 或 API Key 错误 | 检查 config.yaml 配置 |
| 安装脚本报错 | 网络问题 / Git 未安装 | 检查网络、执行   ``` sudo apt install git ``` |

---

## 十一、注意事项

1. **⚠️ 建议先用微信小号测试**

   ，确认稳定后再考虑主号
2. 微信只能链接一个 Agent，如已绑定 OpenClaw 等工具，需先解绑
3. 保持终端运行，退出终端会导致 Bot 停止；如需 7×24 运行，建议部署到 VPS
4. 项目迭代很快，定期执行 

   ```
   hermes update
   ```

    保持最新版本
5. 定时任务配置文件位于 

   ```
   ~/.hermes/cron/
   ```

    目录

---

## 十二、相关链接

| 资源 | 地址 |
| --- | --- |
| GitHub 仓库 | ``` github.com/NousResearch/hermes-agent ``` |
| 中文文档站 | ``` hermesagent.org.cn ``` |
| OpenRouter | ``` openrouter.ai ``` |
| 智谱开放平台 | ``` open.bigmodel.cn ``` |
| DeepSeek | ``` platform.deepseek.com ``` |

---

*本文综合整理自 Hermes Agent 官方文档及社区教程，具体以官方最新版本为准。*
