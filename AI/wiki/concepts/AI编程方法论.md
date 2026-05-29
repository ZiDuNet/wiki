---
type: concept
name: AI编程方法论
created: 2026-05-29
updated: 2026-05-29
---

# AI编程方法论

**类型:** 概念

## 简介

AI编程方法论是指让AI编程代理"知道怎么干活"的一套系统性工作流程和规范。核心洞察是：AI编程代理真正缺的不是能力（模型能力），而是"怎么干"的指令（方法论）。

## 核心要点

### 问题背景

- 很多 AI 编程代理像"有热情没章法的新人"：接到需求就写代码，写到一半发现问题改三轮
- Token 烧了，上下文乱了，效率低下
- 试过多个模型、调过参数，发现模型本身没变——真正决定能不能干活的是方法论

### 方法论本质

类比名校程序员：学历好、智商高，但不告诉项目规范、代码标准、工作流程，一样干不好。

**方法论解决的三个问题：**
1. **干什么**：每一步该做什么
2. **怎么干**：用什么方式执行
3. **干到什么程度**：验收标准是什么

### 实践框架（Superpowers 14技能）

| 阶段 | 技能 |
|------|------|
| 任务接收 | brainstorming（头脑风暴）、writing-plans（写计划） |
| 任务执行 | subagent-driven-development、test-driven-development、executing-plans |
| 质量保障 | requesting-code-review、receiving-code-review、verification-before-completion |
| 问题处理 | systematic-debugging |
| 协作效率 | dispatching-parallel-agents、using-git-worktrees |
| 收尾规范 | finishing-a-development-branch |

## 关键案例对比

| 场景 | 无方法论 | 有方法论 |
|------|----------|----------|
| 接任务 | 直接写代码 | 先问问题，给方案让用户选 |
| 执行 | 写到一半发现问题改三轮 | 先写测试再实现，自动Review |
| 结果 | Token烧一万，上下文乱 | 一次过 |

## 核心观点

- AI + 好方法论可以替代**没有方法论的程序员**
- 不是让 AI 更聪明，而是让它知道怎么干活
- 从被动工具变成有方法、有节奏、有质量意识的协作者

## 相关实体

- [[Superpowers]]
- [[Claude-Code]]
- [[Hermes-Agent]]
- [[OpenClaw]]

## 相关概念

- [[Skill系统]]
- [[TDD]]
- [[代码审查]]
- [[Multi-Agent]]

## 来源文章

- [[GitHub-159K-Superpowers-AI编程方法论]]