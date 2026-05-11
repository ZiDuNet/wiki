---
tags: [Hermes, Agent, Claude, API, Skill]
source: "量子智元"
created: 2026-05-09
updated: 2026-05-10
category: Hermes
---

# Hermes Agent v0.13.0更新：一台机器，三个 AI 团队成员各司其职

> 来源: [量子智元](https://mp.weixin.qq.com/s?__biz=MzkwMTc4NTkwNg==&mid=2247488725&idx=1&sn=fab8ce26de614359b9f7e12a28671053&chksm=c1ce055fc33987e58975ceac5d4d8c8724586250b0c4eee9c645687fcd4fa743147adfe7ec77&mpshare=1&scene=1&srcid=0509rRAXYN57Cx2nl4axlWqw&sharer_shareinfo=a18f79e1da7edb6ac9bcce28cab60bc5&sharer_shareinfo_first=a18f79e1da7edb6ac9bcce28cab60bc5) | 2026-05-09

## 摘要

在折腾 Hermes 的时候，碰到一个挺常见的问题——**一个 Agent 什么都管，context 越来越乱**。日历提醒、代码审查、论文检索全混在一起，记忆库里夹杂着各种碎片。找了一圈，发现 Hermes 其实内置了一个 Profile 机制，专门解决这个问题。
简单说就是：**在同一台机器上跑多个完全独立的 Agent**，各自有自己的配置、密钥、记忆和会话，互不干扰。这篇就记录一下实际操作过程。
把所有任务塞给同一个 Agent，短期内没问题。但时间久了会发现几件烦人的事：
你让 Agent 帮你管代码仓库，它顺便记住了你今天心情不好、想换工作。你让它帮你查论文，它的上下文里还夹着你上周让它安排的婚礼筹备清单。更麻烦的是，**不同任务需要不同的 API 密钥和不同的模型**——研究任务想用 DeepSeek-R1 做深度推理，日常闲聊用便宜的 Haiku 就够，但你没法在同一个 Agent 里同时配两套。
Profile 就是为了解决这个问题——让每个角色只知道它该知道的事情。
先确认一下本地有没有安装 Hermes，命令行跑一下 `hermes --version`。有的话直...

## 相关实体

[[Claude]], [[DeepSeek]], [[Hermes]]

## 相关概念

[[CICD]], [[代码审查]], [[内容创作]]
