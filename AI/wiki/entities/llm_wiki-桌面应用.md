---
type: entity
name: llm_wiki桌面应用
created: 2026-05-11
updated: 2026-05-11
---

# llm_wiki桌面应用

**类型:** 实体 (产品/应用)
**提及文章数:** 1
**GitHub Stars:** 5.8k+

## 简介

llm_wiki桌面应用完整实现Karpathy的LLM Wiki理念，知识被编译而非检索，用得越久越聪明。采用Tauri框架开发，React 19前端，LanceDB嵌入式向量数据库。提供两步思维链摄取、4信号知识图谱、深度研究闭环等核心能力。

## 技术栈

- Tauri — Rust桌面应用框架
- React 19 — 前端框架
- LanceDB — 嵌入式向量数据库
- sigma.js — 网络可视化
- graphology — 图数据结构
- ForceAtlas2 — 图布局算法
- Tavily API — AI搜索服务
- Mozilla Readability.js — 网页解析
- Turndown.js — HTML转Markdown

## 核心特性

- 两步思维链摄取
- 4信号知识图谱（wikilinkx3、来源重叠x4、Adamic-Adarx1.5、类型亲和x1）
- Louvain社区检测
- 多相位检索
- SHA256增量缓存
- 图谱洞察（发现盲区和意外连接）
- 深度研究闭环

## 相关概念

- [[知识图谱构建]], [[LLM-Wiki方法论]], [[知识库构建]], [[GitHub开源项目]]

## 相关文章

- [[llm_wiki-桌面应用实现]]