---
tags: [OpenClaw, Agent, Claude, 飞书, Harness, Prompt, API, Skill]
source: "特别可AI"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# 一文讲透 OpenClaw 里到底该用 Multi-Agent，还是主 Agent + Sub-Agent

> 来源: [特别可AI](https://mp.weixin.qq.com/s?__biz=MzI5MzA4NjkwNQ==&mid=2647668652&idx=1&sn=b3994971066b2eb1d1190872a9fafd91&chksm=f50dfc2ed3df1cdd2dcdaa0badb2cf069a4546416f1a1bab0c2cfc2cb69ec0055f091cac4de8&mpshare=1&scene=1&srcid=0420PCrwDPiujeXOafHfTWSj&sharer_shareinfo=80716824f11f5576fcd83462a79c6a32&sharer_shareinfo_first=80716824f11f5576fcd83462a79c6a32) | 2026-04-20

## 摘要

越来越多人开始搭建多Agent系统，也看到sub-agent的用法，困惑于：
- 要不要直接配多个长期 agent？
- 还是保留一个主 agent，再用 sub-agent 做任务拆解？
- 这两种模式到底差在哪？
- 哪种更适合个人使用，哪种更适合长期体系化？
这篇文章结合 OpenClaw 官方文档来分享：
1. 1. **Multi-Agent 到底是什么**
2. 2. **主 agent + sub-agent 到底是什么**
3. 3. **实际该怎么选、怎么落地**
先给结论：
如果把这两个问题分清，很多架构选择就不难了。
OpenClaw 官方文档对 agent 的定义非常明确：一个 agent 不是一句 prompt，也不是一个会话皮肤，而是一个**完整隔离的大脑**。它有自己的：
- workspace
- `agentDir`
- auth profiles
- session store
- persona / SOUL / AGENTS 规则
- skills
也就是说，**多 agent 并不是“一个 agent 换几套 prompt”，而是多个独立工作单...

## 相关实体

[[Claude-Code]], [[Claude]], [[Gemini]], [[OpenClaw]], [[飞书]]

## 相关概念

[[MultiAgent]], [[内容创作]]
