---
type: concept
name: Managed Agents
created: 2026-05-11
updated: 2026-05-11
---

# Managed Agents

**类型:** 概念 (架构/管理模式)
**提及文章数:** 1

## 定义

Managed Agents是将AI Agent作为团队成员管理的理念和实践。Agent可以像队友一样被分配任务、更新状态、发表评论、报告阻塞，实现真正的团队协作式AI开发。

## 核心特性

### 任务生命周期

| 状态 | 描述 |
|------|------|
| enqueue | 任务排队等待分配 |
| claim | Agent认领任务 |
| start | 开始执行任务 |
| complete | 任务成功完成 |
| fail | 任务失败并报告原因 |

### 管理层能力

- Issues看板管理Agent任务
- WebSocket实时推送进度
- 统一运行时管理（本地+云端）
- daemon自动检测可用Agent CLI
- Skills系统沉淀可复用能力

## 平台实现

[[Multica]] 是Managed Agents的代表性平台：
- 支持Claude Code、Codex、OpenCode、Hermes等多种编码Agent
- 不是CLI替代品，而是协作和管理层
- 适合已使用多个编码Agent的团队

## 适用场景

- 多Agent协作开发
- 自动化部署流程
- PR Review自动化
- 测试补充和维护
- 团队知识沉淀

## 相关实体

- [[Multica]] — Managed Agents平台
- [[Claude-Code]] — AI编程助手
- [[Hermes]] — 开源AI智能体框架

## 相关概念

- [[Agent架构]], [[Skills技能系统]], [[团队协作]], [[多Agent协作]]

## 相关文章

- [[Multica编码Agent团队管理平台]]