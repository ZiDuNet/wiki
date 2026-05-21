---
title: 超级记忆系统
type: source-summary
tags: [LLM Wiki, 记忆系统, agentmemory, 知识图谱, RAG, AI Coding]
sources: [超级记忆系统，融合 Karpathy LLM Wiki、知识图谱、混合搜索的新一代记忆系统.md]
created: 2026-05-22
updated: 2026-05-22
---

# 超级记忆系统

## 核心概念

agentmemory 是一个融合知识图谱、混合搜索并扩展了 Karpathy [[LLM Wiki]] 模式的永久记忆系统，专为 AI Coding Agents 设计。项目目前已有 7650+ Stars。

## 问题背景

AI 编码代理（如 Claude Code、Cursor、Cline）的"健忘"不是 bug，是架构决定的：

- **容量有限**：MEMORY.md 超过 200 行变成噪音，240 条观察占 22K+ tokens
- **不可检索**：无法区分当前项目和历史项目的笔记
- **不会过期**：新旧信息并存，代理无法判断该信哪一条

## 技术方案：三层记忆 + RRF 融合检索

三层索引结构在 LongMemEval-S 基准上达到 95.2% R@5 召回率：

| 层级 | 技术 | 说明 |
|------|------|------|
| 第一层 | BM25 关键词索引 | SQLite FTS5，本地运行，v0.9.12 加入 CJK tokenizer |
| 第二层 | 向量索引 | `all-MiniLM-L6-v2` 本地嵌入模型，零 API 费用 |
| 第三层 | 知识图谱 | 内存条目间建立关系网络 |

三层通过 **RRF（Reciprocal Rank Fusion）** 融合：BM25 权重 0.4，向量权重 0.6，图谱排名作为 tie-breaker。

## Token 成本对比

| 方案 | 年度 Token 消耗 | 年度成本 |
|------|----------------|----------|
| agentmemory | ~17万 tokens | $10 |
| 传统 LLM 摘要 | ~65万 tokens | $500 |

节省 92% token 开销。

## 记忆生命周期

四阶段：存、取、衰减、自动遗忘。

- 高频被检索的记忆保留分增加
- 长期无人问津的记忆保留分递减
- 降至阈值以下进入回收缓冲区（可撤销）

## 与竞品对比

| 项目 | Stars | R@5 | 特点 |
|------|-------|-----|------|
| agentmemory | 7,650 | 95.2% | MCP/REST API，跨代理共享 |
| mem0 | 55,618 | 68.5% | 手动 API，需外部向量库 |
| Letta/MemGPT | 22,693 | 83.2% | 完整 agent runtime，框架锁定 |
| 内置记忆 | - | - | 无检索，全加载 |

## 安装与使用

```bash
npx @agentmemory/agentmemory
```

启动内存服务器（端口 3111），实时查看器（端口 3113）。支持 16 个平台：Claude Code、Codex CLI、Cursor、Gemini CLI、Cline、Windsurf 等。

## 局限性

1. 依赖 iii-engine（Rust 运行时），需从 GitHub Releases 下载
2. LLM 压缩可选但昂贵
3. 记忆注入可能干扰代理

## 未来方向

- 记忆槽（slots）机制：persona、user_preferences、tool_guidelines
- 文件系统连接器：自动监控项目文件变化

## 来源

- 公众号：硅基苔藓
- 原文：[超级记忆系统](https://mp.weixin.qq.com/s?__biz=MzIxMDYwODQ4Nw==&mid=2247484745)
- 相关概念：[[LLM Wiki]]、[[知识图谱]]、[[RAG]]、[[MCP协议]]