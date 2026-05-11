---
tags: [OpenClaw, Agent, Claude, MCP, 飞书, Harness, Prompt, Skill]
source: "歪斯Wise"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# 深度解析三大 Agent 上下文工程：Claude Code、OpenClaw、Hermes 的设计哲学

> 来源: [歪斯Wise](https://mp.weixin.qq.com/s?__biz=MzI4MTA0NzkxMA==&mid=2648896698&idx=1&sn=966f92bb4fa66268fc15cb82cc2a7fb3&chksm=f204f3b54151a383bfc549fc4a0e58c180948976028fb5ef4019871c26233cf5869662cdd8ea&mpshare=1&scene=1&srcid=0423RuFHNSrowSQClK50RH7j&sharer_shareinfo=2e047bb27307ad1503e39ccff702e58c&sharer_shareinfo_first=2e047bb27307ad1503e39ccff702e58c) | 2026-04-23

## 摘要

**⭐️ 关注星标，收看AI实战**
Hermes最近成为了新的热点，除了自我进化机制，更值得注意的是它在上下文管理上做了不少激进设计，比如更早触发压缩、把摘要做成交接文档。
上周写了一篇文章[为什么你的Openclaw龙虾总是智障，ClaudeCode源码泄露揭露：Agent 的差距不在模型，在 Harness Engineering](https://mp.weixin.qq.com/s?__biz=MzI4MTA0NzkxMA==&mid=2648896646&idx=1&sn=911038b1f648dc97d0a821c557a50151&scene=21#wechat_redirect)阐述了Claude Code和Openclaw的Harness机制，能够让AI运行得更加稳定、完善。
在Harness之前，更底层的则是上下文工程，很多时候，模型的幻觉、失忆是因为上下文窗口乱了，如果我们把所有的事情“平权”的放在上下文里，就像大海捞针，模型会很难找到自己想要的东西。
那我们要怎么设计AI产品的上下文呢？
Claude Code 把上下文做成了渐进式调度，OpenClaw 则...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Harness]], [[Hermes]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念

[[Prompt工程]], [[上下文工程]]
