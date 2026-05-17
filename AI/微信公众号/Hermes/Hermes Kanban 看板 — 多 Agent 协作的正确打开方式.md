> 📎 来源: [专业造轮子](https://mp.weixin.qq.com/s?__biz=MzI0OTg0NTk0MA==&mid=2247484244&idx=1&sn=53355fceaea00e9b6885cb2ef46e34c7&chksm=e8ca2ae3d9ab04b796dd8c593efd4451c02aa55799de3f229d46921bdd61e26afa589835a843&mpshare=1&scene=1&srcid=0517zwRjAe3sywUdTKpY55uI&sharer_shareinfo=5506e0865f5d96425219f8d9c5cbab6d&sharer_shareinfo_first=5506e0865f5d96425219f8d9c5cbab6d) | 时间: 2026-05-17 23:52

---

> 当你的 AI 智能体不止一个的时候，怎么让它们像人类团队一样协作？

## 一个老问题

去年 Claude Code 横空出世的时候，开发者圈子里流行一种玩法：开三个终端窗口，一个写后端，一个写前端，一个写测试，让三个 Claude 各干各的。听起来很美，但实际上：

- Agent A 等 Agent B 的接口，但 B 改了接口没人知道
- Agent C 发现自己依赖的模块还没写完，只能阻塞
- 一个跑了 10 分钟后崩溃，什么都没留下
- 你想从手机上看看进度？不存在的

**问题出在哪？** 这些 Agent 之间的协调全是靠人眼盯着终端窗口完成的，没有持久化的工作队列，没有状态管理，没有失败重试，没有人为干预的入口。

而这就是 Hermes Agent 刚刚推出的 **Kanban** 特性要解决的核心问题。

> Hermes Agent 是 Nous Research 开发的开源 AI Agent 框架，与 Claude Code、OpenAI Codex 同属一个品类，但它最大的特点是"什么都能跑"——支持 20+ 模型提供商、运行在终端/Telegram/Discord/Slack 等十几个平台、有跨会话持久记忆、以及一套完整的技能系统。

## 什么是 Hermes Kanban？

**一个持久化的多 Agent 协作看板。**

它的核心是一个 SQLite 数据库（

```
~/.hermes/kanban.db
```

），所有的任务、状态、注释、依赖关系都写在这一份数据里。但有意思的是，它有**两套完全独立的操作界面**：

- **你（人类）** 通过 CLI 命令或 Web Dashboard 操作看板
- **Agent（Worker）** 通过一套专门的 

  ```
  kanban_*
  ```

   工具函数操作看板

两套接口背后走的是同一套数据库代码，数据永远不会漂移。

看板的列从左到右依次是：

```
Triage → Todo → Ready → In Progress → Blocked → Done
```

Triage 是收集原始想法的地方；Ready 是分配给某个 Profile 后等待 Dispatcher 调度的任务；Blocked 是 Worker 需要人类输入才能继续的任务。

## delegate\_task vs Kanban

如果你用过 Hermes或其他Agent，应该熟悉 

```
delegate_task
```

——它可以让一个 Agent 派生子 Agent 去做一件事，然后等结果回来。

Kanban 不是 

```
delegate_task
```

 的升级版，它们是**不同层级的原语**：

| 维度 | delegate\_task | Kanban |
| --- | --- | --- |
| 形态 | RPC 调用（fork → join） | 持久化消息队列 + 状态机 |
| 父 Agent | 阻塞等待子 Agent 返回 | 创建后即忘（fire-and-forget） |
| 子 Agent 身份 | 匿名子进程 | 具名 Profile，有持久记忆 |
| 可恢复性 | 无 — 失败了就失败了 | Block → Unblock → 重试；崩溃 → 自动回收 |
| 人为介入 | 不支持 | 随时评论 / 解封 / 干预 |
| 每个任务参与 Agent 数 | 一个子 Agent | 多个 Agent 接力（重试、Review、后续任务） |
| 审计轨迹 | 上下文压缩后就丢了 | SQLite 永久存储 |
| 协作模式 | 层级式（调用者 → 被调用者） | 对等式——任何 Profile 可以读写任何任务 |

```
delegate_task
```

 是一个函数调用；Kanban 是一个工作队列，每一次握手都是一行可以被任何人看到和编辑的记录。

它们不互斥——一个 Kanban Worker 在执行任务的过程中完全可以内部调用 

```
delegate_task
```

。

## Kanban 的设计哲学

### 场景一：Solo 开发者做一个功能

假设你要写一个认证模块。经典的三步走：设计 Schema → 实现 API → 写集成测试。

```
# 创建三个任务，通过 --parent 建立依赖链
```

关键在依赖引擎：只有 

```
SCHEMA
```

 一开始进入 Ready 状态，其他两个在 Todo 里等待。只有当 

```
SCHEMA
```

 完成后，

```
API
```

 自动提升为 Ready；当 

```
API
```

 完成后，测试任务自动 Ready。

当 backend-dev Worker 被 Dispatcher 派生出来后，它的第一个动作不是跑 CLI 命令，而是调用一个工具函数：

```
# Worker 内部的工具调用，不是人敲的命令
```

当 API Worker 启动后调用 

```
kanban_show()
```

，它会自动看到 SCHEMA 的 

```
summary
```

 和 

```
metadata
```

——下游 Worker 不需要翻聊天记录就知道上游做了哪些决策。

### 场景二：舰队农场（Fleet Farming）

你有三个翻译、五个音频转写、四个商品文案要写，三个不同的 Worker 并行干活。

```
for lang in 日文 韩文 法文; do
```

启动 Gateway（内置 Dispatcher），然后走开。

Dashboard 上看，In Progress 列会按 Profile 分组显示——每个 Worker 当前在干什么一目了然。完成一个，Dispatcher 自动派发下一个。整个队列不需要任何人盯着。

### 场景三：角色 Pipeline + 重试

这才是 Kanban 真正发光的地方。PM 写 Spec → 工程师实现 → Reviewer 审核驳回 → 工程师改 → Reviewer 通过。

当工程师的第一次实现被 Reviewer 驳回后，他调用：

```
kanban_block(
```

任务进入 Blocked 状态。你（或 Reviewer）从 Dashboard 上点了 Unblock 按钮后，Dispatcher 重新派生 Worker。这次 

```
kanban_show()
```

 返回的 

```
worker_context
```

 里包含了前一次运行的 block 原因，所以二次尝试的 Worker 知道要修哪两个问题，不需要重读完整的 Spec。

Dashboard 上这个任务会显示两次 Runs：

```
Run 1 — blocked @backend-dev: "密码强度检查缺失"
```

每次 Run 的 summary、metadata、错误信息都完整保存。这不是事后加上去的"历史记录"——它是 Kanban 的核心数据模型。

### 场景四：断路器 + 崩溃恢复

Worker 会失败。缺少环境变量、OOM 被 kill、网络超时——这些都是日常。Dispatcher 有两道防线：

1. **崩溃检测** — Worker 进程意外退出后，Dispatcher 检测到 PID 消失，自动释放 Claim，下一次 Tick 重新派生
2. **断路器** — 连续 N 次失败后（默认 3 次），任务自动进入 Blocked，不会再浪费算力重试

一个缺少 AWS 密钥的部署任务：

```
hermes kanban runs t_ef5d
```

三次尝试后，断路器跳闸，任务标记为 

```
gave_up
```

。如果有 Telegram/Discord 网关接入，还会推送通知到你的手机上。

## 总结

Hermes Kanban 的价值不在于"又多了一个看板工具"，而在于它为多 Agent 协作提供了一个**正确的数据模型**：每个任务是一行持久化数据，每次握手是任何人可以读写的记录，每个 Worker 是一个完整的操作系统进程。

相比 Cline、Codex 等竞品，Hermes 是目前唯一开源实现持久化多 Agent 看板的框架。如果你正在构建 AI Agent 工作流，或者对多 Agent 协作有兴趣，这绝对值得一试。

- END -
