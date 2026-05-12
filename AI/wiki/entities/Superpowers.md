---
tags: [entity, 开源项目, Skills, 纪律]
sources:
  - Harness/AI编程王炸组合：顶级三剑客 OpenSpec 定方向，Superpowers定纪律，Harness定协同.md
  - Superpowers/装了Superpowers还是不会用？这套完整工作流，让你的AI从_工具_变成_搭档_.md
created: 2026-05-11
updated: 2026-05-12
---

# Superpowers

AI 编程纪律 Skill，三剑客之一（[[OpenSpec]] + Superpowers + [[Harness]]）。

## 角色

- **定纪律**：设定 AI 编程行为的边界和约束
- 与 OpenSpec（定方向）和 Harness（定协同）组合

## 14 个 Skill 流水线

| 阶段 | Skill | 铁律 |
| --- | --- | --- |
| 入口 | using-superpowers | 1%可能就触发 |
| 设计 | brainstorming | 没设计不写代码 |
| 规划 | writing-plans | 计划写给零上下文的人看 |
| 隔离 | using-git-worktrees | 不在主分支上开发 |
| 执行 | subagent-driven-development | 代理不继承历史 |
| 测试 | test-driven-development | 没有失败测试不写代码 |
| 调试 | systematic-debugging | 没找到根因不提方案 |
| 审查 | requesting-code-review | 完成任务必须审查 |
| 收尾 | finishing-a-development-branch | 测试不过不合并 |

## 相关概念

- [[Skills技能系统]] — 纪律约束 Skill
- [[Agent工程化]] — 规范+纪律+协同
- [[TDD]] — 测试驱动开发
- [[AI开发流水线]] — 14 个 Skill 串联
