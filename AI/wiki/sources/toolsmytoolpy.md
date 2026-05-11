---
tags: [Hermes, Agent, Claude, MCP, Prompt, API, Python, OpenAI]
source: "智能思辨录"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# tools/mytool.py

> 来源: [智能思辨录](https://mp.weixin.qq.com/s?__biz=MzY5NzIwOTg4MQ==&mid=2247483790&idx=1&sn=f613d0cf8b37898f6534700223564f6c&chksm=f5f2260398b21c1f818afbe5d8ea0086a06135d78e5dbffa1d3251183d96e53ee33f03d624d2&mpshare=1&scene=1&srcid=0421zp5815pO8LUnQ5QRJpNr&sharer_shareinfo=57eaf6ae12f869696bc2f484f0822823&sharer_shareinfo_first=57eaf6ae12f869696bc2f484f0822823) | 2026-04-21

## 摘要

这篇文章是给想深入了解 Hermes Agent 的小伙伴看的（不讲怎么安装和使用），初心是我想从工程上深入学习一下 AI Agent。为什么是 Hermes 而不是 OpenClaw，主要是因为我觉得 Hermes 的工程架构更加清晰、门槛较低一些。我后续准备做一个系列将 Agent 所学的部分和大家分享讨论。
这篇文章准备从一个宏观的角度去看看如果开发者拿到这么一个项目，我们应该如何启动，能够快速上手。
下面从开发环境、架构、功能地图、定制开发、配置、测试、调试几个部分，将这个项目拆分开来。
▍ 架构概要
Hermes Agent 的核心是一个工具调用循环。整个流程如下：
▍ 功能地图
核心的功能模块：
模块的依赖关系如下：
快速定位：
|  |  |
| --- | --- |
| 想改什么 | 去哪里 |
| 核心对话循环 | `run_agent.py` → `AIAgent` |
| 系统提示词 | agent/prompt\_builder.py |
| 上下文压缩 | agent/context\_compressor.py |
| 工具注册机制 | tools/reg...

## 相关实体

[[Anthropic]], [[Claude]], [[Docker]], [[Hermes]], [[MCP]], [[OpenAI]], [[OpenClaw]], [[Python]]

## 相关概念

[[AI-Agent]]
