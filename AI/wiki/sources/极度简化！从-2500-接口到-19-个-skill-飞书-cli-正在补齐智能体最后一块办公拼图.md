---
tags: [飞书, Skill, CLI, 自动化工作流, Agent]
sources: [飞书/极度简化！从 2500+ 接口到 19 个Skill，飞书 CLI 正在补齐智能体，最后一块办公拼图！.md]
created: 2026-05-10
updated: 2026-05-10
---

# 极度简化！从 2500+ 接口到 19 个Skill，飞书 CLI 正在补齐智能体，最后一块办公拼图！

**Source:** AI编程瓜哥
**Category:** 飞书
**Date ingested:** 2026-05-10
**Type:** article

## Summary

介绍飞书 CLI（lark-cli）将飞书 2500+ API 封装为 19 个 Agent Skill，解决 AI 直接调用飞书 API 的 Token 消耗高、参数幻觉、逻辑复杂等问题。支持消息收发、文档管理、多维表格、日程、任务、会议纪要、审批等全场景。

## Key Claims

- 传统飞书 API 对 Agent 不友好：Token 消耗极高、AI 容易参数幻觉、需处理鉴权分页重试
- lark-cli 封装为 19 个 Skill，一条指令直接交付结果，Token 消耗极低
- 官方预置 Workflow Skill：站会报告自动生成、会议纪要聚合、多维表格自动写入
- 安装简单：`npm install -g @larksuite/cli` + `npx skills add larksuite/cli -y -g`
- 支持 Claude Code、Codex、Gemini CLI 等主流 Agent

## Entities Mentioned

- [[飞书CLI]] — 飞书官方命令行工具，19 个 Skill 封装
- [[OpenClaw]] — 支持 lark-cli 的 Agent 平台
- [[Claude-Code]] — 支持 lark-cli 的编程 Agent

## Concepts Covered

- [[飞书集成]] — 飞书工作流全场景自动化
- [[Skill开发]] — Agent-Native 的 Skill 设计理念
- [[自动化工作流]] — 站会报告、会议纪要、审批等办公自动化
