---
tags: [OpenClaw, Agent, 飞书, Prompt, API]
source: "码农Linx"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# SOUL.md - main我是小飞本，负责协调团队任务分发。我的性格：高效、冷静。你是老板，负责团队协调、任务调度和进度追踪。遇到需要具体执行的任务，请毫不犹豫地分配给对应的专业 Agent。

> 来源: [码农Linx](https://mp.weixin.qq.com/s?__biz=MzI3MzQ3NDMzNw==&mid=2247484718&idx=1&sn=5a3339b6c51d87711a3806a9eaa337d4&chksm=ea6df0e255b4f17c1cde14da95d92b9c53ccbd61342b41d6a18975c29864740bf8b9696c66c0&mpshare=1&scene=1&srcid=0423Sf0x1CWbbq9RyFOum2Ac&sharer_shareinfo=24abf27c6cd99db6b4bbbb610bcbf1f3&sharer_shareinfo_first=24abf27c6cd99db6b4bbbb610bcbf1f3) | 2026-04-23

## 摘要

在构建复杂的 AI Workflow 时，依赖单一的大模型或单一的 Agent，通常难以兼顾不同领域的专业性。上下文一长，AI 就容易“失忆”或“越界”。趋势必然是**多 Agent 协同作业（Multi-Agent）**——让负责调度的“老板”、负责写代码的“技术专家”和负责搜集信息的“情报员”各司其职，通过标准的协议进行串联、并联。
上篇文章我们介绍了多Agent的配置与接入，这里将拆解 OpenClaw 的多 Agent 协作机制，将上篇文章所创建的三个Agent，组建成为一支“数字”团队。文本使用的OpenClaw版本为：v2026.3.1。
**注意，这里使用的是点对点平级的Agent，不是主从/派生Agent。** 不适合一个公司一个 Gateway 多用户共用的情况，可能会有数据泄露的情况。
在 OpenClaw 中，Agent 之间的通讯并非黑盒，而是建立在极其严谨的**会话隔离（Session Isolation）与分发机制**之上，从根本上杜绝了信息串扰。
- **唯一标识符（agentId）**：定义 Agent 时，必须确保所有的
- **指令流转路径**：当你...

## 相关实体

[[OpenClaw]], [[飞书]]

## 相关概念

[[Multi-Agent]], [[工作流自动化]]
