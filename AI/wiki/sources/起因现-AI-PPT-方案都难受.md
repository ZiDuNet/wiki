---
tags: [PPT制作, Agent, Claude, GitHub, PPT, RAG, Prompt, API]
source: "鲸选AI"
created: 2026-05-04
updated: 2026-05-10
category: PPT制作
---

# 起因：现 AI PPT 方案都难受

> 来源: [鲸选AI](https://mp.weixin.qq.com/s?__biz=MzkyMjUxOTI0Mw==&mid=2247529537&idx=1&sn=b081d27ad7ad64e5960f5b0cfa19edbe&chksm=c062a75b67024a6589dee73db98547d68a0e183f7f90520a5789f65a088288e662dddd943237&mpshare=1&scene=1&srcid=0504sNbAf1H7jSz5nXk6prp9&sharer_shareinfo=bcf7df3c965b7b501df7090fbd6f43b9&sharer_shareinfo_first=bcf7df3c965b7b501df7090fbd6f43b9) | 2026-05-04

## 摘要

近期，让我最惊讶的AI体验，可能就是用Codx做PPT，简直是太丝滑了。虽然还是此前被淘汰的模式—Html形式生成。
但生成的效果非常惊艳，而且不可编辑的顽疾也解决了，更重要的是AI 编程越来越成熟，大家都能随手生成一份网页版的PPT。
为了保证每次生成效果，我们没有做成提示词版本，而是做了一个叫 鲸格PPT 的 Skills。主要是考虑国内的很多朋友，用的是没有ChatGPT image 2加成的AI助手，通过复用Skills也许能保持下产出的平均水准。
相比很多PPT SKills ，鲸哥做的不是又一个"AI 帮你填模板"的 PPT 工具，而是一套完整的语义驱动静态演示系统。你给它任何原始素材，它先理解内容结构，再决定怎么呈现。
但这只是表面。先讲述这套Skills 的架构和原理，也许你能更懂它的优势。
这两年 AI 做 PPT 的工具井喷，从 Gamma 到各种国产方案，看起来百花齐放。但你真正用过之后会发现一个共同的问题——它们本质上都是"模板填充机"。
流程永远是：选个模板 → AI 帮你生成文案 → 塞进预设的布局里。看起来很智能，实际上你对最终呈现几乎没有控制力。想调个动...

## 相关实体

[[Claude]], [[DeepSeek]], [[GitHub]]

## 相关概念

[[AI-Agent]], [[多模态]], [[微调]]
