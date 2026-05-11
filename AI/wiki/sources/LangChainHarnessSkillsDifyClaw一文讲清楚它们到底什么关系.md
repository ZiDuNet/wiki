---
tags: [Harness, Agent, Dify, Prompt, Python, OpenAI, Skill]
source: "橘子AI小栈"
created: 2026-04-25
updated: 2026-05-10
category: Harness
---

# LangChain、Harness、Skills、Dify、Claw：一文讲清楚它们到底什么关系

> 来源: [橘子AI小栈](https://mp.weixin.qq.com/s?__biz=MzYzOTc2ODA4Mg==&mid=2247483918&idx=1&sn=3feb5f812fdb816fcd9889bb3bc59860&chksm=f13f2b82272b6da49396d304eaba8aac90faa018cb4c29507e137bdb153fcb545d3667232dda&mpshare=1&scene=1&srcid=0425laoy4gUolm8eHQwAJN5q&sharer_shareinfo=68856789b207d5c247b1b8777a1ddfd5&sharer_shareinfo_first=68856789b207d5c247b1b8777a1ddfd5) | 2026-04-25

## 摘要

最近这两年随着AI的发展，不断的有新的技术名词冒出，26年初Harness一词又在圈内爆火，今天一篇文章讲清楚它们之间的关系
LangChain 是一个开源 Python/JS 框架，核心作用是把 N 个 LLM（大语言模型） 调用、工具、记忆、提示词串成一条"链"，让 AI 完成复杂多步骤任务。现已全面转向构建智能体应用。
主要面向开发者，门槛较高，需要写代码。
Dify（dify.ai）是一个开源 LLM 应用开发平台，核心理念是让非技术人员也能可视化构建 AI 应用。通过拖、拉、拽的方式快速搭建和部署智能体应用
面向开发者或非开发者
Harness就是大语言模型的“行车系统”，用于把 LLM 的 “智能” 转化为可靠、可落地、可生产的能力。
大模型目前的能力极强，但是还有几个致命缺点。
1、一个完整的项目往往做了3、4个功能就宣布 “项目完成”
2、代码写完了但环境有bug，模型自己不知道
3、功能清单上标注 “已完成”，但实际功能是坏的
4、每次新的运行都要重新问 “代码在哪个文件夹”
而Harness这套系统完美解决了这些问题。
2026年3月，LangChain团队做了一个...

## 相关实体

[[Dify]], [[GPT-5]], [[Harness]], [[LangChain]], [[Python]]

## 相关概念

[[AI-Agent]]
