---
type: entity
name: LM Studio
created: 2026-05-28
updated: 2026-05-28
tags: [本地推理, 大模型, GGUF, 离线AI]
---

# LM Studio

**类型:** 实体 / 工具

## 简介

本地大模型运行平台，支持 GGUF 格式模型文件。图形化界面，零代码门槛。提供本地 API 服务（兼容 OpenAI API 格式），默认地址 `http://localhost:1234/v1`。

## 核心能力

- 下载和管理多种开源模型（Llama、Mistral、Phi、Qwen 等）
- 自动匹配硬件能力（CPU / GPU / Apple Silicon）
- 提供本地 API 服务（兼容 OpenAI API 格式）
- 图形化界面，零代码门槛

## 推荐模型

| 场景 | 推荐模型 |
|-----|---------|
| 日常对话与写作 | Qwen2.5-7B / Llama-3.1-8B |
| 代码辅助 | CodeQwen / DeepSeek-Coder |
| 轻量场景 | Phi-3-mini（3.8B，4GB 内存）|

## 相关概念

- [[离线AI工作流]]
- [[本地大模型]]
- [[端侧推理]]

## 相关文章

- [[我把整个-AI-工作流搬到了离线环境Obsidian-LM-Studio-本地大模型]]

## 相关实体

- [[Ollama]]（替代方案，命令行友好）
- [[Obsidian]]（笔记层）