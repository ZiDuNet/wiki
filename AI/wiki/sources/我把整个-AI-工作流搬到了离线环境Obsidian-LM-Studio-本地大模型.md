---
type: source
title: 我把整个 AI 工作流搬到了离线环境：Obsidian + LM Studio + 本地大模型
created: 2026-05-28
updated: 2026-05-28
tags: [离线AI, 本地大模型, Obsidian, LM Studio, 隐私安全, 知识管理]
sources: []
---

# 我把整个 AI 工作流搬到了离线环境

## 核心观点

完整的离线 AI 工作流方案：**Obsidian（笔记与知识管理）+ LM Studio（本地模型运行器）+ 本地 LLM 插件（连接桥梁）**。不依赖任何云端服务，数据永不外传，断网可用。

## 三大动机

1. **隐私与数据安全**：笔记、研究、思考过程不会成为训练数据的一部分
2. **断网可用性**：航班、高铁、咖啡馆 WiFi 挂了都能用
3. **成本可控**：一次性下载，无限次使用，无 Token 费用

## 技术栈四层架构

| 层级 | 工具 | 职责 |
|-----|------|------|
| 模型层 | [[LM Studio]] | GGUF 模型运行，本地 API 服务（localhost:1234） |
| 笔记层 | [[Obsidian]] | 本地 Markdown 存储，双向链接，图谱视图 |
| 连接层 | Copilot/Text Generator/Smart Connections | Obsidian 插件，连接模型 |
| 辅助层 | [[Ollama]]/llama.cpp/PrivateGPT | 命令行工具，本地文档问答 |

## 推荐模型选择

- **日常对话与写作**：Qwen2.5-7B / Llama-3.1-8B
- **代码辅助**：CodeQwen / DeepSeek-Coder
- **轻量场景**：Phi-3-mini（3.8B，4GB 内存）

## 硬件要求

| 等级 | 配置 | 模型能力 |
|-----|------|---------|
| 入门级 | 8GB 内存 | 7B 模型 4-bit 量化，5-10 token/s |
| 舒适级 | Apple Silicon M1/M2/M3 | 7B 模型，20-40 token/s |
| 进阶级 | RTX 4060 | 13B 模型流畅运行 |
| 高性能 | 48GB+ VRAM | 70B 模型（双 RTX 3090/Mac Studio） |

## 关键配置步骤

1. 安装 LM Studio，下载模型（Qwen2.5-7B-Instruct-GGUF）
2. 启动本地 API Server（`http://localhost:1234/v1`）
3. 配置 Obsidian Copilot 插件连接 LM Studio
4. 断网验证：模型响应 + 对话正常 + 笔记保存

## 局限性与应对

- **模型能力上限**：选择最新开源模型（Qwen2.5、Llama-3.1）
- **响应速度**：Apple Silicon 或 GPU 加速
- **模型更新**：关注 HuggingFace，定期下载新版本

## 相关概念

- [[离线AI工作流]]
- [[本地大模型]]
- [[隐私计算]]
- [[知识管理]]

## 相关实体

- [[Obsidian]]
- [[LM Studio]]
- [[Ollama]]