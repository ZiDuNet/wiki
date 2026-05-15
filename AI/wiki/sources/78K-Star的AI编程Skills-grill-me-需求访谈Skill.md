---
title: 78K Star的AI编程Skills：在开发前，先让grill-me对你做一个"需求访谈"
type: source-summary
tags: [Skills, Matt-Pocock, grill-me, TDD, AI编程, 需求对齐, prompt-engineering, karpathy]
sources: ["微信公众号/Skills/78K Star的AI编程Skills：在开发前，先让grill-me 对你做一个\"需求访谈\".md"]
created: 2026-05-15
updated: 2026-05-15
---

> 📎 来源: [H的AI笔记](https://mp.weixin.qq.com/s?__biz=MzAwMDgxMTAyNg==&mid=2247483930&idx=1&sn=a719cfa3635f9a164982c9b2342c4342) | 时间: 2026-05-15

## 核心摘要

Matt Pocock 的 Skills 仓库（78K Star）提供了一套 AI 编程工作流规范。其核心思路与 Karpathy 相反：不是约束 AI，而是**通过 Skill 让 AI 反向追问人类**，确保需求真正对齐后再动手写代码。

## mattpocock/skills 概览

- **Star**: 78K
- **作者**: Matt Pocock（TypeScript 专家，Total TypeScript 作者）
- **形式**: 纯 Markdown 文件，零依赖，零安装
- **安装**: `npx skills@latest add mattpocock/skills`
- **支持**: Claude Code、Codex、Cursor 等多编码 Agent

### 14 个 Skills 分类

**工程类（10个）**：grill-with-docs、diagnose、tdd、improve-codebase-architecture、triage、to-prd、to-issues、zoom-out、prototype、setup

**效率类（4个）**：grill-me、caveman、handoff、write-a-skill

## 重点 Skill 详解

### grill-me（最火）

**作用**：AI 反向追问用户，直到双方理解一致

**核心理念**：大多数人不知道自己想要什么，直到看到错误答案才知道——《程序员修炼之道》

**对比 Claude Code 内置 plan mode**：
- Claude Code 内置：给选择题（原生 HTML/CSS/JS vs React vs Vue），需用户自己懂才能选
- grill-me：问答题 + 推荐，AI 分析并给建议，普通人只需判断"行"或"不行"

**效果**：同一需求从一句话变成完整 PRD，避免"做到一半才发现忘说了"

### grill-with-docs

**作用**：解决"鸡同鸭讲"问题，统一 AI 与人类的认知

**三件事**：
1. **统一语言**：概念统一写入 `CONTEXT.md`，变量/函数/文件名全部使用统一术语
2. **交叉验证**：AI 主动比对用户说法与代码实现，指出不一致
3. **记录重大决策**：满足"难撤销 + 不看上下文会困惑 + 有方案取舍"三条件时建议创建 ADR

### caveman

**作用**：让 AI 用极简语言回复，只说技术要点

**适用**：信息查询、调试；安全/破坏性操作时自动退出 caveman 模式

## 核心价值

这些 Skill 的理念来自《程序员修炼之道》《领域驱动设计》《极限编程》等经典工程实践，作者将其浓缩为 AI 可执行的格式。

**核心观点**：AI 编程的速度在加快，但软件工程的根基没变。越快的工具，越需要好的工程实践来兜底。

## 相关链接

- GitHub: `mattpocock/skills`
- 对比：《[[Karpathy-CLAUDE-md]]》— 约束 AI 行为；本文 — 让 AI 反向追问人
- 相关：《[[程序员修炼之道]]》— 理念源头
