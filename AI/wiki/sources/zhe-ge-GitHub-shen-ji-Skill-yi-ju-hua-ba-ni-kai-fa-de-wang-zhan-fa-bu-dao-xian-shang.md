---
title: "这个 GitHub 神级 Skill，一句话把你开发的网站发布到线上"
type: source-summary
tags: [PinMe, GitHub, Skill, 部署, Claude-Code, AI-Agent, 全栈]
sources: ["微信公众号/GitHub/这个 GitHub 神级 Skill，一句话把你开发的网站发布到线上。.md"]
created: 2026-05-21
updated: 2026-05-21
---

# PinMe 2.0：一句话让 AI 帮你把网站发布上线

## 核心概念

**PinMe** 是一个开源项目，能把做好的静态网页、一张图片、或任何本地文件快速变成公网链接。目前累计部署超过 100 万个网站。

2.0 版本升级：推出了 PinMe Skill，支持一行命令帮你搭好完整 Web 应用（前端 + 后端 + 数据库 + AI Agent 部署适配）。

## 核心能力进化

### 1.0 → 2.0 进化

| 能力 | 1.0 | 2.0 |
|------|-----|-----|
| 静态部署 | ✅ 30 秒转公网链接 | ✅ 继续支持 |
| 全栈部署 | ❌ | ✅ 前端 + 后端 + 数据库 |
| AI Agent 集成 | ❌ | ✅ 内置 Skill |
| 部署量 | - | 100 万+ 网站 |

## 三种使用场景

### 场景一：纯静态页面部署

```bash
npm install -g pinme
```
30 秒内网页/图片转公网链接。

### 场景二：全栈项目部署

同样一行命令，前端 + 后端 + 数据库一键上线。

支持应用：
- 带数据库的记账本
- 报名表收集应用
- ToDo 工具
- 共享像素画板（多人实时协作）

### 场景三：Claude Code 里用

```bash
npx skills add glitternetwork/pinme
```
安装后直接用自然语言描述需求，Claude Code 写完代码自动帮你部署更新。

## 技术架构

- **静态资源**：IPFS 分布式存储
- **全栈项目**：前后端分离架构，前端现代 SPA，后端 Edge Runtime
- **数据库**：Serverless SQL
- **内置能力**：邮件推送 + LLM 调用（Worker 中直接调用）

## 工作流

```
你描述需求 → AI 写代码 → PinMe 自动部署 → 链接给你
```

全程不需要配置服务器、域名、数据库等基础设施。

## 开源地址

https://github.com/glitternetwork/pinme

## 关联

- [[Claude-Code-best-practices]] — Claude Code 最佳实践
- [[claude-code-skills-tui-jian]] — Claude Code Skills 推荐
