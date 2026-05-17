---
title: "OpenHuman：开源的个人AI超级智能，让你的AI真正认识你"
type: source-summary
created: 2026-05-18
updated: 2026-05-18
sources: [OpenHuman：开源的个人AI超级智能，让你的AI真正认识你.md]
tags: [AI助手, 个人知识管理, 本地优先, 开源]
---

## Summary

OpenHuman 是一款由 Tiny Humans AI 开发的开源（GNU 协议）个人 AI 超级智能产品，主打"让 AI 在几分钟内真正认识你"。与传统的 AI 助手（每次对话都要重新解释背景）不同，OpenHuman 通过把用户的所有数据（邮件、文档、聊天记录、日程）压缩成一个"记忆树"，让 AI 能够基于完整的个人上下文来工作。

核心创新点：① 零训练期——连接账号后每 20 分钟自动同步，压缩成≤3k token 的 Markdown 存到本地 SQLite；② 118+ 一键 OAuth 集成（Gmail、Notion、GitHub 等）；③ TokenJuice 压缩层节省 80% token 成本；④ Obsidian 兼容——数据同时存为 .md 文件可用 Obsidian 打开编辑；⑤ 支持 Ollama 完全本地运行。

## Key Claims

1. 传统 Agent（OpenClaw/Hermes）需要手动配置插件、慢慢喂数据，几周后才能有点用；OpenHuman 连接账号即自动同步，一次同步就有完整上下文
2. TokenJuice 压缩层能把 HTML 转 Markdown、缩短 URL、过滤冗余——同样的信息量，token 消耗降到原来的 20%
3. OpenHuman 与 Claude CoWork、OpenClaw、Hermes 的核心差异：零训练期、118+ OAuth 集成、自动每 20 分钟同步、80% token 节省

## Entities Mentioned

- [[OpenHuman]] — 本文核心产品：开源个人 AI 超级智能，通过记忆树让 AI 真正认识用户
- [[Claude CoWork]] — 对比产品之一，不开源，记忆仅聊天级
- [[OpenClaw]] — 对比产品之一，MIT 开源，但需手动配置，记忆依赖插件
- [[Hermes]] — 对比产品之一，MIT 开源，自学习但需手动积累
- [[Ollama]] — 支持本地运行的语言模型运行时
- [[ElevenLabs]] — 语音输出提供商
- [[SQLite]] — 本地数据存储引擎
- [[记忆树]] — OpenHuman 的核心数据结构：将用户数据压缩为 ≤3k token 的 Markdown 块

## Concepts

- [[本地优先]] — 所有记忆数据存到本地 SQLite，云端只跑模型推理
- [[个人AI知识管理]] — 让 AI 基于完整个人上下文工作的理念
- [[Token压缩]] — TokenJuice 压缩层节省 80% token 消耗
- [[OAuth集成]] — 118+ 服务一键 OAuth 连接

## Notable Quotes

> "传统方案（比如 OpenClaw、Hermes）需要你手动配置插件、慢慢喂数据，几周后 AI 才有点用处。OpenHuman 的逻辑：你连账号，它自动拉数据，压缩成记忆——一次同步就有完整上下文。"

## Limitations / Bias

- 目前处于 Early Beta 阶段，产品较粗糙
- 依赖第三方云端模型推理（除非完全本地 Ollama）
- 桌面宠物加入 Google Meet 功能尚未验证实际效果

## Related Pages

- [[Obsidian]] — OpenHuman 数据兼容 Obsidian vault 格式
- [[LLM-Wiki方法论]] — 与 OpenHuman 类似的个人知识管理思路
- [[记忆系统]] — 对比不同 Agent 的记忆系统实现
