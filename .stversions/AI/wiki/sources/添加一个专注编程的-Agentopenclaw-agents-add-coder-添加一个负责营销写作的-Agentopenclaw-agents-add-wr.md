---
tags: [OpenClaw, Agent, Claude, 飞书, API, Python, OpenAI]
source: "听风观潮记"
created: 2026-04-21
updated: 2026-05-10
category: OpenClaw
---

# 添加一个专注编程的 Agentopenclaw agents add coder# 添加一个负责营销写作的 Agentopenclaw agents add writer# 查看已创建的 Agent 列表openclaw agents list

> 来源: [听风观潮记](https://mp.weixin.qq.com/s?__biz=MzA3NzkxNDc1Ng==&mid=2650358409&idx=1&sn=68865d4ffd9c608b34f34c7d328f34a0&chksm=866e39bc20ab7980f7ae1806de6f71d5e961472569999f3b90578cd1550be781ea2124370f06&mpshare=1&scene=1&srcid=0421ABRU6B2e1XEZN9ESCuxk&sharer_shareinfo=6dec456f8b7f35f27128b8ead14738be&sharer_shareinfo_first=6dec456f8b7f35f27128b8ead14738be) | 2026-04-21

## 摘要

不管用的是 Qwen、Kimi 还是其他模型，都有个绕不开的限制：**上下文窗口是有限的。**
"上下文窗口"是什么？简单理解，就是 AI 一次性能"装进脑子"的信息量上限。就像人脑的短期记忆容量有限，AI 能同时处理的文字数量也有个天花板。
这个天花板意味着什么？
丢给 AI 一份 50 页的招标文件，让它写技术方案。写到一半，上下文快满了，它开始"失忆"——前面定的框架、提的要求，记不住了。
上午让它写严肃的商业方案，下午让它帮忙制定旅行计划。模型可能因无法立刻切换语气，之前的对话历史还在上下文里待着，从而给出违和的回答。
工作时需要它写严谨的技术文档，下班后想让它帮忙想个朋友圈文案。同一个 AI 很难立刻切换不同的角色。
这些问题的根源就一个：**单个 AI 的上下文窗口再大，也扛不住复杂任务的消耗。**
OpenClaw采用了这样一套机制来应对这些问题：记忆系统 + 多 Agent 编排。
OpenClaw 的记忆系统基于"文件即真相"的思想，主要由两层组成。
**长期记忆（MEMORY.md）** 存放精选持久化偏好、配置决定与沉淀经验，放在工作区根目录。
有个安全机制：ME...

## 相关实体

[[Claude]], [[Gemini]], [[OpenAI]], [[OpenClaw]], [[Python]], [[Qwen]], [[飞书]]

## 相关概念

[[MultiAgent]], [[内容创作]], [[记忆系统]]
