---
title: Hermes Agent + LLM Wiki + Obsidian 个人知识库
type: source-summary
tags: [Hermes-Agent, LLM-Wiki, Obsidian, 知识库, AI-Agent]
sources: [微信公众号/Obsidian/Hermes Agent + LLM Wiki + Obsidian 个人知识库.md]
created: 2026-05-31
updated: 2026-05-31
---

# Hermes Agent + LLM Wiki + Obsidian 个人知识库

**来源：** 微信公众号/Obsidian/Hermes Agent + LLM Wiki + Obsidian 个人知识库.md
**公众号：** 从AI到Web3的探索之旅
**摄入日期：** 2026-05-31

## 摘要

文章介绍如何用 Hermes Agent + LLM Wiki + Obsidian 打造"会自己长大的"个人知识库。核心观点：随着 AI 对话增多，知识零碎化问题日益严重——需要把知识从"记忆"编译成"结构化笔记"。文章详解 Karpathy 提出的 LLM Wiki 三层架构：Raw Sources（只读原始资料）→ Wiki（AI 编写和维护的实体页/概念页）→ Schema（操作指令）。

## 核心观点

1. **问题本质：知识没有被消化**
   - OpenClaw 的 Active Memory 只是"记录对话"，不是编译知识
   - RAG 只是"检索原文"，不解决知识整合问题
   - 需要 AI 把知识编译成笔记，而不是只做记录

2. **Karpathy LLM Wiki 三层架构**
   - **Raw Sources（原始资料层）**：PDF、网页、论文、代码，永恒只读
   - **Wiki（维基层）**：AI 全自动维护的 Markdown 文件夹，包含 Entity Pages（人物/项目/产品）和 Concept Pages（技术/方法论/思想），通过 `[[双向链接]]` 串联成知识图谱
   - **Schema（指令层）**：配置文件（如 SCHEMA.md），定义 AI 的核心目标、格式规则、链接规范

3. **目录结构示例**
   ```
   knowledge-base/
   ├── raw/              ← 只读证据层
   ├── wiki/
   │   ├── sources/      ← 源摘要
   │   ├── entities/    ← 实体页
   │   ├── concepts/     ← 概念页
   │   ├── index.md     ← 总目录
   │   └── log.md       ← 变更日志
   └── SCHEMA.md         ← 操作契约
   ```

4. **持续维护机制**
   - 每次新文章 → AI 读取 → 更新相关实体页/概念页 → 补充双向链接 → 标注矛盾
   - Wiki 是持久复利的产物，交叉引用越建越丰富

5. **LLM Wiki 对比传统笔记**
   - 传统笔记（Obsidian）：人类手动维护，越记越乱
   - LLM Wiki：AI 自动维护，持续更新，永不过时

## 涉及实体

- [[Hermes-Agent]] — 多渠道 AI Agent 平台，支持 Cron/定时任务、飞书/微信接入
- [[Obsidian]] — 本地笔记软件，天然适合作为 Wiki 的 IDE
- [[OpenClaw]] — 24万星标的多 Agent 协作框架，有 Active Memory 但只是记录而非编译知识

## 涉及概念

- [[LLM-Wiki]] — Karpathy 提出的 AI 全自动构建和维护的结构化知识库模式
- [[知识编译]] — 将零散信息转化为结构化、相互链接的持久知识的过程
- [[双向链接]] — [[wikilink]] 语法，Wiki 页面的核心连接机制

## 相关页面

- [[Hermes-Agent-高级玩法：微信扫码即用-+-LLM-Wiki-知识库，打造你的数据飞轮]] — 同系列文章，侧重微信扫码和数据飞轮角度

## 补充说明

文章配图展示了 LLM Wiki 的完整目录结构，强调"AI 是程序员，Wiki 是代码库，Obsidian 是 IDE"的分工理念。