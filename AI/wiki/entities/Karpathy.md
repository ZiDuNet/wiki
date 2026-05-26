---
type: entity
tags: [AI大神, LLM-Wiki, OpenAI]
sources: [通过飞书妙搭构建LLMWiki应用的实战指南.md]
created: 2026-05-26
updated: 2026-05-26
---

# Karpathy

**类型:** 实体 (人物)
**身份:** AI 大神、OpenAI 创始成员、前 Tesla AI 负责人

## 简介

Karpathy 是 AI 领域知名人物，提出 LLM Wiki 知识管理模式，强调让 LLM 维护结构化 Wiki 而非每次检索。

## LLM Wiki 思路

三层架构：`Raw Sources → Wiki → Schema`

核心观点：
- Wiki 是活的、累积的、自我更新的
- 新文档进来 → LLM 读取 → 提取关键信息 → 增量写入 Wiki 页面
- 回答时，LLM 回答的是已经被整理过的知识，而不是原始碎片

## 原文链接

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 相关概念

- [[LLM-Wiki]] — Karpathy 提出的知识管理模式

## 来源文章

- [[通过飞书妙搭构建LLMWiki应用的实战指南]]