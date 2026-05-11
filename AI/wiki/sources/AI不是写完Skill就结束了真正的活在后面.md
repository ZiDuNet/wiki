---
tags: [Skills, Harness, Prompt, API, OpenAI, Skill]
source: "金技局"
created: 2026-05-05
updated: 2026-05-10
category: Skills
---

# AI不是写完Skill就结束了，真正的活在后面

> 来源: [金技局](https://mp.weixin.qq.com/s?__biz=MzE5ODU0NjU0Mg==&mid=2247484776&idx=1&sn=062e03b77a5cb31bafb52bb024ed4b63&chksm=97c999a5e54fc60a4eca099552961317e391fa303528aef013131b6d82f8b0b7d310889cfbbe&mpshare=1&scene=1&srcid=0505f4x44DzWR0hVMJbyqtNF&sharer_shareinfo=30a97d553069e56a329f37a60fd2569f&sharer_shareinfo_first=30a97d553069e56a329f37a60fd2569f) | 2026-05-05

## 摘要

我第一版Skill写出来的时候，觉得效果不错。结构清楚，风格对味，跑通了几个测试case。于是交给同事用。
反馈来了："我输入的格式稍微不一样，它就开始编东西了。"
又过了两天，另一个反馈："它有时候会跳过中间的分析步骤，直接给一个最终结果，看起来像那么回事但经不起推敲。"
那一刻我意识到一个道理：让AI做对一次不难，让它在任何人手里、任何输入条件下都不出大错，才是真正的工程。
这两件事之间的距离，比我以为的大得多。局长开始花时间去填这个gap，过程中踩了很多坑，也慢慢摸索出了一些方法。现在回头看，我觉得这套方法有一个更准确的名字，就是Harness Engineering。
先说说"写好一个Prompt"和"做好一个Skill"之间的区别。
Prompt解决的是单次交互的问题。你描述清楚意图，AI给你一个不错的输出。这件事依赖的是你当下表达得够不够好，以及模型当下状态够不够聪明。它是一次性的、即兴的。
Skill要解决的是完全不同的问题：在你不在场的情况下，在别人使用的情况下，在输入千奇百怪的情况下，AI依然能给出稳定的、符合标准的输出。
这两者之间的差距，和写一段能跑的demo与写...

## 相关实体

[[OpenAI]]

## 相关概念

[[代码生成]], [[自动化测试]]
