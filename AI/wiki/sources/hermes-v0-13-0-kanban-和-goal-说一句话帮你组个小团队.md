---
tags: [Hermes, Kanban, goal, 多Agent, v0.13]
sources: [Hermes/Hermes v0.13.0 发布了Kanban和_goal： 说一句话，帮你组了个小团队.md]
created: 2026-05-10
updated: 2026-05-10
---

# Hermes v0.13.0：Kanban 和 /goal，说一句话帮你组个小团队

**Source:** 量子智元
**Category:** Hermes
**Date ingested:** 2026-05-10
**Type:** article

## Summary

解析 Hermes v0.13.0 两个核心功能：/goal 持续目标机制和 Durable Multi-Agent Kanban。/goal 让 Agent 不再一问一答，自动持续执行直到目标完成；Kanban 让多 Agent Profile 通过持久化任务板协作。

## Key Claims

- /goal = 持续目标机制：设定目标后 Agent 自动循环执行，直到完成或 20 轮上限
- 轻量"判官"模型评估每轮是否完成，偏保守策略，不确定就继续
- Durable Multi-Agent Kanban = 持久化任务板，不同 Agent Profile 共享
- 两者解决不同问题：/goal 解决单 Agent 持续性，Kanban 解决多 Agent 协作
- 判官出错默认当 continue 处理，turn budget 是最后安全网

## Entities Mentioned

- [[Hermes]] — AI Agent 框架
- [[Hermes-Kanban-保姆级实战教学：从0到1跑通多角色协作写公众号文章全流程]] — 持久化多 Agent 任务板
- [[goal]] — 持续目标机制

## Concepts Covered

- [[多Agent]] — 多 Agent 通过 Kanban 协作
- [[Agent目标]] — 持续目标机制的实现
