---
title: AI 知识库技术演进拆解：从 RAG 到 NotebookLM，再到 LLM Wiki
type: source-summary
tags: [RAG, NotebookLM, LLM-Wiki, 知识库, Karpathy]
sources: [AI 知识库技术演进拆解：从 RAG 到 NotebookLM，再到 LLM Wiki.md]
created: 2026-05-22
updated: 2026-05-22
---

# AI 知识库技术演进拆解：从 RAG 到 NotebookLM，再到 LLM Wiki

> 📎 来源: [叶小钗](https://mp.weixin.qq.com/s?__biz=Mzg2MzcyODQ5MQ==&mid=2247501348&idx=1&sn=5b3ac13a979275591a0a5c3aa84e537b) | 时间: 2026-05-22

## 核心观点

文章系统拆解了 AI 知识库技术的三个演进阶段：
1. **低配 RAG** — 资料切块 → 向量化 → 检索 → 回答
2. **NotebookLM 类产品化 RAG** — 文档理解 → 多索引 → Retrieval and Ranking → Context Engineering → Source Grounding
3. **LLM Wiki / 深度知识库** — 知识抽取 → 实体识别 → 主题页生成 → 关系链接 → 持续演化

---

## NotebookLM 技术架构七层拆解

### 一、Source 接入

**核心产品抽象：** 把资料当成可以被引用和追溯的事实来源，而非临时上下文。

```
Notebook
├── Sources：用户上传的资料
├── Notes：用户笔记
├── Conversations：历史对话
├── Indexes：索引系统
└── Settings：Notebook 配置
```

### 二、文档理解

**关键难点：** 不只是 PDF 转文本，而是**恢复结构**。

```
原始文件
    ↓文本抽取
    ↓版面分析
    ↓标题层级识别
    ↓表格/图片/图注处理
    ↓章节树构建
    ↓元数据绑定
```

> 文档理解是整个 RAG 产品里最难的一层。很多企业知识库一开始 demo 看起来还行，但一进入真实资料就崩。

### 三、Chunk 多粒度

系统维护多种粒度索引：

```
Source 级别
Chapter 级别
Section 级别
Paragraph 级别
Chunk 级别
Sentence 级别
```

**核心原则：** chunk 不能和原文结构脱钩，每个 chunk 必须知道：
- 它来自哪个 source
- 属于哪个章节
- 前后文是什么
- 页码是多少
- 原文位置在哪里

### 四、索引系统

混合索引策略：

```
Vector Index → 处理语义相似
Keyword/BM25 Index → 处理关键词精确匹配
Metadata Index → 处理来源、时间、类型、作者过滤
Document Tree Index → 处理章节层级和上下文扩展
Citation Index → 处理引用回溯
Conversation/Note Index → 处理用户笔记和历史对话
```

### 五、Retrieval and Ranking

**Query Plan 机制：** 先做问题理解，生成查询计划，再做多路召回。

```
用户问题 → Query Plan → 多路召回 → 去重 → 排序
```

排序因素：
- 是否来自可信 source
- 是否覆盖多个 source
- 是否有足够上下文
- 是否和问题意图匹配

### 六、Context Engineering

**Context Package 组成：**
- 用户问题 + 问题意图
- 候选证据 + 证据所属 source
- 章节上下文 + 前后文扩展
- 多份资料摘要
- 历史对话 + 用户笔记
- 引用映射 + 回答约束

### 七、答案生成

**生成规则：**
- 只基于资料回答
- 资料不足时保守回答
- 回答中关键结论要能绑定证据
- 不同 source 有冲突时要指出冲突

---

## Karpathy LLM Wiki 的核心理念

**对比 NotebookLM：**

| NotebookLM | LLM Wiki |
|------------|----------|
| 查询时拼答案 | 提前编译知识结构 |
| 每次重新综合 | 持续沉淀实体页、主题页 |
| 临时性问答 | 增量维护 Wiki |

> 传统 RAG / NotebookLM 是「上传资料 → 查询时召回相关片段 → 临时综合回答」，但每次问问题，模型都在重新从碎片里现拼答案，知识没有持续沉淀。

---

## 技术演进路径总结

```
低配 RAG（底座）
    ↓ NotebookLM 把这个底座产品化、自动化、可信化
    ↓ LLM Wiki 进一步把知识结构沉淀为长期资产
```

**三个阶段是逐层叠加：**
1. 低配 RAG 解决「资料如何被召回？」
2. NotebookLM 解决「资料如何被可信地问答和研究？」
3. LLM Wiki 解决「资料如何被持续沉淀成结构化知识？」

---

## 关键洞察

### 文档理解是上限决定层

> 如果文档理解做得不好，后面就会进入一种很尴尬的状态：垃圾解析 → 垃圾切块 → 垃圾向量化 → 垃圾召回 → 模型一本正经地基于垃圾回答

**Google 的优势：** 本来就是搜索、OCR、文档解析、网页理解、多模态理解领域最强的公司之一。

### 高阶 RAG 不能只有向量库

关键词索引在以下场景更稳定：
- 某个专有名词
- 某个产品名
- 某个公式
- 某个引用页码
- 某个明确标题

---

## 相关实体与概念

- [[NotebookLM]] — Google 的 AI 笔记与研究助手
- [[LLM Wiki]] — Karpathy 提出的知识管理理念
- [[RAG]] — 检索增强生成
- [[Karpathy]] — OpenAI 前研究员，提出 LLM Wiki 概念
- [[知识库]] — AI 时代的核心工具
- [[文档理解]] — RAG 产品最难的一层
- [[Context Engineering]] — 上下文工程

---

## 参考链接

- GitHub Gist: Karpathy《LLM Wiki》(2026-04-04)
- Google NotebookLM 官方博客（2025-10）Retrieval and Ranking 披露