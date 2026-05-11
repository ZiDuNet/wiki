---
tags: [synthesis, skills, agent, 生态, 设计模式]
sources:
  - Agent Skills 解剖：五个设计决策拯救被上下文淹没的 AI Agent
  - MCP 与 Skills：AI Agent 真正走向生产力系统的两块拼图
  - Superpowers：把软件工程最佳实践封装成AI可执行的技能
  - 写好一个 Agent Skill，到底需要注意什么？从 6 个维度拆解 Skill 黄金法则
  - 2026用上这48个Skills，你就跑赢了95%的人
  - Skills商店来了：5w+人在用的热门Skills，我试了一遍
  - Skills推荐 · 特别篇｜PPT-Master：让AI组队帮你生成真正可编辑的PPT
  - Skill配方｜我终于找到了好用的PPT工具
  - Skill配方｜做方案再也不用磕配图了
  - MCP 与 Skills：AI Agent 真正走向生产力系统的两块拼图
  - AI Skill 碎片化的解法来了：一个中央库统一管理 27 个平台
  - Skills.Homes：Claude Code Skill 专属「应用商店」
  - aweskill：让AI Agents 自己搞定skills 管理
  - Skill 的机会不在单点，在编排
  - 分享6个宝藏Skills
  - 必装技能库：baoyu-skills
  - 精选 10 个开发者常用的 AI 智能体技能
created: 2026-05-10
updated: 2026-05-10
---

# Skills 生态全景

## 概述

Skills 是 AI Agent 真正走向生产力系统的关键拼图。如果说 MCP 解决的是"Agent 怎么连接外部世界"，那么 Skills 解决的是"Agent 怎么学会一套稳定的做事方法"。本文综合 52 篇源文章，全面解析 Skills 的设计哲学、核心架构、生态工具和最佳实践。

## 一、Skills 是什么

### 1.1 定义

Skills 是一种轻量、开放的格式，用于用专门知识和工作流扩展 AI Agent 的能力。一个 Skill 的核心就是一个包含 `SKILL.md` 的文件夹，里面至少有 metadata 和 instructions，也可以包含脚本、参考资料、模板和其他资源。

### 1.2 与 MCP、Tool Calling 的区别

| 维度 | Tool Calling | MCP | Skills |
|------|-------------|-----|--------|
| 解决的问题 | 让模型"可以做" | 标准化外部能力暴露 | 让 Agent"知道怎么正确使用" |
| 本质 | 单次功能调用 | AI 时代的连接协议 | 操作经验和流程知识的封装 |
| 加载方式 | 始终加载、始终可见 | 按需连接 | 渐进式披露，按需加载 |
| 成本 | 全额 | 按连接 | 未用时约等于零 |

## 二、Skills 核心架构

### 2.1 Skill 是一个文件夹

```
my-skill/
├── SKILL.md          # 唯一必需文件
├── references/       # Agent 按需读取的文档
├── assets/           # 模板和品牌文件
└── scripts/          # Agent 可执行的代码
```

因为 Skill 就是文件，你可以用 Git 做版本控制，用 Pull Request 做 diff，在项目间复制，发布到 GitHub。**格式即合约**。

同一个 SKILL.md 在 Claude Code、Codex、Gemini CLI、Cursor、Agent Development Kit、LangChain 等工具中都能用。**一个文件夹，多个运行时**。

### 2.2 渐进式披露（三层加载）

这是 Skills 不让上下文爆炸的核心机制：

| 层级 | 内容 | 加载时机 | Token 成本 |
|------|------|---------|-----------|
| L1 元数据 | name + description | 会话开始时始终加载 | ~100 token/Skill |
| L2 指令 | SKILL.md 正文 | 描述匹配用户任务时 | 几千 token |
| L3 参考 | references/assets/scripts | L2 指令明确指向时 | 按需 |

安装了 20 个 Skill 的 Agent，前置成本和安装 1 个的一样。第 21 个不影响之前任务的代价。

**关键：保持 SKILL.md 简短，把边缘情况和参考表格推到 references/ 里。**

### 2.3 Agent 路由查询

当请求进来时，模型扫描描述目录，直接从自己上下文中做决定。没有嵌入步骤，没有相似度分数。**LLM 就是路由器。**

匹配是排他的：每个任务只激活一个 Skill，其他停在 L1。正文永远不进入上下文窗口。

## 三、Skill 黄金法则（6 维度）

### 法则一：Description -- 触发率决定生死

写好 Description 的公式：**做什么 + 什么时候用 + 典型触发词**。

