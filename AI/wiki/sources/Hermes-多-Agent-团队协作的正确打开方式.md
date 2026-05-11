---
tags: [Hermes, Agent, 飞书, API, Skill, OpenClaw]
source: "云起泊言"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# Hermes 多 Agent 团队协作的正确打开方式

> 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868631&idx=1&sn=9b4210e367d4e69335bdb29839fe901d&chksm=86069f6c3975542d995c0f7738c9fb20683c1eaef5a8b321e4ebb83c0d5953b38dcc3442e0d5&mpshare=1&scene=1&srcid=0422zTmaMgdnYUBmWiy96uQa&sharer_shareinfo=7fe5029f8604d0e0fb3977e8c7950858&sharer_shareinfo_first=7fe5029f8604d0e0fb3977e8c7950858) | 2026-04-22

## 摘要

平常我们在使用 **OpenClaw** 跟 **Hermes** 的时候，是不是经常在一个会话中既让它干这又让它干那，比如我的话又是让它写作又是让它帮我出计划写代码，难免会导致上下文的记忆混乱，我让它写代码呢突然给我飙出来一段关于写文章的
而且一次只能处理一个任务，在执行过程中如果想让它同时干别的事，就只能干等着
那么能不能同时有多个Agent，各司其职，互不干扰：
- 子任务 A：负责写作
- 子任务 B：负责写计划、出PRD
- 子任务 C：根据PRD进行编码
这里就要说一下 Hermes 的 **Profiles**功能：可以在同一台机器运行多个独立的Hermes
**Profile** 是一个完全隔离的 Hermes 环境。
- 每个 Profile 都有自己独立的配置、记忆、会话和技能；
- 底层通常是通过单独的 HERMES\_HOME 路径来实现目录级隔离 。
但要注意，默认 profile 仍然是
； 只有你创建并切换到命名 Profile 时，相关配置、记忆、技能、会话和日志等才会跟随当前 HERMES\_HOME 切到
这类路径。
那么我来说一下创建过程吧~
双引...

## 相关实体

[[Hermes]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念


