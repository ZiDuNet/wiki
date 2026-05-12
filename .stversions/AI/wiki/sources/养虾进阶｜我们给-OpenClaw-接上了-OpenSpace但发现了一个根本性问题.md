---
tags: [OpenClaw, Agent, Claude, MCP, 飞书, API, OpenAI, Skill]
source: "嘎叔学AI"
created: 2026-04-25
updated: 2026-05-10
category: OpenClaw
---

# 养虾进阶｜我们给 OpenClaw 接上了 OpenSpace，但发现了一个根本性问题

> 来源: [嘎叔学AI](https://mp.weixin.qq.com/s?__biz=MzIyNjYxNjM0Mg==&mid=2247484960&idx=1&sn=fee301b9cce15ed3be19a4834f5ffae7&chksm=e9b2b5dabfd6023530fa93efd525241e6a60ac3d50d87938120ec639be0708c4a68fd7f27350&mpshare=1&scene=1&srcid=0425hfW2KPGIPw6qLQfu2vGw&sharer_shareinfo=d75ae0fbf966c32c62dc951fcd05ac04&sharer_shareinfo_first=d75ae0fbf966c32c62dc951fcd05ac04) | 2026-04-25

## 摘要

OpenSpace 确实是一个有价值的项目，它的核心理念很清晰：**让 AI Agent 不只是执行任务，还能从任务中学习，变得一次比一次强。**
但经过实机验证，我发现了一个关键问题：**如果你不知道如何正确使用，也没有一个支持多 system message 的模型，OpenSpace 的"自进化"能力根本无法真正生效。**
换句话说：**OpenSpace 的价值取决于驱动它的模型的强弱，而使用强模型的时候我们反而并不需要太过纠结“能力”。这其实就是“一根筋两头堵”。**
下面我会详细展开我们验证的过程、发现的问题、以及这个矛盾的核心所在。
OpenSpace 是港大 HUDS 团队开源的一个"自进化 Skill 引擎"。
它的核心思想是：今天的 AI Agent（无论用 Claude、GPT 还是国产大模型，又或者使用了 OpenClaw 这样的底座工具）都有一个致命缺陷——
OpenSpace 要解决的就是这个问题。它通过三个进化机制让 Agent 真正学会：
| 进化类型 | 触发条件 | 效果 |
| --- | --- | --- |
| **AUTO-FIX** | ...

## 相关实体

[[Claude]], [[DeepSeek]], [[MCP]], [[OpenClaw]], [[Qwen]], [[飞书]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[自进化系统]]
