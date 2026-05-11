---
tags: [Agent, Claude, MCP, API, Skill, OpenClaw]
source: "悟鸣AI"
created: 2026-04-27
updated: 2026-05-10
category: Agent
---

# 给 AI Agent 装上一双会看网页的眼睛：Dokobot Skill 体验

> 来源: [悟鸣AI](https://mp.weixin.qq.com/s?__biz=Mzg3NzI0MzAyNA==&mid=2247493315&idx=1&sn=8cff76d164225c60720f4dbcb5a6ef2b&chksm=ce776dc6b9c9be158808567eb74537c9c769b8fd40d17763ba5bc345875517ba3a56fc4b0cd7&mpshare=1&scene=1&srcid=0427sBS1HseClatWuSzgM3Yp&sharer_shareinfo=d7f5484b1301284430c787d0c8362f08&sharer_shareinfo_first=d7f5484b1301284430c787d0c8362f08) | 2026-04-27

## 摘要

大家好，我是悟鸣。
如果你最近也在折腾 AI agent，大概率会遇到一个很现实的问题：
很多 agent 看起来会“上网”，其实只是会发 HTTP 请求。
这在简单页面上问题不大，但一旦网页是前端渲染的，或者需要登录、滚动、交互，这种能力就很容易不够用了。页面能打开，不代表 agent 真能读懂；接口能返回，也不代表它拿到的是用户真正看到的内容。
这也是我最近看到 Dokobot 时，觉得它挺有意思的原因。
官网：https://dokobot.ai
它想解决的，不是“怎么让 agent 再多发几个请求”，而是一个更底层的问题：
怎么让 agent 真正看见网页。
Dokobot 的思路很直接。它不是再给 agent 包一层更花哨的
，而是直接让 agent 借助真实的 Chrome 浏览器去读网页、搜网页。换句话说，它处理的不是一份冷冰冰的网页源码，而是用户眼前那个已经渲染好的页面。
这一点非常关键。
因为很多我们平时觉得“网页就在那”的内容，其实对 agent 并不天然可见。内容可能是 JS 动态加载出来的，可能要登录之后才能看到，也可能得滚动几屏才会完整出现。用普通抓取方式做这...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Hermes]], [[MCP]], [[Markdown]], [[OpenClaw]], [[Qwen]]

## 相关概念


