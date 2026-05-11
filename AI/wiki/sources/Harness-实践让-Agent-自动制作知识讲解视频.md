---
tags: [Skills, Agent, Claude, GitHub, Harness, Prompt, API, OpenAI]
source: "code秘密花园"
created: 2026-05-09
updated: 2026-05-10
category: Skills
---

# Harness 实践：让 Agent 自动制作知识讲解视频

> 来源: [code秘密花园](https://mp.weixin.qq.com/s?__biz=Mzk0MDMwMzQyOA==&mid=2247505960&idx=1&sn=ac72488e0c5841a949bb139ece4cb746&chksm=c38c477d875a462f38ff4e208148c4e4696d680d077cd8ed67f86db3bbaf21f7b5cf2c0d6960&mpshare=1&scene=1&srcid=0509sNKRnPlbgf4n2Dnibja4&sharer_shareinfo=739eb4f780e1c70ded6564100f74e8dd&sharer_shareinfo_first=739eb4f780e1c70ded6564100f74e8dd) | 2026-05-09

## 摘要

大家好，欢迎来到 **code秘密花园**，我是花园老师。
前段时间我发了几条技术讲解视频，评论区好多同学问：这个视频效果是怎么做的？
趁着五一假期，我把整套流程封装成了一个 Skill，让大家也能低成本复刻这种效果。
今天这期内容信息量很大，我们要讲三件事：
第一，我的视频到底是怎么做的；
第二，背后这个 Skill 是怎么设计的；
第三，手把手带大家走一遍完整的实战流程 — 从一篇文章丢进去，到最后出来一个精美的知识讲解视频。
先声明一下：我之前的视频，不是用视频生成模型做的，也没有用 NotebookLLM。
其实就是网页。我自己 Vibe Coding 出来的网页。
肯定有人会问 — AI 视频生成模型已经很强了，为什么还要折腾网页？
答案就俩字：**可控**。
字体、配色、每一步停留几秒、某一帧要不要出现一个精确的数字 — 这些东西在网页里改几行代码就搞定。
比用视频模型抽卡要稳定得多，成本也更低。
NotebookLM 我也试过，它做不了动画演示效果，出来的都是静态图。
Remotion 这种框架，我觉得它反而限制了模型本身的发挥，有时候还不如直接写来得好。
拿我上期发出的...

## 相关实体

[[Anthropic]], [[B站]], [[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub]], [[Harness]], [[OpenAI]]

## 相关概念

[[Multi-Agent]], [[Vibe-Coding]], [[多模态]]
