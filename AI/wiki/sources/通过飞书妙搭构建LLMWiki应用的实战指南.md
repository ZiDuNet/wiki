---
tags: [LLM-Wiki, 飞书, RAG, 知识管理]
sources: [通过飞书妙搭构建LLMWiki应用的实战指南.md]
created: 2026-05-26
updated: 2026-05-26
---

# 通过飞书妙搭构建LLMWiki应用的实战指南

**来源：** 飞书/光之余影
**摄入日期：** 2026-05-26
**类型：** 实战指南

## 摘要

本文探讨用飞书妙搭实现 Karpathy 的 LLM Wiki 思路，指出传统 RAG 系统的核心问题——每次回答都从零理解材料，没有积累。LLM Wiki 模式让 LLM 提前维护结构化 Wiki，新文档进来 → 提取关键信息 → 增量写入 Wiki 页面 → 更新交叉引用 → 标注矛盾点。飞书妙搭因文档天然在飞书、用户无学习成本、核心价值是界面和流程而成为理想承载工具。

## 核心观点

- **传统 RAG 的困境**：每次回答 LLM 都从零理解材料，没有记忆积累；问综合问题需每次重新检索拼接
- **Karpathy LLM Wiki 思路**：三层架构 `Raw Sources → Wiki → Schema`，Wiki 是活的、累积的、自我更新的
- **飞书妙搭三大优势**：源文档天然在飞书、用户无新工具学习成本、LLM Wiki 核心价值是界面和流程而非底层 Infra
- **最小可行路径**：定义 Wiki 结构（高频问题→第一批页面）→ 妙搭建对话入口 → 建立积累机制（log.md）

## 提及实体

- [[Karpathy]] — 提出 LLM Wiki 模式的 AI 大神，GitHub Gist 分享思路
- [[飞书妙搭]] — 飞书的对话式应用搭建平台，适合承载 LLM Wiki

## 涉及概念

- [[LLM-Wiki]] — Karpathy 提出的知识管理模式，让 LLM 维护结构化 Wiki 而非每次检索
- [[传统RAG困境]] — 每次回答从零理解，没有积累，缺乏文档间关系的真正理解
- [[三层架构]] — Raw Sources → Wiki → Schema 的知识管理架构
- [[Wiki自更新机制]] — 新文档进来自动增量写入、更新引用、标注矛盾

## 相关链接

- Karpathy LLM Wiki 原文: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f