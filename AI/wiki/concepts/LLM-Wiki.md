---
title: LLM Wiki
type: concept
tags: [LLM-Wiki, 知识库, Karpathy, AI-Agent, 知识管理]
sources: [hermes-agent-llm-wiki-obsidian-个人知识库.md, hermes-agent-高级玩法微信扫码即用-LLM-Wiki-知识库打造你的数据飞轮.md]
created: 2025-01-01
updated: 2026-05-31
---

# LLM Wiki

## 定义

**LLM Wiki** 是由 Karpathy 于 2025 年提出的 AI 全自动构建和维护的结构化知识库模式。核心理念：让 LLM 作为"程序员"，持续将原始资料编译成结构化、相互链接的 Wiki 页面，而不是在查询时临时从文档检索。

## 核心原则

1. **Raw 层不可变** — 源文件只读，永远不修改
2. **Wiki 是 LLM 工作区** — 所有页面由 LLM 创建和维护
3. **持续复利** — 每新增一个源文件，Wiki 的交叉引用和综合分析都在变得更丰富
4. **双向链接** — 所有实体页和概念页通过 `[[wikilink]]` 相互连接

## 三层架构

| 层级 | 用途 | 说明 |
|---|---|---|
| **Raw Sources** | 证据层 | PDF、网页、论文、代码，只读 |
| **Wiki** | 工作区 | Entity Pages + Concept Pages + 双向链接 |
| **Schema** | 指令层 | SCHEMA.md/CLAUDE.md，定义操作规则 |

## 关键对比

| 传统笔记 | LLM Wiki |
|---|---|
| 人类手动维护 | AI 自动编译和维护 |
| 越记越乱 | 越积累越丰富 |
| 临时检索 | 持久化的知识图谱 |
| 单点记录 | 交叉引用的网络 |

## 相关工具

- **[[Obsidian]]** — 本地笔记软件，天然作为 Wiki 的 IDE
- **[[Hermes-Agent]]** — 多渠道 AI Agent，执行定时摄入任务
- **[[OpenClaw]]** — 多 Agent 协作框架，其 Active Memory 是"记录"而非"编译"

## 相关文章

- [[Hermes Agent + LLM Wiki + Obsidian 个人知识库]] — 从AI到Web3的探索之旅，详解三层架构和持续维护机制
- [[Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮]] — 侧重微信扫码和数据飞轮角度