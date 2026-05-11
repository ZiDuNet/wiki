---
tags: [Skills, Agent, API, Skill, OpenClaw]
source: "Aloudata"
created: 2026-04-20
updated: 2026-05-10
category: Skills
---

# 加了几个 Skill，小龙虾变身高阶分析师

> 来源: [Aloudata](https://mp.weixin.qq.com/s?__biz=Mzk0NjYzMjU4NA==&mid=2247493780&idx=1&sn=16675ee08486a5d6d0b5cece604381c6&chksm=c2db70ba89a1fafce28529df730e40ce62882028bd4299055b4829cbfff9a3e1d499efae885e&mpshare=1&scene=1&srcid=0420UsjMjaiRVIFHmWwGBVoi&sharer_shareinfo=d2a9b8c880dc600116f59e9632e5010d&sharer_shareinfo_first=d2a9b8c880dc600116f59e9632e5010d) | 2026-04-20

## 摘要

第一期我们让小龙虾接上语义层，它学会了查数和归因。第三期我们换了一个完全不同的业务场景——库存——还多装了四个分析 Skill。同样是你问它答，但每一步回答的深度变了。这篇是完整记录，没时间看视频的话读这篇就够了。
视频在这里 ↓
***01***
**这期装了什么？**
环境还是上次的，metric-query 查指标、metric-attribution 做归因，两个老朋友还在。这期加装了四个新 Skill：
- **anomaly-detection**，判断指标正不正常。给它一段时间序列，它算基线、定区间、做判断，告诉你是真异常还是正常波动。
- **forecast-simulation**，预测趋势和模拟假设场景。你能问「30 天后库存到什么水位」，也能问「如果销量涨 30% 会怎样」，两种情景它都能算。
- **analysis-report**，总编角色——它自己不做分析，它知道一份完整报告应该包含什么内容，然后调度其他 Skill 干活，最后串成一份有叙事线的文档。
- **scheduled-report**，把一轮对话里做过的分析流程录制下来，设成定时任务，以后自...

## 相关实体

[[Markdown]], [[OpenClaw]]

## 相关概念

[[AI-Agent]]
