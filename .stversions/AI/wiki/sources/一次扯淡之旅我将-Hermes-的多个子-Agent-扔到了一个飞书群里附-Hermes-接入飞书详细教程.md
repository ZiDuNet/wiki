---
tags: [Hermes, Agent, 飞书, OpenAI, OpenClaw]
source: "云起泊言"
created: 2026-04-25
updated: 2026-05-10
category: Hermes
---

# 一次扯淡之旅：我将 Hermes 的多个子 Agent 扔到了一个飞书群里（附 Hermes 接入飞书详细教程）

> 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868771&idx=2&sn=43299f187b68194303aeee033470ee0c&chksm=86c60a21a2a1494dc30799e4a42ee764e01b82da86895eb1ffae9d46be201fc2a9fafc6af25f&mpshare=1&scene=1&srcid=04258JwUK3y6WGWOAoJGoOAJ&sharer_shareinfo=23e675f1179b7bf031e609ba0791e30b&sharer_shareinfo_first=23e675f1179b7bf031e609ba0791e30b) | 2026-04-25

## 摘要

我的工作中一直都没怎么接触过飞书，只是在偶尔参与某些产品内测的时候才会把它重新下载回来，在OpenClaw大火的时候看到人人都用飞书接入玩的飞起，那时也没有让我有接入的动力
上次发了一篇关于**Hermes开启多个子Agent**的教程，让我的Hermes分为了三个不同分工的Agent，一个负责写作，一个负责出PRD，一个负责编码，如果要想跟着这篇文章一起实现群组里面接入多个子Agent的话还是建议先看完我之前写的这篇文章：[Hermes 多 Agent 团队协作的正确打开方式](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868631&idx=1&sn=9b4210e367d4e69335bdb29839fe901d&scene=21#wechat_redirect)
当时看到有大佬将Hermes跟OpenClaw两个Agent扔到了某国外软件的群组里面，互相调用，互相督促，感觉还挺好玩的，于是我想尝试将Hermes的多个子Agent扔到同一个群组里面对话，但是死活不行，只有主Hermes能够回复我消息，子Age...

## 相关实体

[[Hermes]], [[飞书]]

## 相关概念

[[MultiAgent]]
