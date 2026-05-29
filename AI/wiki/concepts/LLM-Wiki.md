---
type: concept
name: LLM-Wiki
created: 2026-05-28
updated: 2026-05-29
tags: [知识管理, LLM, Karpathy, 知识编译, GitNexus]
sources: [Karpathy-知识库构建40-万词的-LLM-编译之道.md, karpathy-llm-wiki-context-memory重构企业级的组织记忆.md, karpathy的llm-wiki被搬进代码仓库.md]
---

# LLM-Wiki

**类型:** 概念

## 定义

Karpathy 提出的知识管理方法论：用 LLM 编译知识而非手动编辑 wiki。每次查询都「增加」知识库，知识是活的数据。

## 核心理念

**颠覆性命题**：知识不是"存起来备查"，而是"编译进去活起来"。

- 你不编辑 wiki，LLM 编辑
- 每次查询都「增加」而非「消耗」
- 知识是活的数据，不是死的文档
- ~40 万词规模不需要 RAG

## 三层架构

| 层级 | 说明 | 特点 |
|-----|------|------|
| Raw Sources 源文件层 | PDF、论文、文章、播客笔记、会议记录 | 不可变，LLM 只读取不修改 |
| The Wiki Wiki层 | 摘要页、概念页、实体页、对比分析 | LLM 维护，你读它，LLM 写它 |
| The Schema 规范层 | CLAUDE.md / AGENTS.md | 定义 Wiki 结构、操作流程、格式约定 |

## 三项核心操作

| 操作 | 说明 |
|-----|------|
| Ingest | 知识的编译——将源文件"编译"成 Wiki 页面 |
| Query | 知识的查询——综合分析与引用，沉淀有价值回答 |
| Lint | 知识的维护——定期健康检查 |

## LLM 编译六件事

1. 读取 raw/ 目录
2. 生成摘要
3. 分类整理
4. 生成概念文章
5. 创建索引
6. 添加反向链接

## 增长机制

输出结果归档回 wiki，每次查询都增加知识。Linting 保持健康。

## 为什么传统 RAG 正在失效

传统 RAG 的致命缺陷：**每次查询都是一次"重新发现"**。

Karpathy 所说的 **"rediscovering knowledge from scratch on every question"**——每次都在重新发明轮子。

LLM Wiki 的解法：知识是累积的，不是消耗的。

## 企业级扩展

| 层级 | 特点 | 工具 |
|-----|------|------|
| 个人 | 快速迭代，自主决策 | Obsidian + Claude Code |
| 小团队 | 共享源文件，分工维护 | Obsidian Git 同步 + MCP |
| 部门 | 统一 Schema，权限控制 | Notion + Claude API |
| 企业 | 多语言支持，大规模检索 | 定制 RAG + Wiki 混合 |

## GitNexus 代码仓库知识图谱

Karpathy LLM Wiki 思路被 GitNexus 搬进代码仓库：

|| 对象 | Karpathy LLM Wiki | GitNexus |
|-----|-------------------|----------|
| 面向对象 | 论文、笔记、网页、材料 | 函数、类、依赖、调用链、执行流 |
| 机制 | 把知识沉淀成持续维护的 wiki | 把仓库沉淀成持续查询的结构图 |

共同点：把"临时上下文"变成"持久结构"。

核心观点：AI 编程下一步缺的不是更会聊天的助手，而是更少迷路的助手。

## 相关文章

- [[Karpathy-知识库构建40-万词的-LLM-编译之道]]
- [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]]
- [[karpathy的llm-wiki被搬进代码仓库]]

## 相关实体

- [[Karpathy]]
- [[Obsidian]]
- [[Claude]]
- [[GitNexus]]

## 相关概念

- [[知识编译]]
- [[企业级组织记忆]]
- [[四信号知识图谱]]
- [[传统RAG困境]]
- [[raw目录结构]]
- [[代码仓库知识图谱]]