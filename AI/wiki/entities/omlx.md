---
type: entity
name: omlx
created: 2026-05-12
updated: 2026-05-12
mentions: 1
---

# omlx

**类型:** 实体
**来源:** [[github-ai热榜-5月11日-genericagent-omlx]]

## 简介

Mac 本地推理优化工具，把 90 秒压到 5 秒。GitHub: `https://github.com/jundot/omlx`

## 核心特性

- **内存+SSD 两级 KV 缓存**：所有算过的上下文持久化在 SSD，关掉再重开缓存还在，无需重算
- **菜单栏管理**：点一下切换模型、查看状态
- **连续批处理**：多请求并发，多 Agent 不排队
- **兼容 OpenAI API**：任何客户端直连
- **Support MCP**：Agent 可直接通过 MCP 调用
- **基于 Apple MLX 框架**：直调 Metal GPU，比 Ollama 快 26%-30%，M3 Ultra 上优势最明显

## 定位

让 Mac 本地 Agent 从"能跑"进化到"能用"，不把 MacBook 变成集群，而是把现有硬件利用率推满。

## 相关概念

[[本地部署]], [[MCP协议]], [[AI-Agent]]
