---
tags: [浏览器自动化, OpenClaw, Skill, CLI, Playwright]
sources: [浏览器自动化/CLI+Skill 搭建 AI 浏览器自动化框架：告别重复任务，0 Token 也能跑.md]
created: 2026-05-10
updated: 2026-05-10
---

# CLI+Skill 搭建 AI 浏览器自动化框架：告别重复任务，0 Token 也能跑

**Source:** AI炼金社
**Category:** 浏览器自动化
**Date ingested:** 2026-05-10
**Type:** article

## Summary

介绍用 OpenClaw Browser Automation Skill + agent-browser CLI 实现自然语言控制浏览器的方案。Skill = Markdown 文件，定义工作流步骤；CLI 负责执行。很多场景可 0 Token 运行（纯 Skill 指令，不需 LLM 推理）。

## Key Claims

- 传统浏览器自动化（Puppeteer/Playwright）三宗罪：门槛高、维护累、成本高
- OpenClaw Skill = Markdown 文件，定义触发条件、执行步骤、注意事项
- agent-browser CLI 执行 Skill，支持签到、信息采集、表单填写等重复任务
- 0 Token 模式：纯 Skill 指令流，不经过 LLM 推理也能跑
- 网站改布局只改 Skill 文件，不用改代码

## Entities Mentioned

- [[OpenClaw]] — Agent 平台，支持 Skill 体系
- [[不设置任何云浏览器-API-key-Hermes-自动-fallback-到-agentbrowser-本地模式]] — 浏览器自动化 CLI 工具
- [[Playwright]] — 底层浏览器驱动

## Concepts Covered

- [[浏览器自动化]] — 用 Skill 替代脚本控制浏览器
- [[Skill开发]] — Markdown 格式的 Skill 设计模式
- [[自动化工作流]] — 签到、信息采集等重复任务自动化
