---
title: AI助手集成
type: concept
tags: [AI助手, 集成, Agent, 工具链]
sources: [704-mmx-cli-一句话让AI助手拥有全模态能力.md]
created: 2026-05-16
updated: 2026-05-16
---

# AI助手集成

**类型:** 集成模式
**英文:** AI Assistant Integration

## 简介

通过标准接口（SKILL/MCP/CLI）将外部能力接入AI助手/Agent，实现能力扩展。核心价值：让AI助手突破原生能力边界，调用专业工具。

## 集成方式

- **SKILL机制**：通过技能包扩展AI能力（如mmx-cli的MiniMax-AI/cli skill）
- **MCP协议**：标准化工具调用接口
- **CLI包装**：命令行工具作为Agent工具

## 典型案例

[[mmx-cli]] 集成 OpenClaw、Claude Code、Cursor等主流Agent平台

## 相关概念

[[多模态]], [[CLI工具]], [[Skill编排]], [[MCP协议]]
