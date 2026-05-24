---
title: oh-my-pi
type: entity
tags: [AI编程助手, 终端工具, GitHub项目]
sources: [内置IDE能力的终端AI编程助手.md, 不要错过这10个本周火火火的-GitHub-开源项目.md]
created: 2026-05-24
updated: 2026-05-24
---

# oh-my-pi

> GitHub: https://github.com/can1357/oh-my-pi
> Stars: ~6k (2026-05) | 语言: TypeScript + Rust (~27k行)

## 简介

终端里的 AI 编程助手，内置 IDE 能力，从 Pi 项目 fork 而来。

## 核心能力

- 32 个内置工具
- 40+ LLM Provider
- 13 种 LSP 操作
- 27 种 DAP 操作
- Hashline 编辑（减少 61% Token）

## 技术架构

- 约 27k 行 Rust 原生模块
- 双内核执行（Python + Bun Worker）
- 一级子代理支持

## 安装

```bash
# macOS/Linux
curl -fsSL https://omp.sh/install | sh

# Bun
bun install -g @oh-my-pi/pi-coding-agent
```

## 关联概念

- [[LSP集成]]
- [[DAP调试器]]
- [[Hashline编辑]]
- [[双内核执行]]

## 来源文章

- [[内置IDE能力的终端AI编程助手]]