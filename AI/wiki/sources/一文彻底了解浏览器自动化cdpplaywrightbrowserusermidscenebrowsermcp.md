---
tags: [浏览器自动化, Agent, MCP, API, Skill]
source: "周某人随笔"
created: 2026-04-20
updated: 2026-05-10
category: 浏览器自动化
---

# 一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp

> 来源: [周某人随笔](https://mp.weixin.qq.com/s?__biz=MzU5ODg1NDk1Ng==&mid=2247484662&idx=1&sn=86710f5235fc8287ed0fdf470145617d&chksm=fffea1d0dcfc6c912680c25660ae200d865c88f46fb9ab8495c578f98379d94bd909a1587854&mpshare=1&scene=1&srcid=0420UHPmwHj0QRKC6LcGRqqF&sharer_shareinfo=b9690d7e2f9ba2fd8f91b0266ca7ccb8&sharer_shareinfo_first=b9690d7e2f9ba2fd8f91b0266ca7ccb8) | 2026-04-20

## 摘要

cdp到底是什么？browser-use和Playwright到底是什么关系？browsermcp又是干吗的？如果我想让AI来操作我的浏览器，比如自动发布视频至各大平台，过程中遇到登录态怎么办？页面结构中遇到shadow dom，也就是影子dom，这种普通自动化工具抓不到、点不动的页面结构，该怎么解决？
最近正好在做一个多平台同步发布视频的自动化skill，小红书和抖音整体还算顺，把发布流程拆清楚之后，让它用browser-use去执行，基本就能跑起来。真正卡住的，是视频号。
因为视频号后台里有一部分页面用了wujie的shadow dom结构，你从视觉上看，那个发表视频按钮明明就在页面上，但很多基于DOM的自动化工具就是拿不到。
因为之前做过一些RPA相关的项目，知道字节有一套基于AI多模态的方案，是Midscene，后来就换成了它。它本质上不是先理解底层dom结构，再决定怎么点，而是先去理解页面截图里到底有什么，什么元素在什么位置，知道位置后就可以利用底层操作浏览器的工具去执行了。
整个过程我发现这里其实还是有很多概念和术语的，就想着把这些从底层到最上层都整理一下，并分享给大家。
...

## 相关实体

[[小红书]], [[抖音]]

## 相关概念

[[多模态]], [[浏览器自动化]]
