> 📎 来源: [胖小天](https://mp.weixin.qq.com/s?__biz=MzA4OTI0MDM2Mg==&mid=2247483896&idx=1&sn=cde37379090f6c0614d1d7bea22aee01&chksm=91426e3b42dd1ef4315507e137388fb584969483ddc74ed61a9a655bf2142e652f4be512d548&mpshare=1&scene=1&srcid=04212b3zITLNgIcf0vn4e1Pl&sharer_shareinfo=de33b8029b377c862f2806d773e96611&sharer_shareinfo_first=de33b8029b377c862f2806d773e96611) | 时间: 2026-04-21 09:24

---

Harrison Chase 说了一句话，我记了很久。

> 通才比以往更有价值。

他是 LangChain 创始人，这句话出自他那篇刷屏的《How Coding Agents Are Reshaping EPD》。

当时我就在想：**通才的价值，到底从哪来？**

答案藏在后半句——

> 因为没有沟通开销。

一个能做产品、设计、工程三件事的人，比三人团队更快。

因为没有来回拉扯，没有会议，没有"再对一下"。

但问题是：**即使是通才，时间也有限。**

一个人做三件事，精力分散。

"没有沟通开销"的前提是：你能独立完成所有环节。

直到我看到了 OpenClaw。

---

## 一、范式转变：从"单打独斗"到"团队作战"

先回顾一下我们是怎么用 AI 的。

### 旧范式

一个 ChatGPT，应付所有问题。

问代码、问写作、问分析……都是同一个"人"。

问题来了：

- **上下文混杂**

  ：上一秒还在写代码，下一秒要分析数据，Agent 的"脑子"会乱
- **专业度有限**

  ：同一个 Agent，很难在所有领域都足够深入
- **每次重新教育**

  ：切换任务，要重新解释背景

这就像让一个员工同时做产品、设计、工程。

不是不行，是累。

而且效率会递减。

### 新范式

OpenClaw 的解法很简单：**不让一个 Agent 做所有事。**

```
你（一个人）    │    ├── Agent A：代码专家    ├── Agent B：写作专家    └── Agent C：数据分析专家
```

每个 Agent 有自己的：

- **工作区**

  ：独立的配置和状态
- **记忆**

  ：只记住自己领域的事
- **人设**

  ：专注于某个专业方向

你不再是"一个人做所有事"。

你是"一个人管理一个团队"。

### 范式对比

| 旧范式 | 新范式 |
| --- | --- |
| 一个 Agent 做所有事 | 多个 Agent 各司其职 |
| 用户切换工具 | 主 Agent 派发任务 |
| 知识碎片化 | 每个 Agent 独立记忆 |

这就是 Harrison Chase 说的"没有沟通开销"——

**不是因为你是通才，而是因为你有 Agent 团队。**

---

## 二、技能演进：从"提问者"到"管理者"

ChatGPT 刚出来时，所有人都学了一项技能：**学会提问**。

怎么写 prompt，怎么追问，怎么引导 Agent 输出想要的内容。

这是第一代 AI 时代的核心能力。

后来，Harrison Chase 提出了第二层：

> 每个人都需要产品感——知道告诉 Agent 构建什么。

这是"决策能力"。

现在，多 Agent 时代来了。

**新的核心能力：学会管理。**

### 管理什么？

1. **分工设计**

   ：需要几个 Agent？每个负责什么？
2. **任务派发**

   ：如何拆解复杂任务？如何分配？
3. **结果评估**

   ：如何判断产出质量？如何反馈？
4. **流程优化**

   ：如何自动化？如何持续改进？

### 技能演进路径

```
学会提问 → 学会决策 → 学会管理
```

这不是叠加，是**升维**。

从"与一个 Agent 对话"，到"协调多个 Agent 协作"。

---

## 三、角色映射：你是什么角色？

Harrison Chase 还有一个观点：

> 你要么是建设者，要么是审查者。

**建设者**：执行任务，产出结果。
**审查者**：协调、整合、把控质量。

在 OpenClaw 里，这个映射变得很清晰：

| Harrison Chase | OpenClaw | 你 |
| --- | --- | --- |
| 建设者 | 子 Agent | Agent 团队 |
| 审查者 | 主 Agent | 你 |

**你不是执行者。**

**你是决策者、协调者、审查者。**

Agent 是你的建设团队。

你告诉它们做什么，它们执行。

你审查结果，决定接受还是重做。

### 关键洞察

> 实现成本趋零后，差异化在于：知道构建什么、如何协调、怎样整合。

**系统思维成为新的护城河。**

---

## 四、实战案例：技术博主的一天

说这么多，不如看一个实际场景。

假设你是一个技术博主。

每天要做的事：

- 策划选题、收集资料
- 撰写文章、润色语言
- 生成头图、社群分发

**以前**：需要三人团队——策划、写作、运营。
**现在**：一个人 + OpenClaw。

### Agent 团队设计

```
你（博主）    │    ├── 研究助手    │       └── 收集资料、整理素材、生成大纲    │    ├── 写作助手    │       └── 生成初稿、润色语言、调整风格    │    └── 运营助手            └── 生成头图、提取金句、社群文案
```

### 具体流程

**Step 1：派发研究任务**

你告诉主 Agent："帮我收集 OpenClaw 多 Agent 协作的资料。"

主 Agent 把任务派给研究助手。

研究助手执行，返回资料包。

**Step 2：派发写作任务**

主 Agent 把资料发给写作助手。

写作助手生成初稿，返回给主 Agent。

你审查，反馈修改意见。

写作助手润色，再次返回。

**Step 3：派发运营任务**

主 Agent 把定稿发给运营助手。

运营助手生成头图、提取金句、准备社群文案。

你审查，确认发布。

### 工作流配置

要实现上面的流程，需要先配置好 Agent 团队。

**创建隔离 Agent**

```
# 创建研究助手openclaw agents add --name "研究助手"openclaw agents set-identity \  --agent "研究助手" \  --name "研究员" \  --emoji "📚" \  --theme "专注资料收集、素材整理、大纲生成"# 创建写作助手openclaw agents add --name "写作助手"openclaw agents set-identity \  --agent "写作助手" \  --name "作家" \  --emoji "✍️" \  --theme "专注文章撰写、语言润色、风格调整"# 创建运营助手openclaw agents add --name "运营助手"openclaw agents set-identity \  --agent "运营助手" \  --name "运营" \  --emoji "🚀" \  --theme "专注头图生成、金句提取、社群分发"
```

### Session 传递与获取

主 Agent 如何把任务派发给子 Agent，并获取结果？

**方式一：动态创建子代理（sessions\_spawn）**

主 Agent 可以在对话中动态创建子代理：

```
sessions_spawn  runtime: subagent  mode: run  task: "帮我收集 OpenClaw 多 Agent 协作的资料"
```

子代理执行完成后，会自动回报完成事件。

**方式二：跨会话通信（sessions\_send）**

如果已经有隔离 Agent，可以直接发送消息：

```
# 向"研究助手"发送消息openclaw agent \  --agent "研究助手" \  --message "帮我收集 OpenClaw 多 Agent 协作的资料"
```

**查看会话状态**

```
# 查看所有 Agent 的活跃会话openclaw sessions --all-agents --active 60# 输出示例：# Agent        Session Key              Updated# ----------   ----------------------   --------# main         agent:main:main          2 min ago# 研究助手     agent:research:main      5 min ago# 写作助手     agent:writer:main        15 min ago
```

**获取特定 Agent 的会话历史**

```
# 查看研究助手的会话openclaw sessions --agent "研究助手" --json
```

**查看子代理状态**

```
# 列出当前运行的子代理openclaw sessions --all-agents --active 10
```

### CLI 实操（简化版）

```
# 查看所有活跃的 Agentopenclaw sessions --all-agents --active 60# 查看特定 Agent 的会话openclaw sessions --agent "研究助手"# 向特定 Agent 发送消息openclaw agent --agent "写作助手" --message "根据这份资料写一篇文章"
```

整个流程，你只做了三件事：

1. **决策**

   ：确定选题、方向
2. **审查**

   ：评估初稿、头图
3. **发布**

   ：最终确认

其他的——收集资料、生成初稿、制作头图——都是 Agent 在做。

---

## 五、频道路由：不同场景不同人设

还有一个场景，很实用。

### 问题

你的生活是分层的：

- **微信**

  （家人/朋友）："周末去哪吃？"
- **飞书/企微**

  （工作）："这个架构怎么设计？"
- **QQ**

  （朋友圈）："最近有什么好书？"

同一个 Agent，应付所有场景。

**问题是：语境会混乱。**

你不想让同事看到生活化的语气，也不想用工作腔回朋友。

### 解法：不同频道绑定不同 Agent

```
微信 → 生活 Agent    │    └── 人设：温柔、日常、生活化飞书/企微 → 工作 Agent    │    └── 人设：专业、高效、有条理QQ → 朋友 Agent    │    └── 人设：轻松、幽默、分享欲
```

### 实现

**Step 1：创建 Agent**

```
# 创建生活助手openclaw agents add --name "生活助手"# 创建工作助手openclaw agents add --name "工作助手"# 创建朋友助手openclaw agents add --name "朋友助手"
```

**Step 2：设置 Agent 身份（人设）**

```
# 设置生活助手的人设openclaw agents set-identity \  --agent "生活助手" \  --name "小管家" \  --emoji "🏠" \  --theme "温柔日常，擅长生活建议"# 设置工作助手的人设openclaw agents set-identity \  --agent "工作助手" \  --name "工作秘书" \  --emoji "💼" \  --theme "专业高效，擅长技术问题"# 设置朋友助手的人设openclaw agents set-identity \  --agent "朋友助手" \  --name "老铁" \  --emoji "😎" \  --theme "轻松幽默，擅长推荐分享"
```

**Step 3：绑定频道**

```
# 绑定生活助手到微信openclaw agents bind \  --agent "生活助手" \  --channel wechat# 绑定工作助手到飞书openclaw agents bind \  --agent "工作助手" \  --channel feishu# 绑定朋友助手到 QQopenclaw agents bind \  --agent "朋友助手" \  --channel qq
```

**Step 4：查看绑定状态**

```
# 查看所有路由绑定openclaw agents bindings
```

输出类似：

```
Agent        Channel    Target----------   --------   ------------------生活助手     wechat     所有私聊工作助手     feishu     所有私聊朋友助手     qq         所有私聊
```

**进阶：按账号/群组绑定**

如果你只想让某个特定账号或群组路由到特定 Agent：

```
# 只让"家庭群"路由到生活助手openclaw agents bind \  --agent "生活助手" \  --channel wechat \  --group "家庭群"# 只让"工作群"路由到工作助手openclaw agents bind \  --agent "工作助手" \  --channel feishu \  --group "工作群"
```

一条消息进来，自动路由到对应的 Agent。

**就像你有三个不同的"自己"，在不同频道切换。**

---

## 六、新的护城河：系统思维

Harrison Chase 说：

> 系统思维是需要磨练的技能。

为什么？

因为**实现成本趋零**。

现在每个人都能让 Agent 生成代码、文章、设计。

差异化在哪？

**知道构建什么、如何协调、怎样整合。**

这就是系统思维。

### 你的系统 = Agent 团队 + 流程

```
你的系统思维    │    ├── Agent 分工设计    ├── 任务流转规则    ├── 质量控制标准    └── 持续优化机制
```

### 竞争力重构

- **以前**

  ：谁写代码快、谁文章好
- **现在**

  ：谁的 Agent 团队更高效、谁的系统更完善

**这不是"会用 AI"的竞争。**

**这是"会管理 AI 团队"的竞争。**

---

## 写在最后

Harrison Chase 那篇文章，有句话我很喜欢：

> 每个人都认为自己角色最受益于编码 Agent——他们是对的。

为什么？

因为这个新时代，**背景没那么重要了**。

产品、设计、工程——都可以用 Agent 延伸能力。

关键不是你来自哪个角色。

**关键是你能否管理好你的 Agent 团队。**

---

学会提问，让你能用 AI。

学会决策，让你知道让 AI 做什么。

学会管理，让你能"雇佣" AI 团队。

**一个人就是一个团队。**

这不是口号。

这是 OpenClaw 带来的新可能。

下一个问题：**你的 Agent 团队，需要什么角色？**

---

**延伸阅读**：

- > OpenClaw 官方文档

  > https://docs.openclaw.ai
- Harrison Chase: How Coding Agents Are Reshaping EPD

> 阿里云极速部署，AI流行场景一键体验

> https://dashi.aliyun.com/activity/aigc?userCode=w6nzrfv6

— 完 —
