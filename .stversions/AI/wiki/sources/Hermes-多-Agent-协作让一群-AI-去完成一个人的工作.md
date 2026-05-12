---
tags: [Hermes, Agent]
source: "数语星河"
created: 2026-04-30
updated: 2026-05-10
category: Hermes
---

# Hermes 多 Agent 协作：让一群 AI 去完成一个人的工作

> 来源: [数语星河](https://mp.weixin.qq.com/s?__biz=MzU0MDgzNDkyNg==&mid=2247485450&idx=1&sn=9c517e878cd9788253783cc5dc388675&chksm=fa5f04d1fb88f42041bde45b8d857748211584b10d9d490d5972bba3651697709b2bca7705db&mpshare=1&scene=1&srcid=0430o6Gz21Ya94RZpBeVVPgp&sharer_shareinfo=c277e4e2ac1cbb5bf7a3815c9bfa3379&sharer_shareinfo_first=c277e4e2ac1cbb5bf7a3815c9bfa3379) | 2026-04-30

## 摘要

你可能遇到过一个任务，复杂到单个 AI 根本搞不定。
比如你要做一次代码审查，涉及到代码重构、安全漏洞检测、性能分析、文档生成四个维度，每个维度都需要专门的知识背景和工具支持。让一个 AI 同时处理这四件事，它要么因为上下文太长而卡住，要么顾此失彼，每件事都做得浅尝辄止。
Hermes 的多 Agent 协作系统，就是为了解决这类问题而设计的。你可以把一个复杂任务，分配给多个专业的 AI Agent，让他们各司其职、信息共享、协同完成。
这不只是一个"并发处理"的效率问题，而是一个**能力边界**的问题——有些复杂工作，单个 Agent 的知识和上下文根本不够，需要多个 Agent 各有专长、联合攻关。
Hermes 支持两种多 Agent 协作模式，适用于不同的场景。
**模式一：父子 Agent（Hierarchical模式）**
一个父级 Agent 负责任务拆解和结果整合，多个子 Agent 分别负责执行子任务。
典型的工作流程是这样的：
1. 你给父 Agent 下达一个复杂指令，比如"帮我审查这个代码仓库的安全问题"
2. 父 Agent 分析任务，拆解成"代码扫描"、"漏...

## 相关实体

[[Hermes]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[代码审查]]
