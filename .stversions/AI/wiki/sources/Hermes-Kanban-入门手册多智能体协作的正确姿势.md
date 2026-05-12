---
tags: [Hermes, Agent, Prompt, API, Skill]
source: "傲来说"
created: 2026-05-09
updated: 2026-05-10
category: Hermes
---

# Hermes Kanban 入门手册：多智能体协作的正确姿势

> 来源: [傲来说](https://mp.weixin.qq.com/s?__biz=Mzk0NjQ5MTY0OA==&mid=2247483949&idx=1&sn=ff9999d17c55477cf889637ee7594424&chksm=c2dbc242b15bfc6f21da9acaeb5bff96b09a1b76fc63996e6258bce63f1558239ad4fb629d80&mpshare=1&scene=1&srcid=0509vQaI9dIeMgrTxfXUtbqO&sharer_shareinfo=6e716e7148f03aa86496f35cde530ce4&sharer_shareinfo_first=6e716e7148f03aa86496f35cde530ce4) | 2026-05-09

## 摘要

容我先说句不太中听的话：如果你还在用 `delegate_task` 处理所有复杂任务，那你大概每天都在经历同一件事——任务跑着跑着断了，上下文丢了，然后你不得不从头再来。
这不是你的问题。这是工具的问题。
Hermes Kanban 解决的就是这个事：**当任务复杂到需要多个 AI 专家协作、需要抗崩溃、需要审计追踪的时候，你该怎么组织它们？**
答案不是"更聪明的 prompt"，而是**一套协作系统**。
先说个常识。《孙子兵法》讲："凡治众如治寡，分数是也。" 管理大部队和管理小分队，道理不一样。
AI 协作也一样。
一个小任务，一次推理就能搞定——直接用 `delegate_task` 或者让 AI 自己答，没问题。但当任务变成这样：
- 需要研究员查资料、工程师写代码、测试员跑测试，**三个角色协作**
- 任务跑了一半，服务挂了，重启后还能接着干
- 你需要在中途介入，看看进度，改改方向
- 子任务之间有依赖关系，A 没完 B 不能动
这时候，"更聪明的 prompt" 不管用了。你需要的是一个**任务管理系统**，而不是一句更好的话。
Hermes Kanban 的核心...

## 相关实体

[[Hermes-Agent]]

## 相关概念

[[Kanban看板]]
[[多Agent协作]]
[[Agent架构]]
