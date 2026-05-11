---
tags: [飞书, Agent, Claude, API, Python, Skill]
source: "AI编程瓜哥"
created: 2026-04-13
updated: 2026-05-10
category: 飞书
---

# 安装飞书CLInpm install -g @larksuite/cli

> 来源: [AI编程瓜哥](https://mp.weixin.qq.com/s?__biz=Mzk5MDcyODQ2Mw==&mid=2247493435&idx=1&sn=59458b13858bbd6897c9f7f5b294e735&chksm=c404781b72495f21b1a3f0dd6d809ea1683850040143fcb478e0c71821d47e084cca59d77ab7&mpshare=1&scene=1&srcid=0413MwIFvbTkOPDxA5omNmuw&sharer_shareinfo=b7f33991892d380aadbf9b308cfbc9d6&sharer_shareinfo_first=b7f33991892d380aadbf9b308cfbc9d6) | 2026-04-13

## 摘要

这是我最近被问到最多的问题。
**既然飞书有 2500 多个 API，直接让 AI 写个 Python 脚本去调不就行了，为什么要用这个 CLI？**
确实，传统的飞书 API 很全，但那是给人类看的。对于 Agent 来说，直接调 OpenAPI 的体验非常差。
你要传海量的文档上下文给它，它还经常把
和
搞混，甚至在分页处理时逻辑直接断掉。
的出现，它把飞书全家桶封装成了 19 个的 Skill。
本质上是在做 **Agent-Native** 的基础设施。
它的核心逻辑不是 '**能不能做**'，而是 **在多低成本下，能做到什么程度 ？**
| 维度 | 传统 OpenAPI 调用 | lark-cli AI Skills |
| --- | --- | --- |
| **集成成本** | 需要 AI 理解数千行文档，写请求代码 | 一条结构化指令（如 `+agenda`）直接交付结果 |
| **Token 消耗** | 极高，需要携带大量 API 定义和 Schema | **极低** ，压缩后的 Skill 定义，仅保留核心参数 |
| **执行成功率** | 中等，A...

## 相关实体

[[Claude-Code]], [[Claude]], [[Gemini]], [[Markdown]], [[Node.js]], [[Python]], [[飞书]]

## 相关概念

[[代码生成]], [[工作流自动化]]
