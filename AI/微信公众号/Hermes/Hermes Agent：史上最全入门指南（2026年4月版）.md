> 📎 来源: [AI傻瓜学堂](https://mp.weixin.qq.com/s?__biz=MzI4NDM3MDg4MQ==&mid=2247484353&idx=1&sn=ce0acd34d70aaa42f8bef11c0a43be57&chksm=eaacfd717b16893237e6bebfda2c00ebbf002a42e4c311ab5012628515cf5ca71674d7d7067a&mpshare=1&scene=1&srcid=04223xabdiHtTI0Xz5udsRNh&sharer_shareinfo=569d618bc213a4d81f5720dcf5556f07&sharer_shareinfo_first=569d618bc213a4d81f5720dcf5556f07) | 时间: 2026-04-22 17:35

---

Hermes Agent 是 Nous Research 推出的开源 AI 智能体，运行在你的电脑或 VPS 上，能记住跨会话的学习内容，并可以随时通过 CLI、Telegram、Discord、邮件等多种渠道与你对话。

---

## 一分钟快速了解

用一行 curl 命令安装。选择一个模型提供商（Claude、GPT、GLM、MiniMax 等，或本地 Ollama），给它一个任务——比如"每天早上8点汇总我的 GitHub 通知"，或者"帮我调试这个 Python 脚本"。

它就会开始运行、学习。一周后，同样的任务会产出更精准的输出，因为 Hermes 一直在悄悄编写 skills——记录成功操作的小 Markdown 文件，供下次使用。

这就是整个产品的逻辑：**安装 → 分配任务 → 让它不断进化。**

---

## Hermes 适合谁？

三类人最常用：

**1. 命令行开发者** 你熟悉终端，用 Claude Code 在编辑器里写代码。你需要一个能处理"审计仓库里的死代码"这类任务的助手。 推荐首先使用：hermes CLI + skills

**2. 自动化运营者** 不一定要写代码，只是想让 AI 做重复性工作——汇总新闻、监控市场、生成报告。 推荐首先使用：cron + 消息网关 + memory

**3. Telegram 机器人爱好者** 想要一个随时可联系的 AI 助手，走到哪里都能发消息让它处理。 推荐首先使用：Telegram 网关 + voice + skills

---

## Hermes vs Claude Code / Cursor / OpenClaw

| 特性 | Claude Code | Cursor | OpenClaw | Hermes Agent |
| --- | --- | --- | --- | --- |
| 主要界面 | CLI（在仓库内） | IDE | CLI+配置 | CLI+聊天+cron+Telegram |
| 持久记忆 | 无 | 无 | 无 | 有（跨会话） |
| 自动学习 | 无 | 无 | 无 | 有（通过skills） |
| 定时任务 | 无 | 无 | 无 | 有 |
| 模型选择 | Anthropic | 多个 | 多个 | 18+提供商，可随意切换 |

**关键区别**：Claude Code 是仓库内的编程助手，Cursor 是编辑器内的配对编程，OpenClaw 是配置驱动的任务运行器，而 Hermes 是一个能跨会话学习、可以从任何渠道联系你的自主智能体。

大多数用户会把 Hermes 和 Claude Code 一起用：仓库内用 Claude Code，仓库外的日常事务用 Hermes。

---

## 2分钟安装

**前置条件**：

- macOS、Linux 或 Windows（WSL2）
- 一个终端（bash、zsh、fish 都可以）
- API Key 或本地模型

**安装命令**：

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | sh
```

**首次运行**：

```
hermes
```

按提示配置你的模型 API Key。

**验证安装**：

```
hermes doctor
```

显示全绿就说明准备好了。

---

## 模型选择（最重要的一步）

很多新手在这里翻车。如果 Hermes 感觉反应慢或笨，**几乎都是模型的问题**，不是 Hermes 的问题。

**推荐模型**：

| 模型 | 费用 | 工具调用 | 速度 | 适合场景 |
| --- | --- | --- | --- | --- |
| Claude Sonnet/Opus | $$$ | 优秀 | 快 | 生产级工作流 |
| GPT-5 | $$$ | 优秀 | 快 | 生产级，OpenAI用户 |
| GLM-5.1 | $ | 优秀 | 快 | 性价比之选 |
| MiniMax M2.7 | $$ | 优秀 | 快 | 高性价比 |
| DeepSeek | $ | 好 | 快 | 成本优化工作流 |
| Ollama + Qwen | 免费 | 一般 | 取决于GPU | 本地写代码、聊天 |

**本地模型的局限**：适合单步操作，但多步工具调用会出问题。生产环境建议用 API 模型。

---

## 第一个工作流示例

**示例1：电脑上的编程助手**

```
cd ~/projects/my-repo hermes > 审计这个仓库里的死代码、未使用的导入、超过6个月的注释代码块，生成一个markdown报告
```

第二次问同类问题会更快，因为它已经学会了。

**示例2：VPS上的 Telegram 机器人**

```
hermes gateway setup # 设置 Telegram bot（从 @BotFather 获取token） # 启动常驻 hermes daemon start > 每天早上8点汇总我的GitHub通知并发到这里
```

**示例3：每日简报**

```
hermes > 每个工作日上午7:30，收集：(1)昨晚HN热门10篇 (2)我的未读GitHub通知 (3)深圳天气。发邮件到我的邮箱。
```

---

## 学习循环：最核心的功能

每个任务执行后，Hermes 会自我复盘：成功了吗？哪里花了太长时间？下次能改进吗？当答案是肯定的，它就会写一个 skill 文件到 ~/.hermes/skills/，下次遇到类似任务直接调用。

这就是 Hermes 与其他工具的根本区别：**别的时间在 forgets，Hermes 在 learned。**

**记忆存储三处**：

- MEMORY.md — 短期记忆，最多2200字符
- USER.md — 关于你的事实，最多1375字符
- Session search — 每次对话都可搜索

有限制是故意的。无限记忆最后都会变成垃圾抽屉。

---

## 如何更新？

```
hermes update
```

Hermes 会自述更新内容、备份配置、应用新版本。当前版本 v0.10.0（2026年4月），团队大约每两周发版一次。

---

**编译：AI傻瓜学堂** | 原文：@ksimback | Hermes Atlas
