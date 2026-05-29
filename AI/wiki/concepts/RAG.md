---
type: concept
name: RAG
created: 2026-05-29
updated: 2026-05-29
tags: [知识管理, 检索增强, LLM, 知识编译]
sources: [karpathy-llm-wiki-context-memory重构企业级的组织记忆.md]
---

# RAG

**类型:** 概念

## 定义

Retrieval-Augmented Generation（检索增强生成），一种让 LLM 在生成回答前先检索相关文档的技术架构。

## 传统 RAG 流程

上传文档 → 问问题 → LLM 检索 → 生成答案

## RAG 的本质缺陷

Karpathy 指出传统 RAG 的致命问题：**每次查询都是一次"重新发现"**。

> "rediscovering knowledge from scratch on every question"

每次都在重新发明轮子，没有知识积累机制。

## 问题示例

你花三周研读 20 篇 AI Agent 论文，问 LLM "AI Agent 发展经历了哪几个阶段"，LLM 仍需要在这 20 篇论文中重新检索、重新理解、重新整合。

## LLM Wiki 的解法

| 传统 RAG | LLM Wiki |
|---------|---------|
| 每次重新发现 | 知识累积增长 |
| 知识是消耗品 | 知识是可复合资产 |
| 人工维护 | LLM 自动维护 |
| 检索原始碎片 | 回答已整理知识 |

## 企业级混合方案

大规模场景下，可采用定制 RAG + Wiki 混合架构：
- BM25 传统文本检索
- 向量搜索语义相似度匹配
- LLM 重排序智能结果优化
- Wiki 知识库作为预处理层

## 相关概念

- [[LLM-Wiki]]
- [[传统RAG困境]]
- [[知识编译]]
- [[企业级组织记忆]]

## 相关实体

- [[Karpathy]]

## 来源文章

- [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]]