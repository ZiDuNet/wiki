---
tags: [Hermes, Agent, Claude, MCP, GitHub, 飞书, Prompt, API]
source: "鸿枫技术栈"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# 项目上下文- 这是一个 FastAPI 后端项目，使用 SQLAlchemy ORM- 所有数据库操作必须使用 async/await- 测试文件放在 tests/ 目录下，使用 pytest-asyncio- 禁止提交 .env 文件- API 路由统一使用 /api/v1/ 前缀- Git commit message 遵循 Conventional Commits 规范

> 来源: [鸿枫技术栈](https://mp.weixin.qq.com/s?__biz=MzI4NTA2MjE5OA==&mid=2247485156&idx=1&sn=11bf967b64b1505e548d68b0fd6479b6&chksm=eaec18621aeeaf3e423c23902b440bb8203527f2722a7d3764be3b9340ba7aaadcc386d9621e&mpshare=1&scene=1&srcid=0421umqOHVmUuPrW4YcxkWLo&sharer_shareinfo=8da5bb10c6d842febd1a2b93311183d4&sharer_shareinfo_first=8da5bb10c6d842febd1a2b93311183d4) | 2026-04-21

## 摘要

2026 年 2 月，Nous Research 发布了 Hermes Agent，一个"会自我进化"的开源 AI Agent 框架。不到两个月，GitHub 星标突破 35k，成为 AI Agent 赛道增长最快的项目之一。和 OpenClaw 那种"做完就走"的无状态模式不同，Hermes 的核心理念是 \*\*"the agent that grows with you"\*\*——越用越懂你，用得越久能力越强。
但说实话，很多中文用户装完之后会发现：官方文档全是英文，网上的教程要么太浅要么太散，真正能指导日常使用的高阶技巧几乎找不到。这篇文章就是想把这个缺口补上。我会从实际使用场景出发，把 Hermes Agent 最值得掌握的功能——上下文文件、记忆系统、技能体系、定时任务、安全沙箱——逐个拆开讲，同时在关键位置穿插和 OpenClaw 的对比，帮你看清两者的本质区别。
很多文章喜欢用表格列一堆功能做对比，但看完还是不知道怎么选。我用一句话总结它们的根本区别：
具体来说，差异体现在五个核心维度：
**1. 记忆机制**
OpenClaw 的记忆依赖 Markdown 文件（S...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Docker]], [[GitHub]], [[Hermes]], [[MCP]], [[Markdown]], [[OpenClaw]], [[OpenRouter]], [[Python]], [[SQLite]], [[微信]], [[钉钉]], [[飞书]]

## 相关概念

[[AI-Agent]], [[记忆系统]]
