---
tags: [Superpowers, AI编程, Claude Code, 工程纪律, TDD, 开源]
source: "AI不白学"
created: 2026-05-15
updated: 2026-05-15
category: Superpowers
---

# SuperPowers：规范化开发最佳实践

> 来源: [AI不白学](https://mp.weixin.qq.com/s?__biz=MzkyMDY0MjI0MQ==&mid=2247484373&idx=1&sn=53caa75ac61272f2b001c40302ff3fca&chksm=c09f07c7dc9997d33b91f3a2b817e4ea5a6351d4dde75b1d07766e85c719827d22396ee4530b&mpshare=1&scene=1&srcid=05153E4xEVjpg45nI3CaqRxc&sharer_shareinfo=96e52e0ebdce145572e889348f1ca2e4&sharer_shareinfo_first=96e52e0ebdce145572e889348f1ca2e4) | 2026-05-15

## 摘要

Superpowers 是由 Jesse Vincent 打造的开源 AI 编程工作流框架（177k+ Stars），核心理念是"Process over Prompt（流程大于提示词）"，通过将软件工程最佳实践（TDD、Spec-Driven、Code Review）封装成 AI 可自动执行的 Skills，让大模型从"代码生成器"变成"懂工程的 Junior Engineer"。

## 核心问题

VibeCoding 的问题：
- 需求理解偏差（不澄清细节直接写代码）
- 缺乏标准化工程流程
- 容易跳过需求分析、架构设计、测试验证等关键环节
- 长会话漂移，复杂项目容易失控
- 团队协作时"调教 AI"方式不统一

## 核心价值

把软件工程最佳实践全部封装成 AI 可自动执行的 Skills：
- **TDD（测试驱动开发）**：红-绿-重构循环，先写失败的测试再写实现
- **Spec-Driven（规格驱动开发）**：先敲定规格说明书，作为项目全流程唯一真理基准
- **Code Review**：完成前必须发起代码审查

## 七阶段工作流

| 阶段 | Skill | 作用 |
|------|-------|------|
| 头脑风暴 | brainstorming | 苏格拉底式问答，理清需求 |
| 方案设计 | designing | 拆解设计方案，逐块确认 |
| 编写计划 | writing-plans | 生成详细实现计划文档 |
| 执行开发 | executing-plans | 按计划用子 Agent 执行 |
| TDD 测试 | test-driven-development | 强制先写失败测试再写实现 |
| 代码审查 | requesting-code-review | 完成后发起代码审查 |
| 系统化调试 | systematic-debugging | 4阶段调试法 |

## 安装

```bash
# 全局安装（所有项目生效）
/plugin install superpowers@claude-plugins-official --global

# 项目级安装（仅当前项目生效）
/plugin install superpowers@claude-plugins-official
```

## 关键观点

- **Process over Prompt**：流程大于提示词，给 AI 套上软件工程的"纪律与护栏"
- **强制遵循工程方法论**：让 AI 像资深工程师一样先思考、再规划、后编码、必验证
- **适配主流 AI 编码工具**：Claude Code、Cursor、Codex、OpenCode、Gemini CLI
