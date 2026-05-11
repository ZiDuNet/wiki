---
tags: [Hermes, Agent, Claude, 飞书, Prompt, API, OpenAI, Skill]
source: "蝈蝈的AI笔记"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# 身份你是一位代码任务调度专家。你自己不直接编写代码，而是通过调用 CodeX 或 Claude Code 来完成所有编码工作。# 工作方式- 收到需求时，先分析任务类型和复杂度- 将任务清晰描述后，委派给 CodeX 或 Claude Code 执行- 审查返回的代码质量，必要时要求修改- 向用户汇报结果，而不是自己动手写# 风格- 简洁直接，像技术项目经理- 任务拆解精准，指令清晰无歧义# 避免- 自己生成大段代码- 不加审查地直接转发工具返回结果

> 来源: [蝈蝈的AI笔记](https://mp.weixin.qq.com/s?__biz=MzYzNTE4Njc0OQ==&mid=2247484411&idx=1&sn=41096a1878b0f09854b634a9c93497bb&chksm=f14de851958b5c0b697f3fd46231254bcf8e9f5e5f3c7256f9cb9a4b61a30fe9bb4024f29911&mpshare=1&scene=1&srcid=0422ge91LUJlts6vE0Zcq4bC&sharer_shareinfo=6bfa175b4c5e3773795f9b800e869117&sharer_shareinfo_first=6bfa175b4c5e3773795f9b800e869117) | 2026-04-22

## 摘要

哈喽，大家好，我是蝈蝈
很多人用 Hermes 的方式是一个 Agent 包揽所有事，但用久了会发现一个问题：**Agent 的记忆越积越杂，行为越来越难预测。**写代码时学到的项目习惯，和写日报时积累的表达偏好，全混在同一个 `MEMORY.md` 里——导致 Agent的记忆会变乱。
而 Hermes里的 Profiles 就是解这个问题的。每个 Profile 是完全隔离的独立环境，有自己的配置、记忆、技能和 Gateway，**各自成长，互不干扰。**
**我自己是用 Profiles 功能在同一台机器上同时跑两个完全独立的 Agent，**一个负责每天自动拉数据、整理知识库、推飞书日报, 另一个专门做编程任务。
下面我把整个搭建过程完整记录下来, 直接可以照着做。
**`coder` Profile** 是我们本次新增的, 用来处理代码任务调度员。它自己不写代码，只负责理解需求、拆解任务、调用本地 CodeX 或 Claude Code 执行，审查结果后汇报。这个设计的逻辑是：**CodeX 已经积累了大量专业 coding skill，是真正擅长写代码的工具，**Herme...

## 相关实体

[[ChatGPT]], [[Claude-Code]], [[Claude]], [[Hermes]], [[OpenAI]], [[飞书]]

## 相关概念

[[代码生成]]
