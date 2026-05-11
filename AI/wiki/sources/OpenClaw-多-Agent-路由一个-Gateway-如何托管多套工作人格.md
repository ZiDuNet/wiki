---
tags: [OpenClaw, Agent, Prompt, Skill]
source: "超级AI技术"
created: 2026-04-24
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw 多 Agent 路由：一个 Gateway 如何托管多套工作人格

> 来源: [超级AI技术](https://mp.weixin.qq.com/s?__biz=MzUyNzA1NDY0MQ==&mid=2247484564&idx=1&sn=193a2ce52ff164b3638e024d392ae1dc&chksm=fbdc4623d93aa37b2375283941692866d748971f9c0463d8b8f120ab925867fa8e6036a6759c&mpshare=1&scene=1&srcid=04245YqfbwAgJtfoGtlCo8Wz&sharer_shareinfo=eb65ef4b8b659b9813e3dbb31d720f71&sharer_shareinfo_first=eb65ef4b8b659b9813e3dbb31d720f71) | 2026-04-24

## 摘要

AI推荐
适合读者：想让一个 Gateway 托管多套隔离工作人格的高级用户和技术负责人。
预计阅读：6 分钟
你将看到：
•多 Agent 的本质是 workspace、agentDir、sessions 和 policy 的隔离。
•bindings 决定消息该路由到哪个 agent。
•目录隔离不是安全隔离，真正边界还要靠 sandbox 和 tool policy。
如果你已经把一个 OpenClaw 入口跑稳，用不了多久就会碰到一个更现实的问题：
**工作消息、家庭消息、自动化任务，到底要不要共用同一个脑子。**
很多人第一次做多 Agent，会从“一个研究、一个写作”这种概念分工开始。但在 OpenClaw 里，真正值得先拆开的，通常不是 prompt，而是边界：
• 不同 workspace
• 不同 auth / state
• 不同 session
• 不同工具权限
所以这一篇不先讲抽象架构，而是先解决一个实际问题：
**怎么让一个 Gateway 托管两套不会串上下文、不会串账号、也不会串权限的 Agent。**
1. 你已经至少有一个可用的 OpenClaw ag...

## 相关实体

[[OpenClaw]]

## 相关概念

[[Agent路由]]
[[数据安全]]
