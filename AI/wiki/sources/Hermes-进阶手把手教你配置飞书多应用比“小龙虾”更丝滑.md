---
tags: [Hermes, Agent, 飞书, Prompt, API]
source: "匿星AI"
created: 2026-04-24
updated: 2026-05-10
category: Hermes
---

# Hermes 进阶：手把手教你配置飞书多应用，比“小龙虾”更丝滑！

> 来源: [匿星AI](https://mp.weixin.qq.com/s?__biz=MzYzOTA1MDAzMQ==&mid=2247486412&idx=1&sn=e93487594af381dc378604422c5da6ef&chksm=f1966433199a0b6669d01ba86662a6f46d206fe9a30bb1ea3f07f493cf5707356ade7193d8be&mpshare=1&scene=1&srcid=0424xMMJLZ3PdF3pa6nkKY2x&sharer_shareinfo=0c884d31d9ac91cd49e8e86077ec59f9&sharer_shareinfo_first=0c884d31d9ac91cd49e8e86077ec59f9) | 2026-04-24

## 摘要

既然小龙虾能配置多个飞书应用，那 Hermes 如何配置呢。在看了 Hermes 的源码结构是有点懵的，感觉好乱，无从下手。
花了一天时间，找了两种方案，配置了几次才成功，有需要的朋友可以去尝试。
如果不知道腾讯云如何部署Hermes 看这篇[小龙虾已死，新王Hermes登基，附腾讯云+飞书0基础部署指南](https://mp.weixin.qq.com/s?__biz=MzYzOTA1MDAzMQ==&mid=2247486363&idx=1&sn=56283a3968caa0cc84171888549cf579&scene=21#wechat_redirect)
我是匿星，主业程序员，专注于AI编程，副业工具提效，和5000+朋友一起共同创富！
**实现思路**
Hermes 的 **Profile** 是 Agent 运行实例的配置集合。
我们可以通过为每个飞书应用创建一个独立的文件夹，实现配置与逻辑的完全隔离。
**配置流程简述：**
1. 在
目录下新建独立空间文件夹。
2. 通过与主机器人对话，参考 SOP 自动构建运行环境。
3. 加载必要文件，配置飞书与大模型 Key...

## 相关实体

[[Hermes]], [[OpenClaw]], [[飞书]]

## 相关概念

[[SOP]], [[代码生成]]
