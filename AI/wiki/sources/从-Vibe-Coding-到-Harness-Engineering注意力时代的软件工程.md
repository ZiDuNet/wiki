---
tags: [Vibe Coding, Agent, Harness, Prompt, OpenAI]
source: "愣虾说"
created: 2026-04-29
updated: 2026-05-10
category: Vibe Coding
---

# 从 Vibe Coding 到 Harness Engineering：注意力时代的软件工程

> 来源: [愣虾说](https://mp.weixin.qq.com/s?__biz=MzU4NjU3NjY3MQ==&mid=2247483939&idx=1&sn=6924a6f8724dcc18967b5bbb155f30e8&chksm=fcb83b3e34b23bd3f31f4e44a45e71c1fdae525aeed61d7e9cb5805b70894235de3c6e3c5cef&mpshare=1&scene=1&srcid=0429YCiCFB4O8d98GWq7Hftu&sharer_shareinfo=f2cb77d693c6ba6f7c2f5131cca381e9&sharer_shareinfo_first=f2cb77d693c6ba6f7c2f5131cca381e9) | 2026-04-29

## 摘要

这不是一篇理论文档，而是总结了我通过10天重构 Vibe Coding 产物的实践反思。
📌核心观点
当前大模型的输出，本质是在已有语料和上下文约束下的 概率最优产物 。它擅长生成「看起来像正确答案」的内容，但并不保证这些输出对你的业务目标、架构边界或长期可维护性是最优的。
📚 内容导览
- AI 给我们的答案，本质是概率的产物
- 1.1 为什么这么说
- 1.2 不加约束的 Vibe Coding，在复杂系统里会怎样
- 1.3 结论：没有约束，AI 只是「高性能技术债放大器」
- More Context, Less Control 让「上下文」成为工程底座
- 2.1 DDD：构建高质量的代码上下文
- 2.2 SDD：构建需求上下文
- 2.3 TDD：把约束落到可执行层
- 从Vibe Coding到Harness Engineering的可落地演进路径
- 3.1 Harness Engineering 的关键启示
- 3.2 结合会员系统的重构路线图
- 3.3 不是替代工程，而是重建工程
- 「Attention is all you need」AI 时代，人类的注意...

## 相关实体

[[Harness]], [[OpenAI]]

## 相关概念

[[TDD]], [[Vibe-Coding]], [[代码生成]], [[领域驱动设计]]
