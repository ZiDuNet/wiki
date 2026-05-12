---
tags: [Hermes, Agent, Claude, API, Python, OpenAI, Skill]
source: "斐哥讲AI"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Hermes 的五种多 Agent 协作模式

> 来源: [斐哥讲AI](https://mp.weixin.qq.com/s?__biz=MzYzNTg3NTM2NA==&mid=2247483700&idx=1&sn=3f3184d80fe11f33ecae3e3e52ea3ac1&chksm=f186f2cd852f008fae6e65fc7c26ccdfa8dbdf28a73aff572907a088d778e396914dfdff7a40&mpshare=1&scene=1&srcid=0420b1ftFIt0bsykpHd0Hcuc&sharer_shareinfo=9590649dfa4aeac9a637545d05aff307&sharer_shareinfo_first=9590649dfa4aeac9a637545d05aff307) | 2026-04-20

## 摘要

单个 AI Agent 的能力有上限。当任务复杂到需要并行处理、多角色分工、或跨领域协作时，多 Agent 协作就成了必然选择。
本文系统梳理 Hermes 支持的五种多 Agent 模式，对比不同协作架构的优劣，并给出各场景下的实践建议。
Hermes 的多 Agent 能力分为两层：
|  |  |  |
| --- | --- | --- |
| 层级 | 工具 | 定位 |
| 主 Agent | 当前会话的你 | 协调者：理解任务、分拆计划、分配工作、整合结果 |
| 子 Agent | delegate\_task | 执行者：接任务、执行、回报 |
子 Agent 可以是：
- Hermes 自身（同一模型，不同上下文）
- Claude Code（Anthropic CLI Agent）
- Codex / OpenCode（OpenAI/第三方 CLI Agent）
子 Agent 按顺序一个接一个执行，每个拿到完整上下文，独立完成后把结果交回主 Agent。
- 任务有依赖关系（下一步依赖上一步结果）
- 需要主 Agent 把控流程（每步完成后决策）
- 步骤少（...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Hermes]], [[OpenAI]], [[Python]], [[React]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[TDD]]
