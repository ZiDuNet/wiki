---
title: "从 0 到 1 搭建 AI 知识库：obsidian-wiki 完整实操"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: [从 0 到 1 搭建 AI 知识库：obsidian-wiki 完整实操（保姆级教程）.md]
tags: [知识管理, Obsidian, LLM-Wiki, AI知识库, Karpathy]
---

## Summary

保姆级教程，手把手教如何用 obsidian-wiki 搭建会自我维护的本地 AI 知识库。核心方法是 Karpathy 提出的 LLM Wiki 模式：将知识编译为相互关联的 Markdown 文件，让 LLM 持续维护更新。文章涵盖 obsidian-wiki（GitHub 1.1k★，MIT，v2026.05）的安装、13+ 斜杠命令工作流（/wiki-ingest、/wiki-query、/wiki-update 等），以及将 Claude/Codex 历史对话自动蒸馏为知识页面的能力。

## Key Claims

1. 知识管理核心痛点：同一问题问AI五次、代码和坑散落对话里、文档积攒但找不出结论
2. Karpathy LLM Wiki 核心原则：Compile knowledge once into interconnected markdown files, let LLM keep them current
3. obsidian-wiki 提供 13+ 斜杠命令，核心：/wiki-ingest（摄入源）、/wiki-query（查询）、/wiki-update（更新）
4. 支持将历史对话自动蒸馏为知识页面（Claude/Codex → 知识库）
5. raw/ 是只读证据层，wiki/ 是 LLM 工作区，两者严格分离

## Entities Mentioned

- [[Obsidian]] — 知识库工具
- [[Karpathy]] — LLM Wiki 模式的提出者
- [[Claude]] — AI助手
- [[GitHub开源项目]] — obsidian-wiki 项目

## Concepts

- [[LLM-Wiki]] — 用 LLM 维护的结构化知识库模式
- [[RAG]] — 与知识库检索增强相关
- [[知识管理]] — 整体应用领域

## Notable Quotes

> "Compile knowledge once into interconnected markdown files, then let the LLM keep them current." — Andrej Karpathy

## Limitations

- obsidian-wiki 目前版本较新（v2026.05），生态尚在完善
- 需要投入时间建立和维护知识库秩序，"90%页面是TODO"是常见失败模式
