---
title: Agent工程原则
type: concept
tags: [Agent架构, 工程化, 最佳实践]
sources: [构建可靠AI Agent的十二条军规.md, 不要错过这10个本周火火火的-GitHub-开源项目.md]
created: 2026-05-24
updated: 2026-05-24
---

# Agent工程原则

借鉴 12-Factor Apps，定义构建生产级 AI Agent 的工程原则，确保 Agent 可靠、可维护。

## 核心理念

- 把 LLM 当自然语言到工具调用的转换引擎
- 用确定性代码控制流程
- 小而专注的 Agent

## 12 条原则

1. 自然语言到工具调用
2. 拥有你的 Prompt
3. 拥有你的上下文窗口
4. 工具即结构化输出
5. 统一执行状态和业务状态
6. Launch/Pause/Resume API
7. 用工具调用联系人类
8. 拥有你的控制流
9. 错误压缩到上下文窗口
10. 小而专注的 Agent
11. 从任意位置触发
12. 无状态 Reducer 模式

## 代表项目

- [[12-factor-agents]]

## 来源文章

- [[构建可靠AI Agent的十二条军规]]