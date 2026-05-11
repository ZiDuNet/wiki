---
title: "Playwright 又出新东西了：三个 Agent 帮你全自动写测试"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: ["Playwright 又出新东西了：三个 Agent 帮你全自动写测试.md"]
tags: [Playwright, Test Agents, 自动化测试, AI编程, Planner, Generator, Healer]
---

# Playwright 又出新东西了：三个 Agent 帮你全自动写测试

## 概要

Playwright官方推出Test Agents，包含Planner、Generator、Healer三个AI Agent，实现从测试计划生成到失败修复的全自动化链路。这是自动化测试领域的重要突破，将AI Agent技术与测试工作流深度融合，显著降低测试编写和维护成本。

三Agent分工协作：Planner负责探索应用并输出Markdown格式的测试计划；Generator把测试计划转换为可执行的Playwright测试代码并实时验证；Healer自动修复失败的测试，修不好则标记skip并说明原因。这套系统完整覆盖了测试生命周期。

## 关键要点

1. Planner探索应用并输出Markdown格式的测试计划
2. Generator把测试计划转换为可执行的Playwright测试代码并实时验证
3. Healer自动修复失败的测试，修不好则标记skip并说明原因
4. MCP是感知工具（高Token消耗），CLI是执行工具（低消耗），Agent是自主系统
5. 三者适用不同场景：写单个测试用MCP，搭自动化流程用CLI，建整体测试覆盖用Agents

## 提及实体

- Playwright — 开源自动化测试框架，支持多浏览器
- VS Code — 微软开发的代码编辑器，支持插件扩展
- Claude Code — Anthropic的AI编程助手
- Copilot — GitHub的AI代码助手

## 涉及概念

- [[自动化测试]] — 使用软件工具自动执行测试用例
- [[Test Agents]] — 专用于测试任务的AI Agent系统
- [[MCP协议]] — Model Context Protocol，AI模型上下文协议
- [[Agent架构]] — AI Agent的系统设计和组织方式

## 原始资料链接

[[Playwright 又出新东西了：三个 Agent 帮你全自动写测试.md]]