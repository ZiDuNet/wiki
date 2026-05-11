---
tags: [OpenClaw, Agent, RAG, Prompt, API, Python, Skill]
source: "数智札记"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# IDENTITY.md - Who Am I?

> 来源: [数智札记](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc1MDg4Ng==&mid=2247483979&idx=1&sn=e49a301a7a6725007b303a7f59877376&chksm=c19946ebfe7e2f8f9d063008d90746b8aa0b68d6ccf68a322ae22f59bc5b089a3e78abd54bbd&mpshare=1&scene=1&srcid=0420N8kD8GAiWxG3IV5WuZKM&sharer_shareinfo=78cf2d26cec52350558158c6effd8bff&sharer_shareinfo_first=78cf2d26cec52350558158c6effd8bff) | 2026-04-20

## 摘要

当我让一个 Agent 帮我写文章，它悄悄调动了另外一个 Agent 帮我画图——这就是我今天用 OpenClaw 搭建的多智能体团队。
01
一个 Agent 包含哪些核心要素？
在实操 OpenClaw 创建 Agent 之前，先搞清楚一个问题：一个 AI Agent 到底由什么组件？
1. 身份（Identity）
Agent 是谁？叫什么？什么风格说话？这部分对应 OpenClaw 中的 `IDENTITY.md`。
2. 灵魂（SOUL）
Agent 的思维方式、行为准则、专业能力范围。`SOUL.md` 定义了它"遇到问题怎么想、怎么做"。
3. 工具（Tools）
Agent 能调用哪些工具？搜索、画图、发消息、写文件……对应 OpenClaw 中的 Skills（技能）。
4. 记忆（Memory）
Agent 需要记住什么？短期靠会话，长期靠文件。对应 `MEMORY.md` 和 `memory/` 目录。
5. 上下文（Context）
每次对话的历史、当前任务的背景信息。OpenClaw 会自动维护会话上下文。
6. 执行环境（Workspace）
Agent 的...

## 相关实体

[[OpenClaw]], [[Python]]

## 相关概念

[[AI-Agent]], [[Multi-Agent]]
