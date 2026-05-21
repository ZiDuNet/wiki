---
title: SpectrAI — 面向开发者与团队的多AI协同工作站
type: source-summary
tags: [SpectrAI, AgentTeams, MCP, 多AI协作, Claude, Codex, Gemini, 开源]
sources: [../微信公众号/AgentTeam/[开源]一款面向开发者与团队的多 AI 协同工作站，一个人指挥一支 AI 团队.md]
created: 2026-05-19
updated: 2026-05-19
---

# SpectrAI — 面向开发者与团队的多AI协同工作站

> 来源：[[一飞开源]] | 时间：2026-05-18

## 一句话摘要

SpectrAI（光谱AI）是一款开源多会话AI编程桌面客户端，支持Claude/Codex/Gemini多Provider并行，内置MCP工具网关、Agent Teams、SharedTaskList、TeamBus消息总线，实现一个人指挥一支AI团队协作。

## 核心内容

### 产品定位

**光谱AI (SpectrAI)** — 面向开发者与团队的多AI协同工作站。
- 开源协议：MIT
- 定位：多AI CLI会话编排与管控平台

### 核心功能

#### 多会话管理
- 同时运行多个AI CLI会话
- 结构化对话视图（AI回答气泡 + 工具调用卡片）
- 多标签页切换（聚焦/网格/仪表盘视图）
- 会话恢复（Claude Code支持--resume续接多轮）
- 图片粘贴Ctrl+V直接发送给AI多模态分析

#### Provider Adapter架构

统一BaseProviderAdapter抽象层，屏蔽各CLI差异：

| Provider | 通信方式 | 特性 |
|---|---|---|
| Claude Code | Agent SDK V2 | 可恢复、自动接受、会话追踪 |
| Codex CLI | JSON-RPC | 自动接受 |
| Gemini CLI | NDJSON流式 | 自动接受 |
| iFlow CLI | ACP协议 | 自动接受 |
| OpenCode | 可配置命令行 | 自动接受 |
| 自定义提供者 | 可配置命令行 | 用户自定义 |

#### Agent编排系统

完整MCP基础设施，支持子Agent管理：
- `spawn_agent`：创建子Agent（oneShot或多轮）
- `send_to_agent`：向持久Agent发送追加指令
- `wait_agent`：等待Agent完成
- `get_agent_output/status/list_agents`：监控状态
- `cancel_agent`：终止Agent
- Supervisor模式：自动注入System Prompt引导任务分解

#### Agent Teams — 去中心化多AI协作

区别于Supervisor单中心调度，Teams采用去中心化并行模式：

| 特性 | 说明 |
|---|---|
| 多Provider混搭 | 每角色独立选择Claude/Codex/Gemini，扬长避短 |
| SharedTaskList | SQLite持久化任务队列，原子WHERE认领，零冲突 |
| TeamBus消息总线 | P2P路由，支持单播和广播 |
| MCP原生工具集 | 5个MCP工具：team_message_role/broadcast/claim_task/complete_task/get_tasks |
| DB持久化 | 6张表（teams/roles/instances/members/tasks/messages） |
| 可视化追踪 | TaskKanban看板 + TeamMessageFlow对话流 |

**团队模板化**：预定义角色分工（需求分析师+架构师+前端+后端+测试），一键启动团队实例。

#### 文件资源管理器
- 文件树实时展示（展开/折叠、双击预览）
- AI改动追踪（FS Watch 300ms debounce）
- 多会话归因（工作目录深度+活动时间）
- Git Worktree隔离（独立分支完成任务）

#### Git分支管理面板
- GIT分支侧边栏（定位/历史/Worktree三视图）
- commit消息面板直显
- Git Worktree隔离任务分支

#### 看板式任务管理
- 可视化看板展示任务流转

## 关键实体

- [[SpectrAI]] — 开源多AI协同工作站
- [[Claude-Code]] — Anthropic AI编程工具
- [[Codex]] — OpenAI AI编程工具
- [[Gemini]] — Google AI编程工具
- [[MCP协议]] — Model Context Protocol
- [[一飞开源]] — 内容发布公众号

## 关联概念

- [[Multi-Agent]] — 多智能体协作
- [[Agent-Teams]] — 多角色AI团队协作模式
- [[SharedTaskList]] — 共享任务队列机制
- [[TeamBus]] — P2P消息路由
- [[MCP协议]] — 模型上下文协议
- [[工作流自动化]] — 看板式任务管理

## 标签

#SpectrAI #AgentTeams #MCP #多AI协作 #Claude #Codex #Gemini #开源
