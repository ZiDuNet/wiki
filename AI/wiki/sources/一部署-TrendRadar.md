---
tags: [Hermes, Agent, MCP, 飞书, API, OpenClaw]
source: "可爱的小Cherry"
created: 2026-04-28
updated: 2026-05-10
category: Hermes
---

# 一、部署 TrendRadar

> 来源: [可爱的小Cherry](https://mp.weixin.qq.com/s?__biz=MzA4NzMyNzU5Mg==&mid=2453077562&idx=1&sn=4a527e4ce85dff34d7d1bef1f9f934c3&chksm=8684cde88790fe26d06324ad0639cc750d32de81738426439c7a6bfc752b5c609cee3dc540e6&mpshare=1&scene=1&srcid=0428lRwlp85JCxVkhIYM5ySj&sharer_shareinfo=c801a427b0a99b0d89bbb136e404c102&sharer_shareinfo_first=c801a427b0a99b0d89bbb136e404c102) | 2026-04-28

## 摘要

大家的 OpenClaw、Hermes 跑了几个月了，有没有什么有意思的玩法呢？
我日常除了远程开发一些脚本、聊聊天之外。
还把它们拿来做新闻汇集的工具。每天早、中、晚做个定时任务，自动汇总最近几个小时的国内外新闻，根据我的需要做个提取，然后通过 bark、飞书等 IM 频道定时发送到手机上。
打开手机看看有没有自己感兴趣的，没有就一带而过，有就让 Agent 继续给我更多的信息内容。
每天翻新闻网站的时间节约下来了，不需要从海量的信息里去专门看自己感兴趣的。
OpenClaw、Hermes，直接根据我的需求和爱好，自动判断哪些新闻有价值、哪些新闻我爱看，帮我分门别类。
这一套服务，是基于一个很火的 AI 新闻项目 —— TrendRadar 。
聚合多平台热点 + RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 + AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。
两套服务一共包含两个容器，TrendRadar 主容器用于 AI 热点筛选和新闻检索，TrendRadar MCP 容器用于将主服务向外提供 标准...

## 相关实体

[[DeepSeek]], [[Hermes]], [[MCP]], [[OpenClaw]], [[飞书]]

## 相关概念


