---
tags: [Hermes, Agent, 飞书]
source: "深圳鸣明"
created: 2026-05-04
updated: 2026-05-10
category: Hermes
---

# 用 Hermes + wechat-cli 搭建微信群聊情报助手,自动总结100+群聊消息

> 来源: [深圳鸣明](https://mp.weixin.qq.com/s?__biz=Mzg3NDU3NTIwMQ==&mid=2247489575&idx=1&sn=1986bef8cb7cfa292a09fdf6d7a58835&chksm=cf16fec84bccf51d50d94fe54f0d622864c48ff4fdba31b6ad7997c77287001df6894d05b8e1&mpshare=1&scene=1&srcid=0504GXgBtbYocDeTSlOR8c1F&sharer_shareinfo=10fecbaea2b345ca7dcff475e730be08&sharer_shareinfo_first=10fecbaea2b345ca7dcff475e730be08) | 2026-05-04

## 摘要

大家好，我是明哥。
38岁，程序员，还在职，晚上带娃，还在探索副业。
最近搞了一个小工具，解决了困扰我很久的一个问题。
先说问题是什么。
我在AI破局星球里，加了上百个微信群。
有实战派的、有工具派的、有副业派的，每天消息刷都刷不过来。
但有些群里的信息真的很有价值。
比如有人分享了一个实操经验，比如有人踩了一个坑，这些信息错过了就错过了。
我之前的状态是：要么一直盯着手机刷群，要么干脆放弃某个群，任由有价值的信息沉掉。
两个选择都很糟糕。
所以我想，有没有一种方式，能让我不用一直盯着，但又不漏掉真正重要的东西？
**01**
**解决方案**
**用两个工具搭了一套自动情报系统**
我的方案是这样的：
**wechat-cli** 负责读取微信群聊数据
**Hermes** 负责定时执行、AI总结、推送飞书
每2小时，系统自动做这几件事：
1.
读取所有群聊的最新消息

## 相关实体

[[Hermes]], [[微信]], [[飞书]]

## 相关概念

[[Multi-Agent]]
