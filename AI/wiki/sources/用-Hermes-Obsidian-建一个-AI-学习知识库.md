---
tags: [Obsidian, Agent, RAG, OpenAI, Skill]
source: "亲爱的缪斯"
created: 2026-04-30
updated: 2026-05-10
category: Obsidian
---

# 用 Hermes + Obsidian 建一个 AI 学习知识库

> 来源: [亲爱的缪斯](https://mp.weixin.qq.com/s?__biz=Mzk4ODIzNzc4OQ==&mid=2247484731&idx=1&sn=cf7dfd9ec049ac29d481c343b17d025d&chksm=c40ed7f82150186aebfb2c1e8b6b051c1c1a0e5d214c3e7676daea410350d4fc3ceb13420745&mpshare=1&scene=1&srcid=0430dtz2tLgoQxce3LFwahpi&sharer_shareinfo=d2b5a0b6e717d3bac3cd99c9c946be2f&sharer_shareinfo_first=d2b5a0b6e717d3bac3cd99c9c946be2f) | 2026-04-30

## 摘要

今天教大家如何在自己的本地电脑构建一个 Karpathy LLM Wiki。
先来了解一下什么是 LLM Wiki。
平时我们用 ChatGPT 或者 NotebookLM 查资料，每次问问题它都要重新从文档里找，找完回答，下次再问还是从头来，什么都没积累下来。
LLM Wiki 反过来：你把资料丢进去，LLM 先把它消化成结构化的页面，概念和概念之间互相链接，之后你问任何问题，它在这张已经整理好的网上找答案，不用每次重新发现。
Hermes Agent 把这个做成了内置 Skill，配合 Obsidian 用体验很好。下面说怎么搭。
**第一步：初始化知识库**
打开 Hermes，说：
它会在
下建好这个目录：
**第二步：用 Obsidian 打开同一个文件夹**
Obsidian → Open folder as vault → 选
三个设置：
- 附件目录改成
- Wikilinks 确认是开的（默认就开着）
- 装一个 Dataview 插件（社区插件里搜索安装）
Wiki 路径默认是
，不用配置直接能用。想换路径的话，在
加一行：
Obsidian 的 vault 指向同...

## 相关实体

[[ChatGPT]], [[Hermes]], [[Markdown]], [[Obsidian]]

## 相关概念


