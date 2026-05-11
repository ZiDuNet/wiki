---
tags: [Hermes, Agent, Claude, MCP, GitHub, PPT, API, Python]
source: "climbing.top"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# 仅使用 web 和 terminal 工具

> 来源: [climbing.top](https://mp.weixin.qq.com/s?__biz=MzA5MTk1OTUxMQ==&mid=2649277478&idx=1&sn=8fb85014e2ef76aa0acf502207e976ce&chksm=8963ce386d0336c89eec73273e354f9ac96d26bd508368aef16100e1d47d177431381136fb62&mpshare=1&scene=1&srcid=0420CGtEmEUaHWz0YtjGA4Pq&sharer_shareinfo=9e494f87432b18910842db246364e6a2&sharer_shareinfo_first=9e494f87432b18910842db246364e6a2) | 2026-04-20

## 摘要

• [工具系统概述](#工具系统概述)
• [内置工具分类](#内置工具分类)
• [工具集（Toolsets）](#工具集toolsets)
• [终端后端详解](#终端后端详解)
• [后台进程管理](#后台进程管理)
• [Sudo 支持](#sudo-支持)
• [小结](#小结)
Hermes Agent 拥有 40+ 个内置工具，按逻辑分组为"工具集（Toolsets）"，可以按平台启用或禁用。
工具是 Agent 与外界交互的桥梁——搜索网页、执行命令、操作文件、控制浏览器、管理定时任务等。
| 类别 | 示例工具 | 说明 |
|------|---------|------|
| 🌐 **网络** | `web_search`, `web_extract` | 搜索网页和提取页面内容 |
| 💻 **终端 & 文件** | `terminal`, `process`, `read_file`, `patch` | 执行命令和操作文件 |
| 🌍 **浏览器** | `browser_navigate`, `browser_snapshot`, `browser_vis...

## 相关实体

[[Claude-Code]], [[Claude]], [[Docker]], [[Hermes]], [[MCP]], [[Python]]

## 相关概念

[[CICD]], [[多模态]], [[浏览器自动化]]
