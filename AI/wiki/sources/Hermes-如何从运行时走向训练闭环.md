---
tags: [Hermes, Agent, RAG, Prompt, API, OpenAI, Skill]
source: "AI步步通"
created: 2026-04-30
updated: 2026-05-10
category: Hermes
---

# Hermes 如何从运行时走向训练闭环

> 来源: [AI步步通](https://mp.weixin.qq.com/s?__biz=MzY4NTE4OTYzNg==&mid=2247483879&idx=1&sn=e5476ed648410e6fee4ae41e1e24667f&chksm=f27ffd56e8733bf6c4f19a72825e5df8ca9638acdf0fa47f24af0251906373283f4306525089&mpshare=1&scene=1&srcid=0430gc9rk9OLDvOm87Si5kyo&sharer_shareinfo=fe47854624a882a10a8856cd49f6c6ba&sharer_shareinfo_first=fe47854624a882a10a8856cd49f6c6ba) | 2026-04-30

## 摘要

Agent 系统完成任务之后，执行过程本身也值得被保存下来。Hermes 的一个重要设计是把这些过程结构化：哪些工具被调用、上下文如何变化、结果是否完成、奖励如何计算，都可以继续进入评估、微调和强化学习链路。
这条链路的入口可以来自人工对话，也可以来自定时任务和批量环境。Cron 让任务可以按时间自动触发，并在独立 session 里运行；Trajectory 把多轮对话和工具结果保存成可训练的 ShareGPT JSONL；Environment 把任务、工具、沙盒和评分函数封装起来；RL 工具再把这些 scored trajectories 接到 Atropos 和 Tinker。
这样看 Hermes，它的运行时能力正在延伸成一条数据生成链路。Agent 执行过程可以被复盘、评分和批量生产，最终成为下一轮模型改进的输入。
Hermes 的训练闭环可以拆成四层：Cron 负责主动触发任务，Trajectory 负责保存过程，Environment 负责给任务定义评分标准，Atropos/Tinker 负责把 scored rollouts 送进 SFT 或 RL 训练。
Herme...

## 相关实体

[[Docker]], [[Hermes]], [[LoRA]]

## 相关概念

[[AI-Agent]], [[微调]]