```yaml
# 反面
description: 处理PDF文档

# 正面
description: 从PDF文档中提取文本和表格数据，支持扫描件OCR识别。
  当用户上传PDF文件要求提取内容、解析表格时使用此技能。
```

### 法则二：结构 -- 像函数一样设计边界

一个 Skill 应该完成一个"连贯的工作单元"。判断标准：能不能用一句话说清这个 Skill 解决什么问题？

### 法则三：指令 -- 不要给 AI 留想象空间

明确：输出格式、约束条件、边界情况处理、禁止行为。

### 法则四：触发条件 -- 让 AI 自己判断何时用

采用"触发条件"写法，明确说明在什么场景下必须使用。不是"你可以用"，而是"必须用"。

### 法则五：输出规范 -- 格式即合约

定义清晰的输出结构，让下游工具可以直接消费。

### 法则六：进化 -- Skill 不是一次性的

建立反馈机制，让 Skill 在使用中不断优化。

## 四、Superpowers：工程最佳实践的封装

Superpowers 框架把软件工程最佳实践封装成可自动触发的技能：

### 4.1 核心设计

- **技能优先级高于默认行为**：AI 不能自行决定"太简单不需要用技能"
- **硬性门控（HARD-GATE）**：不可逾越的边界，违反即失败
- **SKILL.md 格式**：YAML frontmatter（name + description）+ Markdown Body

### 4.2 核心技能

| 技能 | 用途 |
|------|------|
| brainstorming | 需求分析，任何创造性工作前必须使用 |
| writing-plans | 将需求转化为实施计划 |
| executing-plans | 执行已审批的计划 |
| verification-before-completion | 完成前验证 |
| systematic-debugging | 系统化调试 |
| test-driven-development | 测试驱动开发 |

### 4.3 工作流

```
用户消息 -> 检查是否有适用的技能（哪怕只有1%可能）-> 加载技能 -> 执行
```

## 五、Skills 生态与平台

### 5.1 分发平台

| 平台 | 特点 |
|------|------|
| **ClawHub** | OpenClaw 官方技能商店，`npx clawhub install skill名称` |
| **Skills.Homes** | Claude Code Skill 专属"应用商店"，分类浏览和安装 |
| **GitHub** | 大量开源 Skills 仓库，通过 `npx skills add` 安装 |
| **aweskill** | 让 AI Agents 自己管理 skills |

### 5.2 安装方式

```bash
# ClawHub 上的 Skill
npx clawhub install skill名称

# GitHub 上的 Skill
npx skills add GitHub仓库地址
```

### 5.3 热门 Skills 分类

**内容创作类：**
- baoyu-skills（13000+ Star）：从选题到发一条龙
- 文章配图神器，100+ 风格任意选

**开发工程类：**
- Superpowers：软件工程最佳实践
- Code Review、TDD、Debugging

**PPT 制作类：**
- ppt-master：多角色 AI 协作，原生 PPTX 输出
- html-ppt-skill：WebGL 流体背景，HTML 格式
- guizang-ppt-skill：电子杂志风格

**科研学术类：**
- 147 个 Claude Scientific Skills
- 文献分析、论文写作

**办公效率类：**
- 飞书 CLI 全家桶
- 会议纪要、周报生成

## 六、如何创建自己的 Skill

### 6.1 基本结构

```
my-skill/
├── SKILL.md
└── references/
    └── example.md
```

### 6.2 SKILL.md 模板

```yaml
---
name: my-skill
description: 一句话说清核心能力 + 什么时候用 + 典型触发词
---

## 触发条件
明确说明在什么场景下使用

## 执行步骤
1. 第一步做什么
2. 第二步做什么

## 输出规范
- 格式要求
- 约束条件

## 禁止行为
- 不要做什么
```

### 6.3 设计原则

1. **Description 优先**：花在 description 上的时间应该多于正文
2. **渐进式披露**：正文保持简短，细节推到 references/
3. **单一职责**：一个 Skill 解决一个连贯的工作单元
4. **格式即合约**：用标准格式确保跨平台兼容

## 相关页面

- [[GitHub-15000-Stars这款-AI-技能集让-Claude-Code-变身内容创作神器]] -- Claude Code 完整使用指南
- [[Agent架构实践]] -- Agent 架构设计
- [[PPT-制作全流程]] -- PPT 相关 Skills 评测
- [[Skills技能系统]] -- Skills 系统概念
- [[Skill开发]] -- Skill 开发指南
- [[Skill设计]] -- Skill 设计模式
- [[MCP协议]] -- 外部服务连接协议
- [[Superpowers]] -- Superpowers 框架
