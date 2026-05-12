---
type: protocol
created: 2026-05-10
updated: 2026-05-10
---

# MCP

**类型:** 协议 (Protocol)
**全称:** Model Context Protocol（模型上下文协议）
**提出方:** [[Anthropic]]

## 简介

MCP（Model Context Protocol）是由 [[Anthropic]] 提出的一种开放标准协议，旨在让 AI 模型能够以统一的方式连接外部工具和数据源。如果说过去的大模型是一个"会说话的大脑"，MCP 解决的核心问题是：**Agent 如何连接外部世界**。

在 MCP 出现之前，每个 AI 工具想连接一个外部服务（如数据库、[[GitHub]]、[[Notion]]）都需要专门开发一套对接方式，既麻烦又不通用。MCP 之后，**一套标准，AI 和任何工具都能直接"握手"**。

## 核心架构

MCP 的架构中有三个核心角色：

1. **Host（宿主）**：用户直接使用的 AI 应用，如 [[Claude-Desktop]]、[[Claude-Code]]、[[Cursor]] 等
2. **Client（客户端）**：运行在 Host 内部的 MCP 客户端，负责与 Server 通信
3. **Server（服务端）**：提供具体能力的独立进程，每个 Server 对接一个外部服务

典型工作流：用户对 AI 说"帮我查一下 GitHub 上某个 Bug 的最新进展"，Host 通过 Client 调用 GitHub Server，Server 执行查询并返回结果，整个过程用户只需一句话。

## 支持平台

支持 MCP 的平台已覆盖几乎所有主流 AI 工具：
- [[Claude-Desktop]] / [[Claude-Code]]
- [[Cursor]] / [[Windsurf]]
- [[VS-Code]] / [[ChatGPT]]
- [[Codex]] / [[Gemini-CLI]] / [[Replit]]

## MCP 与 Skills 的关系

MCP 和 [[Skills技能系统|Skills]] 是 AI Agent 走向生产力系统的两块关键拼图：

- **MCP 解决连接问题**：Agent 怎么连接外部世界（数据库、API、文件系统等）
- **Skills 解决方法问题**：Agent 怎么学会一套稳定的做事方法

两者结合使 AI Agent 的产品形态从"聊天框"进化为一种新的软件架构。

## 与 Harness 的关系

在 [[Harness框架|Harness]] 工程视角下，MCP 是 Harness 的重要组成部分。Harness 包括系统提示词、工具与技能（以及 MCP）及其说明、封装好的基础设施、编排逻辑以及执行稳定性的 Hook 机制。MCP 为 Harness 提供了标准化的工具接入能力。

## Related Entities

[[Claude-Code]] [[Claude-Desktop]] [[Cursor]] [[Codex]] [[Gemini-CLI]] [[baoyu-skills]] [[Anthropic]] [[OpenAI]] [[Harness]] [[Notion]] [[GitHub]]

## Related Concepts

[[MCP协议]] [[Skill设计模式]] [[Harness-Engineering]] [[Skill编排]] [[渐进式披露]] [[Agent开发]] [[上下文工程]] [[Function-Calling]]

## Mentioned In

- [[Agent-Skills-解剖五个设计决策拯救被上下文淹没的-AI-Agent]] — Agent Skills 解剖：五个设计决策拯救被上下文淹没的 AI Agent
- [[MCP-与-SkillsAI-Agent-真正走向生产力系统的两块拼图]] — MCP 与 Skills：AI Agent 真正走向生产力系统的两块拼图
- [[别再手抄设计稿了我做了个-Skill把任意网站变成设计文档]] — 别再手抄设计稿了：我做了个 Skill，把任意网站变成设计文档
- [[怎么创建一个真正能干活的-Skills？]] — MCP Root Cause Service Builder
- [[我给龙虾装上好用的PPT-Skill]] — 我给龙虾装上好用的PPT Skill
- [[最值得安装的20个Skills]] — ClawHub上的Skill
- [[来了叫MCP]] — 来了，叫MCP
- [[AI智能体Skill与MCP现代AI系统的黄金三角]] — AI智能体、Skill与MCP：现代AI系统的黄金三角
- [[Agent-Model-Harness一文讲透-Harness-的设计与未来]] — Agent = Model + Harness
