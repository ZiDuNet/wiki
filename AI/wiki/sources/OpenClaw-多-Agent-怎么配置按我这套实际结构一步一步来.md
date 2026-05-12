---
tags: [OpenClaw, Agent]
source: "左哥AI笔记"
created: 2026-04-20
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw 多 Agent 怎么配置？按我这套实际结构一步一步来

> 来源: [左哥AI笔记](https://mp.weixin.qq.com/s?__biz=MzY4NDIwMzY2Mw==&mid=2247483919&idx=1&sn=3f474c553314b64ce164f11f0e46b66d&chksm=f2c22b8d290e374505ec963ab429ca9d3e029be6c37053f3f041f78c81dd7ce4c767d4af12da&mpshare=1&scene=1&srcid=0420WcUgnyx6tbGhTRdqxNUZ&sharer_shareinfo=91aa3ae651cf8cfd1c7a57310caddba6&sharer_shareinfo_first=91aa3ae651cf8cfd1c7a57310caddba6) | 2026-04-20

## 摘要

很多人对 OpenClaw 多 agent 的第一反应是：
“这个我知道可以做，但到底怎么配？”
这很正常。
因为“多 agent”听起来像能力说明，但你真正上手时，卡住的都是配置问题：
- 新增一个 agent 到底要哪几步
- workspace 应该怎么建
- ```
openclaw.json
：默认主 agent，偏主管/调度角色
- ```
blog
：公众号执行 agent
- 长任务、并行任务：交给 sub-agent
你可以把它理解成：
**一个主 agent 负责接任务和验收，多个长期 agent 负责稳定执行，临时重活再交给 sub-agent。**
如果角色没想清楚，你建再多 agent，最后也只是多几份混乱。
我现在判断一个角色值不值得拆成长期 agent，主要看四件事：
- 这个工作是不是长期重复存在
- 它是不是需要独立 workspace
- 它是不是有稳定交付物

## 相关实体

[[OpenClaw]]

## 相关概念

[[Agent路由]]
[[Agent架构]]
