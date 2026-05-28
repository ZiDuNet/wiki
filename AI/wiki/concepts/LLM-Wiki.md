---
type: concept
name: LLM-Wiki
created: 2026-05-28
updated: 2026-05-28
tags: [知识管理, LLM, Karpathy, 知识编译]
sources: [[Karpathy-知识库构建40-万词的-LLM-编译之道]]
---

# LLM-Wiki

**类型:** 概念

## 定义

Karpathy 提出的知识管理方法论：用 LLM 编译知识而非手动编辑 wiki。每次查询都「增加」知识库，知识是活的数据。

## 五层架构

| 层级 | 内容 | 工具 |
|-----|------|------|
| 输入层 | raw/ 目录 | Obsidian Web Clipper |
| 编译层 | Wiki 生成 | LLM CLI |
| 存储层 | .md 文件 | Obsidian |
| 查询层 | Q&A 系统 | 自建搜索 CLI |
| 输出层 | Markdown/Marp/Matplotlib | 多格式渲染 |

## 核心理念

- 你不编辑 wiki，LLM 编辑
- 每次查询都「增加」而非「消耗」
- 知识是活的数据，不是死的文档
- ~40 万词规模不需要 RAG

## LLM 编译六件事

1. 读取 raw/ 目录
2. 生成摘要
3. 分类整理
4. 生成概念文章
5. 创建索引
6. 添加反向链接

## 增长机制

输出结果归档回 wiki，每次查询都增加知识。Linting 保持健康。

## 相关文章

- [[Karpathy-知识库构建40-万词的-LLM-编译之道]]

## 相关实体

- [[Karpathy]]

## 相关概念

- [[知识编译]]
- [[raw目录结构]]
- [[知识编译系统]]