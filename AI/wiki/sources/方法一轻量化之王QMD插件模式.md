---
tags: [OpenClaw, Agent, RAG, Dify, API]
source: "克拉克说"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# 方法一：轻量化之王——QMD插件模式

> 来源: [克拉克说](https://mp.weixin.qq.com/s?__biz=MzI4MTAzOTQ5OQ==&mid=2648246501&idx=1&sn=4c80fdea0595b128a616e63da589835c&chksm=f25fa038bc02691e52ac3a611f5643de2856d58b1338daf49e27be66841e825af64a1b4a46d4&mpshare=1&scene=1&srcid=0420fxqFxKPZTO8Lg2kAylzQ&sharer_shareinfo=f67b22af82a02d24a5a1fe4841b5ad00&sharer_shareinfo_first=f67b22af82a02d24a5a1fe4841b5ad00) | 2026-04-20

## 摘要

随着 2026 年 3 月 22 日 OpenClaw V2026.3.22 版本的发布，小龙虾的服务框架正式进入了模块化时代。其实，相当于传统的Coze、ADP、Dify来对比，如何进一步让OpenClaw来创建、连接和使用本地/云端的RAG，成为小龙虾是否进一步用户的关键。今天，我试着对比分析基于 OpenClaw 加载本地知识库的三种主流方法，至于优劣，留给各位看官评说。
QMD （Quick Memory Database）是目前 OpenClaw 生态中最受欢迎的本地知识加载方式。它不要求你安装沉重的数据库软件，而是通过 WASM 技术直接在本地运行。它采用了“双重检索”机制：先用 BM25（关键词匹配） 抓准术语，再用 语义向量（Embedding） 理解语境。
1. 无需配置服务器，SDK 级集成，即插即用。端侧友好
2. 对于搜索特定的代码函数名或专业术语，关键词匹配比纯向量搜索更准。
3. 配合最新的 TurboQuant 压缩算法，即便在 16GB 内存的笔记本上也能流畅检索百万字文档。你还别说，Google的TurboQuant有点东西，读不懂，反正看起来很强大。...

## 相关实体

[[OpenClaw]]

## 相关概念

[[嵌入向量]], [[知识图谱]]
