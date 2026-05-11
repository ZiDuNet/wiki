---
tags: [Hermes, Agent, Prompt, Skill]
source: "AI步步通"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# Learning Loop：Hermes 沉淀行为SKILL的法宝

> 来源: [AI步步通](https://mp.weixin.qq.com/s?__biz=MzY4NTE4OTYzNg==&mid=2247483836&idx=1&sn=644bba6cb4b8884e02f08906812fbbed&chksm=f25fa58e1fca3e88d3da8e5b27927ee9040f469548df2562959674e83f5de1f0eb42bb4b7f65&mpshare=1&scene=1&srcid=0421HzW2b439N8HfOfLj7ReJ&sharer_shareinfo=519b8a0a6afcaa2c12967921d76c8014&sharer_shareinfo_first=519b8a0a6afcaa2c12967921d76c8014) | 2026-04-21

## 摘要

很多持续运行的 Agent 都会遇到同一种场景：同一个用户每周五都要拉一遍五家竞品的新动态。第一次，Agent 还能边查边试；第三次，用户已经把截图顺序、分析模板、归档目录都校正过了。这个时候，真正有价值的，是这套流程能不能变成下次开工就能直接调用的方法。
Hermes Agent中的Learning Loop 处理的正是这件事。它负责把一次复杂任务中摸索出来的有效做法，从“本轮对话里的临场发挥”推进成“以后还能直接调用的程序性能力”。Hermes 的经验能不能真正累积，Agent 会不会随着使用次数增长而越来越顺手，关键就看这条链路能不能成立。
Hermes 为这件事补上了完整工程路径：偏好进入
，历史对话留在
，成功路径被整理成
，下一轮任务启动时再重新进入提示词组装链路。沿着这条任务流拆开来看，Hermes 的“越用越聪明”就会落到具体源码文件和运行路径上。
Learning Loop 给 Hermes 带来的增量，是把复杂任务的成功做法保存成程序性记忆。结果会过期，方法会复用，下一轮任务因此可以直接复用上一次沉淀的方法。
在 Hermes 的整个长期记忆体系里，至少有三种完全不...

## 相关实体

[[Hermes]], [[SQLite]]

## 相关概念

[[AI-Agent]], [[工作流自动化]]
