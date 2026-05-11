---
tags: ["Agent开发", "Harness Engineering", "Skill编排", "Skill设计模式", "GitHub开源项目"]
sources: ["微信公众号/Skills/Superpowers：把软件工程最佳实践封装成AI可执行的技能.md"]
created: 2026-04-21
updated: 2026-05-10
---

# Test-Driven Development**铁律：没有失败的测试，就不能写产品代码。**## 流程### RED 阶段写一个**失败的测试**，验证：- 测试失败原因正确- 测试的是正确的行为### GREEN 阶段写**最小代码**让测试通过，验证：- 所有测试通过- 没有为了通过测试而写的多余代码### REFACTOR 阶段在测试保护下重构清理，然后回到 RED 继续下一个行为。## 技术细节### 测试先行原则如果用户说"先写代码再加测试"：1. 告诉他们这是不允许的2. 如果代码已存在，删除它3. 从测试重新开始**你不能"保留参考"代码，不能"边写测试边调整"。**必须亲眼看到测试失败，才能确认测试的是正确的东西。### 验证失败必须正确RED 阶段不仅要"测试失败"，还要确认：- 失败原因是你期望的- 不是因为测试写错了如果测试错误地通过了，这不是好的 RED。

**Source:** 角角的 AI 思考
**Category:** Skills
**Date ingested:** 2026-05-10
**Type:** article

## Summary

不是AI不会写，是AI不听劝。用户说"帮我加个功能"，AI立刻开写，不问需求、不做设计、不管边界。写完就跑，不写测试、不做检查、不考虑回归。

## Entities Mentioned

- [[Superpowers]] — Jesse Vincent 的软件工程最佳实践 Skills 框架
- [[GitHub]] — 代码托管平台，Skills 主要分发渠道

## Concepts Covered

- [[Skill设计模式]]
- [[Harness-Engineering]]
- [[Skill编排]]
- [[Agent开发]]
- [[GitHub开源项目]]
- [[Prompt-Engineering]]
- [[TDD]]
- [[自评失真]]
