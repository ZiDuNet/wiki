---
title: "从手写 Prompt 到可复用 Skills：AI Agent 的"技能包""
type: source-summary
created: 2026-05-22
updated: 2026-05-22
sources: [从手写 Prompt 到可复用 Skills：AI Agent 的"技能包".md]
tags: [Skill, Prompt, AI Agent, 工程化, 知识沉淀]
---

## Summary

这篇文章系统性地介绍了 Skills 的概念、起源和写作方法。Skills 是解决当前 AI Agent 落地中"模型越来越强，但组织化、流程化、可复用的知识仍然很难沉淀"这一核心矛盾的创新方案。

文章对比了 System Prompt、RAG、Plugin 等传统方案的局限性，提出 Skills 作为更轻量、更工程化的解决方案。Skills 本质上是一个文件夹，核心文件是 SKILL.md，包含 YAML 元数据和 Markdown 正文，用于定义操作流程、最佳实践、注意事项和示例。文章还提供了多个实用的 Skills 推荐和写作原则。

## Key Claims

1. System Prompt 写得太长会挤占上下文窗口，而且很难跨场景复用
2. RAG 系统更适合知识检索，但要搭建向量数据库、切分文档、做召回和评估，成本并不低
3. Skills 可以理解为给 AI Agent 准备的"工作手册"，模型是通用大脑，Skills 是不同场景下的操作指南
4. Skill 写作应遵循原子性原则：一个 Skill 只解决一个具体问题
5. Skills 不是一次写完就结束的东西，需要持续复盘，把 Bad Case 变成新规则

## Entities Mentioned

- [[Anthropic]]
- [[MiniMax]]
- [[Claude Code]]
- [[Vercel Labs]]

## Concepts

- [[Skill]]
- [[Prompt工程]]
- [[RAG]]
- [[Plugin]]
- [[AI Agent工程化]]
- [[SKILL.md]]

## Notable Quotes

> "当前 AI Agent 落地中的一个核心矛盾：模型越来越强，但组织化、流程化、可复用的知识仍然很难沉淀。"

> "Skill 的关键不是'写得越多越好'，而是'写得刚好有用'。"

> "对大多数人来说，最佳路径不是直接安装一堆 Skill，而是：先找 3～5 个优秀 Skill，拆开看它们怎么写；再挑一个和自己最相关的场景，改成自己的版本。"

## Limitations / Bias

文章主要聚焦 Skills 的概念介绍，未深入探讨实际部署和运维的复杂性。推荐的 Skills 主要来自官方库，可能存在一定的推广倾向。