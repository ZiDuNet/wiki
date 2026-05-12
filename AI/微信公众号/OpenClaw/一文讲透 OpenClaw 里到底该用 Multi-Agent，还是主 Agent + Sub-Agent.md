> 📎 来源: [特别可AI](https://mp.weixin.qq.com/s?__biz=MzI5MzA4NjkwNQ==&mid=2647668652&idx=1&sn=b3994971066b2eb1d1190872a9fafd91&chksm=f50dfc2ed3df1cdd2dcdaa0badb2cf069a4546416f1a1bab0c2cfc2cb69ec0055f091cac4de8&mpshare=1&scene=1&srcid=0420PCrwDPiujeXOafHfTWSj&sharer_shareinfo=80716824f11f5576fcd83462a79c6a32&sharer_shareinfo_first=80716824f11f5576fcd83462a79c6a32) | 时间: 2026-04-20 19:13

---

越来越多人开始搭建多Agent系统，也看到sub-agent的用法，困惑于：

- 要不要直接配多个长期 agent？
- 还是保留一个主 agent，再用 sub-agent 做任务拆解？
- 这两种模式到底差在哪？
- 哪种更适合个人使用，哪种更适合长期体系化？

这篇文章结合 OpenClaw 官方文档来分享：

1. 1. **Multi-Agent 到底是什么**
2. 2. **主 agent + sub-agent 到底是什么**
3. 3. **实际该怎么选、怎么落地**

先给结论：

> **Multi-Agent 解决的是“长期分工与隔离”。**
> **主 agent + sub-agent 解决的是“任务拆解与调度”。**

如果把这两个问题分清，很多架构选择就不难了。

## 一、Multi-Agent：多个独立 Agent

OpenClaw 官方文档对 agent 的定义非常明确：一个 agent 不是一句 prompt，也不是一个会话皮肤，而是一个**完整隔离的大脑**。它有自己的：

- workspace
- `agentDir`
- auth profiles
- session store
- persona / SOUL / AGENTS 规则
- skills

> 一个 agent 是 fully scoped brain。
> 它有独立的 workspace、状态目录、认证和会话存储。

也就是说，**多 agent 并不是“一个 agent 换几套 prompt”，而是多个独立工作单元并存。**

---

按官方文档，Multi-Agent Routing 的目标是：

- 在一个 Gateway 进程里，运行多个隔离 agent
- 每个 agent 有独立 workspace + auth + sessions
- 通过 bindings，把不同入口的消息路由到不同 agent

关于路由，很多人不理解。路由的意思就是十字路口、分发规则：把一条消息分配给哪个 agent 来处理。可以把 OpenClaw 想成一个总机。消息进来之后，它先不急着回答，而是先判断：这条消息来自哪里、是谁发的、在哪个群/私聊/线程里、应该交给哪个 agent，这一步判断过程，就叫 routing。

- 可以按 channel 路由，比如飞书来的交给 work-agent，Telegram 来的交给 personal-agent；
- 可以按 accountId 路由，同一个平台里，你可以接多个账号，例如两个飞书 bot，不同 bot 收到的消息交给不同 agent；
- 可以按 peer / group / DM / guild / thread 路由，也就是说按聊天对象或聊天场景分流：peer：某个具体的人；group：某个具体群；DM：私聊这种会话形态，相对于群聊而言；guild：服务器/组织空间，常见于 Discord 一类；thread：某个具体讨论串（同一个平台、同一个账号下，不同聊天上下文还能继续分配给不同 agent）；
- 绑定规则是 deterministic，且 most-specific wins。意思是路由结果是确定的，不会一会儿这样一会儿那样，同样的输入条件，永远命中同一条规则；当规则冲突时，更具体的那条优先，例如你同时配了：“所有飞书消息 -> agent A”、“飞书里某个群 -> agent B”，那么这个群里的消息会走 agent B，因为“某个群”比“所有飞书消息”更具体。

> 实用Tips: **OpenClaw 可以把不同来源的消息，自动送进不同 agent。** 比如：飞书接文档处理agent、discord接运营agent...或者飞书里创建多个不同的群，分别对应不同的agent，这是更常用的做法，毕竟我们常用的 IM 只有一两个。

## 二、主 agent + sub-agent：一个总控 + 多个任务执行器

OpenClaw 里对 sub-agent 的定位，和多 agent 很不一样。在 slash commands（TUI中的斜杠命令）里，官方支持：

- `/subagents list|kill|log|info|send|steer|spawn`

在 ACP 文档里，官方还专门对比了：

- ACP session
- OpenClaw native sub-agent run

这说明 sub-agent 不是“长期存在的 agent”，而是：

> **由当前会话拉起的 delegated run（临时委派办个事）。**

- 主 agent：总控、接需求、做判断
- sub-agent：临时被拉起来去干一件具体的事

典型工作方式是：

1. 1. 主 agent 接收用户需求
2. 2. 判断这件事是否适合拆分
3. 3. 拉起一个或多个 sub-agent
4. 4. sub-agent 各自执行
5. 5. 主 agent 回收结果并汇总

所以 sub-agent 更像：

- 临时工
- 分包线程
- 并行执行单元
- 一次性委托执行器

而不是长期角色。

## 三、最核心的区别：组织方式不同

很多人误以为：

- 多 agent = 多个 agent
- 主 + sub-agent = 也是多个 agent

只是叫法不同。

其实不是。

官方文档能看出来，这两者在设计目的上就不同。

---

### 1）Multi-Agent 是“组织结构”

它强调：

- 独立 workspace
- 独立 auth
- 独立 sessions
- 独立 identity
- 独立 routing

所以 Multi-Agent 更像：

> **你在一台 OpenClaw 里养了多个长期岗位。**

它解决的是：

- 谁负责哪类事
- 谁接收哪个入口的消息
- 谁用什么模型与权限
- 谁该跟谁隔离

---

### 2）主 agent + sub-agent 是“任务编排”

它强调：

- 委派
- 并行
- 临时运行
- 当前会话内调度
- 执行完再回收

所以它更像：

> **一个项目经理，临时叫几个人去做子任务。**

它解决的是：

- 一个复杂任务怎么拆
- 哪些事适合并行做
- 主会话如何保持清爽
- 重活怎么外包出去跑

## 四、Multi-Agent 的优势与代价

### 优势 1：长期边界清晰

Multi-Agent 最强的一点，就是边界清晰，很适合长期分工。比如：

- 写作 agent 永远只处理内容
- 运维 agent 永远只处理系统
- 某个 agent 只服务某个 Telegram 账号
- 某个 agent 只绑定某个 Discord bot

这就是结构化隔离。

### 优势 2：入口可直接路由

你可以直接把入口级流量路由给不同 agent，而不是所有消息都先流经一个总控再分发。这很适合：

- 多个账号
- 多个 bot
- 多个团队
- 多个角色
- 多个频道/群聊

### 优势 3：适合权限和认证分离

官方文档反复强调 auth 是 per-agent 的，不自动共享。这对长期生产环境特别重要。因为这意味着你可以做到：

- A agent 用这套 auth
- B agent 用另一套 auth
- 不同 agent 的模型、密钥、服务边界天然分开

### 代价 1：配置和维护成本更高

你要维护的东西会明显增加：

- agent 列表
- workspace
- identity
- bindings
- accountId
- auth 复制或隔离
- 会话归属

如果你拆得太细，很容易出现：

- 自己都记不住谁干什么
- agent 太多导致碎片化
- 调试和维护变复杂

### 代价 2：不适合一开始就过度设计

如果你当前其实还只有一个稳定入口、一个主要使用者、一个主要任务类型，那一下子上很多长期 agent，通常会过度设计。

## 五、主 agent + sub-agent 的优势与代价

这套模式的优点，主要来自“灵活”。

### 优势 1：先不用设计一整套组织结构

你可以先只有一个主 agent。等遇到复杂任务时，再决定：

- 要不要 spawn sub-agent
- 要不要并行
- 要不要长时间后台执行

这比一开始就配很多长期 agent 轻得多。

### 优势 2：复杂任务更容易拆解

比如你要做一篇复杂内容：

- 子代理 A：查资料
- 子代理 B：整理结构
- 子代理 C：校对和反查

主 agent 只负责：

- 理解目标
- 分配任务
- 最终汇总

这类模式特别适合：

- 研究
- 批量整理
- 重型执行任务
- 长上下文拆解
- 并行处理

### 优势 3：主对话体验更统一

对于用户来说，入口通常只有一个。

这意味着体验上更自然：

- 你永远只是在跟一个主 agent 说话
- 复杂性都被隐藏在后面

### 代价 1：主 agent 会变成总控中心

所有任务都先进主 agent，再分发给 sub-agent。

这会导致：

- 主 agent 变成单点中枢
- 复杂任务多时，调度逻辑容易变重

### 代价 2：不天然适合长期角色分工

sub-agent 的强项是执行，不是长期身份。如果你把所有长期角色都硬塞成 sub-agent，最后会比较别扭。因为：

- 它们不是入口级角色
- 不是天然长期驻场
- 不适合承接多渠道长期绑定

## 六、官方文档推荐：到底该选哪种？

### 适合优先 Multi-Agent 的情况

如果你符合下面这些特征，优先多 agent：

#### 1）你有多个长期角色

比如：

- writer
- ops
- research
- assistant

#### 2）你需要不同 workspace

官方文档明确说 workspace 是 agent 的 home。所以当不同角色需要长期维护自己的文件、记忆、persona 和技能时，天然适合拆 agent。

#### 3）你需要不同入口直接进不同 agent

比如：

- 某个 Telegram 账号永远进 writer
- 某个 Discord bot 永远进 coding
- 某些 WhatsApp DM 永远进某个 agent

#### 4）你需要认证与权限隔离

不同 agent 各自持有不同 auth profiles，这就是多 agent 的强项。

---

### 适合优先主 agent + sub-agent 的情况

如果你更像下面这样，优先主 + sub：

#### 1）你目前主要只有一个统一入口

比如你主要就自己在 TUI 里用，或者一个主聊天入口。

#### 2）你更多是复杂任务拆解，而不是长期角色拆分

比如：

- 研究任务拆成几路并行
- 写作任务拆成资料/提纲/校对
- 编码任务拆成检查/修改/验证

#### 3）你暂时不想维护很多长期 agent

这种情况下，sub-agent 的灵活性更好。

#### 4）你更想保留一个统一对话体验

也就是永远跟一个主 agent 交流，后面的复杂性由它内部消化。

另外，我曾经想过，什么场景下非要使用多个 sub-agent，用一个 agent 不够吗？因为“一个 agent 全包”在简单任务里可以，但任务一复杂，就会同时出现四个问题：上下文混乱、步骤互相干扰、速度慢、结果不稳。一个 agent 全做时，常见情况是：一边让它查资料，一边搭结构，一边改措辞，目标容易漂移；不同子任务共用同一上下文，垃圾信息越堆越多，前面查到的弱结论，会污染后面的写作和判断；所有事串行做，慢。以及很难局部重跑，例如“只重做校对，不重做检索”。而拆成多个子 agent 后，每个只做一件事，会更稳：

- 查资料 agent：只负责搜集和筛选信息，优化目标是覆盖率和证据质量；
- 结构 agent：不被检索噪音干扰，只负责组织逻辑；
- 校对/反查 agent：站在“审核者”视角，专门挑漏洞，而不是顺着原答案一路往下写。
  实操下来，多 sub-agent 真得很好用。

---

- Multi-Agent 负责长期隔离与路由
- sub-agent 负责当前任务的拆解与执行

一个很实用的搭法是：

### 长期层

- `main`：总控 / 默认入口
- `writer`：内容创作
- `ops`：系统与运维

### 执行层

在 `writer` 或 `ops` 内部，需要做重活时，再拉 sub-agent。例如：

#### writer 内部

- sub-agent A：搜集资料
- sub-agent B：整理提纲
- sub-agent C：做事实核查

#### ops 内部

- sub-agent A：查日志
- sub-agent B：做配置对比
- sub-agent C：生成修复建议

这通常比“纯多 agent”或“纯主+sub”都更实用。

---

## 七、实操

### 路线 A：Multi-Agent

#### 第一步：先加长期 agent

```
openclaw agents add writeropenclaw agents add ops
```

#### 第二步：看绑定情况

```
openclaw agents list --bindingsopenclaw agents bindings
```

#### 第三步：把入口绑给对应 agent

```
openclaw agents bind --agent writer --bind telegram:writeropenclaw agents bind --agent ops --bind discord:ops
```

#### 第四步：给各自 workspace 补齐人格和规则

每个 agent 的 workspace 里都应该有自己的：

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`

这是官方 workspace 文档里最值得重视的部分。

#### 第五步：重启并验证

```
openclaw gateway restartopenclaw channels status --probeopenclaw agents list --bindings
```

---

### 路线 B：主 agent + sub-agent

#### 第一步：先保留一个主 agent

也就是先不要拆太多长期 agent。

#### 第二步：在复杂任务里使用 sub-agent 命令

TUI 里官方支持：

- `/subagents list`
- `/subagents spawn`
- `/subagents steer`
- `/subagents kill`

这意味着你可以先从任务拆解入手，而不是先做大规模组织设计。

#### 第三步：区分是否用 ACP 外部 harness

- ACP session：是通过 ACP 这个协议去对接外部 agent/harness，比如接 Codex、Claude Code、Gemini CLI，这时 OpenClaw 不再只是内部自转，而是在跟外部执行器通信；
- OpenClaw native sub-agent runtime：是 OpenClaw 自己内部的“子代理执行机制”，主 agent 在当前会话里临时委派一个子任务给另一个执行单元，这是 OpenClaw 内部原生能力。

如果你要“OpenClaw 内部自己拆任务、自己派工人”，用 sub-agent；如果你要“把任务交给外部 agent 系统来跑”，用 ACP。sub-agent 是 OpenClaw 自己家的内部员工，生命周期、上下文、权限、调度都由 OpenClaw 内部控制；ACP 外部 harness 是外包接口 / 协议适配层，有自己的一套运行方式、会话模型、工具能力。

---

## 最后，几个很容易踩的坑

### 坑 1：把 workspace 当成强沙箱

官方文档明确提醒：workspace 是默认 cwd，不是硬沙箱。

如果你需要真正隔离，要看 sandbox 配置，而不是误以为“不同 workspace 就天然安全隔离”。

### 坑 2：一开始就拆太多长期 agent

这通常会让系统提前碎片化。更稳的路线一般是：

1. 1. 先主 agent
2. 2. 再用 sub-agent 处理复杂任务
3. 3. 当某类任务长期稳定后，再升级成独立长期 agent

少即是多。简单为上策。

以上，如果觉得有帮助，欢迎三连。欢迎星标，第一时间收到我的实操分享。下次见。

---

## 参考官方文档

- Multi-Agent Routing
  https://docs.openclaw.ai/concepts/multi-agent
- Agent Workspace
  https://docs.openclaw.ai/concepts/agent-workspace
- Slash Commands
  https://docs.openclaw.ai/tools/slash-commands
- CLI: agents
  https://docs.openclaw.ai/cli/agents
- ACP Agents
  https://docs.openclaw.ai/tools/acp-agents
