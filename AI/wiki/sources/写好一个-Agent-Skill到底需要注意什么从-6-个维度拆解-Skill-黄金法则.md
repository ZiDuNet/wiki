---
tags: [Agent, Prompt, API, Python, Skill]
source: "Skill-is-all-you-need"
created: 2026-04-26
updated: 2026-05-10
category: Agent
---

# 写好一个 Agent Skill，到底需要注意什么？从 6 个维度拆解 Skill 黄金法则

> 来源: [Skill-is-all-you-need](https://mp.weixin.qq.com/s?__biz=Mzg2OTczMDIxOA==&mid=2247483696&idx=1&sn=949d16b0e4c36a6da6106fa50d99e880&chksm=cfc9ab3d1cee501adc21c7f7ac6a94cbc865c6e4b3f396f69f440e35ac7ee6dffbcab97474b1&mpshare=1&scene=1&srcid=0426sg77Vwu6npVHJUJA3ITX&sharer_shareinfo=8a2405eca74a09aa9fbb3aa9e9c783de&sharer_shareinfo_first=8a2405eca74a09aa9fbb3aa9e9c783de) | 2026-04-26

## 摘要

为什么你的 Skill 写了等于没写？
AI 还是乱猜、还是踩坑、还是每次都要你重新教？
问题不在 AI，在你的 Skill 写法。
我见过很多 Skill，写法基本是这个套路：
`---
name: code-review
description: 代码审查
请帮我审查代码，找出bug，给出修改建议。
`
看起来没毛病，对吧？
但你用起来就会发现：
· AI 经常想不起来用这个 Skill——因为 description 太模糊
· 用了之后输出也不稳定——因为指令就一句话，AI 全靠猜
· 每次还要你手动补充"重点看安全漏洞""用中文回复""输出要用表格"——因为该写的东西都没写
**写 Skill 不是写 Prompt。Prompt 是一次性的，Skill 是跨会话复用的操作手册。**
一次 Prompt 没写好，这次对话忍一忍就过去了。但 Skill 没写好，每次对话你都要重新教 AI 一遍——这比不用 Skill 还痛苦。
接下来，我从 6 个维度拆解：写好一个 Skill，到底需要注意什么。
每条法则，都会给你"反面写法"和"正面写法"的对比。读完就能直接上手改你自己的 S...

## 相关实体

[[Excel]], [[Python]], [[微信]]

## 相关概念

[[代码审查]], [[自进化系统]]
