---
type: entity
name: Superpowers
created: 2026-05-29
updated: 2026-05-29
mentions: 1
---

# Superpowers

**类型:** 实体（GitHub 开源项目）
**GitHub Stars:** 159K
**作者:** Jesse Vincent
**提及文章数:** 1

## 简介

Superpowers 是一套**AI 编程代理技能系统**，GitHub 上 159K 颗星。它不是插件工具包，而是教 AI 编程代理"怎么干活"的方法论——从接到任务到交付代码，定义了每一步该干什么、怎么干、干到什么程度算完。

## 14个核心技能

| 技能 | 用途 |
|------|------|
| brainstorming | 接需求先头脑风暴，不急着动手 |
| writing-plans | 写计划，计划通过后再执行 |
| subagent-driven-development | 拆子任务，多子 Agent 并行 |
| test-driven-development | 先写测试再写代码 |
| requesting-code-review | 代码写完主动请求 Review |
| receiving-code-review | 收到 Review 逐条处理 |
| systematic-debugging | 遇到 Bug 系统化排查 |
| verification-before-completion | 完工前逐项验证 |
| using-git-worktrees | 多任务并行互不干扰 |
| writing-skills | 自己写 Skill 扩展能力 |
| finishing-a-development-branch | 收尾规范化 |
| dispatching-parallel-agents | 并行派发子 Agent |
| using-superpowers | 使用指南 |
| executing-plans | 按计划执行不跑偏 |

## 支持平台

**原版官方：**
- Claude Code
- Codex CLI / Codex App
- Gemini CLI
- OpenCode
- Cursor
- GitHub Copilot CLI
- Factory Droid

**中文增强版 superpowers-zh：**
- 扩展支持 17 款工具，包括 Hermes Agent 和 OpenClaw
- 完整汉化 + 新增 4 个中国特色技能

## 安装方式

**原版（Claude Code）：**
```bash
/plugin install superpowers@claude-plugins-official
```

**中文增强版（多工具）：**
```bash
npx superpowers-zh
```

**Hermes Agent：**
```bash
npx superpowers-zh --tool hermes
```

**OpenClaw：**
```bash
npx superpowers-zh
```

## 核心价值

- 从"你问它答"的被动工具变成有方法、有节奏、有质量意识的协作者
- AI 编程代理 + 好方法论可以替代没有方法论的程序员
- 不是让 AI 更聪明，而是让它知道怎么干活

## 相关概念

- [[AI编程方法论]]
- [[Skill系统]]
- [[TDD]]
- [[代码审查]]
- [[Multi-Agent]]

## 相关实体

- [[Claude-Code]]
- [[Hermes-Agent]]
- [[OpenClaw]]
- [[Codex]]

## 来源文章

- [[GitHub-159K-Superpowers-AI编程方法论]]