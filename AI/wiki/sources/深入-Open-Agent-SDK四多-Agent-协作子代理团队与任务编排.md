---
tags: [Agent, Claude, MCP, GitHub, RAG, Prompt, API, Skill]
source: "BMAD实验室"
created: 2026-04-27
updated: 2026-05-10
category: Agent
---

# 深入 Open Agent SDK（四）：多 Agent 协作——子代理、团队与任务编排

> 来源: [BMAD实验室](https://mp.weixin.qq.com/s?__biz=MzAxNTk5Mjk5Mg==&mid=2247484599&idx=1&sn=28e4b80dbf9e3b98e30bccd401c646b1&chksm=9abeef9f27691f2397c278f1f7769aaf1dca1b71eca390cbeee5e2b49903f09919723236ff27&mpshare=1&scene=1&srcid=0427RQ9ihepJYwOZTtvAcCNt&sharer_shareinfo=247ff219864a2480c43cf62ece996318&sharer_shareinfo_first=247ff219864a2480c43cf62ece996318) | 2026-04-27

## 摘要

单个 Agent 再强，也只是一个执行者。真实的开发任务往往是多步骤、多角色的：先有人探索代码库，有人设计方案，再有人写代码、跑测试。一个 Agent 单干，上下文容易膨胀，效率也上不去。
Open Agent SDK 从三个层面解决这个问题：
1. **子 Agent** -- 主 Agent 在运行过程中动态生成子 Agent，把专门的任务委派出去
2. **Task 系统** -- 用任务追踪多步骤工作的进度和结果
3. **Team + 消息传递** -- 多个 Agent 组成团队，通过邮箱系统互相通信
这篇文章逐一分析这三个层面的实现，最后看它们怎么组合起来做任务编排。
子 Agent 的生成不是 AgentTool 直接 new 一个 Agent 出来——中间隔了一层协议。
定义在
里：
两个方法，一个基础版（5 个参数），一个增强版（13 个参数）。协议还提供了默认实现，增强版直接调用基础版，这样已有的实现类不用改代码就能兼容。
为什么要把 spawner 放在
而不是
？因为
需要用它，但
不应该导入
。把协议定义在
，具体实现放在
，通过
注入——这是 SDK 里常...

## 相关实体

[[Claude]], [[GitHub]]

## 相关概念

[[Function-Calling]], [[Multi-Agent]]
