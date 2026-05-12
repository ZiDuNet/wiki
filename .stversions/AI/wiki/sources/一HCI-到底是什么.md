---
tags: [Hermes, Agent, GitHub, API, Python, Skill]
source: "AI 趋势方向"
created: 2026-05-04
updated: 2026-05-10
category: Hermes
---

# 一、HCI 到底是什么？

> 来源: [AI 趋势方向](https://mp.weixin.qq.com/s?__biz=MzU5MTkyMzY4NQ==&mid=2247483692&idx=1&sn=ecd66967aa48e51fd1a365d0d1322040&chksm=ffb6cffa2ddbc953623c51bffa43981db2b4ec67bca0956a7cd79f2c9afba95cf4fdfd60d730&mpshare=1&scene=1&srcid=05040iYwAvDBOJ6yYMyT5vCL&sharer_shareinfo=cb1d24298f2279352a45b1ba13b29b96&sharer_shareinfo_first=cb1d24298f2279352a45b1ba13b29b96) | 2026-05-04

## 摘要

Hermes 又多了一个控制台：不只是 WebUI，而是偏生产级的 Agent 管理后台
如果你已经开始用 Hermes Agent，会慢慢遇到一个问题：
一个 Agent 好管理，多个 Agent 就开始乱。
尤其当你有多个 profile、多条 gateway、多个会话、定时任务、memory、skills、文件、token 成本、团队成员权限时，纯命令行会越来越吃力。
最近看到一个项目：
hermes-control-interface (https://github.com/xaspx/hermes-control-interface)
它不是简单给 Hermes 套一个聊天网页。
它更像是：
给 Hermes Agent 做了一个偏生产级的控制后台。
项目名叫：
Hermes Control Interface
简称 HCI。
当前 README 标注版本是：
v3.5.0
技术栈是：
Vanilla JS + Vite
Node.js
Express
WebSocket
xterm.js

## 相关实体

[[GitHub]], [[Hermes]], [[Nodejs]], [[Python]]

## 相关概念

[[MultiAgent]]
