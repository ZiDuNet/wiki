---
tags: [Harness, Agent, Claude, MCP, Prompt, API, Skill]
source: "技术极简主义"
created: 2026-04-22
updated: 2026-05-10
category: Harness
---

# 一文看懂 Harness engineering：智能体时代的 AI 编程驾驭之道

> 来源: [技术极简主义](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ==&mid=2247486854&idx=1&sn=2c5abf99e3cff4a8cb4169e01967ef2a&chksm=a736007f223b13248674797571b82e2d57463d0af7e5bf40eba460a9c16f608fa99428a2fd52&mpshare=1&scene=1&srcid=0422L0hMSG6GwkHPum2PTaX1&sharer_shareinfo=58693e3655f2580657a4b17355d5d935&sharer_shareinfo_first=58693e3655f2580657a4b17355d5d935) | 2026-04-22

## 摘要

最近常常听到一个声音，Prompt 工程过时了，Context 工程过时了，现在只要学好 Harness 工程就够了。短短一个月，**Harness Engineering** 从一篇博客文章变成了开发者社区的高频词。
在 AI 智能体编程领域，决定结果好坏的最大变量，往往不是模型有多聪明，而是模型之外那一整套状态、工具、环境、反馈回路与约束系统。如果 AI 将成为软件开发流程中的长期参与者，那么软件工程系统本身也需要进化。
LangChain 作者 **Vivek Trivedy** 这篇《The Anatomy of an Agent Harness[1]》试图回答一个越来越关键，但行业内经常被说得很模糊的词：**Harness**。
**Agent = Model + Harness**
**如果你不是模型，那就是 Harness。**
这句话听起来有点绝对，但确实抓住了关键。Harness 本质上就是模型之外的一切：代码、配置，以及各种执行逻辑。模型本身只是能力的来源，只有通过 Harness 把状态、工具调用、反馈循环和约束机制串起来，它才真正变成一个 Agent。
具体来看...

## 相关实体

[[Claude-Code]], [[Claude]], [[Harness]], [[LangChain]], [[MCP]]

## 相关概念


