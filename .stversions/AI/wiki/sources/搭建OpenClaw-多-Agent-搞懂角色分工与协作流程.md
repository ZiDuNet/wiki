---
tags: [OpenClaw, Agent, 飞书, Skill]
source: "百年内无人能懂猫"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# 搭建OpenClaw 多 Agent ：搞懂角色分工与协作流程

> 来源: [百年内无人能懂猫](https://mp.weixin.qq.com/s?__biz=MzYzMTgxMDk4NA==&mid=2247483716&idx=1&sn=5ad9da485c4a0673ba5022101657bb95&chksm=f132a16f1fe7c255506940b244e4f00a30e86985a924e48b519b3f82f62cc8048e7aa21ddd80&mpshare=1&scene=1&srcid=0420bLjTKJ709Gisz7TyN2vQ&sharer_shareinfo=da2a2128171711f9db014dcf414b2ef3&sharer_shareinfo_first=da2a2128171711f9db014dcf414b2ef3) | 2026-04-20

## 摘要

很多人在安装这一步就卡住了，其实并不是因为代码太难，而是没弄明白“每一个配置选项在整个系统里到底是干嘛的”。
[windows系统本地安装部署openclaw详细版教程](https://mp.weixin.qq.com/s?__biz=MzYzMTgxMDk4NA==&mid=2247483699&idx=1&sn=c6cf1dee19d07533a25d96f3b56b72cf&scene=21#wechat_redirect)
所以，这篇内容不打算教你如何死记硬背命令，而是要帮你梳理清楚         OpenClaw的底层逻辑图。
只要你把这套关系摸透了，以后不管是换电脑安装、升级新版本还是调整配置，你都能游刃有余。
咱们换个好理解的说法来类比一下：
- **飞书 / Telegram**
：这就是公司的前台，客户从这里提需求进来。
- **OpenClaw Gateway**
：相当于总机或者是调度中心，负责接听电话并决定把活儿分给谁。
- **Agent**
：也就是干活的员工，他们才是真正动脑子、解决问题的角色。
- **Skills**
：就好比 SOP 操作手册，遇...

## 相关实体

[[OpenClaw]], [[飞书]]

## 相关概念

[[MultiAgent]], [[SOP]]
