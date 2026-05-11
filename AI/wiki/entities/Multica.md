---
type: entity
name: Multica
created: 2026-05-10
updated: 2026-05-11
---

# Multica

**类型:** 实体 (产品/平台)
**提及文章数:** 2

## 简介

Multica是Managed Agents平台，用看板和Issue系统管理Claude Code等编码Agent作为团队协作者。Agent可以像队友一样被分配任务、更新状态、发表评论、报告阻塞。不是CLI替代品，而是协作和管理层；适合已使用多个编码Agent的团队。

## 核心特性

- Issues看板管理Agent任务
- 完整任务生命周期：enqueue、claim、start、complete/fail
- WebSocket实时推送进度
- 统一运行时管理（本地机器和云端实例）
- daemon自动检测本机PATH中可用Agent CLI
- Skills系统沉淀团队可复用能力

## 支持的编码Agent

- Claude Code
- Codex
- OpenCode
- Hermes
- Gemini
- Cursor Agent
- Kimi
- Kiro CLI
- OpenClaw

## Skills系统

Skills系统把经验沉淀为团队可复用能力，如：
- 部署
- PR Review
- 补测试
- 代码审查

## 安装方式

```bash
# macOS/Linux 一键安装
brew install multica-ai/tap/multica
# 配置登录认证 + 启动守护进程
multica setup
```

## 相关概念

- [[Managed Agents]], [[Agent架构]], [[Skills技能系统]], [[团队协作]]

## 相关文章

- [[Multica编码Agent团队管理平台]]
- [[Hermes-Agent进化了，开源Multica实现多agent协作]]