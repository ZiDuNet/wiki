> 📎 来源: [小龙开发者](https://mp.weixin.qq.com/s?__biz=MzY4OTE4MDg2Nw==&mid=2247483861&idx=1&sn=b8c7aa320cbb0e519161274bf6891345&chksm=f2c72fc5054fb30bd5d963149bd9178e58538f4b06c14e30ab642218c7ce4d3cfef51b9ab629&mpshare=1&scene=1&srcid=0420Rjsdu65fv24o127BZxDN&sharer_shareinfo=9dda09a758d0e6c59b82aaaf34e3c681&sharer_shareinfo_first=9dda09a758d0e6c59b82aaaf34e3c681) | 时间: 2026-04-20 19:14

---

一次派出多个助手并行干活，效率提升 300% 的秘诀

**📌 核心摘要：**OpenClaw v2026.3.22 版本全面升级了多智能体架构，支持在一个 Gateway 进程中运行多个完全隔离的 Agent，还能让 Agent 之间相互协作。本文带你从零开始，搭建一个完整的多智能体协作系统，让 AI 从"单兵作战"升级为"团队协作"。

## 一、为什么需要多智能体协作？单 Agent 的三大痛点

单个 AI Agent 虽然强大，但在实际场景中往往力不从心。很多用户在使用 OpenClaw 时，习惯于在一个主 Agent 中完成所有任务，但随着使用时间增长，记忆文件冗余会导致 Agent 出现"神经错乱"或响应偏差。

**⚠️ 单 Agent 的三大痛点：**

| **痛点** | **具体表现** | **影响** |
| --- | --- | --- |
| **上下文频繁切换** | 写代码的 Agent 需要同时处理前端、后端和测试 | 注意力分散，输出质量下降 |
| **话术风格混乱** | 客服 Agent 需要同时对接多个渠道，各渠道话术风格不同 | 响应不专业，用户体验差 |
| **任务类型混杂** | 研究 Agent 既要搜索信息，又要分析数据，还要撰写报告 | 效率低下，容易出错 |

**💡 解决方案：**将不同职能拆分至专属 Agent，通过调度层实现任务分配与结果汇总，能有效避免 AI 幻觉、提升响应专业性与效率。

## 二、核心概念：OpenClaw 的三种 Agent 类型

### 🎯 理解 Agent 类型是搭建多智能体系统的第一步

| **类型** | **生命周期** | **适用场景** | **典型例子** |
| --- | --- | --- | --- |
| **Persistent Agent** | 常驻运行 | 长期驻守某个频道或场景 | 客服 Bot、编程助手、运营助理 |
| **Sub-Agent** | 任务完成即归档 | 临时并行处理子任务 | 搜索信息、运行测试、生成报告 |
| **ACP Agent** | 按协议通信 | 跨平台、跨服务的标准化协作 | 微服务间的 Agent 调用 |

本文重点讲前两种，这是最常用的场景。

## 三、第一步：配置多个 Persistent Agent

### 📝 基础配置：在 openclaw.json 中定义多个 Agent

{

"agents": {

"list": [

{

"id": "coordinator",

"name": "协调员",

"workspace": "~/.openclaw/workspace-coordinator",

"model": "claude-opus-4",

"systemPrompt": "你是团队协调员，负责分配任务和汇总结果。"

},

{

"id": "coder",

"name": "程序员",

"workspace": "~/.openclaw/workspace-coder",

"model": "claude-sonnet-4",

"systemPrompt": "你是一个高效的程序员，专注于代码实现和 Bug 修复。"

},

{

"id": "researcher",

"name": "研究员",

"workspace": "~/.openclaw/workspace-researcher",

"model": "openai/gpt-5.4-mini",

"systemPrompt": "你是一个信息研究员，擅长搜索、对比和总结信息。"

}

]

}

}

### 🔗 为 Agent 绑定频道

{

"agents": {

"bindings": [

{

"agentId": "coordinator",

"channelType": "slack",

"channelId": "#general"

},

{

"agentId": "coder",

"channelType": "slack",

"channelId": "#dev"

},

{

"agentId": "researcher",

"channelType": "discord",

"channelId": "research-channel"

}

]

}

}

### 🛠️ CLI 快速管理命令

# 添加一个新 Agent

openclaw agents add --id "writer" \

--workspace "~/.openclaw/workspace-writer" \

--model "claude-sonnet-4" \

--system-prompt "你是技术写手，擅长把复杂概念讲得简单易懂。"

# 查看所有 Agent

openclaw agents list

# 修改 Agent 配置

openclaw agents config set coder model gpt-5.4

## 四、第二步：配置 Sub-Agent 子智能体（核心精髓）

**🔥 Sub-Agent 是 OpenClaw 多智能体的精髓**——让主 Agent 能够自主"派活"给后台工作单元，实现真正的并行处理。

### ⚙️ 全局配置参数

{

"agents": {

"defaults": {

"subagents": {

"maxConcurrent": 8,        // 最大并发子 Agent 数

"maxSpawnDepth": 2,        // 允许的嵌套深度

"maxChildrenPerAgent": 5,  // 每个 Agent 最多创建的子 Agent 数

"runTimeoutSeconds": 600,  // 超时自动终止（秒）

"thinking": "medium",      // 子 Agent 的思考级别

"cleanup": "delete"        // 任务完成后处理方式

}

}

}

}

### 📊 参数详解

| **参数** | **默认值** | **说明** |
| --- | --- | --- |
| **maxConcurrent** | 8 | 最大并发子 Agent 数 |
| **maxSpawnDepth** | 2 | 允许的嵌套深度（0=主 Agent，1=子 Agent，2=孙 Agent） |
| **maxChildrenPerAgent** | 5 | 每个 Agent 最多创建的子 Agent 数 |
| **runTimeoutSeconds** | 600 | 超时自动终止（秒），0 表示不限 |
| **thinking** | medium | 子 Agent 的思考级别（none/low/medium/high） |
| **cleanup** | delete | 任务完成后处理方式（delete 清除 / keep 保留） |

### 🔒 层级限制：避免无限递归

**0**

**主 Agent**
→ 始终可以创建子 Agent

**1**

**子 Agent**
→ 仅当 maxSpawnDepth ≥ 2 时可创建孙 Agent

**2**

**孙 Agent**
→ 永远不能再创建子 Agent（纯执行者）

### 💬 手动触发子 Agent 命令

# 派生一个子 Agent 执行任务

/subagents spawn "搜索最近一周关于 Claude Opus 4 的评测文章，整理成表格"

# 查看所有子 Agent 状态

/subagents list

# 查看某个子 Agent 的日志

/subagents log

# 向运行中的子 Agent 发送消息

/subagents send  "重点关注性能对比数据"

# 停止子 Agent

/subagents stop

## 五、第三步：为不同 Agent 分配最优模型（成本优化关键）

**💰 多智能体的核心优势之一是按任务分配模型**——复杂推理用旗舰模型，简单任务用轻量模型，大幅降低成本。

### 🎯 模型分配策略示例

{

"agents": {

"list": [

{

"id": "architect",

"model": "claude-opus-4",

"description": "系统架构设计，需要最强推理能力"

},

{

"id": "coder",

"model": "claude-sonnet-4",

"description": "日常编码，速度与质量的平衡"

},

{

"id": "reviewer",

"model": "openai/gpt-5.4-mini",

"description": "代码审查，快速定位问题"

},

{

"id": "translator",

"model": "gemini-3-pro",

"description": "多语言翻译，Google 模型多语言表现更好"

},

{

"id": "data-analyst",

"model": "deepseek-v4",

"description": "数据分析，性价比最高"

}

]

}

}

### 📊 成本对比：多模型分层策略

| **任务类型** | **推荐模型** | **价格参考** | **说明** |
| --- | --- | --- | --- |
| 架构设计 / 复杂推理 | Claude Opus 4 | $15 / 1M tokens | 需要最强推理能力 |
| 日常编码 / 重构 | Claude Sonnet 4 | $3 / 1M tokens | 速度与质量平衡 |
| 代码审查 / 简单任务 | GPT-5.4 Mini | $0.4 / 1M tokens | 快速响应，成本极低 |
| 信息搜索 / 摘要 | Gemini 3.1 Flash | $0.15 / 1M tokens | 超低成本，大上下文窗口 |
| 数据分析 | DeepSeek V4 | $0.27 / 1M tokens | 数学推理强，性价比高 |

**💡 成本实测：**一个典型的研发团队（3 Agent），每天处理 50 个任务，月成本大约在
**$30-80**
之间，远低于为每个 Agent 都使用旗舰模型的方案。

## 六、实战演练：搭建一个 3 人研发团队

### 🚀 完整配置文件 + 工作流演示

### 📄 完整配置文件

{

"providers": {

"ofox": {

"type": "openai",

"baseUrl": "https://api.ofox.ai/v1",

"apiKey": "sk-your-ofox-api-key"

}

},

"agents": {

"defaults": {

"provider": "ofox",

"subagents": {

"maxConcurrent": 6,

"maxSpawnDepth": 2,

"runTimeoutSeconds": 300,

"thinking": "medium"

}

},

"list": [

{

"id": "pm",

"name": "产品经理",

"model": "anthropic/claude-opus-4",

"workspace": "~/.openclaw/team/pm",

"systemPrompt": "你是产品经理。收到需求后，拆解为具体的技术任务，分配给 coder 和 tester。",

"subagents": {

"allowAgents": ["coder", "tester"]

}

},

{

"id": "coder",

"name": "开发工程师",

"model": "anthropic/claude-sonnet-4",

"workspace": "~/.openclaw/team/coder",

"systemPrompt": "你是全栈开发工程师。接到任务后直接编码实现，代码写完后通知 pm。",

"subagents": {

"allowAgents": ["pm"]

},

"tools": ["bash", "read", "write", "edit", "glob", "grep"]

},

{

"id": "tester",

"name": "测试工程师",

"model": "openai/gpt-5.4-mini",

"workspace": "~/.openclaw/team/tester",

"systemPrompt": "你是测试工程师。收到代码后编写测试用例并执行，发现 Bug 直接反馈给 coder。",

"subagents": {

"allowAgents": ["pm", "coder"]

},

"tools": ["bash", "read", "glob", "grep"]

}

],

"bindings": [

{

"agentId": "pm",

"channelType": "slack",

"channelId": "#product"

},

{

"agentId": "coder",

"channelType": "slack",

"channelId": "#dev"

},

{

"agentId": "tester",

"channelType": "slack",

"channelId": "#qa"

}

]

}

}

### 🔄 工作流演示

**1**

在
**#product**
频道对 PM Agent 说：

```
开发一个用户注册 API，要求：POST /api/register，接收 email 和 password，密码至少 8 位...
```

**2**

PM Agent 拆解任务后，自动 spawn 子 Agent 到 coder 工作区：

```
→ [PM] 任务已拆解，正在分配给开发...
```



```
→ [PM → Coder Sub-Agent] 实现用户注册 API（附详细规格）
```



```
→ [PM → Tester Sub-Agent] 准备注册 API 的测试用例（附验收标准）
```

**3**

Coder 和 Tester 的子 Agent
**并行工作**，完成后结果自动汇报给 PM。

## 七、常见问题排查

### ❌ 问题 1：Sub-Agent 权限拒绝

**Error:**
sessions\_spawn permission denied for agent "coder"

**原因：**目标 Agent 的 allowAgents 没有包含请求者。

**解决：**在目标 Agent 的配置中添加授权：

{

"id": "coder",

"subagents": {

"allowAgents": ["pm", "coordinator"]

}

}

### ❌ 问题 2：子 Agent 超时被杀

**Error:**
Sub-agent exceeded runTimeoutSeconds (600s)

**解决：**增大超时时间，或在 spawn 时单独指定：

/subagents spawn --timeout 1200 "执行完整的集成测试套件"

### ❌ 问题 3：内存不足

**多个 Agent 同时运行会占用大量内存**

**建议：**

- 8GB 内存：最多 3-5 个 Persistent Agent
- 16GB 内存：可支撑 8-10 个 Agent
- 及时清理不需要的子 Agent：

  ```
  /subagents stop --all
  ```

### ❌ 问题 4：Agent 之间消息丢失

**关键区别：**

```
sessions_spawn
```

：创建新的子 Agent 会话

```
sessions_send
```

：向已存在的 Agent 会话发送消息

# 向已有 Agent 发消息（不创建新会话）

/subagents send  "你的消息"

# 创建新的子 Agent（新会话）

/subagents spawn "任务描述"

## 八、总结：OpenClaw 多智能体的三个核心能力

## 🎯 核心能力总结

- **Persistent Agent**：常驻不同场景，各司其职
- **Sub-Agent**：自主拆解任务，并行执行
- **跨 Agent 派生**：让 Agent 之间互相调用对方的能力

**配合多模型分配**，每个 Agent 用最合适的模型而不是最贵的。

通过这套架构，你的 AI 团队可以从"单兵作战"真正升级为"团队协作"，效率提升 300% 不是梦想！

**💬 互动话题：**你最想用多 Agent 协作完成什么任务？欢迎在评论区分享你的想法！
