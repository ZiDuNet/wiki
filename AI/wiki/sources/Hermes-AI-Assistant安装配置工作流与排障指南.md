---
tags: [Hermes, Agent, GitHub, Prompt, API, Python, OpenAI, Skill]
source: "AI拉呱"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# Hermes AI Assistant：安装、配置、工作流与排障指南

> 来源: [AI拉呱](https://mp.weixin.qq.com/s?__biz=MzI3NDE5MjExOQ==&mid=2650986900&idx=1&sn=61865396ad393fbb9730a24a7a138d79&chksm=f1cc7c6da3259c6ebf5c682ac3327d4642671fdb649c76c07c4c1a47f5b2a4caf64c32ef6717&mpshare=1&scene=1&srcid=0422yClCKLFggzcr7Xzero9l&sharer_shareinfo=8ea71d208dafb4cb0172a76b7eec679e&sharer_shareinfo_first=8ea71d208dafb4cb0172a76b7eec679e) | 2026-04-22

## 摘要

Hermes Agent 是一个可自托管、模型无关（model-agnostic）的 AI 助手：你可以把它跑在本地机器或低成本 VPS 上，通过终端与消息渠道使用，并通过“技能 + 记忆”把重复任务沉淀成可复用能力，让它越用越顺手。
它最有价值的打开方式，不是“偶尔打开一个聊天窗口问两句”，而是把它当作一层长期运行的基础设施：当 Hermes 作为服务稳定运行、并拥有固定的 home 目录之后，你的提示词会越来越像“运维（ops）”，而不是“聊天（chat）”。
Hermes Agent 是一个开源 AI agent，设计目标是：持久运行、能用工具（终端、文件、网页等），并通过技能与记忆系统持续改进自己的行为。
有两个设计选择特别关键，因为它们决定了你后续的使用方式：
1. 1. **不绑定单一模型厂商**：官方流程支持多种模型提供方，也支持任何 OpenAI-compatible 的端点。切换模型主要通过
完成，而不是改代码。
2. 2. **清晰区分“对话”和“执行”**：你可以聊很久，但一旦要做事，必须通过显式工具与可配置的执行后端来完成。安全性、可复现性、排障能力主要都在这一...

## 相关实体

[[Docker]], [[GitHub]], [[Hermes]], [[OpenAI]], [[Python]]

## 相关概念

[[记忆系统]]
