---
type: entity
name: GitNexus
tags: [代码知识图谱, AI编程工具, MCP, 代码仓库]
sources: [karpathy的llm-wiki被搬进代码仓库.md]
created: 2026-05-29
updated: 2026-05-29
---

# GitNexus

**类型:** 实体 (工具)
**定位:** 代码仓库知识图谱工具，把 LLM Wiki 思路搬进代码仓库

## 简介

GitNexus 把代码仓库做成可查询、可追踪、可更新的结构化知识库。CLI 索引仓库，生成依赖图谱、调用链、cluster 和 execution flow，通过 MCP 暴露给 AI 编程工具。

## 核心功能

### 入口命令

```bash
npx gitnexus analyze
```

索引仓库，生成 agent skills，注册 Claude Code hooks，创建 AGENTS.md / CLAUDE.md 上下文文件。

```bash
gitnexus mcp
```

启动 MCP 服务，让 AI agent 查询图谱。

### 六大工具

|| 工具 | 功能 |
|-----|------|
| query | 怎么找代码 |
| context | 一个符号的上下游关系 |
| impact | 改它会影响谁 |
| detect_changes | 当前 diff 会波及哪些流程 |
| rename | 重命名这种跨文件操作 |
| cypher | 底层图查询能力 |

### Web UI

浏览器里的可视化图谱和 AI chat，适合快速探索。

## 设计哲学

- 搜索返回候选文件，图谱返回结构关系
- 把"临时上下文"变成"持久结构"
- 把 agent 的上下文入口从"文件内容"往前挪到"仓库结构"

## 与 Karpathy LLM Wiki 的呼应

|| 对象 | Karpathy LLM Wiki | GitNexus |
|-----|-------------------|----------|
| 面向对象 | 论文、笔记、网页、材料 | 函数、类、依赖、调用链、执行流 |
| 机制 | 把知识沉淀成持续维护的 wiki | 把仓库沉淀成持续查询的结构图 |

## 支持平台

通过 MCP 暴露给以下 AI 编程工具：

- [[Claude]]
- [[Cursor]]
- [[Codex]]
- [[Windsurf]]

## 核心价值

代码规模进入多模块、多服务、多 agent 协作时，结构化代码记忆从锦上添花变成基础设施。AI 编程下一步缺的不是更会聊天的助手，而是更少迷路的助手。

## 相关论文

- Codebase-Memory：基于 Tree-sitter 的持久知识图谱，token 消耗低一个数量级
- Reliable Graph-RAG for Codebases：AST 派生确定性图谱在覆盖率、成本和多跳 grounding 上更可靠

## 相关概念

- [[代码仓库知识图谱]]
- [[LLM-Wiki]]
- [[MCP协议]]
- [[知识编译]]

## 来源文章

- [[karpathy的llm-wiki被搬进代码仓库]]