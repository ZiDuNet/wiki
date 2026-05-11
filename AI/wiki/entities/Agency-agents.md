---
tags: [entity, 开源项目, Agent, GitHub]
sources:
  - Agent/Agency-agents：别再只会调提示词了，这个开源项目直接给你 144 个 AI 员工.md
created: 2026-05-11
updated: 2026-05-11
---

# Agency-agents

GitHub 开源项目（msitarzewski/agency-agents），提供 144 个专职 AI Agent 角色文件，覆盖 12 个 division。

## 核心特点

- 不是 Agent 框架，而是"AI 员工说明书仓库"
- 每个 Agent 是一个 Markdown 文件，定义身份、任务、边界、交付标准、执行流程
- 角色颗粒度细：Frontend Developer、Backend Architect、Security Engineer、Code Reviewer 等
- MIT License，支持多工具集成

## 12 个 Division

Engineering、Design、Marketing、Product、Strategy、Sales、Support、Finance、Testing、Academic、Game Development、Specialized

## 支持的工具

[[Claude-Code]]、[[Claude]]、GitHub Copilot、Gemini CLI、[[Cursor]]、Aider、Windsurf、Kimi Code、[[OpenClaw]]

## 安装

```bash
./scripts/install.sh --tool claude-code
# 或指定工具
./scripts/install.sh --tool cursor
./scripts/install.sh --tool openclaw
```

## 相关概念

- [[Multi-Agent]] — 不同岗位视角参与同一问题
- [[Agent架构]] — Agent 角色定义方法论
- [[Skills技能系统]] — Agent 角色文件即 Skill
