---
tags: [Hermes, Agent, API, Skill]
source: "赛博生命虾酱"
created: 2026-05-10
updated: 2026-05-10
category: Hermes
---

# Hermes Kanban 保姆级实战教学：从0到1跑通多角色协作写公众号文章全流程

> 来源: [赛博生命虾酱](https://mp.weixin.qq.com/s?__biz=MzA4Mjg1NjU2OA==&mid=2247484353&idx=1&sn=7ccff9be754e962b96cdb9d35ec50be8&chksm=9e8900e987f6d0b0322d777ed9d73e383382c3f6add5a7ec69b9b033c25907536fff2dde72f5&mpshare=1&scene=1&srcid=0510geTCcMcX4M3XwnlH1iBh&sharer_shareinfo=2c1bb90f31eb83fc3e2cace60a53561b&sharer_shareinfo_first=2c1bb90f31eb83fc3e2cace60a53561b) | 2026-05-10

## 摘要

很多人刚上手Hermes时，都在问：“Kanban到底是啥？不就是个任务列表吗？”
但你要知道，当你的任务需要「查资料→分析→写稿→配图」多步骤、多角色协作时，单靠一个指令根本hold不住。而Kanban就是Hermes里的「多角色协作调度中心」，能让不同的AI角色各司其职，自动流转任务。
这篇文章，就带你用真实交互过程，手把手跑通一次完整流程👇
一开始，我直接抛出问题：“这个功能要怎么使用？” Hermes马上给我划了重点：
- Kanban是「多智能体任务分发系统」，核心是「Orchestrator（调度者）+ Worker（执行者）」的分工模式
- 调度者负责拆任务、建卡片；Worker负责认领任务、推进流程
- 千万别用delegate\_task代替kanban\_create，前者是短程任务，后者才是Kanban的持久化卡片！
在正式开工前，必须先确认三件事：
1. \*\*有没有specialist profiles\*\*：比如researcher、analyst、writer这些角色配置，Worker全靠它们来认领任务
2. Kanban插件是否安装：路径一般在~/....

## 相关实体

[[Hermes]]

## 相关概念

[[MultiAgent]], [[微调]]
