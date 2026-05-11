---
tags: [AI编程, Agent, Agent路由, Gateway, OpenClaw, 多Agent协作, 部署, 飞书]
sources: ['微信公众号/OpenClaw/OpenClaw多Agent飞书机器人路由配置实战.md']
created: 2026-05-10
updated: 2026-05-10
---

# OpenClaw多Agent飞书机器人路由配置实战

**Source:** OpenClaw 公众号文章
**Category:** OpenClaw
**Date ingested:** 2026-05-10
**Type:** article

## Summary

> 📎 来源: 不灭的传说 | 时间: 2026-04-21 20:23 > **摘要**：本文详细记录了OpenClaw多Agent系统中飞书机器人消息路由问题的诊断与解决过程。从所有消息错误路由到总指挥，到通过配置bindings实现正确分发，提供了完整的实战经验和避坑指南。 最近在部署OpenClaw多Agent系统时，遇到了一个棘手的问题：我们配置了3个飞书机器人，分别对应3个不同的AI专家Agent（总指挥、编程大师、投资顾问）。但所有用户发送给这些机器人的消息，都被错误地路由到了总指挥Agent。

## Key Claims

- 用户向编程大师机器人发送技术问题 → 总指挥回复
- 用户向投资顾问机器人发送财经咨询 → 总指挥回复
- 多Agent路由必须配置bindings
- accountId是路由的关键标识
- 没有bindings时，所有消息路由到默认或第一个Agent

## Entities Mentioned

- [[OpenClaw]]
- [[飞书]]

## Concepts Covered

- [[Agent路由]]
- [[Skill开发]]
- [[多Agent协作]]
- [[本地部署]]

## Related Sources

- [[OpenClaw文章索引]]
