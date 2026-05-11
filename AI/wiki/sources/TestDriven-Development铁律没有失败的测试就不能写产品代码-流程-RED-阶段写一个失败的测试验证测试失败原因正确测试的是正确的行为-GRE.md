---
tags: [Skills, Agent, GitHub, Prompt, API, Skill]
source: "角角的 AI 思考"
created: 2026-04-21
updated: 2026-05-10
category: Skills
---

# Test-Driven Development铁律：没有失败的测试，就不能写产品代码。## 流程### RED 阶段写一个失败的测试，验证：- 测试失败原因正确- 测试的是正确的行为### GREEN 阶段写最小代码让测试通过，验证：- 所有测试通过- 没有为了通过测试而写的多余代码### REFACTOR 阶段在测试保护下重构清理，然后回到 RED 继续下一个行为。## 技术细节### 测试先行原则如果用户说"先写代码再加测试"：1. 告诉他们这是不允许的2. 如果代码已存在，删除它3. 从测试重新开始你不能"保留参考"代码，不能"边写测试边调整"。必须亲眼看到测试失败，才能确认测试的是正确的东西。### 验证失败必须正确RED 阶段不仅要"测试失败"，还要确认：- 失败原因是你期望的- 不是因为测试写错了如果测试错误地通过了，这不是好的 RED。

> 来源: [角角的 AI 思考](https://mp.weixin.qq.com/s?__biz=MzYzMzcwNDM4OA==&mid=2247484989&idx=1&sn=ca6e9bc972fe4a014634fa15380bd242&chksm=f17cd3894e05c4c901ae6e570588dd3ef5fea8da9a46a7aa30b53dd526b2fa016826e0cf0a4b&mpshare=1&scene=1&srcid=0421nPADJYC3EYg8QeshcDTD&sharer_shareinfo=3a8860cac49bb37d16ff7fe00bd14f29&sharer_shareinfo_first=3a8860cac49bb37d16ff7fe00bd14f29) | 2026-04-21

## 摘要

用AI写代码，最怕什么？
不是AI不会写，是AI不听劝。用户说"帮我加个功能"，AI立刻开写，不问需求、不做设计、不管边界。写完就跑，不写测试、不做检查、不考虑回归。
这些问题，源于AI的训练目标：**生成看起来合理的代码**。而软件工程的核心是**流程和纪律**，这两者之间存在根本矛盾。
Jesse Vincent（Carton创始人，Perl6语言设计者）提出的Superpowers框架，给出了他的答案：**把软件工程的最佳实践封装成可自动触发的技能**。
本文从GitHub源码提取核心设计文档，逐段解析Superpowers的技术架构。下面是里面的skill截图，大家有兴趣可以去github上下载使用。
Superpowers的技能以固定格式存储在
文件中。每个技能包含两个核心字段：
**name 字段**是技能的唯一标识，引用格式为
。
**description 字段**采用"触发条件"写法，明确说明在什么场景下必须使用这个技能。例如：
这种写法让AI能自动判断何时需要加载技能，而不需要用户手动提示。
Frontmatter之后是Markdown格式的正文，通常包含：
- *...

## 相关实体

[[GitHub]], [[Markdown]]

## 相关概念

[[Prompt工程]], [[TDD]], [[代码审查]]
