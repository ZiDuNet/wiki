---
tags: [Hermes, Agent, 飞书, Skill, OpenClaw]
source: "AI学不会"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# 前阵子用 OpenClaw 跑通了新闻聚合推送（[养虾日记🦞-我用4个AI Agent，搭了个内容创作团队](https://mp.weixin.qq.com/s?biz=MzAwMzU3Nzk4Nw==&mid=2247484039&idx=1&sn=fcfe3903019c4c44994f3c1ccd511ade&scene=21#wechatredirect)），定时抓新闻、整理好发给我，体验还行。

> 来源: [AI学不会](https://mp.weixin.qq.com/s?__biz=MzAwMzU3Nzk4Nw==&mid=2247484105&idx=1&sn=571b587f51af1d9669504b5134044a7e&chksm=9a6a9d2bf3a1f3fd8790853944eeff37507de17be9c0e940992bd69198a637f9ae9d51367d59&mpshare=1&scene=1&srcid=0420OypopQhLTuxdeo64ZTQr&sharer_shareinfo=bc018e333699244c0f1b68184c51b7ca&sharer_shareinfo_first=bc018e333699244c0f1b68184c51b7ca) | 2026-04-20

## 摘要

但有个问题：它只能推到飞书和邮箱。飞书我日常不怎么开，邮箱看新闻总觉得差点意思——我每天打开最多的，还是微信。
所以我就想，能不能直接把新闻推到微信上？
最近刚好在研究 Hermes Agent，它也支持原生支持微信接入。折腾了一下，居然很快就搞定了。今天把过程记一下。
先简单说下 Hermes Agent 是什么。
它是 Nous Research 今年2月推出的开源 AI Agent。跟其他 Agent 最大的不同是，它有个**自学习闭环**——你用它完成任务，它会总结经验，自动生成可复用的 Skill。说白了就是越用越聪明。
我之前用 OpenClaw 配置新闻推送，得手写 SOUL.md、AGENT.md、各种配置文件。就像招了个助理，工作手册得你从头写到尾。
Hermes 不太一样。你给它一个任务，它自己学着做。做完一次，下次就会了。
这次接入微信，让我体验了一把这个"自学习"。
说实话，我一开始做好了折腾半天的准备。毕竟接入微信这种事，光各种桥接工具的配置就够头疼的。
现在有agent，就不用再一步一步手动去配置了
我的操作是这样的：**把官方文档链接丢给 Hermes，让...

## 相关实体

[[Hermes]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[内容创作]]
