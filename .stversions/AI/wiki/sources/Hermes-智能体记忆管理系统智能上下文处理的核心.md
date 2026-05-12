---
tags: [Hermes, Agent]
source: "野生AI架构师"
created: 2026-04-26
updated: 2026-05-10
category: Hermes
---

# Hermes 智能体记忆管理系统：智能上下文处理的核心

> 来源: [野生AI架构师](https://mp.weixin.qq.com/s?__biz=MzU3NDQ3MjI3Nw==&mid=2247486077&idx=1&sn=6eb6ec8a50e8e3bd8550fbac29166792&chksm=fc0f418e3949b9a68291ed15d07c3c6760f435d28f31f7c1fa3f31617996c3cd63848901db6a&mpshare=1&scene=1&srcid=0426IKsdoqT6Ohu6hFWUC5MX&sharer_shareinfo=7a4c0aa08c38554a59e36cbf3c835001&sharer_shareinfo_first=7a4c0aa08c38554a59e36cbf3c835001) | 2026-04-26

## 摘要

在 AI 智能体时代，记忆管理是智能体系统的核心组成部分。Hermes 的记忆管理系统负责管理智能体的记忆库，包括用户偏好、重要信息和会话历史，同时处理上下文压缩以适应模型的token限制。
1. MemoryManager 类：记忆提供者的协调者
中的 **MemoryManager** 类是整个记忆管理系统的核心，负责协调内置记忆提供者和外部记忆插件。
1.1 设计理念
MemoryManager 的设计体现了以下几个关键理念：
01**单一责任原则**：每个记忆提供者负责特定类型的记忆管理，MemoryManager 只负责协调它们
02**可扩展性**：支持添加外部记忆插件，扩展系统的记忆管理能力
03**容错性**：一个记忆提供者的故障不会影响其他记忆提供者的运行
04**优先级管理**：内置记忆提供者始终优先于外部记忆提供者
1.2 记忆提供者管理
MemoryManager 实现了严格的记忆提供者管理机制：
内置提供者：始终注册为第一个提供者，且不能被移除
外部提供者：一次只允许注册一个外部记忆提供者，防止工具 schema 膨胀和冲突
工具路由：为每个记忆工具维护到对应...

## 相关实体

[[Hermes-Agent]]

## 相关概念

[[上下文管理]]
[[Agent架构]]
