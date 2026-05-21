---
title: "盘点 10 个 GitHub 新开源项目：Star 快速攀升"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: ["盘点 10 个刚刚开源，但 Star 攀升很快的 GitHub 项目。.md"]
tags: [GitHub, AI开源项目, 本地推理, Agent工具, 幻灯片模板, 学习路线]
---

# 盘点 10 个 GitHub 新开源项目

## 摘要

本文盘点了 10 个近期开源且 Star 快速增长的项目，涵盖本地大模型推理、多后端虚拟文件系统、提示词工程、内容创作 Agent、安全漏洞、桌面应用开发等多个方向。

## 重点项目

### ds4 — Mac 本地 DeepSeek V4 推理引擎

**定位**：antirez（Redis 作者）开源，用 C 语言 + Apple Metal 优化，让 MacBook 本地跑 284B 参数大模型。

**核心技术**：
- KV 缓存磁盘持久化：将 KV 缓存写入 SSD，会话上下文复用
- 2-bit 不对称量化：仅对 MoE 路由专家激进量化，共享专家保持高精度
- M3 Max 128GB：250 tokens/s (prefill)，21 tokens/s (生成)
- M3 Ultra 512GB：468 tokens/s (prefill)
- 兼容 OpenAI 和 Anthropic API 格式，Claude Code、opencode 可直接对接

**链接**：https://github.com/antirez/ds4

### Mirage — 统一虚拟文件系统

**定位**：给 AI Agent 套一层统一虚拟文件系统，ls/cat/grep/cp 等 Unix 命令即可跨服务操作。

**支持服务**：Google Drive、Slack、Gmail、Redis、GitHub、Notion、Linear、Trello、Discord、Telegram、MongoDB、SSH

**特点**：
- Python/TypeScript SDK + CLI
- 内置 OpenAI Agents SDK、Vercel AI SDK、LangChain、Pydantic AI 适配层
- 上线一天破 1000 Star

**链接**：https://github.com/strukto-ai/mirage

### TokenSpeed — Agent 工作负载推理引擎

**定位**：专为 Agent 场景设计的 LLM 推理引擎，目标达到 TensorRT-LLM 级性能 + vLLM 级易用性。

**背景**：
- 主导方：LightSeek Foundation（非营利组织）
- 协作方：NVIDIA DevTech、AMD Triton、通义千问推理团队、Together AI

**实测**：Kimi K2.5 最小延迟场景比 TensorRT-LLM 快约 9%，100 TPS/User 附近吞吐量高约 11%。MLA 已被 vLLM 项目采用。

**链接**：https://github.com/lightseekorg/tokenspeed

### beautiful-html-templates — 32 套 HTML 幻灯片模板

**定位**：给 AI 编程 Agent 用的 HTML 幻灯片模板库，覆盖 Soft Editorial、Retro Windows、Sakura Chroma、8-Bit Orbit 等风格。

**特点**：
- 每套模板含完整视觉系统（字体、配色、装饰、导航）
- 内置 Agent 操作手册，AI 会先匹配风格再生成内容
- 单 HTML 文件，零依赖，浏览器直接演示

**链接**：https://github.com/zarazhangrui/beautiful-html-templates

### awesome-agentic-ai-zh — 从零学 AI Agent 中文路线图

**定位**：7 阶段学习地图，Track A（CLI Power User）教用现成 Agent 工具，Track B（Agent Builder）从零造 Agent 到 Multi-Agent 编排。总时长 14-19 周。

**特色**：繁中、简中、英文三语对照；145 个精选项目；5 条按身份分流路线（研究员、开发者、老师、知识工作者、日常使用者）

**链接**：https://github.com/WenyuChiou/awesome-agentic-ai-zh

### 其他项目

| 项目 | 描述 |
| --- | --- |
| yao-open-prompts | 91 个实战中文提示词，九大场景分类 |
| cheat-on-content | 内容创作 Agent，闭环评分+预测+复盘进化机制 |
| Codex++ | Codex App 增强补丁，解锁 API Key 模式插件 + 会话删除 |
| dirtyfrag | Linux 内核网络提权漏洞链，Ubuntu/RHEL/CentOS/Fedora/openSUSE 通杀 |
| zero-native | Vercel Labs 原生 Shell + Web UI 框架，用 Zig 写原生层 |

## 关键实体

- [[antirez]] — Redis 作者，ds4 项目发起人
- [[Mirage]] — 统一虚拟文件系统
- [[TokenSpeed]] — Agent 推理引擎
- [[Claude-Code]] — 可直接对接 ds4 等工具
- [[Mac本地推理]] — ds4/omlx 等项目所在领域

## 关键概念

- [[本地部署]] — Mac 本地运行大模型
- [[AI编程]] — Agent 编程工具生态
- [[知识库构建]] — 学习路线图类资源
