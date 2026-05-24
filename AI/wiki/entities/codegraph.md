---
title: codegraph
type: entity
tags: [MCP Server, 代码知识图谱, GitHub项目]
sources: [给AI提前做功课的代码知识图谱.md, 不要错过这10个本周火火火的-GitHub-开源项目.md]
created: 2026-05-24
updated: 2026-05-24
---

# codegraph

> GitHub: https://github.com/colbymchenry/codegraph
> Stars: ~18k (2026-05)

## 简介

提前把代码库索引成语义代码知识图谱（MCP Server），让 AI 一上来就了解项目结构。

## 核心能力

- 智能上下文构建
- FTS5 全文搜索
- 影响分析（调用者/被调用者追踪）
- 自动同步（文件监视器）
- 框架感知路由（13 种 Web 框架）

## 性能提升

在 7 个真实代码库基准测试：
- 成本节省 35%
- Token 节省 59%
- 时间节省 49%
- 工具调用节省 70%

## 工作原理

tree-sitter 解析 → AST 提取符号 → SQLite 存储 → MCP 工具查询

## 安装

```bash
npx @colbymchenry/codegraph
codegraph init -i
```

## 关联概念

- [[MCP Server]]
- [[FTS5全文搜索]]
- [[tree-sitter]]
- [[框架感知路由]]

## 来源文章

- [[给AI提前做功课的代码知识图谱]]