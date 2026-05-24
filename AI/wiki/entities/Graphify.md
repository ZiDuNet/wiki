---
type: entity
name: Graphify
created: 2026-05-11
updated: 2026-05-24
tags: [知识图谱, LLM-Wiki, Karpathy, AI技能]
---

# Graphify

**类型:** 实体 (产品/工具)
**提及文章数:** 3
**GitHub:** ⭐20.3k Stars

## 简介

Graphify 是 AI 编程技能，把文件夹变成可查询知识图谱，首次工程化实现 Karpathy 的 LLM Wiki 理念。采用 NetworkX 知识图谱 + Leiden 算法社区检测，无向量数据库，实现 71.5x Token 压缩。双轨提取引擎：代码文件走 tree-sitter AST 零 Token 消耗，文档图片走 LLM 语义提取。

## 核心特性

- 七级流水线处理流程
- 双轨提取引擎（tree-sitter + LLM）
- 三级置信度标签：EXTRACTED(1.0)、INFERRED(0.4-0.9)、AMBIGUOUS(0.1-0.3)
- MCP服务器模式 + Always-On模式
- SHA256增量缓存
- 全模态支持：代码、PDF、Markdown、截图、架构图

## 与wechat-cli的配合

wechat-cli 导出的 Markdown 聊天记录可直接由 Graphify 处理：

```bash
# 安装 Graphify
pip install graphifyy
graphify install

# 在AI编码助手中执行
/graphify wiki/

# 输出知识图谱
graphify-out/
  graph.html        # 可交互可视化图谱
  GRAPH_REPORT.md   # 关键节点、社区结构、推荐问题
  graph.json        # 可查询的持久化图谱
```

## 输出产物

| 文件 | 说明 |
|------|------|
| `graph.html` | 可交互的可视化图谱 |
| `GRAPH_REPORT.md` | 关键节点、社区结构、推荐问题 |
| `graph.json` | 可查询的持久化图谱 |

## 应用场景

1. **代码仓库知识图谱**：从代码库提取实体关系
2. **微信聊天记录编译**：将群聊讨论转化为可查询知识
3. **多模态知识库**：整合文档、图片、截图等多种来源

## 相关概念

- [[知识图谱构建]], [[LLM-Wiki方法论]], [[Token优化]], [[Agent架构]]

## 相关文章

- [[Wechat-Cli-将微信聊天记录导入-Karpathy的-LLM-Wiki]]
- [[Graphify-知识图谱工程化]]
- [[Karpathy的LLM Wiki + 3.5万Star的Graphify：企业级 RAG 缺的真是知识图谱？]]

## 相关实体

- [[Karpathy]]
- [[wechat-cli]]