---
tags: [Hermes, Kanban, Agent协作, 多Agent, SQLite]
sources: [Hermes/Hermes Kanban 解析：与「Agent 协作模式全景解析」的对比分析.md]
created: 2026-05-10
updated: 2026-05-10
---

# Hermes Kanban 解析：与「Agent 协作模式全景解析」的对比分析

**Source:** 星汉问元
**Category:** Hermes
**Date ingested:** 2026-05-10
**Type:** analysis

## Summary

系统性分析 Hermes Kanban v1 设计规范：基于 SQLite 的持久化任务板，多 Agent Profile 通过 OS 进程协作。与学术理论中的 Agent 协作模式（如 Arxiv 论文分类法）进行对比，指出 Kanban 的实用价值。

## Key Claims

- Hermes Kanban 基于 SQLite（~/.hermes/kanban.db），重启不丢失
- 不同 Agent Profile（researcher、writer、backend-eng）共享任务板
- OS 进程隔离：每个 worker 独立进程，崩溃自动重新认领
- 与进程内子 Agent 集群相比更稳定，不因单个 Agent 崩溃影响整体
- 实现了学术理论中的"共享黑板"协作模式

## Entities Mentioned

- [[Hermes]] — AI Agent 框架
- [[Hermes-Kanban-保姆级实战教学：从0到1跑通多角色协作写公众号文章全流程]] — 持久化多 Agent 任务板
- [[SQLite]] — 任务存储后端

## Concepts Covered

- [[Agent协作]] — 多 Agent 通过任务板协作的模式
- [[多Agent]] — Agent 间的分工和通信机制
