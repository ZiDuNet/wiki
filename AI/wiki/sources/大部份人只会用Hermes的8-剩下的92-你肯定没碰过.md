---
tags: [Hermes, Agent, Skills, 高级功能]
sources: [Hermes/大部份人只会用 Hermes 的 8%功能，剩下的92% 功能你肯定没碰过.md]
created: 2026-05-10
updated: 2026-05-10
---

# 大部份人只会用 Hermes 的 8%功能，剩下的92% 功能你肯定没碰过

**Source:** Hermes/大部份人只会用 Hermes 的 8%功能，剩下的92% 功能你肯定没碰过.md
**Date ingested:** 2026-05-10
**Type:** article

## Summary

一篇 [[Hermes]] 高级功能全景指南，作者指出大部分用户只使用了 Hermes 8% 的功能（接入平台、选模型、打 prompt），而剩余 92% 的高级功能——持久记忆、会话分支、文件回滚、语音模式、17 平台全覆盖、自定义斜杠命令等——都在闲置。文章将功能分为 5 部分 15 个功能点进行细致讲解。

## Key Claims

- 大部分用户把全副武装的 AI Agent 当成了"稍微聪明一点的 ChatGPT"
- SOUL.md 定义 Agent 的"灵魂"和语气，MEMORY.md + USER.md 实现持久化记忆
- /snapshot 可保存完整状态并支持回滚，是 Agent 自己的"时光机"
- /branch 可像 Git 一样分支会话，/rollback 实现文件系统检查点恢复
- /steer 和 /queue 支持飞行中实时控制，不中断当前流程即可纠偏
- /model 支持一条命令切换模型，无需重启，覆盖十几家供应商
- 辅助模型可将上下文压缩、会话摘要、标题生成、视觉任务指定给不同模型
- 17 平台网关覆盖 Telegram、Discord、Slack、WhatsApp、飞书、钉钉等
- /voice 支持实时语音交互，/cron + webhook 实现定时任务和事件驱动
- 技能 = 斜杠命令，100+ 内置技能，还可自定义

## Entities Mentioned

- [[Hermes]] — 核心主题，全功能 AI Agent 平台
- [[Hermes-Agent]] — Hermes 的 Agent 实例
- [[Anthropic]] — Anthropic Opus/Haiku 等模型供应商
- [[OpenAI]] — OpenAI 模型供应商
- [[飞书]] — 支持平台之一
- [[Telegram]] — 支持平台之一
- [[OpenRouter]] — 模型路由供应商

## Concepts Covered

- [[记忆系统]] — MEMORY.md + USER.md + FTS5 + LLM 摘要索引
- [[Skills技能系统]] — 100+ 内置技能 + 自定义斜杠命令
- [[SOUL配置]] — SOUL.md 定义 Agent 人格和语气
- [[AGENTS配置]] — 全局指导文件
- [[Cron定时任务]] — 内置定时任务，支持自然语言描述
- [[Webhook自动化]] — 事件驱动推送，替代 Zapier
- [[Token优化]] — 辅助模型分配，避免为 Haiku 级别工作付 Opus 的钱
- [[Agent架构]] — 会话分支、文件回滚、飞行中纠偏等高级特性
- [[多Agent协作]] — 多平台网关、多模型路由
- [[多模态]] — /voice 实时语音交互
- [[Profile系统]] — /personality 切换预设人格
