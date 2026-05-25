---
tags: [MCP, Claude-Code, 工具连接, AI-Agent]
sources: [Claude/GitHub上最火的10个MCP服务器，让Claude Code连接万物（保姆级）.md]
created: 2026-05-25
updated: 2026-05-25
---

# GitHub上最火的10个MCP服务器，让Claude Code连接万物（保姆级）

**来源：** Claude/GitHub上最火的10个MCP服务器，让Claude Code连接万物（保姆级）.md
**摄入日期：** 2026-05-25
**类型：** 工具推荐/教程

## 摘要

本文介绍 MCP（Model Context Protocol）的概念以及 GitHub 上最热门的10个 MCP 服务器。MCP 是 AI 连接外部工具的"万能插座"，让 Claude Code 从"聊天工具"变成"操作系统"。文章详细说明每个 MCP 的用途、适用场景和避坑提示。

## 核心观点

- **MCP本质**：Model Context Protocol，AI 工具的"万能插座"，Claude Code 通过 MCP 连接外部世界
- **MCP SDK 3月份下载量突破9700万次**，已成基础设施
- **Claude Code是大脑，MCP服务器是手脚**：接上 MCP 就能操作浏览器、读数据库、发消息、画图、调API
- **推荐清单**：按需安装，别全装；日常4个常用（pal-mcp-server、mcp-chrome、git-mcp、firecrawl-mcp）

## Top 10 MCP 服务器

| 排名 | 名称 | Star | 用途 | 坑 |
| --- | --- | --- | --- | --- | --- |
| 1 | pal-mcp-server | 11.4K | Claude 调用 Gemini/GPT/Ollama | Token消耗翻倍 |
| 2 | mcp-chrome | 11.1K | 控制 Chrome 浏览器 | 需开调试端口 |
| 3 | mcp-use | 9.7K | 自定义 MCP 服务器开发框架 | 需编程基础 |
| 4 | git-mcp | 7.9K | 消除代码幻觉，实时读 GitHub 源码 | 私有仓库需 Token |
| 5 | firecrawl-mcp | 6K | 网页抓取和信息提取 | 免费额度500次/月 |
| 6 | mcp-playwright | 5.4K | 浏览器自动化 Pro 版（多浏览器支持） | 比 mcp-chrome 更重 |
| 7 | gemini-mcp-tool | 2.1K | 借 Gemini 超长上下文处理大文件 | 需 Gemini API Key |
| 8 | notebooklm-mcp | 1.8K | 连接 Google NotebookLM 做深度研究 | 稳定性一般 |
| 9 | mcp-excalidraw | 1.6K | 让 AI 画流程图/架构图 | 需 Excalidraw 账号 |
| 10 | phantom | 1.2K | 有独立虚拟桌面的 AI Agent | 早期阶段 |

## 场景选型指南

| 场景 | 推荐 |
| --- | --- |
| 让 Claude 调用其他 AI | pal-mcp-server |
| 操作网页/截图 | mcp-chrome（轻量）或 mcp-playwright（重量） |
| 自己写 MCP | mcp-use |
| 减少代码幻觉 | git-mcp |
| 抓网页内容 | firecrawl-mcp |
| 处理超大文件 | gemini-mcp-tool |
| 让 AI 画图 | mcp-excalidraw |

## 涉及实体

- [[Claude Code]] — Anthropic 推出的 AI 编程工具
- [[MCP协议]] — Model Context Protocol，AI 工具连接协议
- [[pal-mcp-server]] — 11.4K Star，让 Claude 调用其他 AI 模型
- [[mcp-chrome]] — 11.1K Star，控制 Chrome 浏览器
- [[git-mcp]] — 7.9K Star，消除代码幻觉
- [[firecrawl-mcp]] — 6K Star，网页抓取

## 涉及概念

- [[MCP服务器]] — MCP 协议的具体实现，为 AI 提供标准化工具接口
- [[AI工具连接]] — 通过 MCP 让 AI Agent 连接外部世界
- [[浏览器自动化]] — mcp-chrome/mcp-playwright 的核心能力