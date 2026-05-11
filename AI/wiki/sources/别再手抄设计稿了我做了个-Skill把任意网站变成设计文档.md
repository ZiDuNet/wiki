---
tags: [Skills, Agent, Claude, MCP, GitHub, RAG, Prompt, Skill]
source: "野生阿飞"
created: 2026-05-05
updated: 2026-05-10
category: Skills
---

# 别再手抄设计稿了：我做了个 Skill，把任意网站变成设计文档

> 来源: [野生阿飞](https://mp.weixin.qq.com/s?__biz=MzI4OTU2NzY3MQ==&mid=2247483754&idx=1&sn=1fdd8d2991266b3677e10c0fb7334f18&chksm=ed2c220ab9bfc65ba85b8053331b1e7395a9c7adfaa26505bdfe0d4e73740e5fcd4877c912d5&mpshare=1&scene=1&srcid=0505Yw1e8Ps4poJOEcnZTKXQ&sharer_shareinfo=13f0f40985fc412dc3201adfd45a0670&sharer_shareinfo_first=13f0f40985fc412dc3201adfd45a0670) | 2026-05-05

## 摘要

最近我一直在想一个问题：
**为什么 Agent 写代码越来越快，但写出来的页面还是经常不好看？**
不是功能不对。
功能通常没问题。
你让它写一个 landing page、一个 pricing page、一个 dashboard，它能很快把结构、组件、交互都搭出来。
但打开页面之后，经常会有一种很熟悉的感觉：
- 间距看起来不成体系。
- 字号层级像是临时凑的。
- 按钮、卡片、导航各有各的风格。
- 页面能跑，但没有成熟产品那种稳定的设计语言。
- 一眼看上去就是“AI 写的页面”。
这不是 Agent 不会写前端。
而是它缺少一份足够清楚的视觉参考。
人类设计师做页面时，脑子里有大量隐含判断：颜色怎么用、标题多大、卡片圆角多少、按钮怎么压住视觉重心、页面哪里需要留白。
但 Agent 没有这些上下文。
你只说“帮我做一个像 Linear 一样干净的页面”，它只能凭训练记忆去猜。
猜得准的时候，页面还可以。
猜不准的时候，就是一股通用 AI 味。
所以我做了一个 Skill：**website-to-design-md**。
它做的事情很简单：

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[GitHub]], [[MCP]], [[Markdown]], [[Next.js]], [[Notion]], [[Tailwind]], [[Vercel]]

## 相关概念

[[Multi-Agent]], [[Vibe-Coding]]
