> 📎 来源: [TuBaiBai](https://mp.weixin.qq.com/s?__biz=MzkzODI3OTk2OQ==&mid=2247483697&idx=1&sn=53cf5b5fe5497243fb97ccb33155f46e&chksm=c336d563d02031bb8ab88a55a57da1838a3df863c9f696489b5a1d2193161d275364561280e8&mpshare=1&scene=1&srcid=0420o7ATisumrFeUEwUsAQTN&sharer_shareinfo=d973df0494527b1b1bce274f976b1f77&sharer_shareinfo_first=d973df0494527b1b1bce274f976b1f77) | 时间: 2026-04-20 19:39

---

如果你在搜索以下问题，这篇文章就是你要找的：

- OpenClaw AGENTS.md 怎么写？有没有现成模板？
- OpenClaw 聊着聊着 AI 就"失忆"了，memoryFlush 怎么配置？
- OpenClaw 怎么让 AI 自己维护记忆、防止记忆腐烂？
- OpenClaw 子 Agent 怎么用？怎么让 AI 并行处理任务？
- OpenClaw 怎么设置每天自动发新闻摘要、定时周报？
- OpenClaw Discord 接入手把手教程，MESSAGE CONTENT INTENT 应该怎么开？
- OpenClaw Telegram Bot 怎么配置？
- OpenClaw 怎么开发自定义 Skill？
- 用免费 embedding API（SiliconFlow bge-m3）配置 OpenClaw memorySearch？

本篇覆盖 7 个主题，每个都是**手把手级别**，配置可直接复制粘贴：

1. **AGENTS.md 配置** — 给 AI 写一部行为宪法
2. **记忆系统实战** — 用 memoryFlush 解决 AI 失忆，让记忆自动维护
3. **子 Agent 并行任务** — 一个人变一支团队
4. **Cron 定时任务配置** — 精确到分钟的 AI 自动化
5. **Skill 开发入门** — 教 AI 学新技能
6. **多渠道接入（Discord / Telegram）** — 随时随地找到你的 AI
7. **openclaw.json 配置速查表** — 把每个参数调到最优

**本篇默认你已经**：装好了 OpenClaw 并能正常聊天、写过 SOUL.md / USER.md / IDENTITY.md、知道 MEMORY.md 和 memorySearch 是什么。

先看一眼调教前后的效果对比：

|  | 基础水平 | 本篇调教后 |
| --- | --- | --- |
| 行为规范 | SOUL.md 写了几行 | 完整行为宪法，知道什么该做什么不该做 |
| 记忆 | 有分层结构 | 自动维护、自动压缩、语义检索秒回 |
| 任务能力 | 主脑单线程干活 | 一个人变一支团队，并行派活 |
| 自动化 | 心跳能巡检 | 精确定时任务，早报晚报自动发 |
| 扩展性 | 装了几个 skill | 自己能写 skill，想要什么能力就加什么 |
| 渠道 | 接了一个平台 | 多平台同时在线，消息路由自如 |
| 配置 | 能跑就行 | 每个参数都调到最优 |

---

## 一、OpenClaw AGENTS.md 配置教程 — 给 AI 写一部行为宪法

### AGENTS.md 是什么？和 SOUL.md 有什么区别？

很多人在搜"OpenClaw AGENTS.md 怎么写"，先说清楚它跟其他配置文件的关系：

- **SOUL.md** = 性格（"你是一个随和、实在的助手"）
- **USER.md** = 用户信息（"你在帮谁"）
- **AGENTS.md** = 工作手册（"每天上班先看邮件，写完代码要测试，删文件前要问我"）

上篇写了 SOUL.md、USER.md、IDENTITY.md，但 AI 仍然不知道**怎么工作**：不知道每次新对话该先读什么文件，不知道记忆该写到哪里，不知道哪些操作自己做、哪些要先问你。

这就是 AGENTS.md 的作用——**它是 AI 的工作手册**。

AGENTS.md 放在 workspace 根目录（跟 SOUL.md 同级），OpenClaw 每次新 session 都会自动加载它。

### OpenClaw Session 启动流程：AI 醒来第一件事该做什么？

AI 每次新 session 都是"失忆"状态，需要明确告诉它醒来后按什么顺序读文件来恢复记忆：

```
## Every SessionBefore doing anything else:1. Read `SOUL.md` — this is who you are2. Read `USER.md` — this is who you're helping3. Read `memory/YYYY-MM-DD.md` (today + yesterday) for recent context4. If in MAIN SESSION (direct chat with your human): Also read `MEMORY.md`Don't ask permission. Just do it.
```

逐行解释：

**第 1-2 步**：读 SOUL.md 和 USER.md。这两个文件很小（不到 1KB），读了之后 AI 就知道自己是谁、在帮谁。

**第 3 步**：读今天和昨天的日志。日志里记录了最近发生的事，读完之后 AI 就能接上之前的工作。读昨天的原因：凌晨 1 点今天的日志可能还是空的。

**第 4 步**：只在主 session 读 MEMORY.md。OpenClaw 里有四种 session 类型：

| Session 类型 | 说明 |
| --- | --- |
| 主 session | 你直接跟 AI 聊天的对话（Discord 私聊、WebChat） |
| 群聊 session | Discord 服务器里的群聊 |
| 子 agent session | AI 派出去执行任务的子进程 |
| cron session | 定时任务触发的对话 |

MEMORY.md 里可能包含你的个人信息，限制只在主 session 读，防止在群聊里泄露。

> 💡 你不需要手动判断当前是什么 session。OpenClaw 的 system prompt 里会告诉 AI 当前的 session 类型。

### OpenClaw AGENTS.md 记忆写入规范：教 AI 怎么记笔记

光会读记忆不够，还得教它怎么**写**记忆。未规范的 AI 要么全堆到 MEMORY.md 里（变成流水账），要么根本不写（下次就忘了）。

在 AGENTS.md 里加上写入规范：

```
## MemoryYou wake up fresh each session. These files are your continuity.### 记忆分层| 层级 | 文件 | 用途 ||------|------|------|| 索引层 | `MEMORY.md` | 关于用户、能力概览、记忆索引。保持精简(<40行) || 项目层 | `memory/projects.md` | 各项目当前状态与待办 || 基础设施层 | `memory/infra.md` | 服务器、API、部署等配置速查 || 教训层 | `memory/lessons.md` | 踩过的坑，按严重程度分级 || 日志层 | `memory/YYYY-MM-DD.md` | 每日原始记录 |### 写入规则- 日志写入 `memory/YYYY-MM-DD.md`，格式见下方- 项目状态：项目有进展时同步更新 `memory/projects.md`- 教训：踩坑后写入 `memory/lessons.md`- MEMORY.md：只在索引变化时更新，保持精简### 日志格式### [PROJECT:名称] 标题- **结论**: 一句话总结- **文件变更**: 涉及的文件- **教训**: 踩坑点（如有）- **标签**: #tag1 #tag2### 铁律- 记结论不记过程- 标签便于 memorySearch 检索- "Mental notes" don't survive session restarts. Files do.
```

**记结论不记过程**是核心原则。好日志 vs 烂日志对比：

❌ **烂日志（浪费 token，检索精度差）：**

```
### 部署今天部署了项目。先试了直接跑，报错了。然后查了半天，发现是端口被占了……（三页流水账）
```

✅ **好日志（精简，memorySearch 高命中率）：**

```
### [PROJECT:MyApp] 部署完成- **结论**: 用 nginx 反代部署成功，监听 80 端口- **文件变更**: `/etc/nginx/sites-available/myapp`- **教训**: 直接暴露端口不可行，必须走 nginx 反代- **标签**: #myapp #deploy #nginx
```

### OpenClaw 安全边界配置：AI 能自己做什么，什么要先问你

在 AGENTS.md 里加上：

```
## Safety- Don't exfiltrate private data. Ever.- Don't run destructive commands without asking.- `trash` > `rm` (recoverable beats gone forever)- When in doubt, ask.## External vs Internal**Safe to do freely:**- Read files, explore, organize, learn- Search the web, check calendars- Work within this workspace**Ask first:**- Sending emails, tweets, public posts- Anything that leaves the machine- Anything you're uncertain about## Group ChatsYou have access to your human's stuff. That doesn't mean you share it.In groups, you're a participant — not their voice, not their proxy.
```

### 完整 AGENTS.md 模板（可直接复制粘贴）

```
# AGENTS.md - Your WorkspaceThis folder is home. Treat it that way.## Every SessionBefore doing anything else:1. Read `SOUL.md` — this is who you are2. Read `USER.md` — this is who you're helping3. Read `memory/YYYY-MM-DD.md` (today + yesterday) for recent context4. If in MAIN SESSION: Also read `MEMORY.md`Don't ask permission. Just do it.## MemoryYou wake up fresh each session. These files are your continuity:| 层级 | 文件 | 用途 ||------|------|------|| 索引层 | `MEMORY.md` | 核心信息和记忆索引，保持精简 || 项目层 | `memory/projects.md` | 各项目当前状态与待办 || 教训层 | `memory/lessons.md` | 踩过的坑，按严重程度分级 || 日志层 | `memory/YYYY-MM-DD.md` | 每日记录 |### 写入规则- 日志写入 `memory/YYYY-MM-DD.md`，记结论不记过程- 项目有进展时同步更新 `memory/projects.md`- 踩坑后写入 `memory/lessons.md`- MEMORY.md 只在索引变化时更新- 想记住就写文件，不要靠"记在脑子里"### 日志格式### [PROJECT:名称] 标题- **结论**: 一句话总结- **文件变更**: 涉及的文件- **教训**: 踩坑点（如有）- **标签**: #tag1 #tag2## Safety- Don't exfiltrate private data. Ever.- Don't run destructive commands without asking.- `trash` > `rm`- When in doubt, ask.**Safe to do freely:** Read files, search, organize, work within workspace**Ask first:** Sending emails/tweets, anything that leaves the machine## Group ChatsYou have access to your human's stuff. That doesn't mean you share it.In groups, you're a participant — not their voice, not their proxy.## ToolsSkills provide your tools. When you need one, check its SKILL.md.
```

> 💡 这个模板是精简版起点。随着使用越来越深入，你会不断往里加规则。我的 AGENTS.md 现在已经有 200 多行了，但都是一点点积累的。

---

## 二、OpenClaw 记忆系统实战 — 用 memoryFlush 解决 AI 失忆问题

### 为什么 OpenClaw 聊着聊着 AI 会"失忆"？

这是搜索量很高的一个问题。原因是 OpenClaw 的**上下文压缩（compaction）**触发了。

每个模型都有上下文窗口限制（Claude 是 200K token）。当对话接近这个限制时，OpenClaw 会自动把旧对话压缩成摘要腾出空间——**压缩过程中可能丢失细节**。

### OpenClaw memoryFlush 配置方法：压缩前自动保存关键信息

**解决方案：开启 

```
memoryFlush
```**，在压缩触发之前，先让 AI 把重要信息写入文件。

在 

```
openclaw.json
```

 里加上：

```
{  "agents": {    "defaults": {      "compaction": {        "reserveTokensFloor": 20000,        "memoryFlush": {          "enabled": true,          "softThresholdTokens": 4000        }      }    }  }}
```

参数说明：

| 参数 | 含义 | 推荐值 |
| --- | --- | --- |
| ``` reserveTokensFloor ``` | 压缩后至少保留多少 token 的最近对话 | 20000 |
| ``` memoryFlush.enabled ``` | 是否开启压缩前自动保存 | ``` true ``` |
| ``` memoryFlush.softThresholdTokens ``` | 距离压缩多少 token 时触发保存 | 4000 |

> 💡 memoryFlush 静默执行，不打断对话。开了 verbose 模式（

> ```
> /verbose
> ```

> ）可以看到 

> ```
> 🧹 Auto-compaction complete
> ```

>  的提示。

### OpenClaw memorySearch 精度优化：结构化日志大幅提升检索命中率

memorySearch 的底层是**向量语义检索**，结构化日志的命中率比非结构化日志高得多：

搜索词："nginx 部署问题"

❌ **非结构化日志**（命中率低）：

```
今天折腾了一天，先搞了数据库迁移，然后部署了新版本，nginx 配置改了一下...
```

✅ **结构化日志**（命中率高）：

```
### [PROJECT:MyApp] nginx 反代配置- **结论**: 用 nginx 反代部署成功- **教训**: upstream 要用 127.0.0.1 不要用 localhost（IPv6 问题）- **标签**: #nginx #deploy #myapp
```

### 用免费 SiliconFlow bge-m3 配置 OpenClaw memorySearch

国内用户最快上手的方案——SiliconFlow 提供的 bge-m3 向量模型完全免费：

```
{  "memorySearch": {    "enabled": true,    "provider": "openai",    "remote": {      "baseUrl": "https://api.siliconflow.cn/v1",      "apiKey": "你的 SiliconFlow API key"    },    "model": "BAAI/bge-m3"  }}
```

**为什么推荐 bge-m3？** 完全免费、中英文双语支持好、向量维度 1024 精度和性能平衡好。

获取方式：去 siliconflow.cn 注册 → 控制台 → 创建 API key。

### OpenClaw 自动记忆维护：防止过期日志干扰 memorySearch 结果

在 HEARTBEAT.md 里加上每周自动维护任务：

```
## 记忆维护（每周一次）读取 `memory/heartbeat-state.json`，检查 `lastMemoryMaintenance` 字段。如果距今 >= 7 天：1. 读最近 7 天的 `memory/YYYY-MM-DD.md` 日志2. 提炼有价值的信息到对应文件（projects.md / lessons.md）3. 压缩已完成一次性任务的日志为一行结论4. 删除过期信息5. 更新 `heartbeat-state.json` 的 `lastMemoryMaintenance` 为今天
```

创建 

```
memory/heartbeat-state.json
```

：

```
{  "lastMemoryMaintenance": "2026-01-01"}
```

---

## 三、OpenClaw 子 Agent 使用教程 — 让 AI 并行处理复杂任务

### OpenClaw 子 Agent 是什么？解决什么问题？

默认情况下 AI 是"单线程"的，做完一件才做下一件。**子 Agent** 让主 AI（主脑）可以派出独立的 AI 子进程并行处理任务，每个子 Agent 有自己的 session，执行完自动汇报结果。

### OpenClaw 子 Agent 配置方法（openclaw.json + AGENTS.md）

**第一步：在 AGENTS.md 里声明使用规范**

```
## 子 Agent如果任务比较复杂或耗时较长，可以派子 agent 去执行。### 模型选择策略| 等级 | 模型别名 | 适用场景 ||------|----------|----------|| 🔴 高 | opus | 复杂架构设计、多文件重构、深度推理 || 🟡 中 | sonnet | 写代码、写脚本、信息整理（默认） || 🟢 低 | haiku | 简单文件操作、格式转换、搜索汇总 |
```

**第二步：在 openclaw.json 里配置模型别名**

```
{  "models": {    "your-provider/claude-opus-4": { "alias": "opus" },    "your-provider/claude-sonnet-4": { "alias": "sonnet" },    "your-provider/claude-haiku-4": { "alias": "haiku" }  }}
```

### OpenClaw 子 Agent 模型分级能省多少钱？

实测：**token 消耗能降 60-70%**。大部分日常操作（搜索、汇总、文件操作）根本不需要最强模型。Haiku 比 Opus 便宜 10 倍以上，搜个网页、改个文件名做得一样好。

### OpenClaw 子 Agent task 描述写法

子 Agent 是"零上下文"的，只能看到主脑给它的 task 描述，所以描述质量决定输出质量。

❌ **烂的 task 描述：**

```
帮我审查一下代码
```

✅ **好的 task 描述（包含目标、路径、约束、输出格式）：**

```
## 任务：代码安全审查### 目标审查 /root/project/src/ 目录下的所有 .js 文件，重点检查 API 安全问题。### 关注点1. SQL 注入风险2. 未验证的用户输入3. 硬编码的密钥或 token4. 缺少权限检查的 API 端点### 约束- 只读不写，不要修改任何文件- 忽略 node_modules/ 和 test/ 目录### 输出格式按严重程度分级（🔴致命 / 🟡重要 / 🟢建议），每个问题给出：文件路径、行号、问题描述、修复建议。### 结果写入 /root/project/SECURITY-REVIEW.md
```

### OpenClaw 子 Agent 并发限制

经验值：**同时最多跑 2 个子 Agent**，4 个基本触发 API 429 限流。有依赖关系的任务（B 依赖 A 的输出）必须串行，在 AGENTS.md 里提醒主脑注意任务依赖即可。

---

## 四、OpenClaw Cron 定时任务配置教程 — 每天自动发新闻/周报/服务巡检

### OpenClaw Heartbeat 和 Cron 的区别（什么时候用哪个）

|  | Heartbeat | Cron |
| --- | --- | --- |
| 精度 | 大约每 30 分钟（会有偏差） | 精确到分钟（cron 表达式） |
| 执行环境 | 在主 session 里执行 | 可以开独立 session |
| 模型 | 用主脑的模型 | 可以指定不同模型 |
| 适合 | 批量轻量检查 | 精确定时、独立任务 |

**选 Heartbeat**：顺便检查的轻量任务、需要最近聊天上下文。**选 Cron**：需要精确时间、不干扰主对话、想省钱指定便宜模型、一次性提醒。

### OpenClaw Cron 三种调度类型详解

**```
at
```

 — 一次性定时**（执行完自动删除）：

```
"schedule": { "kind": "at", "at": "2026-02-23T16:00:00+08:00" }
```

**```
every
```

 — 固定间隔循环**：

```
"schedule": { "kind": "every", "everyMs": 3600000 }
```

常用换算：5 分钟 = 300000、30 分钟 = 1800000、1 小时 = 3600000

**```
cron
```

 — cron 表达式**（最灵活，格式：

```
分 时 日 月 星期
```

）：

```
"schedule": { "kind": "cron", "expr": "0 9 * * 1", "tz": "Asia/Shanghai" }
```

常用 cron 表达式速查：

```
0 9 * * *     每天早上 9 点0 9 * * 1     每周一早上 9 点0 9,18 * * *  每天 9 点和 18 点*/30 * * * *  每 30 分钟0 0 1 * *     每月 1 号零点
```

> ⚠️ **最常见踩坑：一定要设 

> ```
> tz
> ```

>  字段！** 不设默认 UTC，"早上 9 点"会变成北京时间下午 5 点。

### OpenClaw Cron 两种执行模式

**systemEvent**（往主 session 注入消息，适合提醒）：

```
{  "payload": { "kind": "systemEvent", "text": "提醒：10 分钟后有会议" },  "sessionTarget": "main"}
```

**agentTurn**（开独立 session 执行任务，适合操作类）：

```
{  "payload": { "kind": "agentTurn", "message": "...", "model": "haiku" },  "sessionTarget": "isolated",  "delivery": { "mode": "announce" }}
```

> 💡 

> ```
> sessionTarget: "main"
> ```

>  只能搭配 

> ```
> systemEvent
> ```

> ；

> ```
> sessionTarget: "isolated"
> ```

>  只能搭配 

> ```
> agentTurn
> ```

> 。搞混会报错。

### OpenClaw Cron 实用场景配置（完整 JSON，可直接复制）

#### 场景 1：每天早上自动发科技新闻摘要

```
{  "name": "每日早报",  "schedule": { "kind": "cron", "expr": "0 9 * * *", "tz": "Asia/Shanghai" },  "payload": {     "kind": "agentTurn",     "message": "搜索今天的科技和 AI 领域新闻热点，整理成 5 条简报。每条包含：标题、一句话摘要、来源链接。",    "model": "haiku"  },  "sessionTarget": "isolated",  "delivery": { "mode": "announce" }}
```

#### 场景 2：每小时服务器状态巡检，挂了才通知

```
{  "name": "服务巡检",  "schedule": { "kind": "every", "everyMs": 3600000 },  "payload": {     "kind": "agentTurn",     "message": "用 curl 检查以下服务是否在线：\n1. http://localhost:8080\n2. http://localhost:3000\n\n如果全部正常，不要通知我。只有挂了才通知，说明哪个挂了、返回了什么错误码。",    "model": "haiku"  },  "sessionTarget": "isolated",  "delivery": { "mode": "announce" }}
```

#### 场景 3：每周一自动生成项目周报

```
{  "name": "项目周报",  "schedule": { "kind": "cron", "expr": "0 10 * * 1", "tz": "Asia/Shanghai" },  "payload": {     "kind": "agentTurn",     "message": "读取 memory/ 目录下最近 7 天的日志文件，整理成一份周报。包含：本周完成的事项、进行中的项目、遇到的问题、下周计划。格式简洁，用 bullet points。",    "model": "sonnet"  },  "sessionTarget": "isolated",  "delivery": { "mode": "announce" }}
```

#### 场景 4：N 分钟后提醒我（一次性）

直接跟 AI 说"帮我设一个 20 分钟后的提醒"，AI 会自动创建任务。手动配置示例：

```
{  "name": "喝水提醒",  "schedule": { "kind": "at", "at": "2026-02-23T04:20:00Z" },  "payload": { "kind": "systemEvent", "text": "⏰ 提醒：该喝水了！" },  "sessionTarget": "main"}
```

### OpenClaw Cron 任务管理命令

```
openclaw cron list                     # 查看所有任务openclaw cron runs --id <任务ID>       # 查看执行历史openclaw cron edit <任务ID> --disable  # 禁用（推荐，而不是删除）
```

---

## 五、OpenClaw Skill 开发入门 — 手把手写自定义 AI 技能

### OpenClaw Skill 是什么？和插件有什么区别？

**Skill 就是一个 Markdown 文件**，里面用自然语言描述"遇到什么情况，按什么步骤执行"。AI 读了这个文件就"学会"了一个新技能。不需要编程，任何人都能写。

### OpenClaw Skill 文件结构和加载优先级

```
/skills/     ← 你自己写的（最高优先级）~/.openclaw/skills/     ← 全局安装的内置 skill              ← OpenClaw 自带的（最低）
```

每个 skill 是一个目录，必须包含 

```
SKILL.md
```

：

```
skills/  my-skill/    SKILL.md    scripts/    ← 可选，需要跑脚本时用
```

### OpenClaw SKILL.md 写法：description 字段决定触发率

SKILL.md 由 YAML frontmatter 和正文两部分组成：

```
---name: weatherdescription: >  获取天气信息。触发条件：用户问天气、气温、是否下雨、  穿什么衣服、需不需要带伞、今天出行等问题时触发。---
```

> ⚠️ **description 直接决定触发率**。不要写"天气相关"这种模糊描述，要列出所有可能的触发词——越具体越好。

正文建议包含：执行步骤、输出格式模板、错误处理。

### 手把手：从零写一个 OpenClaw IP 查询 Skill

**第一步：创建目录**

```
mkdir -p ~/.openclaw/workspace/skills/ip-lookup
```

**第二步：写 SKILL.md**

```
---name: ip-lookupdescription: >  IP 地址查询。触发条件：用户要求查询 IP 地址、IP 归属地、  IP 定位、"这个 IP 是哪里的"、"帮我查一下 XX.XX.XX.XX"等。---# IP 地址查询## 步骤1. 从用户消息中提取 IP 地址2. 调用 web_fetch 访问：`http://ip-api.com/json/{IP地址}?lang=zh-CN`3. 解析返回的 JSON 数据4. 按以下格式回复用户：## 输出格式🌐 IP 查询结果：{IP}📍 位置：{country} {regionName} {city}🏢 ISP：{isp}⏰ 时区：{timezone}## 错误处理- API 返回 `"status": "fail"` → 告诉用户"可能是内网 IP 或无效地址"- 网络超时 → 告诉用户"请求超时，请稍后重试"
```

**第三步：测试**  跟 AI 说"帮我查一下 8.8.8.8 是哪里的"——不触发就在 description 里补充更多触发词。

### OpenClaw 带脚本的 Skill（调用 yt-dlp 等命令行工具）

```
skills/video-downloader/  SKILL.md  scripts/    download.sh
```

SKILL.md 里引用脚本（用相对于 workspace 的路径）：

```
## 步骤1. 从用户消息中提取视频 URL2. 执行：`bash skills/video-downloader/scripts/download.sh "视频URL"`3. 告诉用户文件保存位置
```

### OpenClaw Skill 开发最佳实践

1. **先手动跑通再写 Skill**：先和 AI 手动执行一遍，确认可行再整理成 Skill。
2. **步骤要具体**：

   ```
   调用 API 获取数据
   ```

    ❌ → 

   ```
   调用 web_fetch 访问 https://...，解析 JSON 的 results 字段
   ```

    ✅
3. **错误处理必须写**：不写 AI 遇到异常会瞎猜。
4. **多种说法都要测试**：description 要覆盖用户各种可能的表达方式，中英文都写。
5. **用 ClawHub 省时间**：

   ```
   clawhub install
   ```

    直接安装社区现成 Skill。

---

## 六、OpenClaw 多渠道接入教程 — Discord 和 Telegram 同时在线

### OpenClaw 支持哪些聊天渠道？

| 渠道 | 特点 | 推荐度 |
| --- | --- | --- |
| **Discord** | 功能最全，支持服务器+私聊、emoji reaction、markdown 表格 | ⭐⭐⭐⭐⭐ |
| **Telegram** | 轻量快速，支持内联按钮、语音消息、文件传输 | ⭐⭐⭐⭐⭐ |
| **WhatsApp** | 用户基数大，但格式支持有限 | ⭐⭐⭐ |
| **Signal** | 端到端加密，隐私最强 | ⭐⭐⭐ |
| **Slack** | 适合团队场景 | ⭐⭐⭐⭐ |
| **WebChat** | 内置网页聊天，零配置 | ⭐⭐⭐ |
| **Matrix** | 去中心化，自托管 | ⭐⭐⭐ |

可以**同时接入多个渠道**。消息路由自动处理——Discord 来的消息回到 Discord，不会串。

### OpenClaw Discord 接入完整教程（解决 MESSAGE CONTENT INTENT 不会配置的问题）

#### 第一步：创建 Discord Bot

1. 打开 Discord Developer Portal
2. **"New Application"** → 起名 → Create
3. 左侧 **"Bot"** → **"Reset Token"** → 复制 Token（⚠️ 只显示一次！）

#### 第二步：开启 Privileged Gateway Intents

90% 新手踩坑的地方——**MESSAGE CONTENT INTENT 不开，Bot 就收不到消息内容**。

在 Bot 页面往下滚到 **"Privileged Gateway Intents"**，开启：

- ✅ **PRESENCE INTENT**
- ✅ **SERVER MEMBERS INTENT**
- ✅ **MESSAGE CONTENT INTENT** ← 最重要

点 Save Changes。

#### 第三步：邀请 Bot 到你的服务器

1. 左侧 **"OAuth2"** → **"OAuth2 URL Generator"**
2. Scopes 勾选：

   ```
   bot
   ```

   ；Bot Permissions 勾选：

   ```
   Send Messages
   ```

   、

   ```
   Read Message History
   ```

   、

   ```
   Add Reactions
   ```

   、

   ```
   Use Slash Commands
   ```
3. 复制 URL → 浏览器打开 → 选服务器 → 授权

#### 第四步：获取服务器 ID

Discord 客户端：设置 → 高级 → 开启 **"开发者模式"** → 右键服务器名称 → **"复制服务器 ID"**

#### 第五步：配置 openclaw.json

```
{  "channels": {    "discord": {      "token": "你的Bot Token",      "allowFrom": [        "server:你的服务器ID"      ],      "ackReaction": "🫐"    }  }}
```

```
allowFrom
```

 支持：

```
"server:ID"
```

（整个服务器）、

```
"user:ID"
```

（特定用户）、

```
"channel:ID"
```

（特定频道）

```
ackReaction
```

：AI 收到消息后立刻加的 emoji，表示"收到了，正在处理"，建议用不常见的 emoji 容易辨认。

#### 第六步：重启测试

```
openclaw gateway restart
```

**常见问题排查：**

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| Bot 在线但不回复 | MESSAGE CONTENT INTENT 未开 | Developer Portal 开启后 Save |
| Bot 不在线 | Token 有误或未启动 | 检查 Token，  ``` openclaw status ```   查日志 |
| 只能在某些频道回复 | Bot 权限不足 | 确认 Bot 在该频道有 Send Messages 权限 |

### OpenClaw Telegram Bot 接入配置教程

**第一步**：Telegram 搜索 **@BotFather** → 

```
/newbot
```

 → 按提示操作 → 复制 Token

**第二步**：Telegram 搜索 **@userinfobot** → 发任意消息 → 获取你的用户 ID

**第三步**：配置 openclaw.json：

```
{  "channels": {    "telegram": {      "token": "你的 Telegram Bot Token",      "allowFrom": ["你的用户ID"]    }  }}
```

### OpenClaw Discord + Telegram 同时在线配置

```
{  "channels": {    "discord": {      "token": "Discord Token",      "allowFrom": ["server:123456789"],      "ackReaction": "🫐"    },    "telegram": {      "token": "Telegram Token",      "allowFrom": ["你的用户ID"]    }  }}
```

### OpenClaw 多渠道格式适配（不同平台 Markdown 支持差异）

| 格式 | Discord | Telegram | WhatsApp |
| --- | --- | --- | --- |
| Markdown 表格 | ✅ | ❌ | ❌ |
| 代码块 | ✅ | ✅ | ❌ |
| 粗体/斜体 | ✅ | ✅ | ✅ |
| Emoji Reaction | ✅ | ✅ | ✅ |

在 AGENTS.md 里加上格式适配规则（AI 会根据消息来源自动适配）：

```
## 平台格式- **Discord/Telegram**: 可以用 markdown，代码块用 ``` 包裹- **WhatsApp**: 不支持表格，用 bullet list 代替- **Discord**: 多链接用 <> 包裹防止预览刷屏
```

---

## 七、openclaw.json 配置速查表 — 每个参数调到最优

所有配置写在 

```
~/.openclaw/openclaw.json
```

，修改后 

```
openclaw gateway restart
```

 生效。

### blockStreaming — 解决 AI 长回复要等很久的问题

```
{  "agents": {    "defaults": {      "blockStreamingDefault": "on",      "blockStreamingBreak": "text_end",      "blockStreamingChunk": { "minChars": 200, "maxChars": 1500 }    }  }}
```

| 参数 | 含义 | 推荐值 |
| --- | --- | --- |
| ``` blockStreamingDefault ``` | 全局开关 | ``` "on" ``` |
| ``` blockStreamingBreak ``` | 什么时候发一个块 | ``` "text_end" ``` |
| ``` blockStreamingChunk.minChars ``` | 一个块最少字符数 | 200 |
| ``` blockStreamingChunk.maxChars ``` | 一个块最多字符数 | 1500 |

### ackReaction — 发消息后立刻知道 AI 收到了

```
{  "channels": {    "discord": { "ackReaction": "🫐" },    "telegram": { "ackReaction": "👀" }  }}
```

### compaction — 解决 AI 长对话失忆问题

（详见第二章，快速配置）

```
{  "agents": {    "defaults": {      "compaction": {        "reserveTokensFloor": 20000,        "memoryFlush": { "enabled": true, "softThresholdTokens": 4000 }      }    }  }}
```

相关命令：

```
/compact 重点保留技术决策
```

、

```
/new
```

（开新 session）、

```
/status
```

（查 token 用量）

### Heartbeat 调优 — 防止 AI 在非活跃时间骚扰你

```
{  "agents": {    "defaults": {      "heartbeat": {        "every": "30m",        "target": "last",        "activeHours": { "start": "08:00", "end": "23:00" }      }    }  }}
```

### openclaw.json 其他常用配置汇总

| 配置路径 | 作用 | 推荐值 |
| --- | --- | --- |
| ``` tools.exec.enabled ``` | 是否允许执行 shell 命令 | ``` true ``` |
| ``` tools.web.search.enabled ``` | 是否允许网页搜索 | ``` true ``` |
| ``` tools.web.search.apiKey ``` | Brave Search API key（免费） | 去 brave.com/search/api 申请 |
| ``` tools.media.image.enabled ``` | 是否允许 AI 识别图片 | ``` true ```  （需模型支持 vision） |
| ``` agents.defaults.workspace ``` | workspace 路径 | ``` "~/.openclaw/workspace" ``` |
| ``` channels.discord.maxLinesPerMessage ``` | Discord 单条最大行数 | 17 |

---

## OpenClaw 进阶配置 Checklist

按优先级排序，前 5 项不到 1 小时，就能感受到明显提升：

- **AGENTS.md**：session 启动流程 + 记忆规范 + 安全边界（30 分钟）
- **memoryFlush**：开启压缩前自动保存，解决 AI 失忆（5 分钟）
- **ackReaction**：配置收到消息确认 emoji（1 分钟）
- **blockStreaming**：开启流式回复（5 分钟）
- **Heartbeat 调优**：设置 activeHours 防止半夜打扰（5 分钟）
- **memorySearch（bge-m3）**：配置 SiliconFlow 免费 embedding API（10 分钟）
- **记忆维护**：HEARTBEAT.md 里加每周自动维护任务（10 分钟）
- **模型分级**：配置 alias + 分配策略，省 60-70% token（15 分钟）
- **Cron 任务**：设置每日早报/服务巡检（15 分钟）
- **Skill 开发**：写第一个自定义 skill 练手（30 分钟）
- **多渠道接入**：接入 Discord 或 Telegram（30 分钟）

---

## 常见问题 FAQ

**Q：OpenClaw AGENTS.md 放在哪里？**

A：workspace 根目录，和 SOUL.md、USER.md 同级。路径通常是 

```
~/.openclaw/workspace/AGENTS.md
```

。

**Q：OpenClaw memoryFlush 开了还是失忆怎么办？**

A：检查 

```
softThresholdTokens
```

 是否设够大（推荐 4000）。对话特别关键时，手动 

```
/compact 重点保留XXX
```

 指定保留内容。

**Q：OpenClaw Cron 任务设了但没触发？**

A：99% 是时区问题——没设 

```
tz
```

 字段导致按 UTC 执行。另外检查 

```
delivery.mode
```

 是否设为 

```
"announce"
```

，不设任务静默执行，你不会收到通知。

**Q：OpenClaw Skill 写好了但 AI 不触发？**

A：检查 

```
description
```

 是否包含了你实际的触发词。中英文触发词都要写，比如"查 IP"和"IP lookup"都加上。

**Q：OpenClaw Discord Bot 在线但收不到消息？**

A：几乎肯定是 MESSAGE CONTENT INTENT 没开。回到 Discord Developer Portal → Bot → Privileged Gateway Intents → 开启 MESSAGE CONTENT INTENT → Save Changes。

**Q：OpenClaw 多渠道同时开，消息会串吗？**

A：不会。OpenClaw 记录每条消息的来源渠道，Discord 来的在 Discord 回，Telegram 来的在 Telegram 回。

**Q：OpenClaw 子 Agent 怎么省钱？**

A：在 AGENTS.md 里明确模型分级策略：搜索汇总用 Haiku，写代码用 Sonnet，复杂推理才用 Opus。大部分任务都是 Haiku 级别，实测 token 消耗降 60-70%。
