---
title: 团队 Hermes 多代理系统部署指南
type: source-summary
tags: [Hermes, 多Agent, 团队协作, Gateway路由, Profile配置, 知识库体系]
sources: [团队 Hermes 多代理系统部署指南.md]
created: 2026-05-24
updated: 2026-05-24
---

# 团队 Hermes 多代理系统部署指南

## 来源信息

- **来源**: AI已经来啦
- **时间**: 2026-05-24
- **链接**: 微信公众号文章

## 概要

本文详细介绍如何使用 [[Hermes Agent]] 搭建一套完整的团队级 AI 代理系统，核心理念是 **专业化分工 + 统一调度**。涵盖 12 个专业角色代理配置、Gateway 智能路由系统、三层知识库体系、批量部署脚本及成本估算。

## 核心问题与解决方案

### 痛点

1. **专业语境缺失**: 通用 AI 无法理解各专业角色的语境和需求
2. **跨角色协作流程不清晰**: 传统 AI 无法理解 PM → 设计 → 前端 → 后端 → QA → DevOps 的完整链条
3. **知识分散难以复用**: 编码规范、设计系统、API 文档分散在多处

### Hermes 解决方案

为每个团队角色创建"量身定制"的 AI 代理：
- 独立的技能配置（Skills）
- 独立的记忆系统（Memory）
- 通过 Gateway 智能路由精准触达
- 代理之间可互相协作形成完整链条

## 整体架构

### 四层架构

| 层级 | 组成 | 职责 |
|-----|------|------|
| 第一层 | Hermes Gateway | 统一入口，负责路由 |
| 第二层 | 平台适配层 | 对接飞书、Slack、Discord、Email |
| 第三层 | Routing Middleware | 核心决策引擎，决定路由目标 |
| 第四层 | Profile Agent 集群 | 12 个角色的专属 AI 代理 |

### 部署方式

**方式一（推荐）**: 单 Gateway + Profile 分离
- 所有代理共享一个 Gateway 入口
- 每个角色有完全独立的 Profile 配置
- 适合: 企业内团队、多角色协作、中大型团队

**方式二**: 共享助手 + 专业子代理
- 所有角色共用一个基础代理
- 遇到复杂问题委托给子代理
- 适合: 小团队、部署简单

## 12 个专业角色配置

### 配置总览

| 角色 | Profile ID | 模型 | max_turns | 工具集 |
|-----|-----------|------|----------|--------|
| 产品经理 | pm | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| UI 设计师 | ui-designer | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| 后端开发 | backend | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| 前端开发 | frontend | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| AI 工程师 | ai-eng | claude-sonnet-4 | 120 | file, browser, web, memory, skills, todo |
| DevOps | devops | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| QA | qa | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| 安全工程师 | security | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |
| Tech Lead | tech-lead | **claude-opus-4** | 120 | file, browser, web, memory, skills, todo |
| 数据分析师 | data-analyst | claude-sonnet-4 | 120 | file, browser, web, memory, skills, todo |
| 算法工程师 | algo-eng | claude-sonnet-4 | 120 | file, browser, web, memory, skills, todo |
| 原型设计师 | prototype-designer | claude-sonnet-4 | 90 | file, browser, web, memory, skills, todo |

> **Tech Lead 使用 claude-opus-4**: 架构决策和技术评审需要最强推理能力

## Gateway 路由架构

### 四种路由方式

| 路由方式 | 优先级 | 描述 |
|---------|--------|------|
| Pairing（用户配对） | 最高 | 用户绑定 Profile，直接路由到专属代理 |
| Command（命令路由） | 高 | `/prd`、`/color`、`/api` 等斜杠命令 |
| Mention（@提及） | 高 | 群聊中 @pm、@backend 等 |
| Keyword（关键词） | 低（兜底） | 分析消息内容关键词判断 |

### 路由优先级

