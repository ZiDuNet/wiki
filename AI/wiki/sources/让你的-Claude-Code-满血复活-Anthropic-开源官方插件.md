---
title: "让你的 Claude Code 满血复活，Anthropic 在 GitHub 上开源了个插件"
type: source-summary
created: 2026-05-25
updated: 2026-05-25
sources: ["让你的 Claude Code 满血复活，Anthropic 在 GitHub 上开源了个插件。.md"]
tags: [Claude, Claude-Code, GitHub, Agent, OpenSource]
---

# 让你的 Claude Code 满血复活

## Summary

Anthropic 在 GitHub 上开源了官方插件仓库 **claude-plugins-official**，目前 2 万多 Star。装上后 Claude Code 可一键安装各类插件，获得 Code Review、功能开发、遗留代码迁移、Hook 管理、多语言 LSP 支持等能力。最核心的插件是 **claude-code-setup**，能自动扫描项目并推荐最优配置。

## Key Claims

1. Claude Code 官方插件市场已经开源，30+ 内部插件 + 10+ 外部插件
2. claude-code-setup 是 X 上被疯狂安利的插件，扫描代码库后一键推荐 MCP Servers、Skills、Hooks、Subagents、Slash Commands
3. feature-dev 把功能开发变成 7 阶段结构化流程（发现需求→探索代码库→架构设计→编码实现→质量审查）
4. hookify 用自然语言配置 Claude Code Hooks，支持 bash/file/stop/prompt 四种触发类型
5. code-modernization 专门做遗留代码现代化，支持 COBOL、Java/C++ 等迁移到现代技术栈

## Entities Mentioned

- [[Anthropic]] — 插件官方发布方
- [[claude-plugins-official]] — GitHub 官方插件仓库
- [[claude-code-setup]] — 项目扫描 + 配置推荐插件
- [[feature-dev]] — 7 阶段结构化功能开发插件
- [[hookify]] — 自然语言配置 Hooks 的插件
- [[code-modernization]] — 遗留代码现代化插件

## Concepts

- [[Claude-Code-Plugins]] — Claude Code 插件系统，一行命令安装
- [[Claude-Code-Skills]] — Claude Code Skills 文件，教 AI 做某类任务
- [[Claude-Code-Hooks]] — Claude Code 自动触发钩子（保存时自动格式化等）
- [[Claude-Code-Subagents]] — Claude Code 子智能体
- [[Claude-Code-MCP-Servers]] — Claude Code MCP Servers 外部工具集成

## Notable Quotes

> "claude-code-setup 是只读的，它只分析不修改，不会动你的任何文件。除非你授权他去修改。"

> "feature-dev 第 4 阶段同时启动 2-3 个架构师 Agent，分别从最小改动、干净架构、务实平衡三个角度设计方案。"

## Limitations / Bias

- 作者立场偏向开发者视角，非开发者受益有限
- 插件列表截至 2026-05-25，可能有新插件陆续加入
