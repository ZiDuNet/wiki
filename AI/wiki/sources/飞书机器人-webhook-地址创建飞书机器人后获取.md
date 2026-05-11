---
tags: [OpenClaw, Agent, Claude, GitHub, 飞书, API]
source: "研磨架构"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# 飞书机器人 webhook 地址（创建飞书机器人后获取）

> 来源: [研磨架构](https://mp.weixin.qq.com/s?__biz=MzUzOTE3OTc5MQ==&mid=2247484277&idx=1&sn=34d8f37b1aaa26c34f952d12902b2b49&chksm=fb60a4aafa91d4192de904a9e9fcee56668ebfb797210fac6d9a1191d53b8c2c3fe49dd128a5&mpshare=1&scene=1&srcid=0423GPSvdEEeHZCH0p8tr0tX&sharer_shareinfo=5adafccc4e5b517bb373dc52db71d003&sharer_shareinfo_first=5adafccc4e5b517bb373dc52db71d003) | 2026-04-23

## 摘要

内容创作者最头疼的事是什么？
不是写，是找选题。
每天刷微博、刷知乎、刷抖音、刷头条……刷了一圈下来，时间花了不少，脑子里还是一片空白。等终于憋出一个选题，热点早就凉透了。
有没有一种工具，能把这些平台的热点自动聚合起来，再主动推给我？
有。这个工具叫 TrendRadar，GitHub 上 50.7K Star，开箱即用，我部署完到现在跑了小半个月，体验很稳。
项目热度急剧爬升：
简单说，它是一个多平台热点聚合器，核心功能有几块：
**第一，多平台热点抓取。** 支持微博、知乎、抖音、B站、今日头条、百度、微博热门话题等平台的内容同步。
**第二，RSS 订阅源支持。** 如果你有固定的信息源，可以在配置里直接加 RSS 地址，支持 Hacker News、V2EX 等技术社区。
**第三，关键词 + AI 双轮筛选。** 既可以按关键词过滤，也可以让 AI 判断"这条内容跟我的方向是否相关"，后者对于选题探索阶段特别有用。
**第四，AI 翻译。** 抓到的海外内容可以直接翻译成中文，不用专门开梯子。
**第五，多渠道推送。** 支持飞书、钉钉、企业微信、telegram电报，配置...

## 相关实体

[[B站]], [[Claude-Code]], [[Claude]], [[Docker]], [[GitHub]], [[OpenClaw]], [[VS-Code]], [[小红书]], [[微信]], [[抖音]], [[钉钉]], [[飞书]]

## 相关概念

[[代码生成]], [[内容创作]]
