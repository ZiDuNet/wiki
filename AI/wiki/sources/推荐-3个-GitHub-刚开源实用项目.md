---
tags: [GitHub, 开源, 工具推荐, Markdown, Agent]
sources: [推荐 3 个 GitHub 上刚开源但实用的项目，收藏一波。.md]
created: 2026-05-31
updated: 2026-05-31
type: source
---

# 推荐 3 个 GitHub 上刚开源但实用的项目，收藏一波

**来源：** 微信公众号/逛逛GitHub
**摄入日期：** 2026-05-31
**类型：** 文章

## 摘要

推荐 3 个近期开源的实用项目：极简 Markdown 笔记工具 files.md（Obsidian 替代品）、AI Agent 生产级生存指南 agents-best-practices、跨平台桌面应用原生感设计指南 native-feel-skill。

## 三个项目

### 1. files.md — 极简 Markdown 笔记工具

**定位：** Obsidian 开源替代品，定位"不被功能绑架的真正笔记空间"

**核心特点：**
- 零安装零依赖，浏览器打开 app.files.md 就能用
- 数据完全属于你，笔记就是本地 .md 文件
- 支持 iCloud/Dropbox/Google Drive 同步
- **LLM 友好**：自带 llms.txt，AI Agent 能直接理解和操作笔记库
- 支持 Telegram 机器人快速记录、知识图谱关联、聊天式快速输入
- 代码量极小，一个人就能看懂整个项目

**作者：** Artem Zakirullin，5 年打磨，2000+ GitHub Stars

**开源地址：** https://github.com/zakirullin/files.md

### 2. agents-best-practices — AI Agent 生产级生存指南

**定位：** Agent Skill，开发生产级 Agent 的完整知识体系

**核心观点：** 模型负责提议行动，Harness 负责验证、授权、执行和记录。模型不是操作者，它只是建议者。

**三大使用场景：**
- 生成 MVP Agent 蓝图：给定业务场景，输出最小可用的生产级安全 Agent 架构
- 审计现有 Agent：诊断脆弱性、成本过高、调试困难等问题，给出修复优先级
- 设计工具、权限和连接器：安全接入 Slack/Linear/Google Drive/内部 API

**特点：** 14 篇参考文档覆盖 Agent 开发方方面面，8 条运行时哲学规则来自实战

**开源地址：** https://github.com/DenisSergeevitch/agents-best-practices

### 3. native-feel-skill — 跨平台桌面应用原生感设计指南

**定位：** Agent Skill，教你怎么让跨平台桌面应用在 macOS/Windows 上运行得像原生应用

**背景：** Raycast 底层是 WebView + Node.js，但用起来丝滑得像原生。有人直接反编译了 Raycast Beta.app，把答案扒了出来。

**作者：** yetone（avante.nvim 插件作者），发布不到两天 1000+ Stars

**可用场景：**
- 重构现有应用，使其更具原生感
- 从零开始开发跨平台原生体验应用

**开源地址：** https://github.com/yetone/native-feel-skill

## 涉及实体

- [[files.md]] — 极简 Markdown 笔记工具
- [[agents-best-practices]] — AI Agent 生产级指南
- [[native-feel-skill]] — 跨平台原生感设计 Skill
- [[Raycast]] — 被逆向工程的桌面应用

## 涉及概念

- [[LLM友好笔记]] — llms.txt 让 AI 能直接操作笔记库
- [[Agent架构]] — 模型提议 vs Harness 执行分离
- [[跨平台桌面应用]] — WebView 实现原生体验