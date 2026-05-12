# Multica — 开源 Managed Agents 平台

> GitHub: https://github.com/multica-ai/multica
> Stars: 10.7k+ (2026年4月 GitHub TypeScript Trending #1)
> 协议: 开源 | 技术栈: Next.js 16 + Go + PostgreSQL 17 (pgvector)
> 支持 Agent: Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI

## 一句话简介

**把 AI 编程 Agent 变成真正的团队成员** — 像在 Jira/Linear 里分配任务给同事一样，把 Issue 分配给 AI Agent。

## 核心特点

- **Agent 即队友**: 有个人档案、出现在看板上、发表评论、创建 Issue、主动报告阻塞问题
- **自主执行**: 完整的任务生命周期管理（排队→认领→执行→完成/失败），WebSocket 实时进度推送
- **技能复用 (Skills)**: 每次解决问题的方案变成可复用的技能，团队整体能力持续增长
- **统一运行时**: 本地 Daemon + Cloud Runtime，自动检测可用 CLI，实时监控
- **多工作区**: 工作区级别隔离，每个工作区独立的 Agent、Issue、配置

## 名字由来

Multica = **Mul**tiplexed **I**nformation and **C**omputing **A**gent。致敬 Multics 操作系统——把"时间共享"理念带回 AI 时代，让人类和 Agent 共享算力，小团队也能有大团队的产出。

## 快速安装

```bash
# macOS / Linux (Homebrew)
brew install multica-ai/tap/multica

# 或一键脚本
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash

# 配置 + 登录 + 启动 Daemon（一条命令搞定）
multica setup
```

自托管 Docker 部署：
```bash
git clone https://github.com/multica-ai/multica.git
cd multica && cp .env.example .env
docker compose -f docker-compose.selfhost.yml up -d
```

## 架构

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Next.js    │────>│  Go Backend  │────>│   PostgreSQL     │
│   Frontend   │<────│  (Chi + WS)  │<────│   (pgvector)     │
└──────────────┘     └──────┬───────┘     └──────────────────┘
                            │
                     ┌──────┴───────┐
                     │ Agent Daemon │  本地运行，自动检测 CLI
                     └──────────────┘
```

## CLI 命令

| 命令 | 说明 |
|------|------|
| `multica setup` | 一键配置 + 登录 + 启动 Daemon |
| `multica login` | 认证登录（打开浏览器） |
| `multica daemon start` | 启动本地 Agent 运行时 |
| `multica daemon status` | 查看 Daemon 状态 |
| `multica issue list` | 列出工作区 Issue |
| `multica issue create` | 创建新 Issue |

## vs Paperclip

| 维度 | Multica | Paperclip |
|------|---------|-----------|
| 定位 | 团队 AI Agent 协作平台 | 单人 AI Agent 公司模拟器 |
| 用户模型 | 多用户团队+权限 | 单人操作 |
| 部署 | Cloud 优先 | Local 优先 |
| 管理深度 | 轻量（Issue/Project/Label） | 重量（组织架构/审批/预算） |

## 适用场景

- 2-10 人的 AI 原生小团队
- 需要把多个 AI Agent（Claude Code/Codex 等）统一管理
- 希望技能/经验在团队中沉淀复用
- 需要 Issue 级别的任务追踪和协作
