---
title: "Hermes Kanban 实战：我是怎样让多个 Agent 真正协作起来的！"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: [Hermes Kanban 实战：我是怎样让多个 Agent 真正协作起来的！.md]
tags: [Hermes-Agent, Kanban看板, Multi-Agent, Agent协作]
---

## Summary

实战记录分享如何用 Hermes 的 Kanban 模块实现真正的多 Agent 协同工作。文章指出 delegate_task 是一次性同步分派（用完结束），而 Kanban 是能持续运转、中断可接续、换角色可接力、崩溃可恢复的工作队列，远超 delegate_task 的能力层级。文章包含详细的任务创建、依赖链配置、三个 Agent 串行协作的完整踩坑记录。

## Key Claims

1. delegate_task 和 Kanban 不在一个层级：前者一次性同步分派，后者是持久运转的工作队列
2. Kanban 四大特性：持续运转（不是用完即焚）、中断可接续、换角色能接力、崩溃可恢复
3. 多 Agent 协作常见失败原因：任务之间没有依赖关系，导致同时启动同时失败
4. 需为 researcher→writer→reviewer 三者建立显式依赖链，确保流水线有序交接
5. 理想中的 Agent 协作和实际跑出来的效果"差了十万八千里"，需要大量调试

## Entities Mentioned

- [[Hermes]] — AI Agent 框架
- [[Multi-Agent]] — 多智能体协同领域

## Concepts

- [[Kanban看板]] — Hermes 的 Kanban 模块用于多 Agent 任务协同
- [[Agent-Teams]] — Agent 团队协作架构
- [[Agent路由]] — 任务分发机制

## Limitations

- 依赖链配置复杂，调试成本高
- 需要对 Hermes 版本和功能有较深理解
