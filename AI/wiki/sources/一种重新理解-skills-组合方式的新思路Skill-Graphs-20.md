---
tags: [Skills, Agent, Claude, Obsidian, Prompt, Skill]
source: "AI的岔路口"
created: 2026-04-24
updated: 2026-05-10
category: Skills
---

# 一种重新理解 skills 组合方式的新思路：Skill Graphs 2.0

> 来源: [AI的岔路口](https://mp.weixin.qq.com/s?__biz=MzI5NTg2OTk2Ng==&mid=2247485339&idx=1&sn=de044b3e4689235fd2d292fdba540c8f&chksm=ed1e75a8aa63362c69f57e65d2c023bec2b2559736a8ccf81c0f6165c94d21774c7a92d3aadb&mpshare=1&scene=1&srcid=0424ByUmxRGU003zSaGyqmMj&sharer_shareinfo=ebe65000a2486f3800f21b9da886c126&sharer_shareinfo_first=ebe65000a2486f3800f21b9da886c126) | 2026-04-24

## 摘要

最近我学到的一件特别有价值的事，就是如何思考“组合 skills”这件事，才能在工作里拿到更大的杠杆。
前阵子 skill graph 这个想法[1] 引起了不少兴趣。它的核心思路是：通过在 markdown 文件里把依赖技能互相链接起来，构建出一张 skill graph，就像你在 Obsidian 里把笔记互相连起来那样。
一个 skill，本质上就是把知识 + 过程编码进一个 markdown 文件里，必要时再附上一些 agent 可以反复调用的脚本。
所以直觉上，skill graph 当然很合理。只要你想把更大的流程，或者完整的岗位职能，编码成 skills，你大概率就会碰到 skills 依赖其他 skills 的情况。
举个例子，一个“起草营销邮件”的 skill，可能就会依赖一个平面设计 skill。
但问题在于：当你的 skill graph 大到一定程度之后，Agents 往往就没法稳定调用到某个深度之后的技能。依赖越多，可靠性通常就越差。（很多在 reddit 和 X 上实际尝试过这套东西的人，也都提到过这一点。）
如果 Skill A 明确写着“去调用 Skil...

## 相关实体

[[Claude]], [[Obsidian]]

## 相关概念

[[Skill编排]]
[[Skill设计模式]]
