---
title: "装了Superpowers还是不会用？这套完整工作流，让你的AI从工具变成搭档"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: ["装了Superpowers还是不会用？这套完整工作流，让你的AI从_工具_变成_搭档_.md"]
tags: [Superpowers, AI Coding, Skills, 开发流程, TDD]
---

# 装了Superpowers还是不会用？这套完整工作流，让你的AI从"工具"变成"搭档"

## Summary

Superpowers 是一套 14 个 Skill 串联的 AI 开发流水线，从需求澄清到代码合并全覆盖。90% 的人只触发其中一两个，问题出在不知道它们怎么串成完整开发流程。本文完整讲解：从 brainstorming（需求澄清）→ writing-plans（任务拆解）→ git-worktrees（隔离开发）→ subagent-driven-development（代理执行）→ TDD（测试驱动）→ code-review（双重审查）→ verification（验证收尾）的完整 7 步流程。

## Key Claims

1. **14 个 Skill 是流水线，不是独立工具** — 每个 Skill 的输出是下一个 Skill 的输入
2. **3 条铁律覆盖 80% 场景**：没设计不写代码、没测试不写代码、没验证不说完成
3. **Sub-Agent 不继承历史** — 每个任务派新代理，保证干净上下文
4. **TDD 比普通 TDD 更严格** — AI 最容易"先写代码再补测试"，铁律是限制 AI 偷懒
5. **receiving-code-review 鼓励反驳** — 技术正确性 > 社交舒适度

## Entities Mentioned

- [[Superpowers]] — 14 个 Skill 组成的开发流水线
- [[Claude-Code]] — 主要使用工具
- [[brainstorming]] — 需求澄清 Skill
- [[writing-plans]] — 任务规划 Skill
- [[TDD]] — 测试驱动开发

## Concepts

- [[AI开发流水线]] — 从需求到上线的完整流程
- [[14个Skill串联]] — 流水线分工
- [[Sub-Agent]] — 独立代理执行
- [[Git-Worktree]] — 隔离工作空间
- [[代码审查]] — 双重审查机制
- [[TDD]] — 测试驱动开发铁律
- [[verification]] — 完成前验证

## Notable Quotes

> "每个 Skill 的输出是下一个 Skill 的输入。你不需要记住 14 个 Skill，只需要记住这条流水线。"

> "verification-before-completion 的'新鲜证据'要求：上一次运行的测试结果不算，必须是当前消息中运行的。"

## Limitations / Bias

- 一次性脚本不适合（流程太重）
- 探索性原型不适合（需求还不清楚）
- 紧急 hotfix 不适合（先止血再补流程）
- 小项目可能流程开销大于收益

## Related Articles

- [[Superpowers]] — 官网
- [[TDD]] — 测试驱动开发
- [[agent-skills]] — 另一个工程纪律项目
