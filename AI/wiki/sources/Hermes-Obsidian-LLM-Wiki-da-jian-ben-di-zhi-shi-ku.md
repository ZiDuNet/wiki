---
title: "Hermes+Obsidian+LLM Wiki搭建本地知识库"
type: source-summary
tags: [Hermes-Agent, Obsidian, LLM-Wiki, 知识管理, 本地部署, Nous-Research]
sources: ["微信公众号/Obsidian/Hermes+Obsidian+LLM Wiki搭建本地知识库.md"]
created: 2026-05-21
updated: 2026-05-21
---

# Hermes + Obsidian + LLM Wiki 搭建本地知识库

## 系统架构

```
文档导入 → Hermes Agent (自动化执行引擎) → LLM Wiki (知识库规范) → Obsidian (展示层)
```

三个工具各司其职：

| 工具 | 角色 | 核心职责 |
|------|------|---------|
| **Hermes Agent** | 自动化执行引擎 | 接收指令，提取结构化知识，按 LLM Wiki 规范创建文件 |
| **LLM Wiki** | 知识库标准规范 | 定义文件结构（raw/sources/entities/concepts/index/log） |
| **Obsidian** | 笔记展示层 | 双向链接和知识网络可视化（Graph View） |

## 核心优点

1. **完全自动化**：AI 自动整理笔记，无需手动维护
2. **本地存储**：数据永远属于自己，不上传服务器
3. **持久化积累**：知识不断积累，不是每次从零开始
4. **只需提问**：你只需要提问和探索，其他交给 AI

## 使用规则

### 规则 1：说「写入知识库」，Hermes 来整理

当你说"写入知识库"、"导入知识库"时，Hermes 自动：
- 提取关键实体（人物、工具、项目）
- 提取核心概念（方法论、技术原理）
- 创建结构化 Markdown 文件
- 添加双向链接连接相关概念
- 更新知识库索引和日志

### 规则 2：说「结合知识库」，Hermes 来检索

当你说"结合知识库"、"查一下知识库"时，Hermes 检索知识库回答，标注来源。

日常对话 Hermes 不会主动读知识库，避免污染。

### 规则 3：Obsidian 随时可用

wiki 目录可直接拖进 Obsidian 当 Vault 使用，双链跳转、Graph View、全文搜索随时可用。

## LLM Wiki 文件结构

```
knowledge_base/
├── raw/sources/     # 原始文章
├── wiki/
│   ├── entities/    # 实体文件（工具、人物）
│   ├── concepts/    # 概念文件（方法论）
│   ├── index.md     # 知识库索引
│   └── log.md       # 更新日志
```

## 安装步骤

1. **Obsidian**：官网下载，本地 Vault
2. **LLM Wiki**：nashsu/llm_wiki GitHub Releases 下载
3. **Hermes Agent**：`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

## 关联

- [[kai-yuan-xiang-mu-84k-stars-llm-wiki-zi-wo-gou-jian-de-ai-ge-ren-zhi-shi-ku]] — 详细介绍 LLM Wiki
- [[Cursor-AI-Agent-dasdsa-Wiki]] — 用 AI Agent 搭建 Karpathy 的 llm-wiki 知识库
- [[Fast-Note-Sync-NAS-shang-de-Obsidian-tong-bu-fang-an]] — NAS 上的 Obsidian 同步方案
