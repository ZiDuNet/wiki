---
title: MCP Server
type: concept
tags: [MCP协议, 工具接口, AI集成]
sources: [给AI提前做功课的代码知识图谱.md, Claude/GitHub上最火的10个MCP服务器，让Claude Code连接万物（保姆级）.md]
created: 2026-05-24
updated: 2026-05-25
---

# MCP Server

Model Context Protocol Server，为 AI Agent 提供标准化工具接口，使其能访问外部数据和执行操作。

## 核心能力

- 标准化工具接口
- 上下文构建
- 数据查询和操作

## Top 10 MCP Servers（2026-05-25）

| 排名 | 名称 | Star | 用途 | 坑 |
| --- | --- | --- | --- | --- |
| 1 | [[pal-mcp-server]] | 11.4K | Claude 调用 Gemini/GPT/Ollama | Token消耗翻倍 |
| 2 | [[mcp-chrome]] | 11.1K | 控制 Chrome 浏览器 | 需开调试端口 |
| 3 | [[mcp-use]] | 9.7K | 自定义 MCP 服务器开发框架 | 需编程基础 |
| 4 | [[git-mcp]] | 7.9K | 消除代码幻觉，实时读 GitHub 源码 | 私有仓库需 Token |
| 5 | [[firecrawl-mcp]] | 6K | 网页抓取和信息提取 | 免费额度500次/月 |
| 6 | [[mcp-playwright]] | 5.4K | 浏览器自动化 Pro 版（多浏览器支持） | 比 mcp-chrome 更重 |
| 7 | [[gemini-mcp-tool]] | 2.1K | 借 Gemini 超长上下文处理大文件 | 需 Gemini API Key |
| 8 | [[notebooklm-mcp]] | 1.8K | 连接 Google NotebookLM 做深度研究 | 稳定性一般 |
| 9 | [[mcp-excalidraw]] | 1.6K | 让 AI 画流程图/架构图 | 需 Excalidraw 账号 |
| 10 | [[phantom]] | 1.2K | 有独立虚拟桌面的 AI Agent | 早期阶段 |

## 日常推荐组合

常用4个：pal-mcp-server、mcp-chrome、git-mcp、firecrawl-mcp

## 场景选型

| 场景 | 推荐 |
| --- | --- |
| 让 Claude 调用其他 AI | pal-mcp-server |
| 操作网页/截图 | mcp-chrome（轻量）或 mcp-playwright（重量） |
| 自己写 MCP | mcp-use |
| 减少代码幻觉 | git-mcp |
| 抓网页内容 | firecrawl-mcp |
| 处理超大文件 | gemini-mcp-tool |
| 让 AI 画图 | mcp-excalidraw |

## 工作原理

数据源 → 索引/处理 → MCP 工具 → AI Agent 调用

## 来源文章

- [[给AI提前做功课的代码知识图谱]]
- [[github上最火的10个MCP服务器-让Claude-Code连接万物保姆级]]