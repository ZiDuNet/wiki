---
type: entity
name: Graphify
created: 2026-05-11
updated: 2026-05-11
---

# Graphify

**类型:** 实体 (产品/工具)
**提及文章数:** 2

## 简介

Graphify是AI编程技能，把文件夹变成可查询知识图谱，首次工程化实现Karpathy的LLM Wiki理念。采用NetworkX知识图谱+Leiden算法社区检测，无向量数据库，实现71.5x Token压缩。双轨提取引擎：代码文件走tree-sitter AST零Token消耗，文档图片走LLM语义提取。

## 核心特性

- 七级流水线处理流程
- 双轨提取引擎（tree-sitter + LLM）
- 三级置信度标签：EXTRACTED(1.0)、INFERRED(0.4-0.9)、AMBIGUOUS(0.1-0.3)
- MCP服务器模式 + Always-On模式
- SHA256增量缓存
- 全模态支持：代码、PDF、Markdown、截图、架构图

## 相关概念

- [[知识图谱构建]], [[LLM-Wiki方法论]], [[Token优化]], [[Agent架构]]

## 相关文章

- [[Graphify-知识图谱工程化]]
- [[Karpathy的LLM Wiki + 3.5万Star的Graphify：企业级 RAG 缺的真是知识图谱？]]