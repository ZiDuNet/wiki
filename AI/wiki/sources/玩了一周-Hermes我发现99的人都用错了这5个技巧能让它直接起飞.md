---
tags: [Hermes, Agent, Claude, MCP, API, OpenAI, Skill, OpenClaw]
source: "元小二学AI"
created: 2026-05-05
updated: 2026-05-10
category: Hermes
---

# 玩了一周 Hermes，我发现99%的人都用错了！这5个技巧能让它直接起飞！

> 来源: [元小二学AI](https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=2650841433&idx=1&sn=e87be00199e2fd6b6f4d9044f17f2c5c&chksm=f02a1be7083f333daebcaa0c2ddd4580055267faf7e8fd647021c61077397d151feb2a42d8ab&mpshare=1&scene=1&srcid=05053ECBqyN2FYe7NPoDQtUQ&sharer_shareinfo=fe940d10d75033c6359e009703fbf696&sharer_shareinfo_first=fe940d10d75033c6359e009703fbf696) | 2026-05-05

## 摘要

你好，我是元小二，专注分享 AI 提效、一人公司实践和个人成长。这里有 OpenClaw、Claude Code、自动化流程、虚拟产品，也有理财、思考和生活系统。
欢迎关注，也欢迎后台留言告诉我，你对哪部分内容感兴趣。
我之前也是随便装一下，跑两句话就扔在那里吃灰，觉得”跟其他工具也差不多”。直到我认真研究了它的底层逻辑，才发现——我之前根本不算在用它，我只是在用一个皮。
下面这 5 个技巧，是我踩了无数坑之后总结出来的，送给你。
Hermes 最聪明的设计，绝大多数人直接忽略掉了。
它把任务拆成了 **8 个独立槽位**（官方叫 auxiliary task slots），每个都能单独指定模型。这不是花架子，这是真正省钱的关键。
核心原则就一句话：**主模型用重炮负责思考，辅助任务全扔给廉价快枪。**
|  |  |  |
| --- | --- | --- |
| 槽位 | 推荐模型 | 理由 |
| Title Gen（标题生成） | `google/gemini-3-flash-preview` | 约 $0.10/M，便宜到离谱，**强烈建议改** |
| Vision（图片...

## 相关实体

[[Anthropic]], [[ChatGPT]], [[Claude-Code]], [[Claude]], [[Hermes]], [[MCP]], [[OpenClaw]], [[OpenRouter]]

## 相关概念

[[AI-Agent]], [[内容创作]], [[记忆系统]]
