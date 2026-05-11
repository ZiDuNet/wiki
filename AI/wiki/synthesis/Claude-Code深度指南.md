---
tags: [synthesis, claude-code, agent, skills, mcp, 最佳实践]
sources:
  - Claude Code 完全教程：8个层级，从安装到一人团队
  - Claude Code 最佳实践：让它强大 100 倍的正确用法
  - Claude Code 最佳实践（要点总结）
  - 拆解 Claude Code 的大循环机制
  - Claude Code 的 Agent 工程
  - 效率暴涨10倍！Claude Code：5核心+42高阶实操技巧
  - (二)Claude Code在企业级前端项目上的实践
  - Claude Code装上Superpowers这个插件，从码农变架构师
  - 文科新手20分钟速通Claude Code
  - 又一款开源神器！Claude Code 成本降低 90%！
  - 告别黑终端！Claude Code 最强桌面客户端来了
  - 全网疯传！字节新发布的Claude code中文使用手册！
  - 10 个顶级 Claude Code Skills，装上就删不掉！
  - Paseo：一个界面统一管理 Claude Code、Codex 和 OpenCode
  - Claude Code Skills：AI编程助手的新进化
  - 这个 GitHub 项目太缺德了，拿鞭子抽 Claude Code。
created: 2026-05-10
updated: 2026-05-10
---

# Claude Code 深度指南

## 概述

Claude Code 是 Anthropic 推出的智能体（Agent）编程工具。它不是一个更聪明的聊天机器人，而是一个运行在你机器上的智能体：读取文件、编写代码、执行终端命令、操作浏览器、部署到生产环境。你不是在"问它问题"，而是给它任务然后走开。

本指南综合 27 篇源文章，覆盖从安装配置到高级工程实践的完整能力栈。

## 一、安装与配置

### 1.1 安装方式

| 方式 | 安装方法 | 能力范围 |
|------|---------|---------|
| IDE 插件 | VS Code / Cursor 扩展面板搜索安装 | 基础功能，适合入门 |
| CLI 终端 | `npm install -g @anthropic-ai/claude-code` | 完整功能，解锁一切 |

CLI 是解锁全部能力的方式。安装后在项目文件夹中启动 `claude` 即可。

### 1.2 订阅方案

| 方案 | 价格 | 适用场景 |
|------|------|---------|
| Pro | $20/月 | 入门使用、轻度开发 |
| Max 5x | $100/月 | 日常正式开发 |
| Max 20x | $200/月 | 重度并行工作、Agent Teams |

### 1.3 关闭确认循环

默认情况下每次文件操作都会弹确认。在个人项目中建议使用：

```bash
alias cc="claude --dangerously-skip-permissions"
```

对于包含敏感数据的项目，使用沙盒模式：

```bash
claude --sandbox /path/to/safe/folder
```

### 1.4 语音输入

Claude Code 的瓶颈不是模型速度，而是指令质量。说话比打字快 5 倍，而且你会解释更完整的上下文。终端中按住空格键即可使用内置语音。

## 二、核心概念：上下文管理

### 2.1 上下文就是一块白板

Claude 有一个上下文窗口，可以想象成一块白板。每条消息、读的每个文件、执行的每条命令都写在上面。白板满了，表现就会下滑。

用好 Claude Code 的核心，就是管理好这块白板。所有技巧都围绕这个概念展开。

### 2.2 常用命令

| 命令 | 作用 |
|------|------|
| `/cost` | 查看当前会话 Token 消耗 |
| `/doctor` | 诊断安装和配置问题 |
| `/clear` | 清空会话重新开始 |
| `/memory` | 查看加载到上下文的所有内容 |
| `/compact` | 压缩上下文 |

## 三、五大核心机制

### 3.1 CLAUDE.md -- 项目记忆

CLAUDE.md 是 Claude 在每次会话开始时都会读取的文件。放在里面的内容会影响每一次协作。

**最佳实践：**
- 保持精简，每行都应该回答"没有这行 Claude 会犯错吗？"
- 当 Claude 犯错纠正后，加一句"更新你的 CLAUDE.md，确保下次不再犯"
- 随时间推移，CLAUDE.md 会变成一份活文档，让 Claude 越来越懂你的工作方式

### 3.2 Skills -- 预封装工作流

把常用操作流程封装成可复用的"技能包"，消除重复沟通成本。技能存放在 `~/.claude/skills/` 目录中，可以链式组合。

### 3.3 Hooks -- 事件驱动自动化

