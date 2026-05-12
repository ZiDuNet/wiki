---
tags: [Hermes, Agent, Claude, RAG, API, OpenAI]
source: "专业造轮子"
created: 2026-04-29
updated: 2026-05-10
category: Hermes
---

# ：当 OpenViking 遇上 GitNexus

> 来源: [专业造轮子](https://mp.weixin.qq.com/s?__biz=MzI0OTg0NTk0MA==&mid=2247484196&idx=1&sn=6839ef89d40fb09e25737529e8f6e220&chksm=e8645de8a331d4caeb017efa5250d4171f4295eac4f809452a27e04292ec99314f9d9eca914c&mpshare=1&scene=1&srcid=04294ZmjLtkzvilIPrITUp72&sharer_shareinfo=6f64a6a257359174d98b2440f2ff36d4&sharer_shareinfo_first=6f64a6a257359174d98b2440f2ff36d4) | 2026-04-29

## 摘要

长期以来，我们团队对 Hermes Agent 的培养思路一直很"卷"——喂更多的数据，挂更大的向量库，调更细的检索参数。
效果确实有。Hermes 成了团队里最博闻强识的"书呆子"：你问它三年前的接口设计、上个月的线上故障复盘、甚至某个冷门库的坑，它都能翻出来。
但用久了，一种微妙的无力感开始蔓延——它懂知识，却不懂"架构"；它记得代码，却不懂"因果"。
直到我们接入了 GitNexus。那不是简单的记忆扩容，而是维度的跃迁。
如果 Hermes 是一个人，OpenViking 就是它的海马体，负责陈述性记忆。
它记得什么？代码片段、API 文档、历史对话、Stack Overflow 的最佳实践……所有以文本形式存在的东西，OpenViking 都能存、能找。
它的工作原理是经典的 RAG：把文本切成块，扔进向量数据库，提问时做相似度检索，把最相关的上下文塞给大模型。
这套流程很成熟，也很靠谱——直到你问它"改了这个函数，谁会挂？"
它沉默了。不是因为它不知道这个函数在哪儿，而是它压根不知道这个函数和谁有关系。
OpenViking 的底层逻辑是"找相似的文本"，不是"找有依赖的代...

## 相关实体

[[Claude]], [[GPT5]], [[Hermes]]

## 相关概念

[[AI-Agent]], [[嵌入向量]], [[知识图谱]]
