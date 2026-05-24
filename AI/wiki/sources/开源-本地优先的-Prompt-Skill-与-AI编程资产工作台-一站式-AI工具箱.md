---
title: "PromptHub：本地优先的 Prompt、Skill 与 AI 编程资产工作台"
type: source-summary
tags: [Prompt管理, Skill管理, Agent管理, 本地优先, 工具箱]
sources: [[开源]本地优先的 Prompt、Skill 与 AI 编程资产工作台，一站式 AI 工具箱.md]
created: 2026-05-25
updated: 2026-05-25
---

# PromptHub：本地优先的 Prompt、Skill 与 AI 编程资产工作台

## 摘要

PromptHub 是一款本地优先的 AI 编程资产管理工具，支持 Prompt 管理、Skill 一键分发到 15+ 平台（Claude Code、Cursor、Codex、Windsurf 等）、项目级 Agent 工作区以及 WebDAV/自部署同步。所有数据默认存在用户本地电脑，采用 AES-256-GCM 加密保护隐私。

## 核心能力

### Prompt 管理
- 文件夹、标签、收藏三层组织，支持拖拽排序
- 模板变量 {{variable}}，复制/测试/分发时弹表单填值
- 全文搜索（FTS5）、Markdown 渲染与代码高亮

### Skill 商店与一键分发
- 内置 20+ 精选技能（Anthropic、OpenAI 等）
- 一键安装到 15+ 平台：Claude Code、Cursor、Windsurf、Codex、Kiro、Gemini CLI、Qoder、CodeBuddy、Trae、OpenCode、Roo Code 等
- 本地扫描自动发现已有 SKILL.md，AI 翻译与润色功能
- Symlink / Copy 双模式，支持平台目标目录覆写

### Rules 与项目工作区
- 集中管理 .cursor/rules、.claude/CLAUDE.md、AGENTS.md 等规则文件
- 扫描项目里的 .claude/skills、.agents/skills 等常见目录
- 全局 Prompt 标签管理

### AI 测试与版本控制
- 内置 AI 测试，支持 OpenAI、Anthropic、Gemini、Azure 等多服务商
- 同一 Prompt 多模型并行对比
- 每次保存自动写入历史版本，支持版本对比与一键回滚
- 商店 Skill 安装时记录内容哈希，检测远端变更

### 数据同步
- 本地优先 + WebDAV 同步（坚果云、Nextcloud 等）
- 自部署 PromptHub Web 同步源 / 备份源
- .phub.gz 压缩格式全量备份/恢复

## 技术信息

- **开源协议：** AGPL-3.0
- **技术栈：** Electron · React · TailwindCSS · Zustand · Lucide
- **运行要求：** Node.js >= 24、pnpm 9
- **仓库：** https://github.com/legeling/PromptHub
- **界面语言：** 7 种（简体中文、繁體中文、English 等）

## 关键概念

- [[本地优先]]
- [[Skill管理]]
- [[Prompt工程]]
- [[版本控制]]
- [[WebDAV]]
- [[AI测试]]

## 实体提及

- [[Claude]]（Code）
- [[Cursor]]
- [[Codex]]
- [[Windsurf]]
- [[Gemini CLI]]

## 注意局限

- Electron 桌面应用，Web 需显式 pnpm build:web 构建
- 主密码保护为 Beta 功能，私密文件夹加密存储为 Beta
