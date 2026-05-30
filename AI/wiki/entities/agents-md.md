---
tags: [AI工程化, AGENTS.md, Claude Code, 多工具协作]
sources: [agents-md-ai辅助开发工程化骨架.md]
created: 2026-05-30
updated: 2026-05-30
---

# AGENTS.md — AI 辅助开发的跨工具工程化配置

AI 辅助开发项目的核心工程化配置文件，作为跨工具的唯一真实来源，约束 Claude Code、Codex、Cursor 等工具的行为。

## 核心作用

- **跨工具统一规则** — 同一份规则在 Claude Code、Codex、Cursor 中都能被识别复用
- **可执行命令精确字符串** — Agent 直接复用，无歧义
- **模块化拆分** — 详细规则拆分到 `rules/` 小文件，`@path/to/file` 引用（支持 5 层递归嵌套）

## 标准内容模块

1. **项目概述** — 技术栈、数据库、关键架构
2. **构建和测试命令** — 可执行精确命令
3. **代码风格** — 注释语言、标识符规范等
4. **测试要求** — TDD 流程、覆盖率要求
5. **安全注意事项** — 凭证管理、注入防御等
6. **PR 规则** — 提交规范、审查要求

## 工具链配置对应

| 工具 | 配置文件 | 薄壳层 |
|------|---------|-------|
| Claude Code | `.claude/agents/`, `CLAUDE.md` | CLAUDE.md |
| Codex | `.codex/agents/`, `.codex/config.toml` | — |
| Cursor | `.cursor/rules/` | `.mdc` YAML frontmatter |
| 共用 | `AGENTS.md`, `rules/` | 唯一真实来源 |

## 涉及概念

- [[AI辅助开发工程化]]
- [[多工具协作]]
- [[Skill工程化]]
- [[RBAC权限工程]]
- [[提示注入防御]]