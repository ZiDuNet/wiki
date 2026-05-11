---
tags: [Hermes, Agent, GitHub, API, Python, OpenAI, Skill, OpenClaw]
source: "Josh哥说点什么"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# 我让 Hermes Agent 自己写了一个数据质量 Skill，结果它真的开始自我修正了

> 来源: [Josh哥说点什么](https://mp.weixin.qq.com/s?__biz=MzkxODU2Nzg3Mw==&mid=2247485418&idx=1&sn=20bb92245661875d0cd4032b10d2ee95&chksm=c081c52f50a9d27842b18dd3690e33a592efe412fab3adbc0235c82119334a7ef27b8fa5c2cc&mpshare=1&scene=1&srcid=04218jiraZhxBybOPfbbhDo4&sharer_shareinfo=c198210b8e2acced3a6a0cec4876dfa0&sharer_shareinfo_first=c198210b8e2acced3a6a0cec4876dfa0) | 2026-04-21

## 摘要

最近我在本机继续折腾 AI Agent。
这次主角不是 Copilot Studio，也不是 OpenAI API 的简单调用，而是一个更接近“个人本地 AI 助理”的框架：**Hermes Agent**。
我的配置大概是这样：
- 本地模型：Gemma4 e4b，作为默认后台模型
- 云端模型：GPT，用于复杂任务补强
- Agent 框架：Hermes Agent + Revolution Package
- 实验任务：让 Hermes 帮我创建一个关于 **Data Quality Detection Skill** 的能力模块
- 技术方向：使用 **Great Expectations（GE）** 做数据质量规则校验
这篇文章不是官方评测，也不是吹水软文。它更像一次真实的本地实验记录：**Hermes 在我的 case 里，到底有没有体现出“自我修正 Skill”的能力？它和 OpenCraw / OpenClaw 这类本地助理相比，差别在哪里？本地模型 + 云模型的双模型方案，是否真的有价值？**
我启动 Hermes Agent 之后，终端里出现了一个很有“黑客电影感”...

## 相关实体

[[GitHub]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[Python]]

## 相关概念

[[AI-Agent]], [[Multi-Agent]], [[SOP]], [[代码审查]], [[代码生成]]
