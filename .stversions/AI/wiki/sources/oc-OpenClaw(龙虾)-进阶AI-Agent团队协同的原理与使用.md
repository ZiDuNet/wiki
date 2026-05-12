---
tags: [AGENTS.md, Agent, Agent路由, Gateway, OpenClaw, SOUL.md, 多Agent协作, 安全隔离]
sources: ['微信公众号/OpenClaw/OpenClaw(龙虾) 进阶：AI Agent团队协同的原理与使用.md']
created: 2026-05-10
updated: 2026-05-10
---

# OpenClaw(龙虾) 进阶：AI Agent团队协同的原理与使用

**Source:** OpenClaw 公众号文章
**Category:** OpenClaw
**Date ingested:** 2026-05-10
**Type:** article

## Summary

> 📎 来源: 码农Linx | 时间: 2026-04-23 13:07 在构建复杂的 AI Workflow 时，依赖单一的大模型或单一的 Agent，通常难以兼顾不同领域的专业性。上下文一长，AI 就容易“失忆”或“越界”。趋势必然是**多 Agent 协同作业（Multi-Agent）**——让负责调度的“老板”、负责写代码的“技术专家”和负责搜集信息的“情报员”各司其职，通过标准的协议进行串联、并联。 上篇文章我们介绍了多Agent的配置与接入，这里将拆解 OpenClaw 的多 Agent 协作机制，将上篇文章所创建的三个Agent，组建成为一支“数字”团队。文本使用的OpenCl...

## Key Claims

- 唯一标识符（agentId）**：定义 Agent 时，必须确保所有的
- 指令流转路径**：当你向 Agent X 下达复杂任务时，X 会通过内置工具
- 会话隔离与穿透**：默认情况下，每个 Agent 处于绝对的上下文隔离中，只关注自己的目标。如果调度者需要跨 Agent 查看历史会话，必须通过

## Entities Mentioned

- [[OpenClaw]]
- [[飞书]]

## Concepts Covered

- [[AGENTSmd配置]]
- [[Agent路由]]
- [[Cron定时任务]]
- [[SOULmd配置]]
- [[多Agent协作]]
- [[数据安全]]
- [[爬虫]]
- [[记忆系统]]

## Related Sources

- [[OpenClaw文章索引]]
