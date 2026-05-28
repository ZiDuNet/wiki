---
type: source
title: Claude Code 使用笔记：怎样用 MCP、Skill、Harness 搭建一个 AI 公司？
created: 2026-05-28
updated: 2026-05-28
tags: [Claude Code, MCP, Skill, Harness, AI操作系统, Agent工程]
sources: []
---

# Claude Code 使用笔记：怎样用 MCP、Skill、Harness 搭建一个 AI 公司

## 核心认知

[[Claude Code]] 不是聊天框，是 **AI 操作系统**。组件类比：

| 组件 | 类比 | 核心职责 |
|-----|------|---------|
| Skill | 员工技能手册 | 员工怎么做事 |
| MCP | 外部工具连接器 | 真正操作外部世界 |
| Harness | 项目经理 | 谁干什么、按什么顺序 |
| Agent | 员工 | 实际执行任务 |
| CLAUDE.md | 公司制度文件 | 约束行为准则 |
| Project | 业务部门 | 隔离不同业务上下文 |

## Skill 三层结构

**好的 Skill 包含三层**：

1. **知识层**：知道什么是好的结构、SEO 规范、平台差异
2. **流程层**：Step 1 → Step 6 的执行步骤
3. **工具调用层**：读文件、调脚本、处理配图

**关键特性**：Skill 会积累，越用越懂用户，不需要每次重新解释背景。

## MCP 真正能力

MCP = Model Context Protocol，让 AI 真正能连接并操作外部世界。

| MCP 类型 | 具体能力 |
|---------|---------|
| GitHub MCP | 读写仓库、提交 PR |
| 飞书 MCP | 读写文档、操作表格 |
| Browser MCP | 控制浏览器、模拟操作 |
| Figma MCP | 读取设计稿数据 |
| WordPress MCP | 发布文章、管理媒体库 |

**Skill vs MCP**：Skill 是大脑，MCP 是手脚。两者结合才是完整员工。

## Harness 四大能力

**Harness = AI 工作流调度器**：

1. **条件判断**：不达标自动重试，重试三次才问人
2. **上下文传递**：Step 1 输出自动作为 Step 3 输入
3. **并行调度**：配音生成和素材筛选同时跑
4. **错误恢复**：MCP 超时自动重试，不崩流程

## CLAUDE.md 四块内容

每个项目的「宪法」：

1. **项目背景**：我是谁、做什么、目标受众
2. **行为规范**：怎么做（语言、价格、数据支撑）
3. **文件结构**：东西放在哪
4. **禁止事项**：不能做什么（不得直接发布、不得用未确认版权图片）

## 三个关键坑

1. **上下文污染**：多项目共用环境，AI 混淆背景
2. **Skill 冲突**：全局 Skill 互相打架，输出四不像
3. **越用越乱**：塞太多 Skill/规则，AI 不知该用哪套

## 项目隔离结构

```
项目目录/
├── CLAUDE.md           ← 项目宪法
├── .claude/
│   ├── skills/         ← 项目专属技能
│   ├── mcp/            ← 项目专属工具连接
│   ├── harness/        ← 项目专属流程调度
│   └── workflows/      ← 周期性固定任务
├── content/
├── scripts/
├── assets/
└── output/
```

## 全局 vs 项目判断

| 放全局 | 放项目 |
|-------|-------|
| 通用能力（humanizer、文档处理） | 业务绑定（geo-blog、dealer-content） |
| 所有项目都可能用到 | 特定品牌/受众/规范 |

**核心原则**：业务 Skill 永远放项目，80% 混乱问题解决。

## 四阶段进化

1. **纯小白**：把 AI 当搜索引擎，每次从零开始
2. **Prompt 重度爱好者**：研究系统提示词，积累模板
3. **AI 工具大师**：装 Skill、配 MCP、搭自动化
4. **AI 系统使用者**：项目隔离、Harness 调度、能力分类

## 相关概念

- [[Harness]]
- [[Skill系统]]
- [[MCP]]
- [[AI操作系统]]
- [[多项目隔离]]
- [[Agent工程]]

## 相关实体

- [[Claude Code]]