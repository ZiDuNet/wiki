> 📎 来源: [土著哥聊AI](https://mp.weixin.qq.com/s?__biz=Mzg2NTIxMzcyOQ==&mid=2247490239&idx=1&sn=8119b5a9945733b1329d9314ff7e3b8b&chksm=cf9e7574b103c82c3ad7077ad28d428a1cebbd4ea8ccc3928bec71203217900941ddfcff4c85&mpshare=1&scene=1&srcid=04301mFhDde2HAySdl0Ymbyf&sharer_shareinfo=4bca0039e8c6d7f97945da57bbf172bf&sharer_shareinfo_first=4bca0039e8c6d7f97945da57bbf172bf) | 时间: 2026-04-30 19:39

---

Hermes 似乎越来越火，有些人已经摸到了门道儿。但绝大多数人在安装完 Hermes 后，仅仅把它当作一个更聪明的 ChatGPT 在用。

用户会连上 Telegram，飞书、微信指向一个模型，输入请求，获取回复。然后关掉 TUI 或者聊天窗口，一天的工作可能就算结束了。

如果你也是这样，那你大概只用到了 Hermes 实际能力的 8%。

以下是 Hermes 中的 15 个特性，我按它们对你产出改变的程度进行了排名。一点不夸张，可能大多数运行了 Hermes 好几个月的人，甚至从未碰过这个列表里的任何一个功能。

## 大多数人完全会跳过的设置阶段

##

## 1、/personality + SOUL.md

##

## 可能你不知道 Hermes 在启动时会固定读取一个名为 SOUL.md 的单一文件。无论你之前在里面写了什么，它都会永远成为你 Agent 的声音。

它会跨越每一个会话，使用 **/personality** 还可以在对话中途随时切换你预命名的人物。

这个 SOUL.md 文件内容只需写一次。你可以定义它的说话方式、它会拒绝什么、它认为自己在为谁而工作。

你就不需要再在每次对话开头都输入一遍「我是一个资深的 XXX 专家」了。

**2、MEMORY.md + USER.md**

这是 Hermes 在每次会话中都会读取的两个持久化文件。

**MEMORY.md** 类似于 Agent 的笔记本，它会随着你跟 Hermes Agent 的每次聊天内容，自动记录关于你项目的真实与重要情况。当然，你也可以自行往里录入并编辑。
**USER.md** 则是它对你这个人的了解：比如你的角色、你的语气、你的上下文、你做决策时的偏好等等。

看到网上有些专业用户讲，如果结合 FTS5 索引和 LLM 摘要器，你的 Agent 可以将 8 周前相关的记忆提取到今天的会话中。不过感觉这两个还是太偏技术化了，对普通人不太适用。但也不乏我们可以简单了解一下大概意思。

**FTS5** 即 SQLite 的一个虚拟表模块，专为应用程序提供高效的全文搜索功能。它允许在海量文本数据中进行快速、精确的关键词查询（如前缀、短语匹配），常用于移动应用本地搜索、全文索引等场景。

**LLM 摘要器**（Large Language Model Summarizer）是利用大语言模型（如 GPT、Claude、LLaMA 等）的强大自然语言处理能力，将长篇文档、文章、报告、会议记录或对话历史，自动压缩成简洁、连贯的重点摘要的技术或工具。它不仅仅是提取原句，而是通过对内容的理解，重新组织语言以精炼出核心观点。

现在的情况是，大多数人每次开启新对话时，都在重新解释这个项目的情况以及介绍自己是谁。

所以编辑并管理好 MEMORY.md 和 USER.md 这两个文件，你就不用每次都重复输入同样的提示词去介绍了，帮你省去了不少麻烦。

**3、/insights [days]**

跨越你运行过的每一个会话的数据分析，哪个项目消耗了最多的 token，哪些模型花了多少钱，Agent 曾经在什么地方卡住了，你不断重复访问的内容是什么。

执行 **/insights 30** 让你对过去一个月的情况一目了然。

这个功能其实也是从 Claude Code 中偷师学艺的。我曾经也写过一篇文章《[Claude Code 新增的 insights 指令是真不错，全面复盘你的 CC 使用情况给出最真实的洞察](https://mp.weixin.qq.com/s?__biz=Mzg2NTIxMzcyOQ==&mid=2247487902&idx=1&sn=91ed5156d796e57e2b3a5033e1ccc0e6&scene=21#wechat_redirect)》，有兴趣的可以读一下。

大多数人盲目地开启新会话，因为根本不知道 Hermes 中也有 /insights 的存在。

**4、/snapshot**

在进行任何危险操作之前，将整个 Hermes 的配置和状态先保存为一个快照（snapshot）。

这样的话，你就可以尽情试验、打破常规，然后用 **/snapshot restore** 指令恢复到已知良好的状态。

类似于 Git 版本恢复~

可绝大多数人并不知道 Hermes Agent 本身也存在回滚功能。

## 很少人理会的执行过程中的控制权

##

## 5、/branch (别名 /fork)

##

## 对当前会话进行 branch（分支）处理，探索不同的路径而不会丢失原始内容。

就像用于对话的 git。

尝试更高风险的方法，同时不会毁掉你现有的优质上下文，行不通的话那就再退回去。

**6、/rollback**

文件系统检查点（checkpoints）。如果 Agent 执行了破坏性编辑并搞崩了你的代码？别急着用 git， 可以直接使用 **/rollback**。

Hermes 会保留它碰过的每一个文件的检查点，你可以恢复其中的任何一个。

大多数人都是在 Agent 吞噬了他们的工作成果后，确实吃到了苦头儿才了解到 Hermes 中还有这么一个功能。

**7、/btw**

CC、OpenClaw 中都具备，Hermes 中也有这个很实用的指令功能。对于临时的附加问题，它会利用当前会话的上下文，但不用调用任何工具，也不会被持久化保存。

这是一个「**快速直觉验证，不要污染我的主线程**」的命令。

大多数人为了一个一次性问题会开启一个全新的会话，然后回来时发现自己所有的上下文都丢了，追悔莫及。

**8、/steer 与 /queue**

如果你正在执行一个冗长的代理性任务，并且已经进行了 3 次工具调用，这时你可能会意识到 Hermes Agent 正在使用你的生产 API，而它本该使用预发布的 API 猜对。

不要直接终止运行~可以使用 **/steer** 指令功能告诉它"使用预发布的 API 而不是生产级的”。

下一次工具调用时它就会看到你上面提交的备注信息，当前回合也不会被中断，提示词缓存也能保持在热启动的状态。

配合 **/queue** 指令使用，可以在不中断当前回合的情况下将下一个回合排入队列。

如果你不知道这两个指令，那多半你会直接终止运行并从头开始。

**9、/yolo、/fast、/reasoning**

大多数用户可能从未触碰过的三个高级开关。

**/yolo** 跳过所有危险命令的审批，就像 CC 中的 claude --dangerously-skip-permissions 指令一样，请谨慎使用。
**/fast** 将会话切换到 OpenAI 优先处理 或 Anthropic 快速模式以获得更低的延迟。
**/reasoning** 用于设置你配置的模型的推理力度级别。

## 其实并不存在模型提供商锁定

##

## 10、/model [--provider] [--global]

##

## Hermes 在设计上是与模型提供商无关的（不绑定任何一家模型提供商，也反之不会被提供商威胁，就像 Claude 反噬 OpenClaw 一样）。

只需一个命令，即可在不重启的情况下切换 Agent 背后的模型。

支持 Anthropic Opus 4.7、OpenAI Codex（通过 OAuth 使用 GPT-5.5，而无需 API key）、OpenRouter、NVIDIA NIM、Kimi、Gemini、AWS Bedrock、Vercel AI Gateway、Xiaomi MiMo、Step Plan、Arcee 等等。

使用 **/model anthropic:claude-opus-4-7** 可切换到 Opus。使用 **/model openrouter:kimi-k2.6** 可降级到更便宜的模型选项来处理繁杂的体力活。

Agent 的状态会无缝继承。

大多数人可能被锁定在单一的模型提供商上，因为他们没有意识到 Hermes 从第一天起就是为便携性而生的。

**11、辅助模型（Auxiliary models）**

Hermes Agent 做的不仅仅是回答你的提示词。它还会像其他 Agent 产品一样压缩上下文、总结会话、生成标题、运行视觉任务。

而 Hermes 是允许你为每一项单独的任务分配不同的模型的。

运行 Opus 4.7 可以作为你的主力大脑，Haiku 4.5 专门用于上下文压缩，另一个小模型还可以用于标题生成。

通过在终端中输入 hermes model 配置一次，辅助界面就会处理剩下的事情。

## 无人激活的到达能力

##

## 12、17 个平台的 Gateway

##

## Telegram、Discord、Slack、WhatsApp、Signal、Email、SMS、Matrix、Mattermost、Feishu、WeCom、DingTalk、BlueBubbles、Home Assistant、QQBot，加上 CLI 和语音。

仅仅一个 Hermes 进程就能驱动它们全部。

终端中运行 hermes gateway，你就可以广播到你团队实际活跃的每一个平台。通过 DM 配对，通过允许列表用户进行访问控制，按频道限制速率。

**13、/voice (4个平台上的实时语音)**

我相信绝大多数人在使用 Hermes Agent 时只知道在聊天窗口中对着它打字，因为有时候我也是这样！

但 Hermes CLI 中是提供实时语音功能的，而且非常方便和强大。

在 Telegram DMs 中以及 Discord 语音频道里，输入 **/voice**，然后直接说话就行了。

在你平时散步、开车或者离开键盘时非常好用，毕竟打字比如说话快！

**14、Cron + /webhook-subscriptions**

Hermes 中也内置 Cron（定时任务）调度器。你可以用自然语言编写日程安排，并告诉它把结果自动传送到你指定的哪个消息平台。比如：

“每周五下午 5 点，总结本周的 GitHub 提交记录并发送到我的飞书上。” Hermes 会自动解析、无人值守运行，并准确将信息投递到你指定的地方。

搭配 **/webhook-subscriptions**（webhook 订阅）进行逆向操作：外部服务（GitHub、Vercel、Stripe）可以直接将 payload 推送到你的消息频道中，模型成本为零。

零 token 消耗，零延迟。

## 高阶用户的杀手锏

##

## 15、Skills 就是「斜杠命令」

##

## 大多数人可能每周只用一次「斜杆命令」。而真正的重度用户已经把他们的整个工作流都构建在其中了。

要知道 Hermes 中开箱即附带了 100 多个 skills，而且每一个都支持斜杠命令。输入「**/**」 它们就会自动补全。

**/architecture-diagram** 用于生成 SVG 架构图。**/excalidraw** 用于手绘图表。**/manim-video** 用于生成 3 蓝色 1 棕色风格的动画。

**/research-paper-writing** 用于端到端的机器学习论文草稿。**/linear** 用于 issue 管理。**/google-workspace** 涵盖了 Gmail、Calendar、Drive、Docs 和 Sheets。**/imessage** 用于发送短信。**/youtube-content** 用于把转录文本转换成线程。**/systematic-debugging** 用于 4 阶段的根本原因分析。**/codex** 和 **/claude-code** 用于把任务委派给其他 Coding Agent。

更重要的是，你可以根据自己的工作流需求编写自己的 skills，然后把它自定义成一个斜杆命令，比如 /my-skills。

这样你只需要构建一次，就可以在任何 Hermes 会话中输入 **/my-skill** 进行调用，它会自动运行，永远如此。

写在最后

如果你已经花钱订阅了一个大模型套餐，甭管是国内的还是国外的。

同时你现在也拥有一个提供持久化记忆、100 多个预置 skills、文件系统回滚、会话分支、中途调整方向、17 个平台消息触达、语音模式、原生多模型提供商路由、辅助模型路由、Cron 自动化、webhook 集成以及能够编写自定义斜杆命令的 Hermes Agent。

而你，却一直把它当成一个稍微高级点儿的聊天机器人在用的话，那将会成为一种对现实的讽刺。

真正区分普通玩家和高阶用户的，并不是比谁接入的模型更牛逼，而是谁能够将 AI 工具真正融入并重塑自己的工作流。

当你把上面 Hermes 的这些隐藏能力全部激活，让它们与你的飞书自动化推送、本地文件系统深度联动，并且掌控整个信息流向时，你得到的就不再是一个聪明的「应答机」了，而是一个真正能够 7x24 小时自我运转、持续进化的跨平台超级助理。

**既然看到这儿了，如果觉得还不错，帮忙随手点个「赞」、「在看」、「转发」三连；如果想第一时间收到推送，也可给我加个星标★，非常感谢！**
