---
title: "基于知识图谱的多模态 GraphRAG 项目实战，系统架构详解"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["基于知识图谱的多模态 GraphRAG 项目实战，系统架构详解[附源码]_1.md"]
tags: [GraphRAG, 知识图谱, RAG, MinerU, LangChain, Neo4j, Milvus]
---

## Summary

作者实战搭建多模态 GraphRAG 系统，解决传统 RAG"语义匹配但缺少关系理解"的问题。架构：PDF/Docx → MinerU 多模态解析 → LangExtract+DeepSeek 实体抽取 → Neo4j（图数据库）+ Milvus（向量库）双存储 → LangChain ReAct Agent 混合检索 → FastAPI → React 前端。核心技术点：五层架构设计、双索引（向量+图）、实体类型体系（TECHNOLOGY/CONCEPT/PERSON/ORGANIZATION/LOCATION）、共现边策略。

## Key Claims

1. **多模态文档解析**：MinerU 云端 API，109 种语言 OCR，版面分析+表格识别+公式识别+图片提取，3-5 秒/页
2. **双索引存储**：Neo4j（图遍历推理）+ Milvus（向量 ANN 检索），共现边策略建立实体关系
3. **实体类型体系**：TECHNOLOGY/CONCEPT/PERSON/ORGANIZATION/LOCATION 五类，图谱密度从 0.3 提升到 1.8
4. **LangChain Agent 多跳问答**：ReAct 策略，4 工具（search_entities/get_neighbors/get_entities_by_type/describe_graph），平均 4-6 次工具调用/问答
5. **效果**：58 页 PDF 索引约 12 分钟，2256 节点/132096 边；复杂问答 10-20 秒

## Entities Mentioned

- [[MinerU]]（文档解析）
- [[Neo4j]]（图数据库）
- [[Milvus]]（向量数据库）
- [[LangChain]]（Agent 编排）
- [[DeepSeek]]（实体抽取模型）
- [[FastAPI]]（后端框架）
- [[React]]（前端）

## Concepts

- [[RAG]] — GraphRAG 是对传统 RAG 的增强，加入知识图谱层
- [[知识图谱]] — Neo4j 构建的实体关系网络，支持多跳推理
- [[GraphRAG]] — 向量检索+图遍历的混合检索方式
- [[Agent]] — LangChain ReAct Agent 的多跳推理能力

## Notable Quotes

> "传统 RAG 更像『语义匹配』，缺少『关系理解』。GraphRAG 做法：先找到 A 公司产品实体 → 找性能指标节点 → 再找 B 公司对应指标 → 做节点级别比较。"

## Limitations

- 完整版 MinerU 需 NVIDIA GPU，MinIO 等依赖较多
- 私有化部署有一定技术门槛
