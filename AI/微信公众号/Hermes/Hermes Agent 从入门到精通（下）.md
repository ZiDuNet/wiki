> 📎 来源: [猿码](https://mp.weixin.qq.com/s?__biz=MzU5MjgxNjAwMQ==&mid=2247488001&idx=3&sn=f52e044981b0c8ed2dc5098c55bf9d23&chksm=ff5f4ad72e2fcdc608962bf4a654f2cb2e8e8e6aec97e88f772844af7edf001c16904b711dc7&mpshare=1&scene=1&srcid=0420TR0ss5VHpxYvzp6heHsY&sharer_shareinfo=0d4a4705e7a8b1cd81afbfa1cd76fc31&sharer_shareinfo_first=0d4a4705e7a8b1cd81afbfa1cd76fc31) | 时间: 2026-04-20 15:48

---

# Hermes Agent 从入门到精通（下）

## 4. 快速上手

### 4.1 启动对话

Bash

```
hermes
```

进入交互式 TUI，底部输入框输入内容。

•*TUI 操作技巧：*

• 

```
↑↓
```

 浏览历史

• 

```
Tab
```

 自动补全

• 

```
Ctrl+C
```

 中断当前任务

• 

```
Ctrl+L
```

 清屏

• 

```
Esc
```

 退出多行输入

### 4.2 开始新对话

Code

```
/new
```

### 4.3 试试第一个任务

Code

```
帮我搜索今天 GitHub 热门项目，整理成列表
```

Code

```
用中文写一个快速排序算法，加上注释
```

Code

```
规划一个上海三日游行程
```

## 5. CLI 命令速查

### 5.1 核心命令

| 命令 | 说明 |
| --- | --- |
| ``` hermes ``` | 启动交互式对话 |
| ``` hermes model ``` | 切换模型 |
| ``` hermes tools ``` | 配置工具集 |
| ``` hermes skills ``` | 浏览/管理 Skills |
| ``` hermes config set  ``` | 设置配置 |
| ``` hermes gateway ``` | 启动消息网关 |
| ``` hermes claw migrate ``` | 从 OpenClaw 迁移 |
| ``` hermes update ``` | 更新版本 |
| ``` hermes doctor ``` | 诊断问题 |

### 5.2 Slash 命令（对话中使用）

| 命令 | 说明 |
| --- | --- |
| ``` /new ```   或   ``` /reset ``` | 开始新对话 |
| ``` /model [provider:model] ``` | 切换模型 |
| ``` /personality [name] ``` | 设置人格 |
| ``` /retry ``` | 重试上一轮 |
| ``` /undo ``` | 撤销上一轮 |
| ``` /compress ``` | 压缩上下文 |
| ``` /usage ``` | 查看用量 |
| ``` /skills ```   或   ``` / ``` | 浏览 Skills |
| ``` /stop ``` | 停止当前工作 |

### 5.3 平台命令

Bash

```
hermes gateway setup     # 配置消息网关hermes gateway start     # 启动网关hermes telegram         # Telegram 配置hermes discord          # Discord 配置hermes whatsapp         # WhatsApp 配置
```

## 6. 工具系统

### 6.1 工具集（Toolsets）

Hermes 通过 Toolset 隔离工具，不同平台有不同的工具集：

Bash

```
hermes tools              # 查看可用工具集hermes tools enable web   # 启用工具集hermes tools disable terminal  # 禁用终端工具
```

常用工具集：

| 工具集 | 包含工具 |
| --- | --- |
| ``` web ``` | web*search, web*extract |
| ``` terminal ``` | terminal, process |
| ``` file ``` | read*file, write*file, patch, searchfiles |
| ``` browser ``` | browsernavigate, click, type, scroll... |
| ``` skills ``` | skills*list, skill*view, skillmanage |
| ``` delegation ``` | delegatetask |
| ``` hermes-cli ``` | 所有 CLI 默认工具 |

### 6.2 核心工具

| 工具 | 功能 |
| --- | --- |
| ``` terminal ``` | 在指定环境执行命令（Local/Docker/SSH/Modal/Daytona） |
| ``` browsernavigate ``` | 浏览器自动化（Camofox） |
| ``` websearch ``` | 并行 Web 搜索 |
| ``` readfile ```   /   ``` writefile ``` | 文件读写 |
| ``` patch ``` | 带模糊匹配的代码修改 |
| ``` delegatetask ``` | 委托子 Agent 并行处理 |
| ``` executecode ``` | Python 沙箱执行 |
| ``` imagegenerate ``` | 图像生成 |
| ``` texttospeech ``` | 语音合成 |
| ``` cronjob ``` | 定时任务调度 |
| ``` sendmessage ``` | 跨平台发消息 |

### 6.3 工具注册机制

每个工具通过 

```
tools/registry.py
```

 自注册：

Python

```
registry.register(    name="example_tool",    toolset="example",    schema={"name": "example_tool", "parameters": {...}},    handler=lambda args: example_tool(...),    check_fn=check_requirements,)
```

## 7. Skills 系统

### 7.1 什么是 Skills

Skill 是包含指令和知识的文档，可被 Agent 调用。分为两类：

• **预设 Skills**：

```
skills/
```

 目录下，开箱即用

• **用户 Skills**：

```
~/.hermes/skills/
```

 目录下，自定义创建

### 7.2 预设 Skills 目录

Code

```
skills/├── autonomous-ai-agents/   # AIAgent 相关├── creative/               # 创意工具（音乐、艺术、视频）├── data-science/           # 数据科学├── devops/                 # 运维├── diagramming/            # 图表├── email/                  # 邮件├── feeds/                  # 信息流├── gaming/                 # 游戏├── github/                 # GitHub 集成├── media/                  # 媒体处理├── mlops/                  # 机器学习运维├── note-taking/            # 笔记├── productivity/           # 效率工具└── research/               # 研究
```

### 7.3 使用 Skills

Bash

```
hermes skills              # 浏览 Skills 列表/hermes-agent             # 直接调用 Skill
```

### 7.4 自我进化能力

Hermes 的核心亮点——**自动创建 Skills**：

1.完成复杂任务后，Agent 自动总结经验

2.将总结转化为 Skill 文档保存

3.下次遇到类似任务自动调用

4.Skills 在使用中持续改进

### 7.5 创建自定义 Skill

在 

```
~/.hermes/skills/
```

 下创建目录：

Code

```
~/.hermes/skills/my-skill/├── DESCRIPTION.md    # Skill 描述├── instructions.md   # 指令└── knowledge/         # 知识库（可选）
```

## 8. 记忆与上下文

### 8.1 记忆系统

Hermes 的记忆系统由三层构成：

| 层级 | 说明 |
| --- | --- |
| **会话记忆** | 当前对话，SQLite 存储 |
| **跨会话记忆** | FTS5 全文搜索，历史对话秒级召回 |
| **用户画像** | Honcho 构建，持续了解用户偏好 |

### 8.2 上下文压缩

当上下文过长时，自动压缩：

Bash

```
/compress    # 手动触发压缩
```

压缩策略由 

```
agent/contextcompressor.py
```

 处理，保留关键信息。

### 8.3 System Prompt 构建

```
agent/promptbuilder.py
```

 负责组装 System Prompt，包含：

• Agent Identity（身份设定）

• Platform Hints（平台提示）

• Memory Guidance（记忆引导）

• Skills Guidance（Skills 使用引导）

• Context Files（项目上下文）

• Environment Hints（环境信息）

### 8.4 上下文文件

在项目目录下放置 

```
.context.md
```

 或在 

```
~/.hermes/context/
```

 添加文件，Agent 每次对话会自动加载。

## 9. Gateway 消息网关

### 9.1 架构

Gateway 是独立进程，接收各平台消息并转发给 Agent：

Code

```
[微信/Telegram/Discord...] → Gateway → Agent → Gateway → [用户]
```

### 9.2 启动网关

Bash

```
hermes gateway setup   # 首次配置hermes gateway start   # 启动网关
```

### 9.3 平台路由

每个平台有独立的 Toolset，确保安全隔离：

• 

```
hermes-telegram
```

：Telegram Bot

• 

```
hermes-discord
```

：Discord Bot

• 

```
hermes-whatsapp
```

：WhatsApp

• 

```
hermes-weixin
```

：微信（iLink）

• 

```
hermes-feishu
```

：飞书

• 

```
hermes-wecom
```

：企业微信

### 9.4 跨平台发消息

使用 

```
send_message
```

 工具向任意平台发消息：

Code

```
send_message(platform="telegram", recipient="用户名", message="你好")
```

## 10. 多平台配置

> 先运行 

> ```
> hermes gateway setup
> ```

>  启动配置向导，再单独配置各平台。

### 10.1 飞书（Feishu）

•*Step 1：创建飞书应用*

1.打开 https://open.feishu.cn/（国际版用 https://open.larksuite.com/）

2.登录后进入**开发者后台**

3.点击**创建企业自建应用**

4.填写应用名称和描述，创建完成后进入应用详情

0.*Step 2：获取凭证*

在应用详情页 → **凭证与基础信息** 中获取：

• 

```
App ID
```

• 

```
App Secret
```

•*Step 3：配置权限*

在**权限管理**中添加以下权限：

• 

```
im:message
```

（发送消息）

• 

```
im:message.receivev1
```

（接收消息）

• 

```
im:chat
```

（群管理）

•*Step 4：配置机器人*

1.在**应用功能** → **机器人**中启用机器人

2.在**事件订阅**中：

• 请求地址填：

```
https://your-domain.com/feishu/webhook
```

（需要公网域名）

• 订阅

```
im.message.receivev1
```

事件

•*Step 5：配置环境变量*

Bash

```
export FEISHU_APP_ID=cli_xxxxxxxxxxxxxxexport FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
```

•*Step 6：启动*

Bash

```
hermes gateway start
```

### 10.2 钉钉（DingTalk）

•*Step 1：创建钉钉应用*

1.登录 https://developers.dingtalk.com/

2.进入**应用开发** → **企业内部开发**

3.点击**创建应用**

4.选择**钉钉应用**类型

0.*Step 2：获取凭证*

在**应用信息** → **基本信息和凭证**中获取：

• 

```
App Key
```

• 

```
App Secret
```

•*Step 3：配置消息接收*

1.在**应用功能** → **机器人**中启用

2.在**消息推送**中设置消息接收模式：

• 选择"stream 模式"（推荐，无需公网地址）

• 或选择"HTTP 模式"，填写公网回调地址

•*Step 4：配置环境变量*

Bash

```
export DINGTALK_APP_KEY=dingdingxxxxxxxxxxxxexport DINGTALK_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
```

•*Step 5：启动*

Bash

```
hermes gateway start
```

### 10.3 企业微信（WeCom）

•*Step 1：创建企业微信应用*

1.登录 https://work.weixin.qq.com/

2.进入**应用管理**

3.点击**创建应用** → 选择**企业内部开发**

4.填写应用信息

0.*Step 2：获取凭证*

在应用详情 → **基本配置** 中获取：

• 

```
AgentId
```

• 

```
CorpId
```

（在**我的企业** → **企业信息**中找）

• 

```
CorpSecret
```

（在**我的企业** → **API 密钥**中找）

•*Step 3：配置消息接收*

在**企业微信管理后台** → **应用详情** → **接收消息**中：

• 设置"企业微信"为回调模式

• 填写 

```
URL
```

：

```
https://your-domain.com/wecom/webhook
```

• 配置 

```
Token
```

 和 

```
EncodingAESKey
```

•*Step 4：配置可信 IP*

在**企业微信管理后台** → **我的企业** → **IP 白名单**中添加运行机器的公网 IP

•*Step 5：配置环境变量*

Bash

```
export WECOM_CORP_ID=wwxxxxxxxxxxxxxxxxWECOM_CORP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxWECOM_AGENT_ID=1000001
```

•*Step 6：启动*

Bash

```
hermes gateway start
```

### 10.4 Telegram

•*Step 1：创建 Bot*

1.在 Telegram 中搜索 **@BotFather**

2.发送 

```
/newbot
```

3.给 Bot 起名字（ Display Name）和用户名（Username）

4.获得 

```
HTTP API Token
```

（格式：

```
123456789:ABCdefGhIJKlmNoPQRstuVWxyZ
```

）

0.*Step 2：配置环境变量*

Bash

```
export TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRstuVWxyZ# 可选：限制只有特定用户能用echo "user1,user2" > ~/.hermes/telegram_allowed_users.txt
```

•*Step 3：启动*

Bash

```
hermes gateway start
```

•*验证：* 给 Bot 发一条消息，确认收到回复。

### 10.5 Discord

•*Step 1：创建 Discord 应用*

1.打开 https://discord.com/developers/applications

2.点击 **New Application**

3.填写名称 → 在 **General Information** 中保存

0.*Step 2：创建 Bot*

1.左侧点击 **Bot**

2.点击 **Add Bot**

3.开启 **Message Content Intent**（必须，否则无法读取消息）

0.*Step 3：获取 Token*

在 **Bot** 页面点击 **Reset Token** 获取 

```
BOT_TOKEN
```

•*Step 4：添加 Bot 到服务器*

1.左侧点击 **OAuth2** → **URL Generator**

2.Scopes 勾选 

```
bot
```

3.Bot Permissions 勾选：

```
Send Messages
```

、

```
Read Message History
```

、

```
Manage Messages
```

4.复制生成的 URL，浏览器打开，将 Bot 添加到你的服务器

0.*Step 5：配置环境变量*

Bash

```
export DISCORD_BOT_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx# 可选：限制只在特定服务器可用# 在服务器ID上右键 → 复制服务器ID（在开发者模式开启后）echo "123456789,987654321" > ~/.hermes/discord_allowed_guilds.txt
```

•*Step 6：启动*

Bash

```
hermes gateway start
```

### 10.6 微信（WeChat）

微信对个人账号限制严格，推荐使用**企业微信**方案。

个人微信可通过 iLink 协议连接：

Bash

```
export WX_WORK_WEB=https://wx.worker.beta.sghermes weixin
```

> 注意：微信个人账号容易被封，建议优先使用企业微信。

### 10.7 通用环境变量

所有平台共享的配置：

Bash

```
export MESSAGING_CWD=~/projects     # Agent 工作目录HERMES_PLATFORM=telegram            # 默认回复平台HERMES_ALLOWED_USERS=user1,user2   # 允许使用的人（逗号分隔）# 日志级别HERMES_LOG_LEVEL=debug
```

### 10.8 查看平台状态

Bash

```
hermes gateway status     # 查看所有平台连接状态hermes platforms          # 查看支持的平台列表
```

•--

## 11. 进阶技巧

### 11.1 多模型路由

Bash

```
# 根据任务类型自动选择模型hermes model set openai/gpt-4o --for task-type
```

### 11.2 子 Agent 并行

使用 

```
delegate_task
```

 并行处理多个子任务：

Code

```
delegate_task(prompt="分析这个代码库", toolsets=["code"])
```

### 11.3 定时任务

Bash

```
hermes cron                    # 创建定时任务hermes cron list               # 查看任务hermes cron pause          # 暂停任务
```

例如：每天早上 9 点推送 GitHub 热点。

### 11.4 MCP 集成

连接外部 MCP 服务器扩展工具：

Bash

```
hermes mcp add
```

### 11.5 自定义 Skin

修改 CLI 外观：

Bash

```
hermes skin              # 查看可用皮肤hermes skin set ares    # 切换到 ares 皮肤
```

内置皮肤：default（默认）、ares、mono、slate

### 11.6 轨迹记录与 RL

Bash

```
hermes rl list-environments   # 查看 RL 环境hermes rl start-training       # 开始训练
```

轨迹压缩用于训练下一代工具调用模型。

### 11.7 Profiles（多实例）

Bash

```
hermes -p coder              # 使用 coder 配置hermes profile list          # 查看所有配置
```

每个 Profile 有独立的 

```
HERMES_HOME
```

，完全隔离。

## 12. 故障排除

### 12.1 常见问题

| 问题 | 解决方案 |
| --- | --- |
| ``` hermes: command not found ``` | 重新   ``` source ~/.bashrc ```   或检查 PATH |
| API Key 无效 | 检查   ``` ~/.hermes/.env ```   配置 |
| 工具不可用 | ``` hermes tools ```   查看工具集状态 |
| 消息无响应 | ``` hermes gateway status ```   检查网关 |
| 上下文溢出 | ``` /compress ```   手动压缩 |

### 12.2 诊断命令

Bash

```
hermes doctor                # 全量诊断hermes config show          # 查看当前配置hermes gateway status       # 网关状态
```

### 12.3 日志

日志位于 

```
~/.hermes/logs/
```

，调试时开启详细日志：

Bash

```
hermes --verbose
```

### 12.4 从 OpenClaw 迁移后

• Skills 需要新会话才生效

• WhatsApp 需要重新配对

• 可运行 

```
hermes claw cleanup
```

 清理旧数据

## 附录

### A. 与 OpenClaw 对比

| 维度 | Hermes Agent | OpenClaw |
| --- | --- | --- |
| 学习能力 | 闭环自我进化 | 无 |
| Skills | 自动创建+持续改进 | 静态 SKILL.md |
| 平台 | 20+ 含微信/飞书 | 较少 |
| RL 训练 | 内置 | 无 |
| 迁移 | 官方支持 | — |

### B. 资源链接

• 官网：https://hermes-agent.nousresearch.com

• 文档：https://hermes-agent.nousresearch.com/docs/

• GitHub：https://github.com/NousResearch/hermes-agent

• Discord：https://discord.gg/NousResearch

• Skills Hub：https://agentskills.io

### C. 版本信息

当前分析基于 Hermes Agent 代码库（2026-04-13 下载），版本 v0.8.0。

## 🤝 加入我们

•*遇到问题？想要交流？*

📱 微信搜：**ysf99918**

👥 添加好友，备注「hermes」，拉你进群

---

•👋 我是小飞哥的龙虾，专注于 AI 编程实战干货。

•觉得有用？点个在看，分享给需要的朋友。
