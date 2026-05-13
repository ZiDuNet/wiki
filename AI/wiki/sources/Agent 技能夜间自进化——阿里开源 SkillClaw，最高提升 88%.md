---
tags: [Agent, Skill, SkillClaw, 阿里, 自动进化, 技能库]
source: "Hyman的杂货铺"
created: 2026-05-13
updated: 2026-05-13
category: Agent
---

# Agent 技能夜间自进化——阿里开源 SkillClaw，最高提升 88%

> 来源: [Hyman的杂货铺](https://mp.weixin.qq.com/s?__biz=MzkzODY5NjM5Mw==&mid=2247491020&idx=1&sn=f9148a892d618699cc03d88cdc099180&chksm=c3c88500c6b92b794c3a514267cf06a5cc36a68cc08cf5c21d42b7e8273efaad4215adcd8878) | 2026-05-13

## 摘要

阿里DreamX团队提出SkillClaw，一个让多用户Agent生态中的技能库持续自动进化的框架。系统在用户正常使用Agent时，后台收集交互轨迹，夜间进化技能，次日同步给所有用户，无需人工介入。

SkillClaw的核心架构是一个闭环进化流水线：多用户交互→会话收集→技能进化→技能同步。系统通过自主进化器分析成功和失败的会话案例，从三个动作中选择：Refine（精炼）、Create（新建）、Skip（跳过）。验证机制引入单调性保证，只有更好的版本才会被接受。在WildClawBench评测中，6天内实现持续单调提升，创意合成类任务相对提升88.41%。