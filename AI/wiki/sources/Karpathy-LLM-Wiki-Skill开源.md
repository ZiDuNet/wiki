---
title: "Karpathy LLM-Wiki Skill 已开源公开"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: ["Karpathy LLM-Wiki Skill 已开源公开.md"]
tags: [LLM Wiki, Karpathy, Skill, Claude Code, Codex, 知识库初始化, 开源项目]
---

# Karpathy LLM-Wiki Skill 已开源公开

## 概要

开源可安装的Skill，用于初始化LLM Wiki，附带真实运行参考实现。skill/是可复用产品本体，llm-wiki/是真实参考实现展示运行效果。四层结构设计：Skill包（bootstrap逻辑）、原始资料层（raw/）、Schema层（AGENTS.md/CLAUDE.md）、Wiki页面层（wiki/）。

三类核心操作：Ingest把资料转成摘要实体概念链接索引、Query基于已编译知识回答、Lint检查矛盾孤儿页缺失链接。不同运行时对应不同schema文件名：Claude Code用CLAUDE.md、Codex用AGENTS.md、Copilot用.github/copilot-instructions.md。

## 关键要点

1. skill/是可复用产品本体，llm-wiki/是真实参考实现展示运行效果
2. 四层结构：Skill包（bootstrap逻辑）、原始资料层（raw/）、Schema层（AGENTS.md/CLAUDE.md）、Wiki页面层（wiki/）
3. 三类核心操作：Ingest把资料转成摘要实体概念链接索引、Query基于已编译知识回答、Lint检查矛盾孤儿页缺失链接
4. 不同运行时对应不同schema文件名：Claude Code用CLAUDE.md、Codex用AGENTS.md、Copilot用.github/copilot-instructions.md
5. 知识持续累积而非每次从零开始：原始资料不可变，Agent持续编译进Wiki

## 提及实体

- Karpathy — AI领域知名研究者，提出LLM Wiki理念
- nanzhipro — LLM-Wiki Skill开源作者
- Claude Code — Anthropic的AI编程助手
- OpenAI Codex — OpenAI的代码生成模型/工具
- GitHub — 代码托管平台

## 涉及概念

- [[LLM Wiki方法论]] — 用AI作为Wiki编辑持续维护知识库的方法
- [[Agent Skills]] — 封装特定工作流的可复用Agent能力
- [[知识库构建]] — 建立结构化知识存储系统的方法
- [[开源项目]] — 公开源代码可自由使用的软件项目

## 原始资料链接

[[Karpathy LLM-Wiki Skill 已开源公开.md]]