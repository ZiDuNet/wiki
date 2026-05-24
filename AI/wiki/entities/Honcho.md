---
type: entity
name: Honcho
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# Honcho

**类型:** 实体 (开源项目)
**提及文章数:** 1
**GitHub Stars:** 3,333 (截至 2026-05-08)

## 简介

Plastic Labs 开发的 AI Agent 记忆库，为 AI Agent 提供持久记忆，让 Agent 真正理解并记住每个用户。

**一句话定位**：为 AI Agent 提供持久记忆，让 Agent 真正理解并记住每个用户。

## 核心特点

1. **持续学习** — 用户画像随时间演化，不只是存储对话
2. **自然语言查询** — 用自然语言问关于用户的问题，不用写 SQL
3. **多实体支持** — 任何实体（用户、Agent、群组、想法）都可以拥有记忆
4. **做了3年** — v3.0.6 经过大量打磨

## 核心概念（4个基本单元）

| 单元 | 说明 |
| --- | --- |
| Workspace | 应用容器，一个 App 对应一个 Workspace |
| Peer | 任何实体，可以是用户、Agent、群组、想法 |
| Session | 一次对话上下文 |
| Messages | 对话内容本身 |

## Benchmark 数据

| Benchmark | Honcho 得分 |
| --- | --- |
| LongMem S | 90.4% |
| LoCoMo | 89.9% |
| BEAM 100K | 0.630 |

## 技术架构

- **Deriver 组件**：后台运行，持续处理 session 数据
- **用户表征（Representation）**：本地 vs 全局区分，同一用户在不同 session 中表征可不同
- **"梦境"任务**：离线深度推理

## 部署方式

- **托管服务**：app.honcho.dev，注册送 $100 免费额度
- **自托管**：PostgreSQL + pgvector + FastAPI

## 链接

- 仓库：https://github.com/plastic-labs/honcho
- 文档：https://docs.honcho.dev
- 测评：evals.honcho.dev

## 相关实体

- [[Plastic-Labs]] — Honcho 的开发团队

## 相关概念

- [[记忆系统]] — Agent 的持久化记忆机制
- [[用户画像]] — Agent 对用户的理解和表征
- [[Agent工程原则]] — Agent 工程化方法论

## 相关文章

- [[Honcho-AI-Agent记忆库3年打磨让Agent真正认识用户]]