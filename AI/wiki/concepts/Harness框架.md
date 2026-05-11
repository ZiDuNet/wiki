---
tags: [concept, 技术理论]
created: 2026-05-10
updated: 2026-05-10
---

# Harness框架

> AI Agent 的 Harness（线束/框架）概念。指 Agent 的运行架构设计，包括工具调用、状态管理、上下文处理等核心机制。

## 核心定义

**Agent = Model + Harness**

Harness 是指"所有不属于模型本身的代码、配置以及执行逻辑"。一个裸模型并不能算作 Agent；只有当 Harness 为其提供状态管理、工具调用能力、反馈循环以及可执行约束时，它才真正成为一个 Agent。

## Harness 的六大组件

1. **系统提示词**：定义 Agent 的身份、行为规则和约束条件
2. **工具与技能（含 [[MCP协议|MCP]]）**：Agent 可调用的能力集合及其说明
3. **封装好的基础设施**：文件系统、沙箱、浏览器等运行环境
4. **编排逻辑**：子 Agent 的生成与交接、模型路由策略
5. **Hook / 中间件**：上下文压缩、续写机制、Lint 检查等执行稳定性保障
6. **记忆系统**：跨会话的状态持久化与检索

## 在不同框架中的体现

### Claude Code 的 Harness
[[Claude-Code]] 通过 CLAUDE.md、Settings、Skills 三层构建 Harness：
- CLAUDE.md 定义项目级上下文和行为规则
- Settings 管理工具权限和 Hook 配置
- Skills 封装可复用的工作流

### OpenClaw 的 Harness
[[OpenClaw]] 的 Harness 体现为"灵魂三件套"：
- [[SOULmd配置|SOUL]] — AI 的性格与风格
- [[AGENTSmd配置|AGENTS]] — AI 的工作手册
- IDENTITY.md — AI 的对外身份形象

### Hermes Agent 的 Harness
[[Hermes-Agent]] 的 Harness 核心是分层记忆架构 + Learning Loop：
- 热记忆 / 温记忆 / 冷记忆三层记忆系统
- 自动从任务执行中沉淀 Skill 的学习闭环
- [[Profile系统]] 实现多 Agent 分身

## Harness Engineering 的意义

Harness Engineering 是继 Prompt Engineering 之后的下一个关键范式：
- **Prompt Engineering** 解决"怎么说"
- **Harness Engineering** 解决"怎么系统性地说"
- 目标是从 Vibe Coding 到可工程化、可复现的 AI 工作系统

## 类别

技术理论

## 相关实体

- [[Claude]]
- [[Claude-Code]]
- [[Cursor]]
- [[GitHub]]
- [[Harness]]
- [[Hermes-Agent]]
- [[MCP]]
- [[OpenClaw]]
- [[Telegram]]
- [[小红书]]
- [[飞书]]

## 相关概念

- [[AGENTS配置]]
- [[Agent工程化]]
- [[Agent路由]]
- [[Cron定时任务]]
- [[PPT制作]]
- [[SOUL配置]]
- [[Skill开发]]
- [[Sub-Agent]]
- [[Token优化]]
- [[一人公司]]
- [[上下文工程]]
- [[企业落地]]
- [[多Agent协作]]
- [[数据安全]]
- [[本地部署]]
- [[浏览器自动化]]
- [[爬虫]]
- [[知识库构建]]
- [[记忆系统]]

## 相关文章

- [[oc-Harness-到底是什么看看-OpenClawHermesClaude-Code-的演绎吧]]
- [[oc-一文讲透-OpenClaw-里到底该用-Multi-Agent还是主-Agent-Sub-Agent]]
- [[oc-从OpenClaw到Hermes-Agent一个AI-Agent使用者的进化手记]]
- [[oc-当OpenClaw遇见Hermes一个关于AI-Agent进化的深度思考]]
- [[oc-我的龙虾能抓任何网页了]]
- [[oc-智能体搭建-如何用OpenClaw搭建你的“一人公司”附完整配置模板]]
- [[oc-深度解析三大-Agent-上下文工程Claude-CodeOpenClawHermes-的设计哲学]]
