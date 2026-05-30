---
tags: [AI工程化, AGENTS.md, Claude Code, 多工具协作, Skill]
sources: [微信公众号/Agent/从PRD到AGENTS.md：AI辅助开发项目的工程化骨架搭建指南（中）.md]
created: 2026-05-30
updated: 2026-05-30
---

# AGENTS.md 工程化 — AI 辅助开发的跨工具规则体系

**来源：** 微信公众号/Agent/从PRD到AGENTS.md：AI辅助开发项目的工程化骨架搭建指南（中）.md
**摄入日期：** 2026-05-30
**类型：** 文章
**作者：** AI系统架构

## 摘要

本文深入讲解 AI 辅助开发项目的工程化骨架：AGENTS.md 作为跨工具唯一真实来源、CLAUDE.md 作为工具专属薄壳、Skills 固化 SOP、子代理与 Rules 分层审查、MCP/Hooks/权限门禁的系统化配置。

## 核心观点

### AGENTS.md — 跨工具的唯一真实来源

- 标准 Markdown，无必需字段，包含：项目概述、构建测试命令、代码风格、测试要求、安全注意事项、PR 规则
- 命令写**可执行的精确字符串**，Agent 会逐字复用
- 详细规则拆分到 `rules/` 小文件，用 `@path/to/file` 引用，Claude Code 支持递归 5 层嵌套

### CLAUDE.md — 工具专属薄壳

- 多工具并存时，CLAUDE.md 退化为轻量壳，只加 Claude 特性（Skills 优先级、子代理调度、会话纪律）
- 显式引用根目录 AGENTS.md，避免多份规则长期漂移
- Codex 用 `.codex/config.toml` 控制 sandbox/approvals
- Cursor 用 `.cursor/rules/` 下 `.mdc` 文件，YAML frontmatter 控制激活

### Skills — 跨工具可复用工作流

- SKILL.md 的 YAML frontmatter 只有 `name` 和 `description` 两个必填字段
- 发现机制完全依赖 `description` 关键词匹配，无 triggers/tools 额外字段
- Skill 本质是被触发时替代临场发挥的标准作业程序（SOP）
- 示例工程 Skill：RBAC 权限校验（`skills/rbac-permission-check/`）、Flyway 迁移（`skills/flyway-migration/`）、Redis 缓存模式（`skills/redis-cache-pattern/`）、Vue3 功能模块（`skills/vue3-feature-module/`）

### 子代理与 Rules — 审查约束分层

- Claude Code 子代理放 `.claude/agents/.md`，Codex 多代理角色放 `.codex/agents/.toml`
- 示例：security-reviewer 负责权限注解审计、认证链路审查、数据流审查、越权测试覆盖
- Rules 分层组织（`rules/common/security.md`），让不同语言/模块互不干扰

### MCP/Hooks/权限门禁

- `.mcp.json` 配置 MCP 服务，但每个工具描述都占用上下文预算，只启用当前任务真正需要的
- Claude Code PostToolUse Hooks 可自动触发 `./mvnw spotless:apply` 或 `pnpm lint --fix`
- `.claude/settings.json` 配置 permissions（allow/ask/deny）三层权限体系
- `.claudeignore` 与 `Read(.env)` 规则共同构成双保险防护

## 工具链全景

| 工具 | 配置文件 | 核心机制 |
|------|---------|---------|
| Claude Code | `.claude/agents/`, `.claude/settings.json`, `CLAUDE.md` | Skills 优先级 + 子代理 + Hooks |
| Codex | `.codex/agents/`, `.codex/config.toml` | TOML 配置 sandbox/approvals |
| Cursor | `.cursor/rules/` | `.mdc` YAML frontmatter 激活 |
| 共用 | `AGENTS.md`, `rules/` | 跨工具唯一真实来源 |

## 涉及概念

- [[AI辅助开发工程化]] — 用配置和规则约束 AI 行为，保证输出质量和一致性
- [[多工具协作]] — Claude Code、Codex、Cursor 等工具并存时的规则体系设计
- [[Skill工程化]] — 把 SOP 写成 SKILL.md 替代临场发挥
- [[RBAC权限工程]] — Controller 方法级权限注解 + TDD 测试路径覆盖
- [[数据库迁移工程]] — Flyway SQL 迁移的安全执行规范
- [[提示注入防御]] — 第三方 skills/agents/MCP 引入的安全风险与审查要求

## 提及实体

- [[AGENTS.md]] — 跨工具规则源，项目的核心配置文件
- [[CLAUDE.md]] — Claude Code 专属薄壳配置
- [[Claude Code]] — AI 编程工具，子代理和 Hooks 机制的代表
- [[Codex]] — OpenAI 的 CLI 编程工具
- [[RBAC]] — 基于角色的访问控制，文中示例的安全架构
- [[Flyway]] — 数据库迁移工具