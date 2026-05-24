---
title: Skills装太多怎么办？用Skills Manager桌面应用统一管理
type: source-summary
tags: [Skills, Skill管理, 桌面应用, Tauri, CLI]
sources: [微信公众号/Skills/『AI提效』Skills装太多怎么办？ 用Skills Manager 桌面应用统一管理！.md]
created: 2026-05-24
updated: 2026-05-24
---

# Skills装太多怎么办？用Skills Manager桌面应用统一管理

> 📎 来源: [效能跃迁实验室](https://mp.weixin.qq.com/s?__biz=MzYzOTE4NzgxNQ==&mid=2247484443) | 时间: 2026-05-24

## 核心定位

**Skills Manager** 是一款**跨平台桌面应用**（Tauri 2 + React + Rust），口号是「一个应用，统一管理所有 AI 编码工具的 Skills」。

GitHub: https://github.com/xingkongliang/skills-manager

## 解决的痛点

| 痛点 | Skills Manager 方案 |
|------|---------------------|
| 工具多、路径乱 | Cursor/Claude Code/Codex/Windsurf 等 15+ 工具统一管理 |
| 想「我的技能库」 | 中央库 ~/.skills-manager 集中收纳 |
| 需要 Preset（预设） | 前端套件/安全审计套件一键挂上/卸下 |
| 项目级与全局分开管 | 全局工作区 + 项目工作区 + 关联工作区 |
| 需要图形化操作 | Marketplace 浏览、卡片上点 Agent 角标安装 |

## 能力一览

| 能力 | 说明 |
|------|------|
| **统一技能库** | 默认 ~/.skills-manager，集中存放已安装 skill |
| **安装来源** | Git、本地目录、压缩包、应用内 Marketplace、SkillsMP AI 搜索 |
| **Preset** | 命名技能组；在工作区点 Preset 标签批量激活/停用（一次性复制，非实时订阅） |
| **全局工作区** | 按 Agent 查看其全局目录里实际存在的全部 skill |
| **项目工作区** | 管理某项目下各 Agent 的本地 skill，与中央库双向同步 |
| **多工具同步** | 软链接或复制；skill 卡片上 per-Agent 角标显示/切换安装状态 |
| **标签与筛选** | 按来源、标签筛选；批量启用/禁用、导出、删除 |
| **Git 备份** | 对 skills/ 子目录做版本历史；支持远程 push/pull 与快照恢复 |
| **CLI** | skills-manager-cli 与桌面共用 SQLite，适合脚本与 Agent 自动化 |

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

可在设置里**添加自定义工具路径**。

## 核心概念

### Preset（预设）

可复用的 skill 分组；激活 = 把这一组复制到当前选定的 Agent 范围，**不是**云端实时联动。

### 全局工作区

管 `~/.claude/skills/`、`~/.cursor/skills/` 这类**用户级**目录。

### 项目工作区

管当前项目里的**项目级** skill 目录。

### 关联工作区

把任意目录指成 skill 根，适合非默认路径的合集。

## 安装与使用

### 普通用户

到 Releases 下载对应系统的安装包（macOS .dmg / Windows 安装程序）。

macOS 首次打开若被 Gatekeeper 拦截，可**右键 → 打开**，或执行：
```bash
xattr -cr /Applications/Skills\ Manager.app
```

### 开发者本地跑

```bash
git clone https://github.com/xingkongliang/skills-manager.git
cd skills-manager
npm install
npm run tauri:dev
```

### CLI 安装

```bash
npm run cli:install
```
将 skills-manager-cli 装到 ~/.cargo/bin；与桌面应用**共用 SQLite**。

## 上手路径

1. 从本地/Git/压缩包/Marketplace 安装若干 skills 到中央库
2. 打开**全局工作区**，选一个 Agent（如 Cursor）
3. 点 **Preset** 标签，一键挂上预设里的 skills
4. 若要管某仓库的项目级 skill，进**项目工作区**
5. 需要多机同步：在**设置**配 Git 远程，在**我的 Skills** 里**开始备份 / 同步到 Git**

## 使用边界

| 边界 | 说明 |
|------|------|
| Skill 内容安全 | 应用不审计第三方 skill 脚本；安装前请自行阅读 SKILL.md |
| Preset 非实时同步 | 改 Preset 或中央库后，已复制内容不会自动回滚 |
| CLI 与桌面并发 | 共用数据库，CLI 写入后桌面端需刷新或重启 |
| macOS 签名 | 未 Apple 公证，首启可能需处理 Gatekeeper |

## 技术栈

- **Tauri 2** — 跨平台桌面框架
- **React** — 前端 UI
- **Rust** — 后端核心（CLI 共用）
- **SQLite** — 本地数据库

## 相关实体

- [[Skills-Manager]] — 本工具
- [[Tauri]] — 跨平台桌面框架
- [[AgentSkills]] — Agent Skills 约定标准

## 相关概念

- [[中央技能库]] — ~/.skills-manager 统一存放
- [[Preset]] — 预设技能组
- [[多工具同步]] — 软链接/复制方式同步
- [[Git备份]] — skills/ 目录版本历史
- [[技能分发]] — 统一管理多 Agent 的 Skills

## 延伸阅读

- Skills Manager 仓库：https://github.com/xingkongliang/skills-manager
- 中文说明：https://github.com/xingkongliang/skills-manager/blob/main/README.zh-CN.md
- AgentSkills 约定：https://agentskills.io