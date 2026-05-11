---
tags: [synthesis, agent, multi-agent, 架构, 协作模式, harness]
sources:
  - Agent = Model + Harness！一文讲透 Harness 的设计与未来！
  - 从_单打独斗_到_团队协作_：多Agent系统如何改变AI工作方式
  - 深入 Open Agent SDK（四）：多 Agent 协作——子代理、团队与任务编排
  - 企业应用 AI Agent 的架构设计
  - 多智能体系统：把 AI 组建成一家公司，而不是堆砌人头
  - 写好一个 Agent Skill，到底需要注意什么？
  - SuperAgent 架构爆发：57K Stars 背后的 AI 员工操作系统真相
  - 单Agent时代正式结束：一个干不过，就上300个
  - 我把整个技术团队做成了 AI Agent：10 个角色、18 个 Skill
  - 当Agent开始干活，每个人都是"管理者"
  - 传统 SaaS 接一层 Agent 操作引擎
  - 转AI Agent工程师路线图
  - ReAct、Plan、Multi-Agent全都支持并行了
created: 2026-05-10
updated: 2026-05-10
---

# Agent 架构实践

## 概述

Agent 架构是 AI 从"聊天工具"走向"生产力系统"的关键。本文综合 30 篇源文章，从单 Agent 到多 Agent 协作，从 Harness 工程到企业落地，系统梳理 Agent 架构的设计哲学与实践路径。

## 一、核心公式：Agent = Model + Harness

### 1.1 什么是 Harness

Harness 是"所有不属于模型本身的代码、配置以及执行逻辑"。裸模型不能算作 Agent；只有当 Harness 为其提供状态管理、工具调用能力、反馈循环以及可执行约束时，它才真正成为 Agent。

Harness 通常包括：
- 系统提示词
- 工具与技能（以及 MCP）及其说明
- 封装好的基础设施（文件系统、沙箱、浏览器）
- 编排逻辑（子 Agent 生成与交接、模型路由）
- Hook 或中间件（上下文压缩、Lint 检查等）

### 1.2 Harness 的六大组件

| 组件 | 作用 | 实现方式 |
|------|------|---------|
| 文件系统 | 持久存储与上下文管理 | 提供读写抽象 + Git 版本控制 |
| Bash/代码执行 | 通用工具能力 | ReAct 循环 + 代码生成 |
| 沙箱 | 安全执行环境 | Docker 容器隔离 + 命令白名单 |
| 工具系统 | 专用能力扩展 | Function Calling + MCP |
| 记忆系统 | 跨会话状态保持 | 文件存储 + 向量检索 |
| Hook 机制 | 可控边界与自动化 | PreToolUse / PostToolUse / Stop |

## 二、单 Agent vs 多 Agent

### 2.1 单 Agent 的适用场景

单 Agent 适合：目标明确、步骤有限、不需要并行处理的任务。

Claude Code 的核心执行路径就是一个单线程主循环（async generator function）：
- 简单、好调试、好测试
- 复杂度低，错误处理清晰
- Anthropic 工程团队的总结："一个简单的单线程主循环，配合有纪律的工具，就能实现可控的自主性。"

### 2.2 多 Agent 的价值

当任务具备以下特征时，多 Agent 架构更有优势：
- 需要多种专业能力
- 需要并行处理
- 需要角色分工与协作

Anthropic 数据：一个以 Claude Opus 4 为主 Agent、Sonnet 4 为子 Agent 的系统，研究任务性能比单 Agent 高出 90.2%。

**但前提条件很严格：** 任务天然适合分工、职责边界清晰、子 Agent 只返回摘要（避免上下文污染）。多 Agent 系统在适合的任务上提升 81%，在错误场景上可能降低 70%。

## 三、多 Agent 组织架构（四种模式）

### 3.1 层级型（Hierarchical）

```
Orchestrator（CEO）
    /    |    \
 Agent  Agent  Agent（部门）
```

最常见的模式。一个主 Agent 负责规划和协调，分发任务给专业子 Agent，最后汇总结果。

- **优点**：集中控制，调试简单，适合合规要求高的场景
- **风险**：Orchestrator 可能成为瓶颈
- **代表**：Anthropic Research、Hermes Agent

