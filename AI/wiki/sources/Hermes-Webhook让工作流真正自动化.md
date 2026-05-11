---
tags: [Hermes, Agent, GitHub, 飞书, Prompt, API, Python, Skill]
source: "i龙虾"
created: 2026-04-23
updated: 2026-05-10
category: Hermes
---

# Hermes + Webhook：让工作流真正自动化

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484434&idx=1&sn=fefc5fd1ab6b30e708391a19c161b23c&chksm=ea657a07f2a3d6c20713ff3b034e3ceec9be14bf26df283cd18c1a2854fd87139d8c8e17545f&mpshare=1&scene=1&srcid=0423FIMvQOA53i8HDOgvTMi2&sharer_shareinfo=b7f65e246cdac9f998db797746b47e9e&sharer_shareinfo_first=b7f65e246cdac9f998db797746b47e9e) | 2026-04-23

## 摘要

你有没有听过这种声音——"AI Agent 吹了这么久，到底能干啥？"
说实话，我自己以前也是这么想的。装了一堆工具，配了一堆技能，然后呢？打开聊天窗口，问一句，答一句，跟搜索引擎有啥区别？直到我开始玩 Webhook，才真正理解什么叫"Agent 在你睡觉的时候替你干活"。
今天我想聊的，就是把 Hermes Agent 和 Webhook 结合起来，怎么搭出一套真正自动化的流程。不是那种"我手动跑一下脚本"的伪自动化。外部事件一触发，Agent 自己就开工了——审查代码、推送通知、分析数据、回写结果。全程你不需要打开任何一个聊天窗口。
很多人觉得 Webhook 是个很技术的概念，其实特别简单。
打个比方。你家来了个快递，轮询（Polling）的方式是你每隔5分钟开门看一眼有没有人。Webhook 是装了个门铃——快递到了，一按，你立刻就。
技术上说，就是一个外部服务在某件事发生时，往你指定的 URL 发一个 HTTP POST 请求，请求里带着事件详情的 JSON 数据。谁下了你的店铺订单、哪笔支付到账了、哪个 PR 被提交了——发生即通知，实时的。
GitHub、微信支付、支付...

## 相关实体

[[Docker]], [[GitHub]], [[Hermes]], [[OpenClaw]], [[Python]], [[Supabase]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[事件驱动]], [[代码审查]]
