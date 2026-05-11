---
tags: [concept, 配置管理]
created: 2026-05-10
updated: 2026-05-10
---

# AGENTS.md配置

> OpenClaw 的 Agent 配置文件，定义 Agent 的行为规则、工具权限、协作模式等。是 Agent 工程化的核心配置。

## 核心定义

AGENTS.md 是 [[OpenClaw]] 框架中最重要的配置文件之一，相当于 AI Agent 的"员工手册"。它定义了 Agent 在接手任务时应该遵循的工作流程、确认机制、权限边界和协作规则。

与 [[SOULmd配置|SOUL]] 不同：SOUL.md 管"怎么说话"（性格和风格），AGENTS.md 管"怎么做事"（工作流程和行为规则）。

## 核心配置内容

### 1. 接活规则
- 接活先复述理解，确认方向对了再动手
- 不明确的需求要主动追问
- 禁止未确认就直接执行高风险操作

### 2. 任务流程
- 用户说"写一篇"、"帮我写" → 进入内容创作模式
- 用户说"/发布" → 进入发布确认模式
- 确认要素：目标读者 + 核心价值 + 预期篇幅

### 3. 权限与安全
- 文件操作权限边界（哪些目录可读/可写）
- 网络访问限制
- 数据处理安全规则

### 4. 协作模式
- 多 Agent 场景下的任务分发规则
- 子 Agent 的调用时机和交接流程
- Agent 之间的通信协议

## 配置文件体系

```
~/.openclaw/workspace/
├── SOUL.md          # AI 的性格与风格
├── USER.md          # 关于用户的信息
├── AGENTS.md        # AI 的工作手册 ← 本页面
├── IDENTITY.md      # AI 的对外身份形象
├── TOOLS.md         # 工具使用说明
├── HEARTBEAT.md     # 心跳定时任务描述
└── MEMORY.md        # 长期记忆
```

## 实用配置模板

社区总结的 10 套可直接复制的配置，覆盖：
- 内容创作（公众号/小红书/知乎）
- 信息获取（新闻聚合/竞品监控）
- 代码开发（PR Review/测试）
- 日常办公（邮件/日报）
- 彩蛋配置（AI 自动打卡/任务失败自动复盘）

## 常见问题

装了满满的 Skills、写好了 SOUL.md，Agent 还是在乱跑？问题通常在于：
- AGENTS.md 从来没有认真写过
- 写得太抽象，AI 不知道怎么执行
- 缺乏具体的判断条件和分支逻辑

## 类别

配置管理

## 相关概念

- [[SOUL配置]] — Agent 性格配置
- [[Harness框架]] — AGENTS.md 是 Harness 的核心组件
- [[Agent工程化]] — Agent 工程化的配置实践
- [[门禁机制]] — AGENTS.md 中的权限控制机制
- [[Cron定时任务]] — 与 HEARTBEAT.md 配合实现定时任务
- [[多Agent协作]] — 多 Agent 场景下的 AGENTS.md 编排
- [[Token优化]] — 精简配置减少 Token 消耗
- [[数据安全]] — 权限边界与数据保护
- [[记忆系统]] — 与 MEMORY.md 的协同

## 相关实体

- [[OpenClaw]] — AGENTS.md 的主要使用框架
- [[Hermes-Agent]] — 类似的配置体系
- [[飞书]] — 通过飞书交互时遵循 AGENTS 规则
- [[小红书]] — 内容创作场景下的配置参考

## 相关文章

- [[oc-OpenClaw实操指南19｜SOULmd-AGENTSmd实战给AI注入性格边界和判断力]] — 实战详解
- [[oc-OpenClaw总失控你缺的不是Skill是一份AGENTSmd配置SOP]] — 10 套可复制配置
- [[oc-OpenClaw进阶多Agent路由协作权限全在这里了]] — 多 Agent 配置
- [[oc-一文讲透-OpenClaw-里到底该用-Multi-Agent还是主-Agent-Sub-Agent]] — Agent 模式选择
- [[oc-智能体搭建-如何用OpenClaw搭建你的“一人公司”附完整配置模板]] — 完整配置模板