```
@特定代理 → /命令 → 关键词匹配(阈值0.7) → 用户已配对 → 默认Profile
```

### 命令路由表

| 命令 | 路由到 | 用途 |
|-----|-------|------|
| `/prd` | pm | 起草 PRD |
| `/color` | ui-designer | 生成配色 |
| `/api` | backend | 设计 API |
| `/rag` | ai-eng | RAG 设计 |
| `/debug` | qa | 调试问题 |
| `/deploy` | devops | 部署 |
| `/data` | data-analyst | 数据分析 |

### 关键词路由规则示例

- **产品经理**: 需求、PRD、用户故事、优先级、产品规划、竞品分析
- **UI设计师**: 配色、设计、界面、图标、视觉、组件、设计规范、品牌
- **后端开发**: API、数据库、服务、接口、后端、REST、ORM
- **AI应用工程师**: LLM、RAG、Agent、Prompt、大模型、Embedding
- **DevOps**: 部署、CI/CD、Docker、K8s、监控、告警

## 三层知识库架构

| 层级 | 名称 | 内容 | 权限 |
|-----|------|------|------|
| 第一层 | 共享知识库 | 公司规范、技术栈标准、API文档、编码规范 | 所有Profile可读，Tech Lead可读写 |
| 第二层 | 角色知识库 | PRD模板、设计系统、数据库Schema等 | 仅本角色可读写 |
| 第三层 | 外部知识源 | Obsidian、飞书云文档、GitHub Wiki、内部文档站 | 通过 MCP 协议集成 |

### 知识库目录结构

```
~/.hermes/knowledge/
├── shared/                  # 共享知识库
│   ├── company norms/
│   ├── tech stack/
│   └── api-docs/
├── profiles/                # 角色知识库
│   ├── pm/prd-templates/
│   ├── backend/schemas/
│   └── ui-designer/design-system/
└── external/                # 外部知识源配置
    ├── obsidian-config.json
    ├── feishu-wiki-config.json
    └── github-wiki-config.json
```

## 批量部署脚本

```bash
# 1. 创建 Profile
hermes profile create pm --model sonnet-4 --max-turns 90

# 2. 配置工具集
hermes profile config set pm toolsets "file,browser,web,memory,skills,todo"

# 3. 批量部署
./scripts/batch-deploy.sh --count 100 --team engineering

# 4. 验证部署
hermes gateway status && hermes profile list
```

### 用户绑定命令

```bash
# 将用户绑定到 pm Profile
hermes pairing approve --profile pm
```

## 成本估算（100 人团队/年）

| 方案 | 年成本 | 适用场景 |
|-----|-------|---------|
| 本地化部署（DeepSeek-R1 671B） | ~210万（一次性硬件） | 大规模、长期、数据私有 |
| Claude Code 企业版（$200/人/月） | ~144万/年 | 高 AI 能力要求 |
| GitHub Copilot Enterprise（$39/人/月） | ~28万/年 | 轻量级开发辅助 |
| **混合方案（推荐）** | **80-120万/年** | 性价比最优 |

> **选型建议**: 小团队（<10人）用 Copilot Enterprise；中等团队（10-50人）用混合方案；大型团队（>50人）做 TCO 分析

## 核心价值总结

1. **专业化分工**: 正确的 AI 做正确的事
2. **智能路由**: Gateway 四种路由方式降低使用门槛
3. **知识库让 AI 懂行**: 三层体系确保建议基于团队实际规范
4. **批量部署**: 新成员几分钟获得完整 AI 辅助能力
5. **混合方案性价比最优**: 不同角色用不同工具

## 相关实体

- [[Hermes Agent]] - 核心产品
- [[Anthropic]] - 模型提供商（claude-sonnet-4, claude-opus-4）

## 相关概念

- [[多Agent协作]]
- [[Profile系统]]
- [[Gateway路由]]
- [[知识库体系]]
- [[MCP协议]]
- [[专业化分工]]