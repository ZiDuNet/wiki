---
tags: [OpenClaw, Agent, Claude, MCP, GitHub, API, OpenAI, Skill]
source: "去玩AI"
created: 2026-04-13
updated: 2026-05-10
category: OpenClaw
---

# 突然间，又多了一个Hermes智能体。

> 来源: [去玩AI](https://mp.weixin.qq.com/s?__biz=Mzg5MzkwMTI1MQ==&mid=2247488927&idx=1&sn=aca3d59009c730207e80fb13720de44d&chksm=c1fe59465782d81e4e6ee44e4be36fecfa932a480babf06348e1c6a4f9e0bca2dc8a1422e919&mpshare=1&scene=1&srcid=0410VdTFokasgDsrBiTvbby9&sharer_shareinfo=8edb0568d43ddf44603b75b0f98421a0&sharer_shareinfo_first=8edb0568d43ddf44603b75b0f98421a0) | 2026-04-13

## 摘要

现在都在吹这个Hermes - Agent。
说它是可以自我进化的智能体。
如果你已经在用 **OpenClaw**（或早期的 Clawdbot / Moldbot 一路跟过来），最近很难不刷到 **Hermes Agent**——同一类「自托管 + 消息网关」赛道里，Nous Research 用 MIT 协议又铺了一套，并且 **官方写了从 OpenClaw 一键迁移**。
这篇只做三件事：**OpenClaw 与 Hermes 各是什么**、**同维度对比**、**Hermes 的亮点与迁移命令**（均以 官方文档 为准，不替官方吹牛）。
**OpenClaw**：社区里非常活跃的开源个人/团队 Agent 路线，多通道、技能生态（如 Clawhub）、很多人已经把它跑在 Telegram / Discord 等场景里。
**Hermes Agent**：Nous Research 出品的另一套 **自托管** 开源 Agent，同样能接 **CLI + 多种 IM**。文档里把重心放在 **持久记忆 → 任务后沉淀技能 → 跨会话再捞回来** 这一整条「闭环」上（下一节拆开讲）...

## 相关实体

[[Anthropic]], [[Gemini]], [[GitHub]], [[Hermes]], [[MCP]], [[OpenAI]], [[OpenClaw]], [[OpenRouter]], [[SQLite]]

## 相关概念

[[SOP]], [[记忆系统]]
