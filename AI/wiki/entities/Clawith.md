---
type: entity
name: Clawith
created: 2026-05-12
updated: 2026-05-12
mentions: 1
---

# Clawith

**类型:** 实体
**来源:** [[clawith-ai-agent-员工管理平台]]

## 简介

Clawith 是将 AI Agent 打造成"持续在线数字员工"的开源管理平台（Apache 2.0）。GitHub: `https://github.com/dataelement/Clawith`

## 核心定位

**"AI 数字员工的操作系统"** ——让 Agent 拥有独立身份、长期记忆、独立工作空间，通过触发器自主感知和行动，并支持多 Agent 间互相发消息和委派任务。

## 关键设计

- **Trigger Daemon**：asyncio 后台任务，每 15 秒 tick 一次，支持 6 种触发器
- **Focus Items**：触发器必须绑定，形成"关注→检查→完成"闭环
- **Autonomy Policy（L1/L2/L3）**：分级权限控制
- **渐进披露 Prompt**：技能只注入索引，Agent 按需加载
- **不依赖 LangChain/LangGraph**：自研简单封装

## 架构

- Frontend: React 19 + Vite + TypeScript（端口 3008）
- Backend: FastAPI 单体（端口 8008）
- PostgreSQL + Redis + Docker Engine

## 相关实体

[[OpenClaw]], [[Multica]], [[Dify]], [[CrewAI]], [[Coze]]

## 相关概念

[[AI数字员工]], [[数字员工操作系统]], [[AI-Agent]], [[多Agent协作]], [[记忆系统]]
