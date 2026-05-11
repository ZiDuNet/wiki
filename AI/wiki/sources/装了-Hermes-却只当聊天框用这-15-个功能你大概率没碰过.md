---
tags: [Hermes, Agent, Claude, GitHub, 飞书, Prompt, API, OpenAI]
source: "云起泊言"
created: 2026-04-29
updated: 2026-05-10
category: Hermes
---

# 装了 Hermes 却只当聊天框用？这 15 个功能你大概率没碰过

> 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868914&idx=1&sn=f716475e83811c3d7b35a191c7587d6d&chksm=86351b1354bf2d086ae3f8366e9a7e80eee65900a8807fef934cfe010444ef3049d65b8ee230&mpshare=1&scene=1&srcid=0429PJyMomdeJK1K9lSlDzzP&sharer_shareinfo=15d3f7a0b0eac3aa7910a69902b3b202&sharer_shareinfo_first=15d3f7a0b0eac3aa7910a69902b3b202) | 2026-04-29

## 摘要

很多人装 Hermes，接上飞书，配个模型，打字问问题、收回答，然后关窗口。我刚开始也是这么用的。后来才发现，这么搞大概只用到了 Hermes 8% 的能力。
有国外大佬列了 15 个大多数用户从没碰过的功能，我挑了翻译过来，加上我自己的理解和使用感受，按实际价值排了个序。
Hermes 启动时会读一个文件叫 SOUL.md。你在里面写什么，它就变成什么。语气、拒绝范围、写给谁看——全部写一次就行。
配合 `/personality` 命令，对话中途都能切换人格。
大多数人的做法是每次开新对话都重新打一遍"你是一个资深 XX 专家"。我之前也干过这事。后来才知道，把这段话写进 SOUL.md，一劳永逸。
两个持久化文件，每次会话 Hermes 都会读。
MEMORY.md 是它对你项目的记忆，USER.md 是它对你的了解——你的角色、语气偏好、权衡取舍。而且这俩文件都有 FTS5 索引和 LLM 摘要，8 周前的一条记忆今天都能被拉出来用。
现实情况是，大多数人每次开新聊天都要重新介绍自己是谁、在做什么项目。
这个命令能看到你所有会话的分析数据：哪个项目烧了最多 token、各 pr...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[DeepSeek]], [[GPT-5]], [[Gemini]], [[GitHub]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[OpenRouter]], [[Vercel]], [[微信]], [[钉钉]], [[飞书]]

## 相关概念

[[TDD]]
