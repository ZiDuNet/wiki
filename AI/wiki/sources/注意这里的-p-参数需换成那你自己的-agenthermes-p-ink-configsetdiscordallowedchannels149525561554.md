---
tags: [Hermes, Agent, Obsidian, 飞书, Prompt, API, Skill, OpenClaw]
source: "林月半子的AI笔记"
created: 2026-04-23
updated: 2026-05-10
category: Hermes
---

# 注意这里的 -p 参数，需换成那你自己的 agenthermes -p ink config set discord.allowedchannels "1495255615545544819"

> 来源: [林月半子的AI笔记](https://mp.weixin.qq.com/s?__biz=MzU4MjY5NTc4OQ==&mid=2247499297&idx=1&sn=7db7f2f709e45d71545c76ad93e28b38&chksm=fc32c0433ee54813a5a68a383c6117c18a913f91b2e2d64e8f9d2da2a5f7061cb2c3a03c9dcc&mpshare=1&scene=1&srcid=0423UiMiA6uNCctGofuIObd1&sharer_shareinfo=ccb8f289f5a5176d41568414e30d20ba&sharer_shareinfo_first=ccb8f289f5a5176d41568414e30d20ba) | 2026-04-23

## 摘要

关注 「**林月半子的AI笔记**」，设为「**星标**」
我是林月半子，教你用AI干掉90%的重复劳动**！**
当 Hermes 出来的时候，好多人问我多 Agent 之间的协作是怎么玩的。
周末我找了时间自己做了一把实践，原本以为会很顺利，没想到中间翻了好几次车，最后硬是一个坑一个坑填过来的。这篇把完整过程记下来，跟着做，你也能在自己的 Discord 里，看到几个 AI 像同事一样互相接力干活。
但在动手之前，有句话得先讲在前头。协作是能力的放大器，不是补丁。如果单个 Agent 本身是个废柴，拉三个废柴来协作，结果就是三倍的废柴，三个废柴开会，废柴还是废柴。SOUL.md 写细、skills 配齐、模型选对，把 Agent调教好，这是多 Agent 能跑的前提，不是结果。
好，话撂这儿了，开始正题。
要做 Agent 协作，第一步得先把不同的 Agent 建出来。在 Hermes 里，这件事是通过 Profile 来实现的。
profile 其实就是 Hermes 的人格档案。一个 profile 就是一个完全独立的 AI 分身，有自己的 config.yaml、.env、S...

## 相关实体

[[Hermes]], [[Markdown]], [[Obsidian]], [[OpenClaw]], [[飞书]]

## 相关概念

[[AI-Agent]], [[Multi-Agent]], [[知识管理]]