### 3.2 顺序型（Sequential）

```
Agent A -> Agent B -> Agent C -> Result
```

流水线模式。每个 Agent 处理完传给下一个。

- **优点**：复杂度低
- **缺点**：执行慢，一个环节卡住全链等待
- **适合**：文档审查、数据处理管道

### 3.3 网络型（Network / Peer-to-Peer）

```
Agent A <-> Agent B
    |         |
Agent C <-> Agent D
```

去中心化模式，Agent 之间点对点通信。

- **优点**：弹性高，适合动态场景
- **风险**：协调复杂，可能出现冲突

### 3.4 事件驱动型（Event-Driven）

异步执行，响应式架构。适合实时系统，但需要强大的事件总线。

## 四、Agent 角色设计

### 4.1 三层架构

```
顶层: Orchestrator（编排者）
  - 角色：项目经理/架构师
  - 职责：接收需求，分解任务，分配，整合结果

中层: Specialist Agents（专家型 Agent）
  - 研究员、设计师、编码师、评审员
  - 具备专业工具集，不参与决策调度

底层: Tools（工具层）
  - 终端命令、文件操作、网络请求、浏览器
  - 无智能，纯功能执行
```

### 4.2 深度限制

最大生成深度（max_spawn_depth）默认 2 层：
- 防止无限递归和资源耗尽
- 保持任务的可控性和可追溯性
- 类似企业架构的"管理幅度"

### 4.3 实战案例：10 个角色的 AI 团队

| 角色 | 核心职责 |
|------|---------|
| Knowledge Curator | 知识守门人，自动审查沉淀 |
| CTO | 技术战略、商务拓展 |
| 架构师 | 方案评审、架构设计 |
| 部门总监 | 团队管理、项目管控 |
| 后端工程师 | 编码、接口设计、代码审查 |
| 前端工程师 | 页面开发、组件设计 |
| QA 工程师 | 测试用例、缺陷跟踪 |
| DevOps 工程师 | 部署、监控、CI/CD |
| 需求分析师 | 需求收集、文档输出 |
| PM/PMO | 项目计划、进度跟踪 |

这套系统的关键是 **记忆层** 和 **Knowledge Curator（知识守门人）**，让系统具备自进化能力。

## 五、Agent 工程化最佳实践

### 5.1 子 Agent 通信

通过邮箱系统实现 Agent 间通信：
- 每个子 Agent 有独立上下文
- 子 Agent 只返回摘要给主 Agent
- 避免上下文污染

### 5.2 错误处理

生产级 Agent 的韧性来自错误后的结构化证据：
1. **可继续错误**：工具返回失败结果，下一轮改策略
2. **可等待错误**：API 限流进入 retry
3. **可解释终止**：命中预算上限，给出 subtype
4. **不可恢复中断**：请求取消或运行时崩溃

### 5.3 任务编排

Open Agent SDK 提供三个层面的解决方案：
- **子 Agent**：主 Agent 动态生成，委派专门任务
- **Task 系统**：追踪多步骤工作的进度和结果
- **Team + 消息传递**：多个 Agent 组成团队，通过邮箱系统通信

## 六、选型建议

| 场景 | 推荐架构 | 理由 |
|------|---------|------|
| 个人开发 | 单 Agent + Skills | 简单高效，成本低 |
| 小团队协作 | 层级型 2 层 | 职责分明，易调试 |
| 研究分析 | 主 Agent + 并行子 Agent | 天然适合分工 |
| 企业生产 | 层级型 + 沙箱 + 审计 | 合规可控 |
| 数据管道 | 顺序型 | 步骤明确，流程固定 |

## 相关页面

- [[GitHub-15000-Stars这款-AI-技能集让-Claude-Code-变身内容创作神器]] -- Claude Code Agent 工程深度解析
- [[Skills生态全景]] -- Skills 设计与使用
- [[拆开Hermes-Agent企业怎么自建一套会“越用越强”的AI-Agent系统]] -- 企业级落地方法论
- [[Harness框架]] -- Harness 设计哲学
- [[Multi-Agent]] -- 多 Agent 协作
- [[React]] -- ReAct 循环
- [[Agent工程化]] -- Agent 工程化实践
- [[自进化系统]] -- Agent 自进化设计
