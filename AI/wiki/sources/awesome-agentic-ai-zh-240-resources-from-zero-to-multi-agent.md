---
title: awesome-agentic-ai-zh：240+ 资源，从零到构建多 Agent 系统的完整学习地图
type: source-summary
tags: [Agent, 学习路线图, GitHub, 开源项目]
sources: [awesome-agentic-ai-zh-240-resources-from-zero-to-multi-agent.md]
created: 2026-05-29
updated: 2026-05-29
---

# awesome-agentic-ai-zh：240+ 资源完整学习地图

> 来源: 网线那头有只猫 | 时间: 2026-05-29

## 项目概述

**awesome-agentic-ai-zh** 是 GitHub 上的开源学习路线图项目，目前 **1,743 Stars**，MIT 协议，由开发者 WenyuChiou 主导维护。

### 三大核心

| 核心 | 内容 | 规模 |
|---|---|---|
| **学习路线图** | 8 个阶段，从 Python 基础到多 Agent 系统 | 8 stages、2 tracks |
| **资源整理** | 240+ 精选项目，每个附星数、适合谁、教什么 | 240+ projects |
| **动手练习** | 每阶段 1-5 个基础练习，70-150 行代码起步 | 23 个练习 |

**三语完整维护**——繁体中文（主版）、简体中文、英文，非机翻。

---

## 两套学习路径 ⭐

### Track A — CLI Power User（8-10 周）

**适合**：不想自己写 Agent，但想用现成工具提效的人。

**路线**：Stage 0-2（基础）→ A1（选一个 CLI Agent）→ A2（建立工作流）→ A3（接入生产环境）

**核心内容**：7 个主流 CLI Agent 对比（Claude Code、Codex、OpenCode、Gemini CLI 等）、CLAUDE.md 配置、slash command、MCP 接入 CI 自动化。

**目标**：把 CLI Agent 用到极致，成为效率高手。

### Track B — Agent Builder（16-22 周）

**适合**：想从零打造自己 Agent 的人。

**路线**：Stage 0-2（基础）→ 3（Tool Use + ReAct）→ 4（框架学习）→ 5（Claude Code 生态）→ 6（RAG + Memory）→ 7（Multi-Agent）→ 8（Agent Interfaces）

**核心内容**：function calling、LangGraph/AutoGen/CrewAI 框架、MCP/Skills/Plugins 生态、向量数据库、多 Agent 编排、eval/observability。

**目标**：从 LLM 使用者进化为 Agent 系统构建者。

---

## 8 个阶段一览

| Stage | 主题 | 预估时间 |
|---|---|---|
| 0 | 基础准备（Python/Git/API） | 1-2 周 |
| 1 | LLM 基础（Token/API/各家对比） | 1 周 |
| 2 | Prompt 设计（系统 prompt/few-shot/CoT） | 1-2 周 |
| 3 | 工具使用与第一个 Agent（Function Calling/ReAct） | 2-3 周 |
| 4 | Agent 框架（LangGraph/AutoGen/CrewAI） | 2-3 周 |
| 5 | Claude Code 生态（MCP/Skills/Plugins）⭐ | 3-4 周 |
| 6 | 上下文管理（RAG/Memory/向量数据库） | 2 周 |
| 7 | 多 Agent 与生产化（编排/Eval/Observability） | 2-4 周 |
| 8 | Agent Interfaces（Computer Use/Browser/Sandbox） | 2-3 周 |

---

## 三层概念进化

实用的认知框架：

1. **Prompt Engineering**（Stage 2）→ 单一 prompt 怎么写
2. **Context Engineering**（Stage 3+）→ 动态组合 system prompt + memory + 检索结果 + tool schema
3. **Harness Engineering**（Stage 7）→ agent loop / eval / observability / deploy 完整生产系统

---

## 五条延伸路线

| 角色 | 内容 |
|---|---|
| 🔬 研究员 | 文献整理、paper 写作、multi-agent review |
| 💻 开发者 | Cursor、Aider、CLI delegation、code review |
| 🎓 教师 | 备课、投影片、学生 feedback、伦理 |
| 📊 知识工作者 | 邮件、会议纪要、报告自动化 |
| 👥 日常使用者 | 写信、学习、隐私场景、CLI 入门 |

---

## 实战亮点

- **7 步打造第一个 AI Agent**——Paper Summary Bot，约 350 行真实代码，同一项目贯穿所有阶段
- **每个练习都有正确用法提醒**——不要直接抄 starter.py 答案，要自己重写

---

## 相关实体

- [[WenyuChiou]] — 项目维护者
- [[Claude-Code]] — Track A 重点工具
- [[LangGraph]] — Stage 4 框架
- [[AutoGen]] — Stage 4 框架
- [[CrewAI]] — Stage 4 框架

## 相关概念

- [[Agent学习路线图]] — 本项目核心产出
- [[Context-Engineering]] — 三层概念第二层
- [[Harness-Engineering]] — 三层概念第三层
- [[Agent框架]] — Stage 4 内容

---

## 资源链接

- **GitHub**: https://github.com/WenyuChiou/awesome-agentic-ai-zh
- **在线文档**: https://wenyuchiou.github.io/awesome-agentic-ai-zh/
- **协议**: MIT（完全免费）