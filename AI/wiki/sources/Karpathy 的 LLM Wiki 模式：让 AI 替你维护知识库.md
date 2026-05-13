---
tags: [LLM Wiki, Karpathy, 知识管理, RAG, 知识库]
source: "翊行代码"
created: 2026-05-13
updated: 2026-05-13
category: LLM Wiki
---

# Karpathy 的 LLM Wiki 模式：让 AI 替你维护知识库

> 来源: [翊行代码](https://mp.weixin.qq.com/s?__biz=MjM5NTQ3NDAwMw==&mid=2452918134&idx=1&sn=67cb0d1b1a742ebc9c2c106e8b29a703&chksm=b0f14eb17672240513ef569bb66f25c7d8cfe09bfcc435bdd500e9ad8bbe88d641481e1b4863) | 2026-05-13

## 摘要

Karpathy提出LLM Wiki模式，一种更适合个人知识管理的理念。与传统RAG每次问答时都要从零发现知识不同，LLM Wiki让AI增量维护一个持久化的Wiki——当添加新文档时，AI会阅读、提取关键信息、整合进现有Wiki、更新相关实体页面、标记矛盾之处。

LLM Wiki有三层架构：Raw Sources（原始文档，只读）、Wiki（LLM生成和维护的Markdown文件）、Schema（指令文件）。三个核心操作：Ingest（摄入新文档）、Query（向Wiki提问）、Lint（健康检查）。核心洞察：人类放弃Wiki是因为维护成本增长比价值快，而LLM不厌倦bookkeeping工作，可以轻松一次改15个文件。