---
title: Gateway路由
type: concept
tags: [Hermes, 多Agent, 路由, 智能分发]
created: 2026-05-24
updated: 2026-05-24
---

# Gateway路由

**Keywords:** gateway, routing, agent路由, 智能分发

## 定义

Gateway 路由是 [[Hermes Agent]] 多代理系统的核心组件，负责接收用户请求并将其精准路由到对应的专业代理。Gateway 是整个系统的"交通枢纽"。

## 四种路由方式

### 1. Pairing（用户配对路由）
- 最精准的路由方式
- 每个用户绑定专属 Profile
- 直接路由到绑定的代理

```bash
hermes pairing approve --profile pm
```

### 2. Command（命令路由）
- 用户输入斜杠命令
- Gateway 按命令表直接路由

| 命令 | 路由目标 | 用途 |
|-----|---------|------|
| `/prd` | pm | 起草 PRD |
| `/color` | ui-designer | 生成配色 |
| `/api` | backend | 设计 API |
| `/rag` | ai-eng | RAG 设计 |
| `/debug` | qa | 调试问题 |
| `/deploy` | devops | 部署 |

### 3. Mention（@提及路由）
- 群聊场景核心路由方式
- @pm、@backend 等直接路由

### 4. Keyword（关键词路由）
- 兜底方案
- 分析消息内容关键词
- 匹配阈值 0.7

## 路由优先级

```
@特定代理（最高） → /命令 → 关键词匹配 → 用户已配对 → 默认Profile（兜底）
```

## 关键词路由规则

| 角色 | 触发关键词 |
|-----|----------|
| 产品经理 | 需求、PRD、用户故事、优先级、产品规划 |
| UI设计师 | 配色、设计、界面、图标、视觉、组件 |
| 后端开发 | API、数据库、服务、接口、REST、ORM |
| AI工程师 | LLM、RAG、Agent、Prompt、Embedding |
| DevOps | 部署、CI/CD、Docker、K8s、监控 |

## 降级策略

- 关键词匹配阈值: 0.7
- 匹配分数低于阈值时，降级到用户已绑定 Profile
- 确保绑定用户始终得到专属代理服务

## 核心价值

- **降低使用门槛**: 用户无需学习复杂命令
- **精准触达**: 正确的问题到达正确的代理
- **多场景覆盖**: 四种路由方式互相补充

## 相关实体

- [[Hermes Agent]]
- [[Anthropic]]

## 相关概念

- [[多Agent协作]]
- [[Profile系统]]
- [[专业化分工]]

## 来源文章

- [[团队Hermes多代理系统部署指南]]