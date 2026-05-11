---
tags: [RAG, 知识图谱, LLM-Wiki, Graphify, 企业级, Karpathy]
sources: [LLM Wiki/Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？.md]
created: 2026-05-11
updated: 2026-05-11
---

# Karpathy的LLM Wiki + 3.5万Star的Graphify：企业级 RAG 缺的真是知识图谱？

**Source:** LLM Wiki/Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？.md
**Date ingested:** 2026-05-11
**Type:** article

## Summary

一篇深度工程实践文章，用 30 份合成合同和 48 个测试问题，对比基础 RAG、LLM Wiki 模式和受控 schema 综合方案。结论：企业级 RAG 真正缺的不是知识图谱，而是受控 schema、结构化字段、原文引用、权限边界和可复跑评测。LLM Wiki 的知识预编译思路值得抄，Graphify 的结构化导航思路可借鉴，但不能照搬自由生成方式。

## Key Claims

- LLM Wiki 不是 RAG 替代品，而是 RAG 缺失的知识预编译层
- LLM Wiki 知识形态：摘要页、实体页、综合页、索引页（vs 传统 RAG 的 chunk）
- Graphify 的 71.5x token reduction 是上下文节省，不是准确率提升
- 合同知识库中，图谱只适合解决跨文件、跨实体、跨时间的问题
- 受控 schema + 结构化字段 + 条款级索引 + 关系表 + 原文引用 = 企业级合同知识库
- 基础 RAG 24 题准确率 25%，LLM Wiki 小样本 100%，受控 schema 综合方案 24/24 全对
- 企业级四大工程障碍：成本、可控性、权限、合规审计

## Entities Mentioned

- [[Karpathy]] — LLM Wiki 原始作者
- [[Obsidian]] — LLM Wiki 的 Markdown 浏览载体
- [[Claude-Code]] — 运行 LLM Wiki ingest 的工具
- [[Codex]] — 运行 LLM Wiki ingest 的工具
- [[GitHub]] — 项目托管平台

## Concepts Covered

- [[RAG]] — 基础向量 RAG 的局限（全局问题不稳定）
- [[RAG检索增强]] — 企业级 RAG 需要结构化补充
- [[知识库构建]] — 受控 schema + 预编译 + 原文引用
- [[知识图谱]] — Graphify 自动知识图谱的适用边界
- [[知识管理]] — 个人知识库 vs 企业知识库的最佳实践差异
- [[Agent架构]] — Agent 驱动的知识预编译工作流
- [[上下文工程]] — 知识预编译减少重复 token 消耗
- [[Token优化]] — 预编译一次反复使用 vs 每次临时检索
