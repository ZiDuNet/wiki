---
type: concept
name: Agent-Harness
tags: [Agent, 执行环境, 工程化]
sources: [GitHub 炸了：19 万星的 Agent 配置天花板，一天涨 2k+星.md]
created: 2026-05-26
updated: 2026-05-26
---

# Agent Harness

## 核心定义

Harness（执行环境）是 Agent 工程化的核心问题：不是让模型更聪明，而是让协作方式更稳。

## 痛点

- 昨天讲过的项目背景，今天又要重讲一遍
- 装了一堆 MCP，上下文却越用越短
- 改完代码心里没底，不知道有没有踩安全雷

## 解决方案

[[ECC]] 等工作台试图解决的正是 Harness 问题：
- 记忆机制保留会话间上下文
- 安全扫描发现密钥/Hook 风险
- 规范化 Skill 减少重复配置

## 相关实体

- [[ECC]] — 解决 Harness 问题的开源工作台
- [[Claude Code]] — Harness 概念的讨论对象之一
- [[OpenClaw]] — Harness 概念的另一实践者
- [[AgentShield]] — 安全扫描工具