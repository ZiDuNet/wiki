---
title: Profile系统
type: concept
tags: [Hermes, Profile, 多Agent, 配置管理]
created: 2026-05-24
updated: 2026-05-24
---

# Profile系统

**Keywords:** profile, Hermes, 多Agent, 配置分离

## 定义

Profile 系统是 [[Hermes Agent]] 的多代理配置管理机制，每个 Profile 代表一个独立的 AI 代理实例，拥有独立的技能配置、记忆系统和工具集。

## 核心特性

### 配置独立
- 每个 Profile 有独立的模型配置
- 独立的 max_turns（最大交互轮数）
- 独立的工具集（toolsets）
- 独立的 Skills 和 Memory

### 角色专业化
- 为不同团队角色创建专属 Profile
- PM、UI设计师、后端、前端、DevOps 等
- 每个角色理解自己的专业语境

## Profile 配置示例

```bash
# 创建 Profile
hermes profile create pm --model sonnet-4 --max-turns 90

# 配置工具集
hermes profile config set pm toolsets "file,browser,web,memory,skills,todo"

# 用户绑定
hermes pairing approve --profile pm
```

## 12 个团队角色 Profile

| Profile ID | 角色 | 模型 | max_turns |
|-----------|------|------|----------|
| pm | 产品经理 | claude-sonnet-4 | 90 |
| ui-designer | UI设计师 | claude-sonnet-4 | 90 |
| backend | 后端开发 | claude-sonnet-4 | 90 |
| frontend | 前端开发 | claude-sonnet-4 | 90 |
| ai-eng | AI工程师 | claude-sonnet-4 | 120 |
| devops | DevOps | claude-sonnet-4 | 90 |
| qa | QA | claude-sonnet-4 | 90 |
| security | 安全工程师 | claude-sonnet-4 | 90 |
| tech-lead | Tech Lead | **claude-opus-4** | 120 |
| data-analyst | 数据分析师 | claude-sonnet-4 | 120 |
| algo-eng | 算法工程师 | claude-sonnet-4 | 120 |
| prototype-designer | 原型设计师 | claude-sonnet-4 | 90 |

## 关键参数说明

### max_turns
控制单次会话 Agent 与模型的最大交互轮数：
- 常规角色: 90
- 复杂推理角色（AI工程师、数据分析师、Tech Lead）: 120

### 模型选择
- Tech Lead 使用 **claude-opus-4**（最强推理能力）
- 其他角色使用 **claude-sonnet-4**

## 部署架构

**推荐方案**: 单 Gateway + Profile 分离
- 所有代理共享一个 Gateway 入口
- 每个角色完全独立的 Profile 配置
- 统一管理、统一监控、角色隔离

## 批量部署

```bash
./scripts/batch-deploy.sh --count 100 --team engineering
hermes gateway status && hermes profile list
```

## 核心价值

- **专业化分工**: 正确的 AI 做正确的事
- **配置隔离**: 角色之间完全独立
- **批量管理**: 脚本化部署大规模团队

## 相关实体

- [[Hermes Agent]]
- [[Anthropic]]

## 相关概念

- [[多Agent协作]]
- [[Gateway路由]]
- [[知识库体系]]

## 来源文章

- [[团队Hermes多代理系统部署指南]]