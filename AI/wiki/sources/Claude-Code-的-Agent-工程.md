---
tags: [Claude, Agent, Prompt, API, OpenAI]
source: "SooKool"
created: 2026-04-24
updated: 2026-05-10
category: Claude
---

# Claude Code 的 Agent 工程

> 来源: [SooKool](https://mp.weixin.qq.com/s?__biz=Mzg4MTk0Njc5Mw==&mid=2247483917&idx=1&sn=9f5c08fb3277222bdf423f7a2a91065a&chksm=ced1074017e3b55116012a8513b284e34ad779c59f2d84491b94da61353e559300503e680fa9&mpshare=1&scene=1&srcid=0424pkz4ej2EdJBV6zwJgtwP&sharer_shareinfo=85dfa206741752e074bcec4dcf2f0773&sharer_shareinfo_first=85dfa206741752e074bcec4dcf2f0773) | 2026-04-24

## 摘要

● Claude Code “开源”
Claude Code 的 Agent 工程
Claude Code 的源码泄露之后我和AI一起分析了一遍。模型调用部分平平无奇，标准 API streaming。但围绕它的工程量大到离谱，是调用本身的几十倍。这篇先讲五个对我有启发的设计，也是 Claude Code 跟市面上其他 Agent 拉开差距的地方。
—— ✦ ——
一、模型还在说话，工具已经跑完了
大多数 Agent 框架处理工具调用的流程是：模型输出完 → 解析出要调哪些工具 → 一个一个执行 → 拿到结果 → 下一轮。四步串行，中间全在等。
Claude Code 砍掉了这个等待。
它有一个叫 `StreamingToolExecutor` 的组件。模型在流式输出的过程中，只要吐出一个 tool\_use 的 JSON block，执行器立刻把这个工具启动。不等模型说完。模型接着吐第二个工具调用，执行器看一眼：是只读操作（读文件、搜代码）就直接并行启动，最多同时跑 10 个；是写操作就排队串行。
等模型把话说完的时候，读操作基本都已经返回结果了。
这种"边说边干"的流水线策略，在一...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Markdown]], [[OpenAI]], [[React]]

## 相关概念

[[Function-Calling]], [[Multi-Agent]], [[记忆系统]]
