---
tags: [Hermes, Agent, GitHub, Obsidian, RAG, API, OpenAI, Skill]
source: "智客随笔"
created: 2026-04-25
updated: 2026-05-10
category: Hermes
---

# 用好 Hermes 的这个技能，让你的 Agent 越用越聪明，Token 成本暴降 90%

> 来源: [智客随笔](https://mp.weixin.qq.com/s?__biz=MjM5MjA2MDQxMg==&mid=2448720300&idx=1&sn=3c59598bcfbcf16869e88d5cbf5b675f&chksm=b3570549009caa6bbfc4fb87c7714c609c8f5a61b3253acef4aa14f0c88be1e88e3dfc3e5f10&mpshare=1&scene=1&srcid=04257QaofK5I2a9i1zUUfTBV&sharer_shareinfo=815101224c529d6a18e2b0ea4175f152&sharer_shareinfo_first=815101224c529d6a18e2b0ea4175f152) | 2026-04-25

## 摘要

最近大家都在折腾给 LLM （大模型）挂“外挂大脑”。
最典型的用法就是 RAG （检索增强生成）：你把几百页的 PDF 、文档扔给 AI ，然后问它问题。 AI 去文档里找相关的段落，再回答你。
**这个思路是对的**。 它解决了“上下文太长”的问题。
但作为一个常年跟知识库死磕的博主，我得泼一盆冷水：
**传统的 RAG 方案，依然只是个“物理搬运工”。它只是在“省着用”，并没有真正“存下来”**。
每次你问问题， AI 都要重新把那几千字的原文片段读一遍。它就像一条只有 7 秒记忆的金鱼，永远在重复劳动。
今天我要讲一套真正的**降维打击**方案——**LLM Wiki （编译型知识库）**。
它不仅能把 Token 消耗砍掉 90%，还能让你的知识库像生物神经网一样，越用越聪明。
先给不熟悉原理的朋友补个课，现在大多数人的做法通常是这样的：
假设你要调研一个项目，手头有 50 页的 PDF 、 3 篇公众号长文、 2 个 Github Readme ，加起来大概 **3 万字**。
你把这 3 万字一股脑塞进对话框（或者扔进知识库），然后开始提问：
•“这个项目的技术栈是什么？...

## 相关实体

[[ChatGPT]], [[Hermes]], [[Markdown]], [[Obsidian]]

## 相关概念

[[RAG]]
