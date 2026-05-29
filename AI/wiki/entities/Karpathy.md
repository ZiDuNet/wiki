---
type: entity
tags: [AI大神, LLM-Wiki, OpenAI]
sources: [通过飞书妙搭构建LLMWiki应用的实战指南.md, karpathy-llm-wiki-context-memory重构企业级的组织记忆.md, Karpathy的LLM Wiki思路我用Hermes跑通了.md]
created: 2026-05-26
updated: 2026-05-29
---

# Karpathy

**类型:** 实体 (人物)
**身份:** AI 大神、OpenAI 创始成员、前 Tesla AI 负责人

## 简介

Karpathy 是 AI 领域知名人物，提出 LLM Wiki 知识管理模式，强调让 LLM 维护结构化 Wiki 而非每次检索。2026 年 4 月在 GitHub 上发布不到 500 行的 Markdown 文件，48 小时内席卷整个 AI 社区。

## LLM Wiki 核心理念

三层架构：`Raw Sources → Wiki → Schema`

核心观点：
- Wiki 是活的、累积的、自我更新的
- 知识不是"存起来备查"，而是"编译进去活起来"
- 每次查询都"增加"而非"消耗"知识
- 新文档进来 → LLM 读取 → 提取关键信息 → 增量写入 Wiki 页面
- 回答时，LLM 回答的是已经被整理过的知识，而不是原始碎片

## 三项核心操作

| 操作 | 说明 |
|-----|------|
| Ingest | 知识的编译——将源文件"编译"成 Wiki 页面 |
| Query | 知识的查询——综合分析与引用，沉淀有价值回答 |
| Lint | 知识的维护——定期健康检查，确保 Wiki 不会"腐烂" |

## 企业级组织记忆

Karpathy 模式解决了知识维护成本问题：
- LLM 不会厌倦、不会忘记更新交叉引用
- 一次能处理 15 个文件
- 知识不再是一次性的消耗品，而是可以被编译、累积、复合的资产

## 原文链接

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 相关概念

- [[LLM-Wiki]] — Karpathy 提出的知识管理模式
- [[企业级组织记忆]]
- [[知识编译]]
- [[四信号知识图谱]]

## 来源文章

- [[通过飞书妙搭构建LLMWiki应用的实战指南]]
- [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]]
- [[karpathy的llm-wiki思路我用hermes跑通了]]

## GitNexus 代码仓库知识图谱

Karpathy LLM Wiki 思路被 GitNexus 搬进代码仓库：
- 把 agent 的上下文入口从"文件内容"往前挪到"仓库结构"
- 代码规模进入多模块、多服务时，结构化代码记忆成为基础设施
- AI 编程下一步缺的不是更会聊天的助手，而是更少迷路的助手

## 来源文章

- [[通过飞书妙搭构建LLMWiki应用的实战指南]]
- [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]]
- [[karpathy的llm-wiki被搬进代码仓库]]