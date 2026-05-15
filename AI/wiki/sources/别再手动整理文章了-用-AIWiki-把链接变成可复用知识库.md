---
title: 别再手动整理文章了！用 AIWiki 把链接变成可复用知识库
type: source-summary
tags: [AIWiki, 知识库, Obsidian, LLM-Wiki, Karpathy, 内容管理, Agent]
sources: ["微信公众号/知识库/别再手动整理文章了！用 AIWiki 把链接变成可复用知识库.md"]
created: 2026-05-15
updated: 2026-05-15
---

> 📎 来源: [MaxKing宝藏](https://mp.weixin.qq.com/s?__biz=MzkwNzU5OTI0OA==&mid=2247484146&idx=1&sn=e503fcd9c51c3c5edb2e3fdd5c562704) | 时间: 2026-05-15

## 核心摘要

AIWiki 解决的是**"收藏链接到 AI 可继续使用"**的核心问题：传统收藏夹只存链接，人工每次都要重新读、拆、组织；AIWiki 将资料结构化入库，之后可让 AI 基于资料做选题、大纲、专题整理。

## 关键内容

### 核心区别

| | 普通收藏夹 | AIWiki |
|---|---|---|
| 目标 | 自己以后找 | AI 后续调用 |
| 产出 | 链接 | 结构化知识资产 |

### 入库后生成的内容

1. **raw** — 原始资料记录
2. **Source Card** — 来源/主题/核心信息摘要
3. **Claim 建议** — 可沉淀的观点/判断/证据
4. **创意素材** — 案例/表达/角度/可复用内容
5. **选题候选** — 可能发展的文章方向
6. **草稿大纲** — 可扩写的初始结构

### 使用场景

- **场景一**：单篇 → 生成选题 + 大纲 + 开头 300 字
- **场景二**：多篇同主题 → 整理专题（共同问题、高频观点、争议点、专题大纲）

### 安装方式

让 AI Agent（Claude Code、Codex、OpenClaw 等）执行安装和入库：
> "请帮我安装 AIWiki，并新建一个测试 Obsidian 知识库目录。安装完成后，帮我跑通一篇文章链接入库流程。"

### 关键人物/项目

- **[[Karpathy-LLM-Wiki]]** — 思想源头（LLM Wiki 模式）
- **[[Dan-Koe-内容积木]]** — 另一思想源头（内容积木思路）
- **[[MaxKing宝藏]]** — 作者
- **AIWiki** — 开源工具（npm 发布），Karpathy LLM Wiki + Dan Koe 内容积木思路的结合

## 相关链接

- 前篇：《[别再把资料丢进收藏夹了，我开源了AIWiki](https://mp.weixin.qq.com/s?__biz=MzkwNzU5OTI0OA==&mid=2247484138&idx=1&sn=fc0a00de73a3559da3340d268b19d918)》
