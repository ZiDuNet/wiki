---
title: "给Karpathy的LLMWiki装上自动引擎"
type: source-summary
created: 2026-05-22
updated: 2026-05-22
sources: [给 Karpathy 的 LLM Wiki 装上自动引擎.md]
tags: [LLM Wiki, 知识库自动化, AutoCLI, 定时任务, Hermes]
---

# 给Karpathy的LLMWiki装上自动引擎

## Summary

介绍如何将手动维护的LLM Wiki知识库升级为自动运转系统。三个阶段：1)用AutoCLI自动抓取X/公众号/B站等内容；2)用Agent自动编译wiki页面；3)接入微信/飞书推送日报。配合定时任务实现每日自动运转。

## Key Claims

1. 阶段一：AutoCLI自动抓取信息（X、公众号、B站、知乎、Reddit等），按日期归档
2. 阶段二：Agent按AGENTS.md规则自动编译wiki页面，更新index.md和log.md
3. 阶段三：微信/飞书推送日报，知识库主动找用户
4. 三个定时任务串成一条链：5点抓取→6点编译→8点推送
5. Karpathy的LLM Wiki模式：Obsidian是IDE，LLM是程序员，wiki是代码库

## Entities Mentioned

- [[AutoCLI]]
- [[LLM Wiki]]
- [[Hermes]]
- [[Claude Code]]
- [[Obsidian]]

## Concepts

- [[LLM Wiki方法论]]
- [[知识库自动化]]
- [[AutoCLI]]
- [[定时任务]]
