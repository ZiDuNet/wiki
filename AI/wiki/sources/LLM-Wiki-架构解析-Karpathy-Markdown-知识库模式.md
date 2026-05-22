---
title: LLM Wiki 架构解析：Karpathy 的 Markdown 知识库模式
type: source-summary
tags: [LLM-Wiki, 知识管理, RAG, Karpathy]
sources: ["../微信公众号/LLM Wiki/LLM Wiki 架构解析：Karpathy 的 Markdown 知识库模式.md"]
created: 2026-05-22
updated: 2026-05-22
---

# LLM Wiki 架构解析：Karpathy 的 Markdown 知识库模式

> 来源: [技术极简主义](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ==&mid=2247487035&idx=1&sn=16227b052787487b3c93004bbe5ee198)
> 时间: 2026-05-22

## 核心观点

**LLM Wiki 解决的是「把读过的资料组织起来」而非「把资料找出来」**。RAG 更像后者，而 LLM Wiki 试图在模型上下文之外，维护一套可持久化、可编辑、可审计的知识 artifact。

## LLM Wiki 的四层架构

```
Raw Sources → Ingest/Knowledge Compile → Markdown Wiki 文件树 → Query/Update Loop
```

### 1. Raw Sources（只读证据层）

原始资料层：论文、网页、PDF、会议记录、代码仓库等。**Raw Sources 是地图背后的地形，Wiki 是地图，不是领土。**

### 2. Ingest / Knowledge Compile（知识编译）

分两个阶段：
- **Stage 1**：分析——抽取实体、概念、关系、与已有 Wiki 的连接、潜在矛盾和开放问题
- **Stage 2**：生成——写出来源摘要、实体页面、概念页面、index.md、log.md

### 3. Markdown Wiki 文件树

| 文件/目录 | 作用 |
|-----------|------|
| `index.md` | 知识库入口，提供导航和索引 |
| `log.md` | 记录导入、更新、查询等操作历史 |
| `overview.md` | 提供整体概览和高层摘要 |
| `sources/` | 保存或引用原始资料来源 |
| `entities/` | 存放人物、项目、组织等实体页面 |
| `concepts/` | 存放抽象概念、主题、方法论页面 |
| `queries/` | 存放查询过程、问题、回答和中间结果 |

### 4. Query / Update Loop（查询更新循环）

- 搜索 Wiki 页面，必要时回到 Raw Sources
- 把选中的 Wiki 页面、原文片段、日志历史打包进上下文窗口
- 回答可保存回 Wiki，但应被视为可审阅更新

## LLM Wiki vs 其他方案

| 方案 | 核心机制 | 优点 | 局限 |
|------|---------|------|------|
| RAG | 查询时检索原始片段 | 保留原文依据，启动成本低 | 不沉淀结构化理解 |
| 笔记软件 | 人手动整理 | 可控、准确 | 维护成本高 |
| 传统知识库 | 人或系统维护 | 规范、稳定 | 难跟随资料演化 |
| **LLM Wiki** | **LLM 辅助维护 Markdown Wiki** | **可读、可改、可复用、可持续更新** | **摘要漂移、错误固化、非确定性** |

## 风险与适用场景

### 四类风险

1. **信息损失**：原始资料被压缩时细节可能丢失
2. **摘要漂移**：概念页被多次改写后偏离原始材料
3. **冻结错误**：错误写进 Markdown 后被复用
4. **非确定性**：同样资料可能生成略有差异的页面

### 适用场景

✅ 适合：个人研究资料整理、长期项目知识库、代码仓库理解、团队内部资料汇总、AI Agent 的长期工作记忆

⚠️ 慎用：法律、医疗、金融、合规审计等强事实一致性场景

## 实践建议

1. 保留 `raw/`，不让 Wiki 替代原始资料
2. 先建立 `wiki/index.md` 和 `wiki/log.md`
3. 每个重要页面保留来源链接
4. 对关键概念页设置人工 review
5. 增加 lint 规则检查断链、孤立页面

## 相关链接

- llm-wiki.md: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- nashsu/llm_wiki: https://github.com/nashsu/llm_wiki

## 相关概念

[[RAG]], [[RAG检索增强]], [[知识管理]], [[AI-Agent]], [[Multi-Agent]]
