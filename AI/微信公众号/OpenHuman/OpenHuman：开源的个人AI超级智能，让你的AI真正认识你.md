> 📎 来源: [AI科技新纪元](https://mp.weixin.qq.com/s?__biz=MzA5NTk3MjA5OQ==&mid=2464279111&idx=1&sn=81bcd05046e6fa2359d7334d8693a7ad&chksm=865ac1707c1121be88ea36c60c1575780de772d4304a18372a76d8e429b164c98ba6f2299d41&mpshare=1&scene=1&srcid=05176bBib0ez8XWXHwBux6fG&sharer_shareinfo=1392e8a45f192902fcfb210bb48871fe&sharer_shareinfo_first=1392e8a45f192902fcfb210bb48871fe) | 时间: 2026-05-17 23:40

---

全文约1800字，阅读约5分钟

---

说实话，现在市面上的AI助手有个共同问题：它们都是"陌生人"。

你用Claude，它只记得这一轮对话；你用ChatGPT，每次都要重新解释背景。想要一个真正了解你工作、生活、习惯的AI？你得自己搭建，或者忍受漫长的"训练期"。

这几天GitHub上有个项目火了——OpenHuman。一个开源的个人AI超级智能，主打一个核心卖点：**让AI在几分钟内真正"认识你"**。

---

## 它是什么？

OpenHuman是一个桌面端的AI代理助手，开源（GNU协议），用Rust写的。核心思路：

> 把你的所有数据（邮件、文档、聊天记录、日程）压缩成一个"记忆树"，AI通过这个记忆树来理解你——不是聊天记忆，而是真正的知识库。

简单说：你连上Gmail、Notion、GitHub这些账号，OpenHuman每20分钟自动拉取数据，压缩成Markdown存到本地SQLite，AI就能基于这些"压缩后的你"来工作。

---

## 核心功能一览

| 功能 | 说明 |
| --- | --- |
| **桌面UI** | 清洁界面，无需终端，几步点击即可上手 |
| **桌面宠物** | 有个形象，会说话、会反应，还能加入Google Meet会议 |
| **118+集成** | Gmail、Notion、GitHub、Slack、Stripe、Calendar等，一键OAuth连接 |
| **自动拉取** | 每20分钟自动从连接的账号拉取最新数据 |
| **记忆树** | 把你的数据压缩成≤3k token的Markdown块，存到本地SQLite |
| **Obsidian兼容** | 同样的数据也会存成.md文件，可用Obsidian打开编辑 |
| **Token压缩** | 工具调用、网页抓取、邮件内容都会压缩，节省80%token成本 |
| **模型路由** | 自动把任务分发到合适的模型（推理/快速/视觉） |
| **本地AI** | 支持Ollama，可完全本地运行 |
| **语音功能** | 语音输入 + ElevenLabs语音输出，宠物会对口型 |

---

## 为什么值得关注？

**1. 零训练期**

传统方案（比如OpenClaw、Hermes）需要你手动配置插件、慢慢喂数据，几周后AI才有点用处。OpenHuman的逻辑：你连账号，它自动拉数据，压缩成记忆——**一次同步就有完整上下文**。

**2. 本地优先，隐私安全**

所有记忆数据存到你本地的SQLite，加密存储。云端只跑模型，不存你的知识。

**3. 省钱**

TokenJuice压缩层能把HTML转Markdown、缩短URL、过滤冗余——同样的信息量，token消耗能降到原来的20%。

**4. 对比Claude/OpenClaw**

| 对比项 | Claude CoWork | OpenClaw | Hermes | OpenHuman |
| --- | --- | --- | --- | --- |
| 开源 | ❌ | ✅ MIT | ✅ MIT | ✅ GNU |
| 上手难度 | 桌面+CLI | 终端优先 | 终端优先 | 清洁UI，几分钟 |
| 记忆方式 | 聊天级 | 插件依赖 | 自学习 | 记忆树+Obsidian vault |
| 集成数量 | 少 | 自己配置 | 自己配置 | 118+一键OAuth |
| 自动同步 | ❌ | ❌ | ❌ | ✅ 每20分钟 |
| Token成本 | 全消耗 | BYO模型 | BYO模型 | 压缩80% |

---

## 安装步骤

OpenHuman目前处于Early Beta阶段，有桌面版和脚本安装两种方式。

### 方法一：下载桌面版（推荐）

访问官网下载DMG或EXE：
https://tinyhumans.ai/openhuman

Mac、Windows都有现成安装包。

### 方法二：命令行安装

**MacOS / Linux：**

```
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
```

**Windows（PowerShell）：**

```
irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex
```

---

## 配置步骤

安装后，首次运行会进入引导流程：

### 1. 连接账号

点击"Integrations"，选择你要连接的服务：

- Gmail（邮件同步）
- Notion（文档同步）
- GitHub（代码仓库同步）
- Google Calendar（日程同步）
- Slack（聊天同步）

每项都是一键OAuth，授权即可。

### 2. 开启Auto-Fetch

连接后，打开"Auto-Fetch"开关。系统会每20分钟自动拉取这些账号的最新数据。

### 3. 配置模型

如果你有OpenAI、Anthropic等API密钥，在"Model Routing"里填入。

如果想完全本地运行，可以配置Ollama：

```
# 安装Ollamacurl -fsSL https://ollama.ai/install.sh | sh# 拉取模型ollama pull llama3
```

然后在OpenHuman设置里指向本地Ollama。

### 4. 打开Obsidian Vault

OpenHuman会把记忆存到本地Obsidian兼容目录。路径一般在：

```
~/openhuman/obsidian-vault/
```

你可以用Obsidian打开这个目录，直接浏览、编辑AI整理的知识库。

---

## 实用场景

**场景一：邮件助手**

连接Gmail后，AI已经读过你最近的邮件。你问："上周John发的那个项目进度邮件，核心结论是什么？"——它能直接回答，不需要你转发邮件。

**场景二：代码助手**

连接GitHub后，AI知道你参与的所有仓库。你说："帮我写一个符合本项目风格的PR描述"——它能参考你的commit历史、PR模板来写。

**场景三：会议助手**

桌面宠物可以"加入"你的Google Meet会议（作为参与者）。它能听会议内容、做笔记，会后给你总结。

**场景四：个人知识库**

所有数据压缩成Obsidian笔记。你可以用Obsidian的图谱视图看到自己的"知识网络"。

---

## 常见问题

**Q：数据安全吗？**
A：记忆数据存本地SQLite，加密存储。云端只跑推理，不存原始数据。

**Q：支持哪些模型？**
A：内置模型路由，可配置OpenAI、Anthropic等API；也支持本地Ollama。

**Q：Windows能用吗？**
A：有Windows安装包，脚本安装也支持。

**Q：费用怎么算？**
A：项目开源免费。如果你用云端模型，需要自己的API密钥；本地Ollama完全免费。

**Q：和Obsidian什么关系？**
A：OpenHuman把记忆存成Obsidian兼容格式，你可以用Obsidian打开编辑。但OpenHuman本身是个独立应用。

---

## 小结

OpenHuman解决了一个痛点：**AI助手都太"冷"了，每次对话都要从头解释**。它的方案是：把你的所有数据压缩成一个记忆树，AI基于这个"你"来工作——几分钟内就能用上真正懂你的助手。

目前还是Early Beta，有些粗糙，但思路很有意思。如果你想要一个"私人AI大脑"，值得试一下。

**GitHub地址**：https://github.com/tinyhumansai/openhuman

---

如果对您有启发，点个关注吧。
