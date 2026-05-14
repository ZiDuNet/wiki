---
tags: [Obsidian, 知识库, Karpathy, LLM Wiki, AI知识管理, 第二大脑]
source: "ferlich"
created: 2026-05-15
updated: 2026-05-15
category: Obsidian
---

# Claude Code + Obsidian：个人知识库从工具到思维的完整指南

> 来源: [ferlich](https://mp.weixin.qq.com/s?__biz=MzYyNTQ0MTgwMQ==&mid=2247484219&idx=1&sn=eb378ad0a10afdf35f3310ccb8fb034e&chksm=f1c050ed97777e71b6d84b72590a0d802f163df2b04a42ad04f7b79c98b7eca051d9dc95bb02&mpshare=1&scene=1&srcid=05153hUVZCc2cGidsq58pF8Z&sharer_shareinfo=8b7b7620e70ada06999e9ba17817ff33&sharer_shareinfo_first=8b7b7620e70ada06999e9ba17817ff33) | 2026-05-15

## 摘要

文章介绍 Karpathy 分享的个人知识库方法：三层架构（raw/wiki/schema），让 AI 维护一个持续生长的 Wiki，从"每次从零开始"变为"知识持续积累复利"。从工具层面和思维层面两个维度详细阐述如何搭建真正的第二大脑。

## 为什么这套方法火了？

传统 RAG 的问题：对话一关，一切归零。下次再问，AI 从头开始分析，不记得上次聊过什么。

Karpathy 的思路：让 AI 维护一个持续生长的 Wiki，像代码仓库一样，知识编译一次，持续维护，不断复利。

## 三层架构

### 最底层：raw（只读证据层）
- 你读过的文章、论文、截图，原封不动扔进去
- AI 只读不改

### 中间层：wiki（LLM 工作区）
- AI 自动生成的 Markdown 文件
- 每个概念、每个人物、每个工具，都有独立页面
- 页面之间互相链接

### 最上层：schema（操作契约）
- 纯文本文件，告诉 AI 知识库的规则是什么

## AI 的三件事

1. **消化**：新文章来了，AI 读一遍，提取关键信息，更新相关页面，建立交叉引用
2. **查询**：你提问，AI 在 wiki 里搜索，综合出带引用的答案，好的答案直接写回 wiki
3. **检查**：定期扫描，找矛盾、找孤立页面、找过期内容

## 思维层面

大多数模仿者只学到皮毛——他们只是把笔记软件换成了 Obsidian，但思维模式没变。

真正的关键：
- 不是什么都让 AI 记，而是什么都思考
- 知识库是思考的延伸，不是思考的替代
- 先有框架再有内容，而不是堆积内容等框架自动出现
