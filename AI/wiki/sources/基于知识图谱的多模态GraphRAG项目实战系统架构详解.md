---
title: "基于知识图谱的多模态 GraphRAG 项目实战，系统架构详解[附源码]"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["基于知识图谱的多模态 GraphRAG 项目实战，系统架构详解[附源码].md"]
tags: [RAG, 知识图谱, GraphRAG, 多模态, LangChain, Neo4j, Milvus]
---

## Summary

作者构建了一套完整的多模态 GraphRAG 知识库问答系统，解决传统 RAG"语义匹配强、关系理解弱"的问题。核心技术栈：MinerU（文档解析）→ LangExtract + DeepSeek（实体抽取）→ Neo4j + Milvus 双存储（知识图谱 + 向量库）→ LangChain ReAct Agent（混合检索问答）→ FastAPI + React（前后端）。对比传统 RAG，GraphRAG 在复杂多跳问答（如"A 公司产品相比 B 公司的优势"）上有显著优势，可做实体关系路径推导而非简单语义匹配。

## Key Claims

1. **双索引架构**：左路（结构化语义）存入 Neo4j 知识图谱，重点在于实体、关系及图遍历能力；右路（语义向量）存入 Milvus 向量库，重点在于 Embedding 和 ANN 搜索。两者互补，兼顾关系推理与语义召回。
2. **实体抽取体系（五类）**：TECHNOLOGY（技术/框架/工具/算法）、CONCEPT（抽象概念/理论/方法论）、PERSON、ORGANIZATION、LOCATION。加了五类后图谱密度从 0.3 升到 1.8，问答召回质量明显提升。
3. **共现边策略**：不直接让 LLM 输出一对一关系（不稳定、易编造），而是用同一页出现的任意两个实体自动生成一条 CO_OCCURS_IN（共现）边，简化但足够实用。
4. **LangChain ReAct Agent 编排**：多跳问答（找方案实体 → 找技术指标 → 找竞品对应指标 → 做比较）通过 Agent 自己决定下一步工具调用（search_entities、get_neighbors、get_entities_by_type、describe_graph）来实现，每轮问答平均调用 4-6 次工具，延迟 8-15 秒。
5. **与传统 RAG 核心区别**：传统 RAG 是"语义匹配"，GraphRAG 是"关系理解"；传统 RAG 适用简单问答，GraphRAG 适合需要推理的复杂问题；索引内容从 chunks 文本块升级为实体 + 关系 + 原始文本。
6. **完整 pipeline**：PDF 文件 → MinerU 云端解析 → content_list.json → text_assembler 格式转换 → 每页 .txt → LangExtract + DeepSeek 实体抽取 → kg_builder 图谱构建 → LangChain ReAct Agent 多跳问答 → 最终回答。

## Entities Mentioned

- [[MinerU]] — PDF 文档解析工具（浙江大学实验室开源）
- [[LangExtract]] — LLM 结构化信息抽取框架
- [[Neo4j]] — 图数据库，用于知识图谱存储
- [[Milvus]] — 开源向量数据库，用于语义召回
- [[LangChain]] — LLM 应用开发框架
- [[FastAPI]] — Python Web 框架

## Concepts

- [[GraphRAG]] — 结合知识图谱与向量检索的 RAG 增强方案
- [[知识图谱构建]] — 从文档中抽取实体、关系构建图谱的技术
- [[RAG]] — 检索增强生成
- [[多模态]] — 支持多种数据格式（PDF、图片、表格等）的处理能力
- [[混合检索]] — 融合关键词检索、向量检索、图检索的复合检索方式

## Notable Quotes

> "GraphRAG 的做法是：先找到 A 公司产品实体 → 找它的性能指标节点 → 再找 B 公司产品的对应指标 → 做节点级别的比较，回答有据可查。"

## Limitations / Bias

- 完整方案依赖云端 API（MinerU、DeepSeek），有成本和网络依赖
- 系统复杂度较高，从零搭建需要较多工程工作
- 作者为方案实践者，存在实现路径偏好