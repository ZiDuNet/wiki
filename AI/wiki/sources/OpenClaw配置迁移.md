---
tags: [OpenClaw, Agent, 飞书, API, Skill]
source: "大刘AI编程"
created: 2026-04-27
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw配置迁移

> 来源: [大刘AI编程](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487634&idx=1&sn=e8d8bb0d57141082a3425d125f90a747&chksm=97cca56bbe0bf0bb254ef3f5d07acbe9b85bfdf581d168f360b2544cdaf31eb183bdba25d526&mpshare=1&scene=1&srcid=0427R7DqTbc6GweQFSAE5B7e&sharer_shareinfo=6720374a2c1b4c2b52192eb969cf6fe3&sharer_shareinfo_first=6720374a2c1b4c2b52192eb969cf6fe3) | 2026-04-27

## 摘要

大家好，我是大刘。
之前咱们玩 AI，大多是把它当个“加强版搜索聊天框”。但随着 Hermes 这种 Agent 框架的成熟，玩法变了——**我们不再是调教一个 AI，而是要像带团队一样，指挥一群 AI。**
想象一下：一个 Agent 埋头写代码，另一个 Agent 负责评审找 Bug，你只需要在群里发号施令。
今天，我就手把手把这个“一人团队”组建起来。
前文[全流程图文部署！把 Hermes 塞进你的微信、飞书和 TG，打造 24 小时在线的 AI 助手](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487542&idx=1&sn=c86b8c3256fb739ade5cd31ed2ce7ac0&scene=21#wechat_redirect)已经详细讲解了具体的安装步骤了。
如果你之前在同一台机器跑过 OpenClaw，那么一条命令平迁：
会把
下的配置全部迁到
，冲突默认 skip。
迁移完之后，习惯性动作是跑一下
检查身体。
按照提示执行：
此时还报MiniMax不通？
执行
，我看正常对话是没有问题...

## 相关实体

[[Hermes]], [[OpenClaw]], [[微信]], [[飞书]]

## 相关概念

[[Multi-Agent]], [[代码生成]]
