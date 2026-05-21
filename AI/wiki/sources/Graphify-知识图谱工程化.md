---
title: "Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: ["Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品.md"]
tags: [Graphify, 知识图谱, NetworkX, tree-sitter, Leiden算法, 置信度标签, Karpathy, Token压缩]
---

# Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品

## 概要

Graphify是AI编程技能，把文件夹变成可查询知识图谱，首次工程化实现Karpathy的LLM Wiki理念。从Wiki升级为Graph：NetworkX知识图谱+Leiden算法社区检测，无向量数据库。双轨提取引擎：代码文件走tree-sitter AST零Token消耗毫秒级完成，文档图片走LLM语义提取并行子代理。

三级置信度标签让知识可追溯：EXTRACTED(1.0)、INFERRED(0.4-0.9)、AMBIGUOUS(0.1-0.3)。71.5x Token压缩：付一次编译成本，后续查询读取紧凑graph.json而非原始文件。全模态支持：代码、PDF、Markdown、截图、架构图、白板照片都能提取概念和关系融入图谱。

## 关键要点

1. 从Wiki升级为Graph：NetworkX知识图谱+Leiden算法社区检测，无向量数据库
2. 双轨提取：代码文件走tree-sitter AST零Token消耗毫秒级完成，文档图片走LLM语义提取并行子代理
3. 三级置信度标签让知识可追溯：EXTRACTED(1.0)、INFERRED(0.4-0.9)、AMBIGUOUS(0.1-0.3)
4. 71.5x Token压缩：付一次编译成本，后续查询读取紧凑graph.json而非原始文件
5. 全模态支持：代码、PDF、Markdown、截图、架构图、白板照片都能提取概念和关系融入图谱

## 提及实体

- Graphify — AI编程技能，将文件夹转为可查询知识图谱
- Karpathy — AI领域知名研究者，提出LLM Wiki理念
- NetworkX — Python网络分析库，用于图数据结构
- tree-sitter — 代码解析工具，支持多语言AST
- Anthropic — Claude模型开发公司

## 涉及概念

- [[知识图谱构建]] — 建立实体关系网络的技术和方法
- [[LLM-Wiki方法论]] — 用AI作为Wiki编辑持续维护知识库的方法
- [[Token优化]] — 减少AI调用Token消耗的策略
- [[Agent架构]] — AI Agent的系统设计和组织方式

## 原始资料链接

[[Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品.md]]