---
tags: [Hermes, Agent, Prompt, API, OpenAI]
source: "跨境AI入门指南"
created: 2026-05-05
updated: 2026-05-10
category: Hermes
---

# Part 14 Hermes Agent的外部记忆（Memory Providers ）

> 来源: [跨境AI入门指南](https://mp.weixin.qq.com/s/3Hu9iC2h3qhzcxDkLD-ODg) | 2026-05-05

## 摘要

https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers
从 Persistent Memory 进入 Memory Providers，学习的焦点从"内置的轻量级记忆系统"转向了"可插拔的外部记忆后端"。这一页的核心是：当内置 memory 的 2,200 + 1,375 字符限制不够用时，Hermes 提供了 8 种不同设计哲学的外部记忆方案来扩展。
文档开篇就明确了一个关键设计原则：
内置的 MEMORY.md 和 USER.md 始终正常工作。外部 provider 是附加的（additive）。这意味着：
- 内置 memory 仍然在 session 启动时注入 system prompt
- 外部 provider 在此基础上额外注入上下文、提供搜索工具
- 两者共存，各有分工
文档还强调：**一次只能激活一个外部 provider**。你不能同时启用 Honcho 和 Hindsight。
当一个外部 memory provider 激活时，Hermes 自动执行 6 ...

## 相关实体

[[Hermes]], [[OpenAI]], [[OpenRouter]], [[SQLite]]

## 相关概念

[[知识图谱]], [[记忆系统]]
