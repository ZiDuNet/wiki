---
tags: [GitHub, Agent, Claude, PPT, RAG, Prompt, Skill]
source: "逛逛GitHub"
created: 2026-04-30
updated: 2026-05-10
category: GitHub
---

# 推荐 3 个 GitHub 画图 Skill，一句话生成流程图、架构图。

> 来源: [逛逛GitHub](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533360&idx=1&sn=1847cadb7dbb7224a9a692729b8db51e&chksm=f8a15ce0878228fdf7680ea441b21ee5d323bb8c5f9694e8674f8700d5f57da9066c6976b156&mpshare=1&scene=1&srcid=0430Xiw3WVqgUOWlXxgVVd2w&sharer_shareinfo=663e07306f704a500dfbca8d03a3490b&sharer_shareinfo_first=663e07306f704a500dfbca8d03a3490b) | 2026-04-30

## 摘要

01
**一句话画出能直接发布的技术图**
最近在 GitHub 上翻到一个画图的 Skill，叫 fireworks-tech-graph，目前已经攒到了 3.6k Star。
这个项目干的事情说白了就是：你用大白话描述一下想要的图，它帮你生成 SVG，再导出成高清 PNG，直接就能塞到博客或者 PPT 里。
我看了一下它的能力矩阵，还挺顶的。
一共支持 14 种图表类型，UML 全家桶都有，还专门做了 AI/Agent 方向的模板。
比如 RAG pipeline、多 Agent 协作流程这种，在国内写 AI 相关内容的场景特别实用。
视觉风格也有 7 种可选，暗黑终端风、科技线稿风、手绘风都能切。
同一张图换个风格再生成一次就行，不用自己动手改样式。
它是个 Claude Code 的 Skill，装起来一行命令:
Mac 上还要 `brew install librsvg` 装一下底层依赖，用来把 SVG 转成 PNG。
装完之后，直接跟 Claude 说给我画一张 RAG pipeline 的流程图，用暗黑终端风格，几秒钟就给你一张能直接用的图。
02
**Architect...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]], [[微信]]

## 相关概念

[[Multi-Agent]], [[微调]]
