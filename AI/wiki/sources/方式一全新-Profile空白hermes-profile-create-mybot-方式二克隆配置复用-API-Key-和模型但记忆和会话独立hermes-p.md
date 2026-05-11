---
tags: [Hermes, Agent, Claude, MCP, API, Python, OpenAI, Skill]
source: "智客随笔"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# 方式一：全新 Profile（空白）hermes profile create mybot# 方式二：克隆配置（复用 API Key 和模型，但记忆和会话独立）hermes profile create work --clone# 方式三：完整克隆（包含记忆、会话、技能等更多状态）hermes profile create backup --clone-all

> 来源: [智客随笔](https://mp.weixin.qq.com/s?__biz=MjM5MjA2MDQxMg==&mid=2448720216&idx=1&sn=7c71c331554b720625cc0f1c2a6605d6&chksm=b32a6ffde58c965d8b780f0b46eec6d01c7da4314e57042e4077f887a5bfd44317944d83b741&mpshare=1&scene=1&srcid=0421jc0Gpu51zFuPKyrBZwZ1&sharer_shareinfo=cc7d8e7bc331bc6155abe11b8df5587c&sharer_shareinfo_first=cc7d8e7bc331bc6155abe11b8df5587c) | 2026-04-21

## 摘要

多 Agent 协作与生产化部署
Hermes 对子 Agent 并发做了保护性限制，实战中不建议一上来就把并发拉得太高。
对大多数在线模型场景，**更稳妥的起点仍然是 2~3 个子 Agent**，再根据额度、限流情况和结果质量逐步调整。
**专家建议：在实际使用中，并发数不建议超过 3 个。**
特别是当使用官方 API 时，建议从 2 个起步，以防止触发 API 平台的 Rate Limit 或被封禁 IP，从而影响正常任务的执行。在实战中，追求理论最大并发往往不如控制成本与上下文质量重要。
Hermes 支持主 Agent 通过
等方式派生子 Agent 执行拆分后的任务。
**基本用法（在对话中引导主 Agent）：**
**子 Agent 往往从一个新的会话上下文开始，它并不会天然继承主 Agent 的完整历史。**
因此，你必须在
字段中把子 Agent 所需的背景信息传完整：
**最重要的经验：不要假设子 Agent 知道"这个错误""刚才那个文件""上一步那个思路"是什么。**
Profile 是一个完全隔离的 Hermes 环境。每个 Profile 都有自己独立的...

## 相关实体

[[Docker]], [[Hermes]], [[MCP]], [[Python]]

## 相关概念

[[MCP协议]], [[Multi-Agent]], [[记忆系统]]
