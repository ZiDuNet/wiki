> 📎 来源: [智趣AI生活派](https://mp.weixin.qq.com/s?__biz=MzkxMzYyNDYzMg==&mid=2247486292&idx=1&sn=8b513b5570a1753a5b4b0410f5294cd7&chksm=c0ff69cfbec16aff832502435005251e0b4d5383cc5572f0b808a422f63c19619e97d57d6ea3&mpshare=1&scene=1&srcid=0420uF7bVlXSmXgrSJRWxZeW&sharer_shareinfo=40a6b83523d7b2b48e4a7402e6dc7166&sharer_shareinfo_first=40a6b83523d7b2b48e4a7402e6dc7166) | 时间: 2026-04-20 21:32

---

![](assets/img_6fbafb1cfe07.jpg)

Hermes Agent 新手10个技巧

让你的 AI 智能体越用越聪明

从安装到进阶，一篇搞定这个开源自我进化 AI 智能体

- - - - - - - - - - - - - - - -

如果你还没听说过 Hermes Agent，那你可能错过了 2026 年最值得关注的开源 AI 项目之一。由 Nous Research（开源大模型社区的明星团队）打造，它是一个真正能“自我进化”的 AI 智能体——它会记住你教给它的一切，越用越聪明。

与 Claude Code、Cursor 等绑定单一模型的工具不同，Hermes Agent 是一个开源（MIT 协议）、模型无关、跨平台的通用 AI 智能体框架。它可以运行在你的终端、Telegram、Discord、Slack 等 14+ 平台上，支持 OpenAI、Anthropic、OpenRouter 以及任何 OpenAI 兼容端点。截至 2026 年 4 月，它已在 GitHub 上获得超过 24,000 颗 Star，是当前最活跃的开源 Agent 框架之一。

今天这篇文章，我们将从零开始，整理出 10 个新手必知的实用技巧，帮你快速上手这个强大的 AI 工具。

- - - - - - - - - - - - - - - -

01. 一行命令完成安装，别想太复杂

很多新手觉得 AI 工具的安装一定很复杂，但 Hermes Agent 的安装真的只需要一行命令。前提是你的电脑上已经装好了 git（这对开发者来说基本是必备的）。

安装命令

# Linux / macOS / WSL2

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

 

# 安装完成后重载 Shell

source ~/.bashrc

 

首次启动三步走

# 第1步：运行配置向导

hermes setup

 

# 第2步：选择模型提供商并输入 API Key

hermes model

 

# 第3步：开始对话

hermes

 

|  |
| --- |
| 小贴士  如果你在国内使用，可以在 setup 时选择“Custom OpenAI-compatible endpoint”，填入国内可访问的 API 代理地址（如 apiyi.com 的 base\_url），即可无障碍连接 GPT、Claude 等主流模型。 |

- - - - - - - - - - - - - - - -

02. 别再重复输入相同的指令，用 AGENTS.md 一劳永逸

你是不是经常发现自己反复告诉 AI：“用 tab 缩进”“测试放在 tests/ 目录”“我们用 pytest”…… 这些重复的指令完全可以一次性解决。

在你的项目根目录创建一个 AGENTS.md 文件，Hermes Agent 会在每次启动会话时自动加载它，相当于给 AI 预设了“项目规则”。

AGENTS.md 示例

# 项目上下文

- 这是一个 FastAPI 后端项目，使用 SQLAlchemy ORM

- 数据库操作一律使用 async/await

- 测试文件放在 tests/ 目录，使用 pytest-asyncio

- 缩进用 tab，行宽 120

- 永远不要提交 .env 文件

 

更棒的是，如果你已经有 .cursorrules 文件，Hermes Agent 也能自动读取，无需重复配置。

- - - - - - - - - - - - - - - -

03. 让 AI “记住”你，善用持久记忆功能

![](assets/img_6ff904521e8d.jpg)

Hermes Agent 最独特的功能之一就是持久记忆。它使用 SQLite + FTS5 全文搜索存储对话历史，让 AI 能够跨会话记住你的偏好和习惯。

如何使用记忆功能：在一次产出的对话结束后，你可以说：

"记住这个，下次用的时候直接调用"

 

"保存到记忆：我们的 CI 使用 GitHub Actions，部署文件是 deploy.yml"

 

"清理一下记忆，把 Python 3.9 的信息替换成 3.12"

 

|  |
| --- |
| 注意  记忆空间是有限的（MEMORY.md 约 2200 字符，USER.md 约 1375 字符）。当存储满时，AI 会自动合并旧条目。你也可以主动让它“清理记忆”来释放空间。 |

- - - - - - - - - - - - - - - -

04. 把复杂流程变成“技能”，一键复用

![](assets/img_020c14851037.jpg)

如果你发现某个任务需要 5 步以上才能完成，而且以后还会反复做——那就把它保存为“技能”吧！

创建技能：当 Hermes 完成一个复杂任务后，说：

"把你刚才做的保存为技能，叫 deploy-staging"

 

调用技能：下次只需输入：

/deploy-staging

 

Hermes 会自动加载完整的操作流程，包括步骤、注意事项和验证方法。更强大的是，当它再次遇到类似任务时，还会根据新经验自动优化这个技能——这就是“自我进化”的核心。

输入 /skills 可以查看所有已经积累的技能列表。

- - - - - - - - - - - - - - - -

05. 提示词要具体，别让 AI 猜

模糊的指令产生模糊的结果。这是所有 AI 工具的通用原则，但在 Hermes Agent 中尤为重要，因为它拥有文件搜索、终端执行、代码运行等 40+ 工具。

反面教程

❌ 不好："修复代码中的错误"

✔ 好："修复 api/handlers.py 第 47 行的 TypeError，process\_request() 函数从 parse\_body() 接收到了 None"

关键原则：提供文件路径、错误信息、期望行为。一条精确的指令胜过三轮来回的确认。直接粘贴错误堆栈，Hermes 能自动解析。

- - - - - - - - - - - - - - - -

06. 善用快捷键，效率翻倍

Hermes Agent 的 CLI 藏着很多实用的快捷键，掌握它们能让你的工作效率大幅提升：

|  |  |
| --- | --- |
| 快捷键 | 功能说明 |
| Alt+Enter / Ctrl+J | 换行不发送，适合编写多行提示词 |
| Ctrl+C 单次 | 中断 AI 回复，可立即重新输入指令 |
| Ctrl+C 双击 | 强制退出 Hermes |
| Ctrl+V | 直接粘贴剪贴板图片，AI 可视觉分析 |
| / + Tab | 查看所有可用的斜杠命令 |
| /compress | 压缩对话历史，减少 token 消耗 |
| /usage | 查看当前 token 使用量 |
| /model | 会话中切换模型 |
| /title | 为当前会话命名，方便后续查找 |

 

|  |
| --- |
| 实用技巧  当 AI 走向错误方向时，不要等它说完！按一次 Ctrl+C 中断，然后立即输入新的指令来纠正方向。这比等它完成再重新开始要高效得多。 |

- - - - - - - - - - - - - - - -

07. 会话恢复与管理，别让上一次的努力白费

关闭终端不意味着丢失上一次的对话。Hermes Agent 提供了完善的会话管理功能：

# 恢复最近一次会话

hermes -c

 

# 按标题恢复特定会话

hermes -r "我的研究项目"

 

# 列出所有会话

hermes sessions list

 

建议养成用 /title 命名会话的习惯，比如 /title auth-refactor 或 /title 研究-LLM量化。名字化的会话很容易找到和恢复，而未命名的会话会堆积成一堆无法区分的条目。

- - - - - - - - - - - - - - - -

08. 多平台部署，一个 Agent 服务全场景

![](assets/img_5c159f23726d.jpg)

Hermes Agent 不仅仅是一个终端工具。通过内置的 Gateway 功能，你可以同时在多个平台上与同一个 Agent 对话：

•CLI 终端：本地开发工作

•Telegram / Discord / Slack：团队协作

•WhatsApp / Signal：私人助手

•Email / SMS：消息推送

•Home Assistant：智能家居控制

 

启动 Gateway

hermes gateway

 

一条命令，你的 Agent 就能同时服务 Telegram、Discord 等多个平台。用 /sethome 命令设置“主频道”，定时任务和 Cron 结果会自动推送到这里。

- - - - - - - - - - - - - - - -

09. 省钱技巧：聚聪合理用 Token，让成本可控

AI 工具用久了费用可能不低，以下是几个实用的省钱技巧：

1. 善用 /compress：长会话会累积大量 token。当感觉回复变慢或被截断时，运行 /compress 可以压缩对话历史，保留关键上下文的同时大幅减少 token 用量。

2. 切换模型：复杂推理用前沿模型（Claude Sonnet/Opus、GPT-4o），简单任务切换到更快更便宜的模型。用 /model 即可随时切换。

3. 批量操作用脚本：与其让 AI 一次次执行终端命令，不如让它写一个 Python 脚本一次性完成。比如“写一个 Python 脚本把所有 .jpeg 改名为 .jpg 并执行”比逐个重命名便宜得多。

4. 并行委派：需要同时研究多个主题？让 Agent 使用 delegate\_task 并行处理，每个子任务独立运行，只返回最终摘要，大幅减少主对话的 token 消耗。

定期运行 /usage 查看 token 消耗，或 /insights 查看近 30 天的使用模式，做到心中有数。

- - - - - - - - - - - - - - - -

10. 安全第一：别让 AI “乱来”

![](assets/img_449915f7a061.jpg)

AI 智能体拥有终端执行权限，安全问题不容忽视。以下是几个必须掌握的安全技巧：

1. 用 Docker 隔离不可信代码：在 .env 文件中设置 TERMINAL\_BACKEND=docker，这样即使 AI 执行了危险命令，也不会影响主机系统。

# 在 .env 文件中配置

TERMINAL\_BACKEND=docker

TERMINAL\_DOCKER\_IMAGE=hermes-sandbox:latest

 

2. 命令审批是你的安全网：Hermes 会自动检测危险命令（如 rm -rf、DROP TABLE 等）并要求你确认。选择“session”而非“always”，直到你对工具充分了解。

3. 限制机器人访问权限：如果你在 Telegram/Discord 上部署了 Hermes，一定要配置用户白名单，千万不要设置 GATEWAY\_ALLOW\_ALL\_USERS=true。

# 推荐：按平台配置白名单

TELEGRAM\_ALLOWED\_USERS=123456789,987654321

DISCORD\_ALLOWED\_USERS=123456789012345678

 

4. 用 DM Pairing 管理团队访问：启用 DM 配对功能后，团队成员私信机器人时会收到一次性配对码，你审批后才能使用，简单又安全。

- - - - - - - - - - - - - - - -

写在最后

Hermes Agent 代表的是 AI 智能体的一个新方向：不再是“用完即弃”的一次性工具，而是“越用越懂你”的长期伙伴。它的持久记忆、自动技能生成、跨平台部署等特性，让它在众多 Agent 框架中脱颖而出。

无论你是想要一个 24/7 的个人 AI 助手、一个团队的智能 Bot，还是一个能控制智能家居的助手，Hermes Agent 都值得你花时间学习。

开源、免费、MIT 协议——现在就去 GitHub 搜索 NousResearch/hermes-agent，开始你的 AI 智能体之旅吧！

 

|  |
| --- |
| 参考资源  GitHub 仓库：NousResearch/hermes-agent 官方文档：hermes-agent.nousresearch.com 开源协议：MIT License 当前版本：v0.8.0+（2026年4月） |

 

— END —

如果觉得这篇文章有用，欢迎转发分享！
