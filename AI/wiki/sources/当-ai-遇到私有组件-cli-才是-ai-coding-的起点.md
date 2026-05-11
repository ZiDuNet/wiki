---
tags: [AI编程, MCP, 企业AI, CLI, Skill]
sources: [AI Coding/当 AI 遇到私有组件，Cli 才是 AI Coding 的起点.md]
created: 2026-05-10
updated: 2026-05-10
---

# 当 AI 遇到私有组件，Cli 才是 AI Coding 的起点

**Source:** 深入浅出AI
**Category:** AI Coding
**Date ingested:** 2026-05-10
**Type:** article

## Summary

深入分析企业 AI Coding 的核心难题——AI 不认识私有组件。以 Ant Design CLI 为例，提出 CLI + Skill + MCP 三层架构：CLI（动作层）→ Skill/Rules（工作流层）→ MCP（接入层），将企业私有能力整理成 AI 可识别、可调用、可编排的接口。

## Key Claims

- 企业 AI Coding 最大痛点：AI 不认识私有组件、设计系统、研发规范
- 仅靠文档补、Prompt 补、只接 MCP 都不够，需要系统化分层
- Ant Design CLI 三层架构：CLI 动作层 → Skill 工作流层 → MCP 接入层
- CLI 本质是动作接口，将散落知识变成可执行、可编排的命令
- 对弱模型更友好：减少自由度，提升稳定性，不一定要用最贵的模型
- 企业应该把私有能力整理成结构化、可调用、可编排的动作层

## Entities Mentioned

- [[Ant Design-CLI]] — Antd 的命令行工具，覆盖组件查询、诊断、迁移等能力
- [[Bolt.new]] — 公共技术栈 AI Coding 工具
- [[V0]] — 公共技术栈 AI Coding 工具
- [[Lovable]] — 公共技术栈 AI Coding 工具

## Concepts Covered

- [[AI编程]] — 企业私有组件环境下的 AI 编程挑战
- [[MCP协议]] — 标准化接入层，解决工具暴露而非执行问题
- [[Skill开发]] — Skill/Rules 固化可复用的执行路径
- [[企业AI落地]] — 私有组件库如何面向 AI 整理能力
- [[自动化工作流]] — 组件查询→示例获取→模板组装→代码生成→校验的完整流程
