---
tags: [Hermes, Agent, Claude, MCP, GitHub, Obsidian, 飞书, PPT]
source: "鸟窝聊技术"
created: 2026-04-28
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 提供了大量的斜杠命令和内置的Skill——不仅打通了 Telegram、Discord、飞书等多个消息平台，还在会话管理、技能系统和记忆机制上引入了不少新玩法。今天我把 Hermes 的斜杠命令体系完整梳理一遍，按使用频率分类，方便大家各取所需。

> 来源: [鸟窝聊技术](https://mp.weixin.qq.com/s?__biz=MzU2ODc4NzUxMg==&mid=2247490356&idx=1&sn=370b1094a35235a20b1b71a34cec4c80&chksm=fd45d448c9ad50024fcf184411956b16779ddaf696bfb4c146e744c40159201dc17a9afabbd6&mpshare=1&scene=1&srcid=0428ZWcWQUEHb32fJAZyonrn&sharer_shareinfo=9174e34d36721fb2dcd3b3f6063e5137&sharer_shareinfo_first=9174e34d36721fb2dcd3b3f6063e5137) | 2026-04-28

## 摘要

Hermes Agent 提供了大量的斜杠命令和内置的Skill——不仅打通了 Telegram、Discord、飞书等多个消息平台，还在会话管理、技能系统和记忆机制上引入了不少新玩法。今天我把 Hermes 的斜杠命令体系完整梳理一遍，按使用频率分类，方便大家各取所需。
• • •
开一个新会话，
是别名。如果想换模型，直接
或者
都可以，支持模糊匹配。
执行后：清空会话历史、重置会话 ID、清除会话级别的模型覆盖和安全状态，全新开始。
切换当前会话的模型，支持多种方式：
- ❋直接切换：
- ❋跨 provider 切换：
（切换到 zai provider 的 glm-5）
- ❋自定义端点：
或
（命名自定义 provider）
- ❋自动检测：
（自动从端点识别模型）
加上
参数，把模型设置永久写入
。
对话太长、上下文快撑不住的时候用。它会把当前会话的上下文压缩一遍，同时可以指定重点保留什么。

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Gemini]], [[GitHub]], [[Hermes]], [[LoRA]], [[MCP]], [[Notion]], [[Obsidian]], [[OpenAI]], [[OpenRouter]], [[Python]], [[Vercel]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[DevOps]], [[MCP协议]], [[TDD]], [[事件驱动]], [[代码审查]], [[工作流自动化]], [[微调]]
