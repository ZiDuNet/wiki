---
type: concept
name: LLM Wiki方法论
created: 2026-05-11
updated: 2026-05-11
---

# LLM Wiki方法论

**类型:** 概念 (方法论)
**提及文章数:** 6

## 定义

LLM Wiki方法论是用AI作为Wiki编辑持续维护Markdown知识库的方法，替代传统RAG的无状态查询模式。核心理念：知识被编译而非检索，用得越久越聪明。

## 核心原则

1. **编译模式 vs 检索模式** — RAG每次查询无状态，知识无法积累；LLM Wiki让AI提前整理知识并持续维护更新
2. **三层结构** — raw（原始资料只读）/ wiki（AI编译后的知识）/ CLAUDE.md（控制AI行为）
3. **回填循环** — 每次查询结果存回wiki实现复利，这是核心超能力
4. **四个持续循环操作** — Ingest摄入、Compile编译、Query提问、Lint巡检

## 实现工具

| 工具 | 描述 |
|------|------|
| wiki-skills | 提供/wiki-init、/wiki-ingest、/wiki-query、/wiki-lint等现成命令 |
| Graphify | 把文件夹变成可查询知识图谱，71.5x Token压缩 |
| llm_wiki桌面应用 | 完整实现LLM Wiki理念的桌面应用 |
| Claudian | Obsidian插件，将Claude Code集成到Obsidian |

## 自动化层级

1. 单命令编译
2. Slash Commands
3. 定时任务（scheduled tasks）
4. GitHub Actions
5. Agent Skills

## 相关实体

- [[Karpathy]] — AI领域知名研究者，提出LLM Wiki理念
- [[Graphify]] — 知识图谱工程化实现
- [[Claudian]] — Obsidian集成Claude Code
- [[Obsidian]] — 本地知识管理工具

## 相关概念

- [[知识库构建]], [[知识图谱构建]], [[RAG]], [[知识管理]]

## 相关文章

- [[LLM-Wiki方法论知识库维护]]
- [[Karpathy-LLM-Wiki实战指南]]
- [[Karpathy-LLM-Wiki-Skill开源]]
- [[Graphify-知识图谱工程化]]
- [[llm_wiki-桌面应用实现]]
- [[Cursor-AI-Agent搭建Wiki]]