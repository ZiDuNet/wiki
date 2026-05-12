---
tags: [OpenClaw, Agent, Claude, RAG, Prompt, API, Python, OpenAI]
source: "快AI慢调"
created: 2026-04-24
updated: 2026-05-10
category: OpenClaw
---

# “影子 Agent”大爆发：如何排查潜伏在企业内网深处的、那些只有 IP 没有身份的 OpenClaw 实例？

> 来源: [快AI慢调](https://mp.weixin.qq.com/s?__biz=MzI3ODY0NjA3NA==&mid=2247484819&idx=1&sn=2323543a97a477c2858e08ca4ffda0cb&chksm=eaee5bb4086364fed9cf40d69c8e975a920f342cd75d1135e49797380878488b1f08d3027ad0&mpshare=1&scene=1&srcid=0424zaC1l1mAoJA6vASLeMCn&sharer_shareinfo=1341f0ba43a7ebc9ccbec8855a50bc86&sharer_shareinfo_first=1341f0ba43a7ebc9ccbec8855a50bc86) | 2026-04-24

## 摘要

周二，一位在某大型制造业做 CISO（首席信息安全官）的朋友给我打了个电话。
他语气里透着一种见鬼了的困惑：“我们内网的防火墙告警疯了。数据中心监控到，行政部有一台平时只用来做登记的破旧台式机，**每天都在往海外疯狂发送数以万计的加密 API 请求。**”
他第一反应是中勒索病毒了，或者是遭遇了高级持续性威胁（APT）攻击。
等安全团队如临大敌地冲进行政部，把那台电脑断网、拔盘、做内存取证后，真相却让人啼笑皆非：
根本没有黑客。**是行政部的一个实习生，为了偷懒，自己跟着 B 站教程在这台电脑上部署了一个本地的 OpenClaw 实例。** 他让这个 Agent 自动去抓取内网的考勤数据、员工档案，然后调用外部的大模型 API 来生成月度绩效报表。
最致命的是，这个实习生随手把服务起在了默认的 `0.0.0.0` 端口上，连最基本的密码都没设。
我朋友叹了口气说：
这就是 2026 年企业安全领域最头疼的新名词——**影子 Agent（Shadow Agent）。**
今天，我们就来聊聊这些潜伏在你企业内网深处的数字幽灵，以及如何把它们揪出来。
一、 从“影子 IT”到“影子 Agen...

## 相关实体

[[Anthropic]], [[Docker]], [[Excel]], [[Nodejs]], [[OpenAI]], [[OpenClaw]], [[Python]]

## 相关概念

[[RAG]]
