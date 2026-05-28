---
type: source
title: Karpathy 知识库构建：40 万词的 LLM 编译之道
created: 2026-05-28
updated: 2026-05-28
tags: [LLM Wiki, Karpathy, 知识编译, 知识管理, Obsidian, 自动化]
sources: []
---

# Karpathy 知识库构建：40 万词的 LLM 编译之道

## 核心观点

Karpathy 用 LLM 搭建了 **100 篇文章、40 万词** 的个人知识库。关键洞察：Token 去向变了——从「写代码」转向「编译知识」。他不手动编辑 wiki，这是 **LLM 的领域**。

## 五层架构

| 层级 | 内容 | 工具 |
|-----|------|------|
| **输入层** | raw/ 目录 | Obsidian Web Clipper |
| **编译层** | Wiki 生成 | LLM CLI |
| **存储层** | .md 文件 | Obsidian |
| **查询层** | Q&A 系统 | 自建搜索 CLI |
| **输出层** | Markdown/Marp/Matplotlib | 多格式渲染 |

## 核心理念

- 你不编辑 wiki，**LLM 编辑**
- 每次查询都「增加」而非「消耗」
- 知识是**活的数据**，不是死的文档

## raw/ 目录结构

```
raw/
├── articles/      # 文章
├── papers/        # 论文
├── repos/         # 代码仓库
├── datasets/      # 数据集
└── images/        # 图片（LLM 可引用）
```

## LLM 编译六件事

1. 读取 raw/ 目录，扫描原始数据
2. 生成摘要（核心观点）
3. 分类整理（按概念归类）
4. 生成文章（每个概念写专题）
5. 创建索引（自动维护 index.md）
6. 添加反向链接（文章关联）

## Wiki 目录结构

```
wiki/
├── index.md          # 总索引（LLM 维护）
├── concepts/         # 概念文章（LLM 生成）
├── summaries/        # 摘要文章
└── connections.md    # 反向链接
```

## 关键发现：不需要 RAG

~40 万词规模下，LLM 自动维护索引表现良好。不需要向量数据库，不需要复杂检索 pipeline。原因：LLM 能「理解」知识结构，不是机械检索关键词。

## 输出归档机制

输出结果归档回 wiki，每次查询都增加知识库。知识是累积的，不是消耗的。

## Linting 健康检查

LLM 定期执行：
- 发现不一致数据
- 补充缺失数据（带 web search）
- 发现潜在连接
- 建议新文章主题

## 相关概念

- [[LLM-Wiki]]
- [[知识编译]]
- [[raw目录结构]]
- [[知识编译系统]]

## 相关实体

- [[Karpathy]]
- [[Obsidian]]