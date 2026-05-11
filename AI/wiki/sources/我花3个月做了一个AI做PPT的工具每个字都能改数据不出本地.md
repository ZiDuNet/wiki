---
tags: [PPT制作, Agent, Claude, GitHub, PPT, API, Python, OpenAI]
source: "陪陪源码网"
created: 2026-04-30
updated: 2026-05-10
category: PPT制作
---

# 我花3个月做了一个AI做PPT的工具，每个字都能改，数据不出本地

> 来源: [陪陪源码网](https://mp.weixin.qq.com/s?__biz=MzIyODM5MzQwNA==&mid=2247485487&idx=1&sn=35d05b5b7646f138773ff0410a6ad723&chksm=e98039323a81767fd88650b50163e8ad763eed5d603c7acac98bc3e16a43b856c4e75b14f9cc&mpshare=1&scene=1&srcid=0430JCailHdsosM3Ph5VQHqc&sharer_shareinfo=a8bb16b284934d436737070c7cc53220&sharer_shareinfo_first=a8bb16b284934d436737070c7cc53220) | 2026-04-30

## 摘要

先说一个很扎心的事实——
**市面上绝大多数号称"AI一键生成PPT"的工具，生成的都不是真正的PPT文件。**
你可能遇到过这种情况：花了一下午调试，终于生成了一份看起来不错的PPT，结果到演示现场发现有个错别字，点了一下文本框——整页图直接飞了。
因为整页都是一个截图，根本不是真正的文字。
这其实就是我做这个东西的起因。
我工作里需要经常做PPT，也试过市面上几乎所有AI PPT工具。
但是用下来就四个字：**都不对劲**。
有的要你充会员才能导出高清版本，有的生成的文件换个电脑就变形，有的说是PPT结果打开是一张一张的图，关键元素根本改不了。
最让我崩溃的一次是有个重要客户，我在酒店用手机改了份PPT，发现某个数据错了，想改却点不动——因为整页是一张图。
我就想：**有没有一个方案，能让AI真正理解PPT文件格式，生成真正可编辑的PPTX？**
然后我就开始自己搞了。
**简单说：丢进去一份PDF、Word、网页链接或者文字，拿回来一份原生可编辑的PowerPoint。**
什么叫"原生可编辑"？
就是每一个形状、每一个文本框、每一个图表，都是PowerPoint原生的Drawi...

## 相关实体

[[Claude]], [[Cursor]], [[Markdown]], [[Python]], [[VS-Code]], [[微信]]

## 相关概念

[[AI-Agent]]
