---
title: 分享4个新发现的宝藏Skills
type: source-summary
tags: [Skills, AI-Agent, 评测框架, Skill管理, 设计工具, Claude-Code]
sources: ["微信公众号/Skills/分享4个新发现的宝藏Skills.md"]
created: 2026-05-15
updated: 2026-05-15
---

> 📎 来源: [开启新人生](https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjAyOQ==&mid=2247483924&idx=1&sn=0d7ad3a74262f0588a33723c9fa9a9b9) | 时间: 2026-05-15

## 核心摘要

作者推荐了 4 个实测有价值的 AI Agent Skills，涵盖测试评估、官方技能库、设计工作流和跨平台 Skill 管理工具。

## 四个 Skills

### 1. agent-skills-eval

**定位**：Agent Skills 的测试运行器/评估框架

- 针对 `SKILL.md` 编写评估用例
- 对比实验（带技能 vs 不带技能）用评审模型打分
- 输出 JSON 报告 + HTML 可视化
- 支持 CLI 一键运行和 SDK 集成 CI 流水线

**适用场景**：AI Agent 开发者验证自定义技能效果、集成到开发管道进行自动化评估

### 2. anthropics/skills

**定位**：官方示例 Skills 集合

- 包含文档处理（PDF、XLSX）、代码审查、TDD、架构设计、GitHub Issues 管理等
- 可动态加载到 Claude 等代理
- 适合软件工程工作流

**相关**：常与 `skill-creator` 工具结合使用

### 3. Owl-Listener/designer-skills

**定位**：设计全流程 Skill 集合

- 87 个 Skills + 27 个命令 + 8 个插件
- 覆盖：用户研究、设计系统、UI设计、交互、项目交付、handoff 到开发
- 支持生成设计 rationale、case studies、dev handoff 包

**适用场景**：indie 开发者、全栈/产品构建中 AI 辅助设计

### 4. skills-manage

**定位**：跨平台 AI 编码代理技能可视化管理工具

- 支持 Claude Code、Cursor、Gemini CLI、Codex 等 20+ 平台
- 基于 `~/.agents/skills` 目录集中管理
- 功能：软链接同步、版本控制、权限管理、使用统计、批量安装/更新

**适用场景**：一人公司或开发团队管理大量 Skill.md 文件

## 相关概念

- [[Skill-评估框架]] — 量化验证 Skill 效果的方法论
- [[Skill-管理工具]] — 跨平台 Skill 集中管理方案
- [[anthropics-skills]] — 官方 Skill 示例库
