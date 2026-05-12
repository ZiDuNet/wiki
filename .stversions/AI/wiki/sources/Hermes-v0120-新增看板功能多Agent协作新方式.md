---
tags: [Hermes, Agent, 飞书, PPT, API, Skill]
source: "i龙虾"
created: 2026-05-04
updated: 2026-05-10
category: Hermes
---

# Hermes v0.12.0 新增看板功能，多Agent协作新方式

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484564&idx=1&sn=e410889004e5cd1efd309eb93f871001&chksm=ea8be11cf37b1ec201cff46626605b40fba89dd11d6e3477fe30a5758401d7a403b9ae9ef657&mpshare=1&scene=1&srcid=0504ip2NOs22sRUgdvo2UW7W&sharer_shareinfo=b79618f82d16339d8dc1ad7071d24cb2&sharer_shareinfo_first=b79618f82d16339d8dc1ad7071d24cb2) | 2026-05-04

## 摘要

今天凌晨1点30Nous Research在推特发了条消息，配了个视频。视频大概90多秒，讲的是 Hermes Agent 的新功能。
这个视频，是 Hermes Agent 自己规划、自己拍的。
不是那种"AI生成了个PPT"的意思。是真的让它自己拆任务、排依赖、找素材、剪片子，全程没有人工插手。一个Agent当导演，拆成一堆子任务，分给不同的Worker去干，最后拼出了一个完整的演示视频。
我反复看了两遍。不是因为视频多好看，是因为这个协作方式，跟以前完全不一样了。
用过AI Agent框架的人都知道，”多Agent协作”这个概念炒了很久了。但实际用起来呢？
最常见的做法是：主Agent调用子Agent。主Agent觉得"嗯，这事儿该让翻译Agent干了"，于是spawn一个子Agent，等它干完，再spawn下一个。像极了项目经理站在工位后面盯着每个人干活。
主Agent得操心所有调度。谁先干谁后干，谁卡住了怎么处理，全靠主Agent判断。一旦任务复杂了，主Agent自己就成了瓶颈。更要命的是，子Agent一旦崩了，整个流程就卡住了，你得手动介入。
还有种做法是用subagent...

## 相关实体

[[Hermes]], [[OpenClaw]], [[飞书]]

## 相关概念

[[AI-Agent]], [[MultiAgent]]
