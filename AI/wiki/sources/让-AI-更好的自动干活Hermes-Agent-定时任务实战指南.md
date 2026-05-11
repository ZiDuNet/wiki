---
tags: [Hermes, Agent, 飞书, PPT, Prompt, Skill, OpenClaw]
source: "Colin的AI指南"
created: 2026-04-23
updated: 2026-05-10
category: Hermes
---

# 让 AI 更好的自动干活：Hermes Agent 定时任务实战指南

> 来源: [Colin的AI指南](https://mp.weixin.qq.com/s?__biz=MzUxNzE2NTU5MQ==&mid=2247483758&idx=1&sn=d2d6cedd9a313432edec2114e891722d&chksm=f86a07068b4e06a6f81ec8fc4dcf8891c4202567d6d4b0e0bcddc883f047d9c6258401855e90&mpshare=1&scene=1&srcid=0423t5gn9IwbkO6FmZUpFBL6&sharer_shareinfo=b28cfd269719481091449da5fb0d2c27&sharer_shareinfo_first=b28cfd269719481091449da5fb0d2c27) | 2026-04-23

## 摘要

在上一篇文章中，我们讨论了如何在本地安装部署 Hermes Agent，今天我们继续讨论下：怎么更好地使用 Hermes。
相信很多人跟我一样，使用 Hermes 或者 OpenClaw 的时候，经常会用到的一个场景就是：设置定时任务，让 Hermes 或者 OpenClaw 定时的处理一些工作内容或者任务，完成任务之后再通知我们，这就是定时任务。
这篇文章，我们一起来看看，什么是 Hermes 定时任务的正确打开方式。
在开始实际的使用前，我们先来了解一下 Hermes 的定时任务是怎么运作的：
Hermes 提供了一个内置的 Cron 调度器，允许 Agent 在后台"无人值守"地运行任务，并将结果推送到任何集成的通讯平台（如 飞书、微信、Telegram、Discord 等），支持我们通过自然对话或者修改配置文件来设定及处理定时任务。
定时任务的执行由网关（Gateway）守护进程处理，每 60s 会触发一次检查，判断定时任务是否需要执行，如果有需要执行的定时任务，就进行处理。
所有的定时任务都保存在 ~/.hermes/cron/jobs.json 文件下，你也可以在 Herm...

## 相关实体

[[Hermes]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念


