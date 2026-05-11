---
tags: [OpenClaw, Agent, GitHub, 飞书, Skill]
source: "REITs研习笔记"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# 用 OpenClaw 打造微信公众号文章阅读助手：一个自动抓取、查询、推送全流程的Skill

> 来源: [REITs研习笔记](https://mp.weixin.qq.com/s?__biz=MzkyMzcwMzcwMw==&mid=2247484116&idx=1&sn=891cd3286c85801c6956afeada47eaca&chksm=c05bf31d3d9625dd6a8b9c2bcebd09644f74a35c7fb7d1ddf6cdda4ad8edf04272da38804c6b&mpshare=1&scene=1&srcid=0420SqF7EXFSITDDSkA07Ow5&sharer_shareinfo=cd99aed01d61aa29b74d0f56b50e292f&sharer_shareinfo_first=cd99aed01d61aa29b74d0f56b50e292f) | 2026-04-20

## 摘要

你有没有这样的困扰：每天要翻十几个公众号才能看完行业动态；想找一篇几天前读过的文章却怎么也翻不到；或者想针对某篇推文做深度分析，却只能手动复制粘贴……
现在，我开发了一个 Skill（可直接应用于 OpenClaw）—— **wechat-query-skill**，它把微信公众号的订阅、新文章内容缓存、查询、推送、巡检串成了一条自动化流水线。
你只需要用自然语言对 Agent 说一句话，剩下的全部自动完成。
GitHub 源码：**https://github.com/adennng/wechat-query-skill**
- 你拥有一个微信公众号（订阅号、服务号均可）
- 本地环境已安装 Docker
- 首次使用或登录失效时，需要**公众号管理员微信**扫码登录（登录有效期为4天，可随时重新登录续期）
- 支持 Linux / macOS / Windows
这个 Skill 的核心思路很简单：
- 先把服务部署起来
- 用公众号管理员微信扫码登录
- 把想跟踪的公众号订阅进来
- 后台自动轮询已订阅的公众号并把文章缓存到本地数据库
- 之后查询、分析、推送都优先基于缓存库进行...

## 相关实体

[[Docker]], [[GitHub]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念


