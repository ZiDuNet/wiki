---
tags: [Harness, Agent, Claude, GitHub, Prompt, Skill]
source: "程序员的鱼缸"
created: 2026-04-29
updated: 2026-05-10
category: Harness
---

# 厌烦了理论，给你Harness真正的工程实践

> 来源: [程序员的鱼缸](https://mp.weixin.qq.com/s?__biz=MzAwNjYwMzY1OQ==&mid=2247483973&idx=1&sn=6903aca768a958842994cd07af533e8f&chksm=9acc7d46f4f5c38999875c566f6304f5be3646e99a25cd3ae4f76008fd5b972d5e40f67cb879&mpshare=1&scene=1&srcid=0429zrTmlolwxrHpg62Lbv1l&sharer_shareinfo=990955a79969c689011f0994f8932806&sharer_shareinfo_first=990955a79969c689011f0994f8932806) | 2026-04-29

## 摘要

Harness被说的太多，但是绕来绕去都是那几篇文章中介绍的理论。我不知道其他人看起来感觉如何，反正我是看了半天也不知道他们说的啥。
所以，talking is cheap, show me the prompt。
接下来用实践介绍Harness到底是如何应用的。
开始之前，仍然要重申Harness四大支柱。
上下文架构(Context Architecture):
上下文需要根据当前Agent的需要去披露，而不是在最开始一股脑的就全扔给他。还记得之前的Skill“渐进式披露”的概念吗。对，就是要构建一个上下文的架构出来，让agent在不同的时候能拿到指定的上下文。
这也就引出了下一个支柱。
Agent专业化(Agent Specialization)
用专门的Agent去执行专业领域的任务。比如搜索、测试、review等行为，通过system prompt，指定的工具集，只属于自己的context等来执行自己的任务。
持久化记忆(Persistent Memory)
对于任务进度、任务执行图等信息，将它们存储在外部存储里面，而不是塞到上下文。这样不管是特意或者被迫的重新开始会话，我们...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]]

## 相关概念


