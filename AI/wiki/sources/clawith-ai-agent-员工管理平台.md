---
title: "Clawith：把 AI Agent 当员工管理的开源平台"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: [Clawith：把 AI Agent 当员工管理的开源平台.md]
tags: [AI-Agent, Agent平台, 开源, 多Agent协作, 自主Agent]
---

# Clawith：把 AI Agent 当员工管理的开源平台

## 摘要

Clawith 是一个将 AI Agent 打造成"持续在线数字员工"的开源管理平台（Apache 2.0）。与 Dify/Coze 等无状态应用不同，Clawith 的 Agent 拥有独立身份（soul.md）、长期记忆（memory.md）、文件系统工作空间，能通过触发器（Trigger）自主感知和行动，并支持多 Agent 间互相发消息、委派任务。定位为"AI 数字员工的操作系统 + 组织管理平台"。

## 核心特性

- **持续在线**：Agent 不是"一次性聊天"，而是像雇员一样 7×24 小时工作
- **身份与记忆**：soul.md 定义人格，memory.md 跨对话持久化
- **文件系统即状态**：Agent 的一切都是 Markdown 文件，可 git 化管理
- **Trigger Daemon**：每 15 秒 tick 一次，支持 cron/once/interval/poll/on_message/webhook 六种触发器
- **Focus Items**：触发器必须绑定"关注项"，形成"关注什么→何时检查→检查完标记完成"闭环
- **Autonomy Policy（L1/L2/L3）**：分级权限控制，不是简单 allow/deny
- **渐进披露 Prompt**：技能只注入索引，Agent 按需自己加载完整内容
- **不依赖 LangChain/LangGraph**：自研简单封装，依赖少但复杂编排需自己造轮子

## 架构

- **前端**：React 19 + Vite + TypeScript + Zustand + TanStack Query（端口 3008）
- **后端**：FastAPI 单体 + Uvicorn + WebSocket + JWT/RBAC（端口 8008）
- **存储**：PostgreSQL（数据持久）+ Redis（缓存/队列）+ Docker Engine（代码执行沙箱）
- **Agent 工作空间**：`./backend/agent_data/<id>/` 下含 soul.md、memory/memory.md、skills/、relationships.md

## 部署

- **推荐**：Docker Compose，一行启动
- **裸机**：Python 3.12+、Node.js 20+、PostgreSQL 15+、2核4G30G
- **国内加速**：docker.1panel.live / hub.rat.dev 镜像源，pip 指向清华源

## 与同类平台对比

| 平台 | 定位 | Agent 生命周期 | 自主性 | 多 Agent 协作 |
| --- | --- | --- | --- | --- |
| **Clawith** | AI 数字员工操作系统 | 持久存在 | ⭐最强 | Agent 间直接通信 |
| Multica | AI 编码团队 Jira | 任务级 | 中 | 看板间接协作 |
| Dify | LLM 应用开发平台 | 无状态 | 弱 | 不支持 |
| CrewAI | 多 Agent 编排框架 | 临时组队 | 中 | 原生支持 |
| Coze | Bot 构建平台 | 持久但无自主 | 弱 | 不支持 |

## 关键注意点

- **Token 消耗较高**：心跳/触发器定期唤醒，建议调大间隔 + 配 `max_tokens_per_day` 配额
- **单体瓶颈**：Trigger Daemon 是 asyncio task，百个以上 Agent 后 15 秒循环可能跑不完
- **安全**：生产环境需限制 docker.sock 访问、改 SECRET_KEY、开 HTTPS、定期备份 `/data/agents/`

## 值得关注的点

1. **Aware 系统（自适应触发）** 是最大差异化——Agent 自己管理日程，不被动等消息
2. **Focus-Trigger 绑定** 设计精巧，让 Agent 的"注意力"有结构化表达
3. **文件系统即状态** 对调试非常友好
4. 项目仍在早期（161 Issues、57 PRs），API 可能快速变化

## 实体

- [[Clawith]]
- [[Trigger-Daemon]]
- [[Focus-Items]]
- [[Autonomy-Policy]]
- [[OpenClaw]]
- [[Multica]]
- [[Dify]]
- [[CrewAI]]
- [[Coze]]

## 概念

- [[AI数字员工]]
- [[数字员工操作系统]]
- [[AI-Agent]]
- [[多Agent协作]]
- [[记忆系统]]
- [[渐进式披露]]

## 来源

> [[Clawith：把 AI Agent 当员工管理的开源平台]]
