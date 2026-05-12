---
title: "一文讲清：Prompt 和 Skill 的区别是什么？"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: [一文讲清：Prompt 和 Skill 的区别是什么？.md]
tags: [Prompt, Skill, AI-Agent, 上下文工程, 岗位说明书]
---

# 一文讲清：Prompt 和 Skill 的区别是什么？

## 摘要

Prompt 是"临时给 AI 派活"，Skill 是"给 AI 定好一个岗位"。Skill 本质是一个文件夹（SKILL.md + 模板/参考文档/脚本），是在特定时候注入 AI 上下文的结构化指令。选择框架：低复杂+高确定 → Prompt；高复杂+高确定 → Skill；高复杂+不确定 → Agent。

## Prompt vs Skill 的本质区别

| | Prompt | Skill |
| --- | --- | --- |
| **本质** | 临时派活 | 岗位说明书 |
| **格式** | 非结构化 | 结构化（SKILL.md + 支持文件） |
| **稳定性** | 输出波动大 | 输出稳定可重复 |
| **可复用性** | 只在脑子里，他人无法复用 | 可 git 共享，团队可用 |
| **迭代方式** | 每次重新说 | 持续优化沉淀 |

## Skill 是什么

Skill 是一个文件夹，最核心的是 `SKILL.md`，写清楚：这个 Skill 是干嘛的、怎么干、干到什么标准。里面可以有模板、参考文档，甚至直接执行的脚本。

**从技术层面**：Skill 是在特定时候注入 AI 上下文的一段结构化指令。

## Skill 的使用边界

### 什么适合做成 Skill

**你已经明确知道怎么做、且需要反复做的事**。典型案例：公众号写作流程（选选题→调研→写初稿→审稿→配图→发文章），做成 Skill 后输入 `/gzh-write` 即可自动走完全流程，还带自评分机制（5 个维度，不及格自动修改）。

### 判断标准

- **低复杂 + 高确定** → Prompt 就行
- **高复杂 + 高确定** → Skill
- **高复杂 + 不确定（怎么做还不知道）** → Agent

## 四个避坑点

1. **Skill 不是越多越好**：选 3-4 个最好用；装到 8-10 个 Claude 开始犯迷糊，不同 Skill 指令互相冲突
2. **大多数 Skill 是"垃圾"**：RoboRhythms 的文章 "Most Claude Code Skills Are Garbage"——这些 Skill 在重复 Claude 本来就会的事。好的 Skill 解决 AI 真正不会的问题
3. **Skill 管不了需要外部能力的事**：需要调用外部 API、操作 SaaS、访问私人数据源 → 需要 MCP。Skill 管"怎么干"，MCP 管"用什么工具干"
4. **Skill 内容会被截断**：Claude Code 上下文有限，每个 Skill 只保留前 5,000 token，总预算 25,000 token。SKILL.md 建议控制在 500 行以内，详细内容放支持文件按需加载

## 概念澄清

- **SKILL.md** = 岗位说明书
- **MCP** = 工具目录（用什么工具干）
- **CLAUDE.md** = 不管干什么都遵守的规则（不管干什么）
- **Hooks** = 可自动执行的触发动作

## 实体

- [[Skill开发]]
- [[Skills技能系统]]
- [[MCP协议]]

## 概念

- [[Prompt-Engineering]]
- [[上下文工程]]
- [[AI-Agent]]
- [[渐进式披露]]

## 来源

> [[一文讲清：Prompt 和 Skill 的区别是什么？]]
