---
title: "Hermes + Obsidian + LLM Wiki：搭建一个「会自己长大」的本地知识库"
type: source-summary
created: 2026-05-18
updated: 2026-05-18
sources: [Hermes + Obsidian + LLM Wiki：搭建一个「会自己长大」的本地知识库.md]
tags: [LLM-Wiki, Obsidian, Hermes, 知识管理, 本地优先]
---

## Summary

本文系统介绍 Karpathy 提出的 LLM Wiki 方法论，以及如何用 Hermes Agent + Obsidian 实现自动化知识管理。核心洞见：RAG 是"被动检索"——每次从零开始找碎片；LLM Wiki 是"主动积累"——知识编译一次、持续维护，复利增长。

三层架构：① Raw Sources（原始资料，只读）→② Wiki（AI生成和维护的摘要/实体/概念/对比/综述页）→③ Schema（CLAUDE.md/SCHEMA.md 控制行为规范）。三大操作：Ingest（摄入新资料）、Query（基于Wiki回答）、Lint（定期健康检查）。

Hermes Agent 内置 llm-wiki skill，可自动执行：提取实体和概念→创建结构化Markdown→添加双向链接→更新索引和日志。Obsidian 作为展示层，双向链接+Graph View让知识网络可视化。Karpathy 的那句话点睛：**Wiki 是一个 persistent, compounding artifact（持久的、会复利的制品）**。

## Key Claims

1. RAG 每次从零检索，知识是静态的；LLM Wiki 持续积累，知识是动态复利的——随资料量增大，两者差距越来越大
2. Hermes 的两条铁律：说「写入知识库」才整理，说「结合知识库」才检索——避免无关对话污染知识库
3. LLM Wiki 天然本地优先：纯 Markdown 文件目录，不需要向量数据库、不需要 embedding pipeline
4. Karpathy："Wiki 是一个 persistent, compounding artifact（持久的、会复利的制品）"——复利是 LLM Wiki 和 RAG 的本质区别

## Entities Mentioned

- [[LLM-Wiki]] — Karpathy 提出的 LLM Wiki 方法论（持久复利知识库）
- [[Karpathy]] — LLM Wiki 方法论的提出者
- [[Hermes]] — llm-wiki skill 的执行引擎，支持自动化知识库维护
- [[Obsidian]] — 本地双向链接笔记工具，知识网络展示层
- [[Graph View]] — Obsidian 的知识图谱可视化功能
- [[llm-wiki skill]] — Hermes 内置的 LLM Wiki 操作技能

## Concepts

- [[LLM-Wiki方法论]] — 让 LLM 增量构建并维护持久化 Wiki 的方法论
- [[RAG vs Wiki]] — 被动检索 vs 主动积累的本质区别
- [[知识复利]] — Wiki 作为 compounding artifact 的核心理念
- [[三权分立]] — Raw Sources（只读）/ Wiki（AI维护）/ Schema（规范）的架构设计
- [[Ingest-Query-Lint]] — LLM Wiki 的三大核心操作
- [[双向链接]] — Obsidian 的核心特性和 Wiki 知识关联机制
- [[本地优先]] — 所有数据在本地，纯 Markdown，无云端依赖
- [[BM25搜索]] — Wiki大了之后的本地搜索方案（qmd工具）

## Notable Quotes

> "RAG 模式下，知识库本质上是一个'更好的搜索引擎'。而 LLM Wiki 模式下，知识库是一个'活的、会生长的有机体'——它在不断摄入、编译、关联、修正。"

> Karpathy："Wiki 是一个 persistent, compounding artifact（持久的、会复利的制品）。"

## Related Pages

- [[知识库构建]] — 更广泛的个人知识库建设
- [[记忆系统]] — 与其他 Agent 记忆系统的对比
- [[Hermes]] — Hermes Agent 的 llm-wiki skill 实现
- [[OpenHuman]] — 对比：另一种个人 AI 知识管理方案
