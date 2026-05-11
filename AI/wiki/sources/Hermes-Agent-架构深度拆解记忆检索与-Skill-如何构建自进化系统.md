---
tags: [Hermes, Agent, Claude, Obsidian, Prompt, API, OpenAI, Skill]
source: "探寻AIGC"
created: 2026-04-30
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 架构深度拆解：记忆、检索与 Skill 如何构建自进化系统

> 来源: [探寻AIGC](https://mp.weixin.qq.com/s?__biz=MzkzODY5NTYyMA==&mid=2247483953&idx=1&sn=2e5f5f5c678f036dbf6e6b27689ce605&chksm=c3df4149b44969b72e664cfd2a279c3385362ca7657fbd1d4f90553e73c2bc75b8fc7c998874&mpshare=1&scene=1&srcid=0430P5hm0ZaynetOKyl5yTnG&sharer_shareinfo=42c67ef75ab8376803286eb384a29d87&sharer_shareinfo_first=42c67ef75ab8376803286eb384a29d87) | 2026-04-30

## 摘要

用过 ChatGPT 或 Claude 的朋友都有这种体验：每次新开对话，AI 都像个"陌生人"，完全不记得你们之前聊过什么。
这不是技术限制，而是**架构设计的选择**。
大多数 AI 助手采用"无状态"设计——每次请求都是独立的，服务器不会保存你的对话历史。好处是成本低、响应快，坏处就是**没有记忆**。
一些进阶方案尝试用"向量数据库"存储历史对话，但效果并不理想：
- 检索精度低，经常召回不相关内容
- 存储成本高，历史数据越积越多
- 缺乏结构化，重要信息淹没在海量记录中
**Hermes 的解决思路完全不同**：不是简单地"存储更多"，而是设计了一套分层的记忆架构，让 AI 像人脑一样工作。
Hermes 把记忆分成三层，每层有明确的职责、存储位置和读取时机：
| 层级 | 名称 | 存储内容 | 容量 | 读取方式 |
| --- | --- | --- | --- | --- |
| 第一层 | 热记忆 | 当前会话上下文、系统提示词 | 8K tokens | 每次请求自动加载 |
| 第二层 | 温记忆 | MEMORY.md（环境/经验/约定）| ~800 tok...

## 相关实体

[[ChatGPT]], [[Claude]], [[Hermes]], [[Markdown]], [[Notion]], [[Obsidian]], [[OpenClaw]], [[SQLite]]

## 相关概念

[[嵌入向量]], [[自进化系统]], [[记忆系统]]
