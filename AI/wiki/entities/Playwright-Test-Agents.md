---
type: entity
name: Playwright Test Agents
created: 2026-05-11
updated: 2026-05-11
---

# Playwright Test Agents

**类型:** 实体 (产品/工具)
**提及文章数:** 1

## 简介

Playwright官方推出的Test Agents系统，包含Planner、Generator、Healer三个AI Agent，实现从测试计划生成到失败修复的全自动化链路。这是自动化测试领域的重要突破，将AI Agent技术与测试工作流深度融合。

## 三Agent架构

| Agent | 职责 | 功能 |
|-------|------|------|
| Planner | 探索应用 | 输出Markdown格式的测试计划 |
| Generator | 代码生成 | 把测试计划转换为可执行的Playwright测试代码并实时验证 |
| Healer | 修复维护 | 自动修复失败的测试，修不好则标记skip并说明原因 |

## 工具选择指南

| 工具类型 | Token消耗 | 适用场景 |
|---------|----------|---------|
| MCP | 高 | 写单个测试 |
| CLI | 低 | 搭自动化流程 |
| Agents | 自主 | 建整体测试覆盖 |

## 相关概念

- [[自动化测试]], [[Agent架构]], [[MCP协议]], [[Test Agents]]

## 相关文章

- [[Playwright-三Agent全自动写测试]]