---
tags: [Agent, Claude, MCP, Harness, Prompt, API, Skill]
source: "图灵编辑部"
created: 2026-04-30
updated: 2026-05-10
category: Agent
---

# Agent = Model + Harness！一文讲透 Harness 的设计与未来！

> 来源: [图灵编辑部](https://mp.weixin.qq.com/s?__biz=MjM5Njc0MjIwMA==&mid=2649841560&idx=1&sn=7d8801a8c62297e6d0f74179d47b84e1&chksm=bf5f7aa188d215b93ace9de6f5db23ec46c2d8250acd250cd468f85793d6107194d052c260fd&mpshare=1&scene=1&srcid=04306nTRTsnTlwGfJc9qlX4a&sharer_shareinfo=58dd3c5896d87cd5fa35a922d63c4dbe&sharer_shareinfo_first=58dd3c5896d87cd5fa35a922d63c4dbe) | 2026-04-30

## 摘要

Harness 工程就是围绕模型构建系统，把它变成可以实际工作的引擎。模型本身提供智能，而 Harness 让这种智能变得可用。本文会先定义什么是 Harness，再从模型这一基本出发点，推导出现阶段以及未来 Agent 所需要的核心组成。
***01***
Agent = Model + Harness。如果你不是在训练模型，那么你做的大多属于 Harness 的范畴。
所谓 Harness，是指：“即所有不属于模型本身的代码、配置以及执行逻辑。”
一个裸模型并不能算作 Agent；只有当 Harness 为其提供状态管理、工具调用能力、反馈循环以及可执行约束时，它才真正成为一个 Agent。
更具体地说，Harness 通常包括：系统提示词、工具与技能（以及 MCP）及其说明、封装好的基础设施（如文件系统、沙箱、浏览器）、编排逻辑（例如子 Agent 的生成与交接、模型路由），以及用于保证执行稳定性的 Hook（钩子机制）或中间件（如上下文压缩、续写机制、Lint 检查等）。
在实际系统中，模型与 Harness 的边界可以有多种划分方式，而且往往并不清晰。但从工程视角来看，这样的...

## 相关实体

[[Claude-Code]], [[Claude]], [[Harness]], [[LangChain]], [[MCP]], [[ReAct]]

## 相关概念

[[MultiAgent]], [[上下文工程]]
