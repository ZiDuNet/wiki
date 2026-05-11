---
type: tool
created: 2026-05-10
updated: 2026-05-11
---

# Obsidian

**类型:** 知识管理工具
**官网:** obsidian.md
**核心特性:** 本地优先、Markdown 原生、双向链接、插件生态

## 简介

Obsidian 是一款基于本地文件的 [[Markdown]] 知识管理工具，以"双向链接"（Bidirectional Links）和"知识图谱"（Graph View）为核心特色。所有数据存储在用户本地设备上，以纯文本 Markdown 文件形式存在，不依赖云服务，强调数据所有权和隐私安全。

## 在 AI 知识管理中的角色

Obsidian 在 AI Agent 生态中扮演着关键的知识基础设施角色：

### Karpathy 知识库方法

AI 大神 Karpathy 提出了一套构建 LLM Wiki 的方法论，核心是让大模型从"临时回答工具"变成"长期知识维护者"。架构分为三层：

1. **Raw Sources（原始资料层）**：收集原始素材和参考文档
2. **Structured Pages（结构化页面层）**：由 LLM 将原始资料消化成结构化 wiki 页面，概念间通过 wikilinks 互相链接
3. **Query Layer（查询层）**：在已整理的知识网上检索答案

### 与 Hermes Agent 的结合

[[Hermes]] Agent 内置了 LLM Wiki Skill，可以配合 Obsidian 使用：
- 初始化知识库目录结构
- 自动生成 wikilink 互联的页面
- 通过 Obsidian 打开同文件夹作为 Vault
- 推荐安装 Dataview 插件增强查询能力

### 关键配置

使用 Obsidian 搭建 AI 知识库时的推荐设置：
- 附件目录统一管理
- 确认 Wikilinks 功能开启（默认开启）
- 安装 Dataview 社区插件用于动态查询
- 目录结构推荐：01-收集箱 / 02-领域笔记 / 03-永久笔记

## 知识管理的痛点与解法

文档增多后常见问题：
- 同样的问题每次需重新引导 AI 回复，缺乏积累
- 回答偏离已有方法论，需要反复校正
- 重要信息淹没在海量文档中

解决方案是通过结构化页面 + wikilinks 构建"知识网络"，让 AI 在已整理的知识网上检索而非从头处理。

## Related Entities

[[Claude-Code]] [[Cursor]] [[Codex]] [[baoyu-skills]] [[GitHub]] [[Matt-Pocock]] [[skills-sh]] [[Hermes]] [[Markdown]]

## Related Concepts

[[知识管理]] [[知识库构建]] [[RAG检索增强]] [[Skill设计模式]] [[Harness-Engineering]] [[Skill编排]] [[Agent开发]] [[PPT制作]] [[AI编程]]

## Mentioned In

- [[AI时代高效开发的skill技能]] — 1 产品规划的skill
- [[一种重新理解-skills-组合方式的新思路：Skill-Graphs-2.0]] — 一种重新理解 skills 组合方式的新思路：Skill Graphs 2.0
- [[分享6个宝藏Skills]] — 1. Awesome-Claude-Skills
- [[我装了-1000-个-skills，最后只保留了这-35-个]] — 我装了 1000 个 skills，最后只保留了这 35 个
- [[用-Hermes-Obsidian-建一个-AI-学习知识库]] — 用 Hermes + Obsidian 建一个 AI 学习知识库
- [[Obsidian本地知识库文档多而杂难维护不够智能通过AI大神Karpathy这套方法5分钟搭建最懂你的知识库]] — Karpathy 方法搭建智能知识库
- [[Obsidian内容创作系统如何让你的文章没有AI味]] — Obsidian 内容创作系统
- [[告别AI失忆-OpenClaw-Obsidian搭自媒体记忆宫殿]] — OpenClaw+Obsidian 搭建自媒体记忆宫殿
- [[我用Obsidian搭建了一个全球信息订阅系统]] — RSS Dashboard 插件搭建全球信息订阅
- [[给知识库装上水管：信息自动流进来]] — 四层信息处理系统设计
