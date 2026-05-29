---
type: source-summary
source: 微信公众号/LLM Wiki/Karpathy 的 LLM Wiki 思路，我用 Hermes 跑通了.md
author: Turing 实验室
date: 2026-05-28
tags: [Karpathy, Hermes, Claude Code, LLM Wiki, 工程落地]
entities: [Hermes, Claude Code, Karpathy]
concepts: [Claude Code基建, Hermes知识库维护, 工具分工哲学]
---

# Karpathy 的 LLM Wiki 思路，我用 Hermes 跑通了

> 📎 来源: [Turing 实验室](https://mp.weixin.qq.com/s?__biz=MzkzMjY2ODgxMA==&mid=2247483721) | 时间: 2026-05-28 20:35

## 核心命题

两步接力跑通 Karpathy LLM Wiki——**Claude Code 做基建部署 Hermes，Hermes 做长期知识维护**。

## 工具分工哲学

| 工具 | 角色 | 定位 | 特点 |
|------|------|------|------|
| Claude Code | 建筑队 | 一次性、强执行的基建任务 | 能力强，无状态，干完就撤 |
| Hermes | 物业/施工管家 | 长期知识管理 | 理解偏好、自我纠错、归类体系 |

**关键洞察：** 把研究员当建筑工用，是浪费。把建筑队当研究员用，是灾难。

## 第一步：Claude Code 搞定基建

目标：用 Hermes 执行 LLM Wiki 任务。

障碍：部署 Hermes 需配环境、装依赖、调网关——典型的脏活。

解法：把 Hermes 搭建文档丢给 **Claude Code**，告诉它："按文档，帮我把环境跑通。"

结果：Claude Code 读文档、写配置、解报错，一次性搞定。

## 第二步：Hermes 落地知识库

基建完成后，Hermes 上场：

1. **自建结构**：按 Karpathy gist 三层架构（Raw Sources → Wiki → Schema）创建目录
2. **自我检查**：对照核心思想检查目录结构、索引是否正确
3. **跑测试**：确认"摄入→查询→Lint"三条链路全通

用户只需：确认结构 → 丢进第一篇文档 → Hermes 自动读取、提取、归档、建立交叉引用。

## 现状与下一步

骨架搭好，测试通过。持续喂素材 → 观察归纳逻辑微调 Schema → 发现知识盲区。

**核心原则：** 知识的价值不在于你读了多少，而在于你累积了多少。让 AI 帮你做累积。你负责思考。

## 新学习模式

知识不再是静态笔记，而是会自己生长的有机体：
- 每读一篇新资料 → 整个知识库微小变化
- 旧观点被修正，新连接被建立，隐藏矛盾被标注

不再是在"记笔记"，而是在"养一个系统"。

## 相关实体

- [[Hermes]] — 长期知识维护的 AI Agent
- [[Claude Code]] — 基建部署的建筑队
- [[Karpathy]] — LLM Wiki 思路提出者

## 相关概念

- [[LLM Wiki]] — Karpathy 提出的知识管理模式
- [[Claude Code基建]] — 一次性强执行的基建任务
- [[Hermes知识库维护]] — 长期知识管理与自进化
- [[工具分工哲学]] — 建筑队 vs 物业的分工智慧

## 原文金句

> "工具没有优劣，只有位置放得对不对。"
> 
> "把研究员当建筑工用，是浪费。把建筑队当研究员用，是灾难。"