---
tags: [Deep-Research-Agent, Multi-Agent, MCP, Hermes, OpenClaw]
sources: [如何基于 Openclaw、Hermes、Opencode、pi-agent 来搭建自己的 Deep Research Agent.md]
created: 2026-05-26
updated: 2026-05-26
---

# 如何基于 Openclaw、Hermes、Opencode、pi-agent 搭建 Deep Research Agent

**来源：** OpenClaw/即心的AI笔记
**摄入日期：** 2026-05-26
**类型：** 技术指南

## 摘要

文章分析 OpenClaw、Hermes、Opencode、pi-agent 四个框架搭建 Deep Research Agent 的可行性与具体路径。推荐以 Hermes 或 OpenClaw 作为主运行时 + OpenCode 处理 coding-heavy 子任务 + MCP 统一工具层。六步法实现：基础部署 → Multi-Agent 架构改造 → MCP 工具集成 → 迭代反思循环 → 输出持久化 → 优化生产化。

## 核心观点

### 框架对比（Deep Research 适配性）

| 框架 | 特点 | 适配建议 |
|------|------|----------|
| [[OpenClaw]] | 最成熟 always-on 运行时，持久 workspace/memory，heartbeat 调度 | 长期研究助手，能自主跑几天跟踪主题 |
| [[Pi-agent]] | 极简核心（4 工具），高度可扩展，通过 MCP 接入外部工具 | 底层 harness，自定义 research skills |
| [[Hermes Agent]] | **最推荐**，自带 closed learning loop，持久记忆，用户建模 | 越用越懂研究偏好 |
| [[OpenCode]] | 偏 coding，支持 Primary Agents + Subagents，多模型混合 | 数据分析、图表生成子任务 |

### 六步搭建法

1. **基础部署**：VPS/Mac Mini 持久运行，多模型配置，启用持久内存
2. **Multi-Agent 架构**：Planner → Researcher → Critic → Synthesizer → Coder 五角色
3. **MCP 工具集成**：Tavily/Perplexity 搜索、学术 API、多模态、浏览器自动化
4. **迭代反思循环**：Self-Reflection + 状态机 + Grounding（来源+引用追踪）
5. **输出持久化**：结构化报告 → workspace 目录 → 通知归档 → 新 Skill 入库
6. **优化生产化**：Observability + Cost Control + Eval + Scaling

## 提及实体

- [[OpenClaw]] — 最成熟的 always-on Agent 运行时
- [[Hermes Agent]] — 自带 learning loop 的持久化 Agent（最推荐）
- [[OpenCode]] — 偏 coding 的 Agent 框架，支持多 Agent
- [[Pi-agent]] — 极简核心 Agent，仅 4 基础工具

## 涉及概念

- [[Deep-Research-Agent]] — 深度研究智能体，能长期跟踪主题、迭代研究、生成报告
- [[Multi-Agent架构]] — Planner/Researcher/Critic/Synthesizer/Coder 五角色分工
- [[Learning-Loop]] — Hermes 的闭环学习系统，从经验创建/改进 Skills
- [[MCP工具层]] — 统一的 Agent 工具接口协议
- [[迭代反思循环]] — Self-Reflection + 状态机 + Grounding 的研究方法论

## 实践 Tips

- 从简单开始：先做单主题研究 Skill，再扩展 multi-step
- Hermes 可直接 import OpenClaw 配置，降低切换成本
- 上下文管理：用总结 + RAG 避免爆炸
- Hallucination 控制：multi-source verification + Critic Agent