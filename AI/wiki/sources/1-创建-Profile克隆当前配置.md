---
tags: [Hermes, Agent, GitHub, API, Skill]
source: "极客BIM设计工坊"
created: 2026-05-03
updated: 2026-05-10
category: Hermes
---

# 1. 创建 Profile（克隆当前配置）

> 来源: [极客BIM设计工坊](https://mp.weixin.qq.com/s?__biz=MzI2MjA3ODk0OQ==&mid=2648116573&idx=1&sn=804498068a6945746a9639fea018a01f&chksm=f3d635e9e276c94431408a91d73b6e57b0f72e79ca701f0c1af31ffeb913fe19ce9ccdeb7aca&mpshare=1&scene=1&srcid=0503XKDsG8iNtKeA0FZZ3RCr&sharer_shareinfo=e141e35dec7079bbbc418afb0e396d14&sharer_shareinfo_first=e141e35dec7079bbbc418afb0e396d14) | 2026-05-03

## 摘要

Hermes Agent · 2026年5月
KEY TAKEAWAY
多 Bot 的核心不是"怎么建"，而是"为什么建"和"怎么分"。理解 Profile 隔离机制，掌握角色设计思路，比照着教程敲命令重要得多。
1
核心机制
3
设计原则
4
角色模板
为什么要读这篇文章
网上有很多 Hermes 多 Bot 教程，手把手教你敲命令。但大多数教程有一个问题：只告诉你"怎么做"，不告诉你"为什么这么做"。
结果就是，你照着教程建了四个 Bot，但不知道该怎么分配角色，不知道什么场景该用什么 Bot，最后四个 Bot 变成了四个长得一样的复制品。
这篇文章不讲具体步骤（步骤看官方文档就行），讲的是方法和理念。理解了这些，你自然知道该怎么建。
一个 Bot 的问题
一个 Hermes Bot 能干所有事，但干不好。原因很简单：
●　**模型冲突**　日常聊天用便宜模型够了，写代码要用贵的，算命要用中文好的。一个 Bot 只能绑一个模型。
●　**人设分裂**　SOUL.md 定义了 Bot 的人格。你让它既当严肃的代码工程师，又当深夜聊天伙伴，它会精神分裂。
●　**记忆污染**　所有对话...

## 相关实体

[[Hermes-Agent]]

## 相关概念

[[Profile系统]]
[[Agent路由]]
[[记忆系统]]
