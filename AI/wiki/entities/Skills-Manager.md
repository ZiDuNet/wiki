---
type: entity
name: Skills-Manager
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# Skills-Manager

**类型:** 实体（工具/软件）
**提及文章数:** 1

## 简介

Skills-Manager 是一款**跨平台桌面应用**（Tauri 2 + React + Rust），用于统一管理所有 AI 编码工具的 Skills。口号：「一个应用，统一管理所有 AI 编码工具的 Skills」。

## 核心定位

把分散在各 Agent 目录里的 Skills，收进一个中央技能库，再用图形界面安装、分组、同步到 Cursor / Claude Code / Copilot 等 15+ 工具。

## 技术栈

- **Tauri 2** — 跨平台桌面框架
- **React** — 前端 UI
- **Rust** — 后端核心（CLI 共用）
- **SQLite** — 本地数据库

## 支持工具（15+）

- Cursor
- Claude Code
- Codex
- OpenCode
- Amp
- Kilo Code
- Roo Code
- Goose
- Gemini CLI
- GitHub Copilot
- Windsurf
- TRAE IDE
- Antigravity
- Clawdbot
- Droid

## 核心能力

| 能力 | 说明 |
|------|------|
| 统一技能库 | 默认 ~/.skills-manager，集中存放已安装 skill |
| 安装来源 | Git、本地目录、压缩包、应用内 Marketplace、SkillsMP AI 搜索 |
| Preset | 命名技能组；在工作区批量激活/停用 |
| 全局工作区 | 按 Agent 查看其全局目录里的全部 skill |
| 项目工作区 | 管理项目级 skill，与中央库双向同步 |
| 多工具同步 | 软链接或复制；per-Agent 角标显示安装状态 |
| Git 备份 | 对 skills/ 子目录做版本历史；支持远程 push/pull |

## CLI

`skills-manager-cli` 与桌面共用 Rust 核心，适合脚本与 Agent 自动化。

```bash
npm run cli:install
```

## 项目地址

- GitHub: https://github.com/xingkongliang/skills-manager
- 中文 README: https://github.com/xingkongliang/skills-manager/blob/main/README.zh-CN.md

## 相关概念

- [[中央技能库]] — ~/.skills-manager 统一存放
- [[Preset]] — 预设技能组
- [[多工具同步]] — 软链接/复制方式同步
- [[Git备份]] — skills/ 目录版本历史
- [[技能分发]] — 统一管理多 Agent 的 Skills

## 相关文章

- [[Skills装太多怎么办-用Skills-Manager桌面应用统一管理]]