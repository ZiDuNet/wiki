> 📎 来源: [猿码](https://mp.weixin.qq.com/s?__biz=MzU5MjgxNjAwMQ==&mid=2247488075&idx=2&sn=89029b061ba3ca7e5e9c56ddaf08c866&chksm=ff368ee9495b39d68b1347432ffdb2330e3fe659112f8d693b1df3e45d08f9ea0eb0c512ead7&mpshare=1&scene=1&srcid=0422LTHUceocJFT8m8lgodeA&sharer_shareinfo=7d918c3e12f62a579cdbc6422237387e&sharer_shareinfo_first=7d918c3e12f62a579cdbc6422237387e) | 时间: 2026-04-22 17:35

---

# 🚀 Hermes Agent 中文新手指南 | AI 编码助手来了！

> 📦 开源免费 | ⚡ 即装即用 | 🤖 支持多平台

## 🤖 Hermes Agent 是什么？

> **Hermes Agent**

> 是 Nous Research 开发的一个开源 AI Agent 框架，可以在终端、消息平台和 IDE 中运行。
> 与 **Claude Code、Codex、OpenClaw** 属于同一类产品——通过工具调用与系统交互的自主编码 Agent ✨

## 💪 Hermes 能做什么？

### 🧑‍💻 编程开发

•写代码、改 Bug、重构、写测试

•Git 操作（创建分支、提交代码、合并 PR）

•项目构建和部署

### 📁 文件处理

•读写文件、批量修改

•搜索文件内容（比 grep 更智能）

•生成项目结构、处理文档

### 🌐 网页与研究

•搜索网页并提取信息

•读论文、整理资料

•做竞品分析、写市场调研报告

### ⚙️ 系统运维

•执行 Shell 命令

•管理进程和服务

•部署应用、监控日志

### ⏰ 定时自动化

•每天定时执行任务

•定期生成报告

•设置提醒

> **📌 示例：每天早上 9 点发送天气提醒**

> Bash

> ```
> > hermes cron create "09 * * *" --prompt "查询北京天气，发送到我的邮箱"
> ```

### 💬 消息平台 Bot

•**Telegram** — 随时随地用手机问 Hermes

•**Discord** — 在 Discord 服务器里当助手

•**邮件** — 发送邮件、定时报告

•**WhatsApp** — 像发消息一样对话

### 🎙️ 语音交互

•发送语音消息，自动转文字

•让 Hermes 语音回复你

•支持 Edge TTS（免费）、Kokoro（免费）、ElevenLabs（效果更好）

### 🧠 记忆与学习

•跨会话记住你的偏好

•保存常做的事成"技能"一键调用

•记住项目背景，下次直接上手

### 👥 多 Agent 协作

让多个 Agent 同时工作，分工合作：

Code

```
# Agent A 做后端tmux new-session -d -s backend 'hermes -w'tmux send-keys -t backend 'Build a RESTAPIwithFastAPI' Enter# Agent B 做前端tmux new-session -d -s frontend 'hermes -w'tmux send-keys -t frontend 'Build a React dashboard' Enter
```

## 🚀 5 分钟快速上手

### 第一步：安装（1 分钟）

> Bash

> ```
> > curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
> ```

### 第二步：配置模型（2 分钟）

> Bash

> ```
> > hermes setup
> ```

> 选择 

> ```
> model
> ```

>  按提示配置，或直接：

> Bash

> ```
> > hermes model
> ```

> 然后选择你的 API 提供商，填入 API Key。

### 第三步：开始对话

> Bash

> ```
> > hermes
> ```

> 直接输入你的问题，例如：

> Code

> ```
> > 帮我写一个计算器程序
> ```

> 💡 **Tip:** 安装后先用 

> ```
> hermes chat -q "..."
> ```

>  体验单次查询，觉得好用再 

> ```
> hermes
> ```

>  进入交互模式 ✨

## 🎯 新手必试的 5 个任务

| 任务 | 命令 |
| --- | --- |
| 🧑‍💻 帮你写代码 | ``` hermes chat -q "写一个读取 CSV 文件并统计每列平均值的 Python 脚本" ``` |
| 📖 解释代码 | ``` hermes chat -q "帮我解释这段代码的作用：[粘贴代码]" ``` |
| 🔍 搜索资料 | ``` hermes chat -q "搜索并总结最近关于大语言模型微调的技术文章" ``` |
| 📁 管理文件 | ``` hermes chat -q "把当前目录下所有 .py 文件中的 TODO 注释提取出来" ``` |
| ⏰ 设置提醒 | ``` hermes cron create "tomorrow 10am" --prompt "提醒我开会" ``` |

## 📋 必须记住的命令

### 对话中常用命令

| 命令 | 作用 |
| --- | --- |
| ``` /new ```   或   ``` /reset ``` | 开新会话 🔄 |
| ``` /clear ``` | 清屏并新建会话 |
| ``` /retry ``` | 重发上一条消息 |
| ``` /undo ``` | 撤销上一次交换 |
| ``` /config ``` | 显示当前配置 ⚙️ |
| ``` /model [名称] ``` | 显示或切换模型 🤖 |
| ``` /yolo ``` | 危险命令免确认 ⚠️ |
| ``` /quit ```   或   ``` /exit ``` | 退出 👋 |

### 终端常用命令

| 命令 | 作用 |
| --- | --- |
| ``` hermes doctor ``` | 检查配置是否正确 🔍 |
| ``` hermes tools list ``` | 查看可用工具 |
| ``` hermes sessions list ``` | 查看历史会话 📜 |
| ``` hermes --resume ``` | 继续上次的会话 🔙 |

## 🛠️ 支持的模型提供商

| 提供商 | 配置名 | 所需环境变量 |
| --- | --- | --- |
| OpenRouter | ``` openrouter ``` | ``` OPENROUTER_API_KEY ``` |
| Anthropic | ``` anthropic ``` | ``` ANTHROPIC_API_KEY ``` |
| DeepSeek | ``` deepseek ``` | ``` DEEPSEEK_API_KEY ``` |
| MiniMax | ``` minimax ``` | ``` MINIMAX_API_KEY ``` |
| Hugging Face | ``` huggingface ``` | ``` HF_TOKEN ``` |

## ❓ 常见问题

> **Q: 执行命令前 Hermes 一直问确认？**

> 加上 

> ```
> --yolo
> ```

>  跳过危险命令确认：

> Bash

> ```
> > hermes --yolo
> ```

> **Q: 想让 Hermes 记住项目背景怎么办？**

> 在第一个问题里说明即可：
> *"我的项目是一个电商后端，用 FastAPI + PostgreSQL，帮我写一个商品接口"*

> **Q: 修改配置后不生效？**

> 执行 

> ```
> /reset
> ```

>  开始新会话即可 ✅

## 📈 下一步学什么

1.🔗 **配置多个平台** → 用 

```
hermes gateway setup
```

 连接 Telegram/Discord

2.⏰ **定时任务** → 用 

```
hermes cron
```

 设置自动化

3.📚 **保存技能** → 把常用工作流保存为技能

4.👥 **多 Agent** → 同时运行多个 Hermes 分工合作

5.🔌 **扩展能力** → 连接 MCP 服务器、编写自定义工具

## 🔗 资源链接

> 📖 官方文档：https://hermes-agent.nousresearch.com/docs/
> 🐙 GitHub：https://github.com/NousResearch/hermes-agent
> 🔧 安装问题：

> ```
> hermes doctor
> ```

>  检查

> 🚀 **安装后先用 

> ```
> hermes chat -q "..."
> ```

>  体验单次查询，觉得好用再 

> ```
> hermes
> ```

>  进入交互模式！**