| 类型 | 触发时机 | 常见用途 |
|------|---------|---------|
| PreToolUse | 工具执行前 | 验证、安全检查 |
| PostToolUse | 工具执行后 | 格式化输出、反馈循环 |
| Stop | 完成回复后 | 发送桌面通知 |

### 3.4 MCP -- 连接外部服务

通过 Model Context Protocol 连接外部工具和数据源，扩展 Agent 的能力边界。

### 3.5 Subagents -- 并行分身术

可以同时开多个 Claude Code 会话处理不同任务，配合 Git Worktrees 实现多分支并行开发。

## 四、大循环机制深度解析

Claude Code 的核心是一套持续推进的 Agentic Loop，拆为四层：

1. **QueryEngine** -- 负责 turn 推进
2. **Tool System** -- 负责动作执行
3. **Permission / Hook** -- 负责拦截边界
4. **React + Ink** -- 负责终端渲染

### 4.1 流式工具执行

`StreamingToolExecutor` 让模型在流式输出时，只要吐出一个 tool_use 的 JSON block，执行器立刻启动工具。读操作并行（最多 10 个），写操作串行。模型说完话时，读操作基本已返回结果。

### 4.2 四级上下文压缩

| 级别 | 策略 | 特点 |
|------|------|------|
| L1 | Snip Compact | 裁掉旧历史，几乎无信息损失 |
| L2 | Microcompact | 清掉旧工具调用冗余 |
| L3 | Context Collapse | 折叠成摘要，可逆可审计 |
| L4 | Autocompact | 子 Agent 做完整总结，重武器 |

### 4.3 记忆系统

不是向量数据库，而是 Markdown 文件加 YAML frontmatter。每条记忆一个文件，`MEMORY.md` 做索引（限制 200 行）。

四种记忆类型：
- **User**：用户画像
- **Feedback**：纠正和确认
- **Project**：项目动态
- **Reference**：外部资源指针

用 Claude Sonnet 做轻量推理挑选最相关的 5 个记忆注入上下文，比向量检索更准确。

## 五、最佳实践

### 5.1 先规划，再动手

利用 Plan Mode（规划模式），Claude 只读文件不写代码。完整工作流：

1. 进入 Plan Mode，让 Claude 理解代码关系
2. 让 Claude 写出完整计划
3. 你审核计划
4. 切回正常模式按计划执行
5. 清晰的提交信息提交代码

### 5.2 给 Claude 提供可验证的测试用例

不要只说"写一个邮箱验证函数"，而是说"写完后用这些用例测试：hello@gmail.com 通过，hello @ 失败"。

### 5.3 提示词要具体

模糊版："给 auth.py 写测试"
具体版："给 auth.py 写测试，重点覆盖用户会话在请求中途过期的场景。不要用 mock。特别关注 token 看起来有效但实际已过期的边界情况。"

### 5.4 范式转换：从打字员到项目经理

| 错误用法 | 正确用法 |
|---------|---------|
| 写一行、问一句 | 描述完整任务让 AI 自主执行 |
| 盯着终端看 AI 打字 | 启动任务后去做别的事 |
| 让 AI 帮你写函数 | 让 AI 完成整个功能模块 |

核心转变：你的工作是**定义目标 -> 分配任务 -> 验收结果**。

## 六、企业级实践要点

### 6.1 OpenSpec + SDD 范式

通过 OpenSpec 实践规范驱动开发（SDD），在 CLAUDE.md 中配置工作流：
- `/opsx:propose` -- 提出方案
- `/opsx:apply` -- 应用变更
- `/opsx:verify` -- 验证结果
- `/opsx:sync` -- 同步规格
- `/opsx:archive` -- 归档需求

### 6.2 Git Hooks 集成

在 CLAUDE.md 中定义 Git Hooks 配置，实现：
- pre-commit：代码规范检查
- commit-msg：提交信息格式验证
- 安全审查：防止敏感信息泄露

### 6.3 成本控制

- 合理设置 max_tokens，按任务类型分档
- 使用 Prompt Caching 降低 90% 成本
- `/cost` 命令监控每次重度任务的 Token 消耗
- 使用 `--sandbox` 限制文件写入范围

## 相关页面

- [[Skills生态全景]] -- Skills 设计与使用深度指南
- [[Agent架构实践]] -- Agent 架构设计方法论
- [[MCP协议]] -- 外部服务连接协议
- [[Claude-Code]] -- Claude Code 实体页
- [[上下文工程]] -- 上下文管理核心概念
- [[CLAUDEmd配置]] -- 项目配置最佳实践
- [[Skill开发]] -- 如何创建自己的 Skill
