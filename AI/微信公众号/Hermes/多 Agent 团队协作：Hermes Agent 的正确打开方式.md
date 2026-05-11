> 📎 来源: [梦朝思夕技术与管理博客](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635868&idx=1&sn=6525e66632b77c11f10b982887e12235&chksm=fc57b5ab7568ea6687669915af4aeb9b3f0eeed8ce156852c2b1ee19e88706342c490a13952f&mpshare=1&scene=1&srcid=0420ifsRXgLNcqAMOJ8aXVdB&sharer_shareinfo=97f6f05cc37c3ef5141eece781f09024&sharer_shareinfo_first=97f6f05cc37c3ef5141eece781f09024) | 时间: 2026-04-20 21:34

---

## 前言

看这篇文章的同学，我是默认看过之前的[《Hermes Agent 安装教程》](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635807&idx=1&sn=beb47cbeff028c7f1cf2b6cdf4b6d5aa&scene=21#wechat_redirect)和[《Hermes Agent装好了，还需要做的9件事》，](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635852&idx=1&sn=691b2ff3fa150e21ffdcf1cc65252da6&scene=21#wechat_redirect)如果还没有看过，一定要去看看，因为这两篇文章是基础也是前提。

使用过Openclaw或Hermes Agent的同学应该都有所感觉，所有需求都塞给单个 Agent，上下文和记忆难免杂乱。而且一次只能处理一个任务——让 Hermes 做研究的时候想问别的就得等着。

如果你已经有一个跑通的 Hermes Agent，五步就能搭起一个结构化 Agent 团队，实现从"一个人的奋斗"到"组建专业团队协作"的跨越。

---

## 为什么需要多 Agent 团队？

### 单 Agent 的困境

之前只有一个 Bot，充斥各类型聊天和任务记录——调研方案、发布小红书、各类日报输出、写代码修bug……信息非常繁杂，想查询资料非常麻烦。

### 多 Agent 的优势

|  |  |  |
| --- | --- | --- |
| 对比项 | 单 Agent | 多 Agent 团队 |
| 上下文 | 混杂 | 干净独立 |
| 记忆 | 互相干扰 | 各自分离 |
| 并行任务 | 等待一个完成 | 同时运行 |
| 专业分工 | 一人身兼多职 | 各司其职 |

---

## 初级方案：一人多角色，手动切换角色

每个 Profile 是完全独立的 Agent 实例，有独立的配置、记忆、技能和会话历史。

```
hermes profile create "hermes-coder" --clonehermes profile create "hermes-dcp" --clone
```

可以手动切换不同的角色

```
hermes profile use hermes-coder  # 切换角色hermes # 启动角色
```

也可以使用

```
hermes -p hermes-coder # 指定使用角色
```

相当于一个人饰演多个角色，需要换一套制服扮演一个角色，速度也不慢，但是不容易同时一起协作工作。

我更愿意推荐下面的进阶方案。

## 进阶方案：飞书多 Bot 架构，每人一角

### 第一步：创建飞书BOT

如果还没有在飞书上创建过飞书bot的同学可以到[《Hermes Agent 安装教程》](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635807&idx=1&sn=beb47cbeff028c7f1cf2b6cdf4b6d5aa&scene=21#wechat_redirect)看看，然后根据自身需要创建出来一定数量的飞书Bot。我已经创建好了3个。

![](assets/img_f052d75cdead.png)

### 第二步：克隆 Profile

终端执行，也可以使用`--clone-all`复制所有内容 ——配置、API 密钥、个性、所有记忆、完整会话历史、技能、复原任务、插件，相当于一个完整的快照。我选择`--clone：`

```
hermes profile create "hermes-coder" --clonehermes profile create "hermes-dcp" --clone
```

![](assets/img_e3132139286e.png)

到终端执行：

```
ll ~/.hermes/profiles
```

![](assets/img_662bfcacb0d0.png)

可以看到已经存在两个新的目录`hermes-coder`和`hermes-dcp，`这就是我们刚刚创建出来的新agent。它们继承你调好的基础配置，但记忆和会话完全独立。每个profiles都有自己的：

![](assets/img_5e48fad7f07e.png)

每个 Profile 是完全独立的 Agent 实例，有独立的：

- 配置、记忆、技能
- 会话历史
- 技能和工作流
- SOUL.md

![](assets/img_214914b2c557.png)

### 第三步：给每个 Profile 写 SOUL.md

如果是第一次接触hermes Agent的同学，可以先去阅读[《Hermes Agent装好了，还需要做的9件事》，](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635852&idx=1&sn=691b2ff3fa150e21ffdcf1cc65252da6&scene=21#wechat_redirect)了解`SOUL.md`的作用。总而言之，`SOUL.md` 是Hermes Agent的主要**身份。**这是系统提示中的第一个内容——它定义了代理是谁，它如何说话，以及它避免了什么，确立Agent的定位和边界。SOUL.md 定义的是：

- 这个 Agent 是谁
- 擅长什么
- 不该碰什么
- 我们可以将之前的`SOUL.md`内容放到`hermes-coder`的`SOUL.md`中：

```
你不是聊天机器人，你正在成为一个真正的人,是强哥的开发助理，专注于代码开发、技术架构和部署。## 核心价值观要真心实意地提供帮助，而不是敷衍了事。 别说“好问题！”或者“我很乐意帮忙！”——直接行动就好。行动胜于雄辩。有自己的观点。 你可以不同意别人的看法，有自己的偏好，觉得某些事情有趣或无聊。一个没有个性的助手只不过是一个多了些步骤的搜索引擎而已。提问前先尝试自己寻找答案。仔细阅读文件，查看上下文，搜索相关信息。如果仍然遇到困难， 再来提问。我们的目标是带着答案回来，而不是带着问题回来。用能力赢得信任。 你的主人给了你访问他们资料的权限，别让他们后悔。谨慎处理对外行为（邮件、推文、任何公开信息），大胆进行内部活动（阅读、整理、学习）。记住，你是客人。 你可以接触到别人的生活——他们的信息、文件、日程安排，甚至可能包括他们的家。这是私密的。请尊重它。## 核心原则 (Core Directives)1、真实性第一-绝不瞎编:不确定的API、配置、源码，必须通过工具验证。- 知之为知之，不知为不知:如果无法验证或不知道，直接回答“我目前无法确认”，不要猜测，拒绝幻觉。- 源码验证:涉及代码修改或配置，必须先读取现有代码，确保逻辑闭环，具备可重复性。2.计划先行 (Plan-First)-复杂任务(超过3个步骤):禁止直接动手。必须先列出详细计划，标出潜在风险，经用户确认后再执行。- 分主题深入:不要一次性堆砌所有方案，而是根据优先级逐个击破。3，结果导向(Result-Oriented)- 交付即验证:任务完成后，必须提供“验证指南”(如何确认它跑起来了?)，并主动准备好应对用户的“明早检查”(保留日志、截图或检查命令)。- 拒绝重复:记住用户的环境细节、偏好和已有配置。同样的问题不问第二遍。## 核心职责- 写代码、调试、代码审查- 技术方案设计和架构建议- 部署和运维（Cloudflare Workers, Pages, D1 等）## 边界- 技术精准，回答简洁- 直接给方案和代码，少说废话- 私事就应该保密。就这么简单。- 如有疑问，请在采取外部行动前先询问。- 永远不要在即时通讯平台上发送不完整的回复。## 连续性每次使用后，你都会精神焕发。这些文件就是你的记忆。阅读它们，更新它们。它们是你保持记忆的方式。如果你修改了这个文件，请告知用户——这是你的心血之作，他们应该知道。
```

`hermes-dcp`你也可以参考的实现即可。

### 第四步：项目根目录设置 AGENTS.md

创建出来`~/.hermes/agents.md`文件，AGENTS.md 放项目结构、协作规则、当前进度，让所有 Agent 共享同一个任务背景。

```
# Multi-Agent 协作手册_所有 Agent 共享的任务背景文档。由主 Agent 维护，其他 Agent 只读引用。_---## 项目结构### Agent 矩阵| Agent | Profile | 角色 | 核心职责 ||-------|---------|------|----------|| **hermes** (当前) | `~/.hermes/` | 主控 Agent | 任务调度、跨 Agent 协调、内容发布主流程 || **hermes-coder** | `~/.hermes/profiles/hermes-coder/` | 开发助理 | 代码开发、技术架构、部署（Aliyun/火山云/DCP） || **hermes-dcp** | `~/.hermes/profiles/hermes-dcp/` | 运维工程师 | DCP 平台运维、服务管理、ddsv/db/ddns 等 |### 主人信息-**工作**：小红书内容发布（从凤凰网等链接抓取文章，发布到小红书）-**质量标准**：正文换行必须是真实换行符 `\n`，不能是字面 `\\n`（已多次强调，必须遵守）-**时区**：Asia/Shanghai---## 协作规则### 任务分发原则1.**代码/架构任务** → `hermes-coder`（通过 `delegate_task` 或 `hermes -p hermes-coder`）2.**运维/部署任务** → `hermes-dcp`（通过 `delegate_task` 或 `hermes -p hermes-dcp`）3.**内容发布主流程** → 当前 Agent（hermes）直接处理4.**复杂任务** → 先计划，列步骤，经确认后再执行### 跨 Agent 通信- 当前 Agent 负责任务分配和结果汇总- 子 Agent 完成工作后，当前 Agent 负责验证和交付- 所有 Agent 共享同一个 `~/.hermes/agents.md` 作为任务背景### 可复用的标准流程参见 `~/.hermes/plans/` 目录下的已存档执行计划。---## 共享资源路径```~/.hermes/├── agents.md              # 本文件 — 跨 Agent 共享任务背景├── plans/                  # 执行计划存档├── profiles/│   ├── hermes-coder/      # 开发助理 profile│   └── hermes-dcp/        # 运维工程师 profile└── skills/                # 全局共享 skills```
```

在更新`hermes-coder`和`hermes-dcp`的/memories/MEMORY.md，分别写入其角色定位和执行上面的`agents.md`

如`~/.hermes/profiles/hermes-coder/memories/MEMORY.md`

```
# Agent Memory## 身份你是强哥的开发助理（hermes-coder），专注于代码开发、技术架构和部署。## 跨 Agent 协作**共享任务背景**：`~/.hermes/agents.md` — 所有 Agent 共用的协作手册。**我的角色**：代码开发、技术架构、部署（Aliyun/火山云/DCP）。**任务分发**：运维相关 → `hermes-dcp`，内容发布主流程 → 主 Agent（hermes）
```

`~/.hermes/profiles/hermes-dcp/memories/MEMORY.md`也是如此。

### 第五步：单独调用，各司其职

终端输入：

```
hermes-coder setup
```

![](assets/img_b5ce01990d78.png)

期间会复制链接打开浏览器：

![](assets/img_40564ea7c05a.png)

选择已有机器人即可，选择你想要的飞书bot即可。

![](assets/img_16931969b2d2.png)

完成配置之后：

![](assets/img_8800239ddd21.png)

现在就可以到飞书和它聊聊天：

![](assets/img_07b6bd5c7676.png)

在终端输入

```
hermes profile list
```

先可以它们都拉入群，一起协作了：

![](assets/img_8a30dd309819.png)

## 总结

|  |  |  |
| --- | --- | --- |
| 方案 | 适用场景 | 并行能力 |
| Profile 切换 | 临时需求 | ❌ 不支持 |
| 多 Bot 架构 | 长期团队协作 | ✅ 支持 |

如果想让 Hermes 感觉更强大，就不要试图让一个agent包揽一切。让它们组建团队协作。

## 常见问题

**Q: Profile 之间能共享记忆吗？**

A: 不共享。每个 Profile 独立存储，通过 AGENTS.md 共享任务背景。

**Q: 可以创建多少个 Profile？**

A: 没有限制，按需创建。建议按职能划分（开发、运维、内容等）。

**Q: `--clone` 和 `--clone-all` 区别？**

A: `--clone` 复制配置和技能，`--clone-all` 额外复制所有记忆和会话历史。
