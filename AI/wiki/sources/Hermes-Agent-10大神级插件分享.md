---
title: Hermes Agent 2026年5月必装的10大神级插件
type: source-summary
tags: [Hermes, Plugin, 浏览器自动化, 飞书, GitHub]
sources: [../微信公众号/Hermes/「爱马仕」Hermes Agent：2026 年 5 月必装的 10 大神级插件分享.md]
created: 2026-05-16
updated: 2026-05-16
---

# Hermes Agent 10大神级插件

## 核心摘要

Hermes Agent v0.13.0 "Tenacity" 版本发布，GitHub Star 突破 102k。本文从 80+ 个插件中精选 10 个最实用神器，覆盖浏览器自动化、办公集成、开发工具、监控调试、多媒体等多个场景。

## Top 10 插件详解

### 1. Browser-Use ⭐9.9/10
让 Hermes 真正拥有"手"和"眼睛"，像真人一样操作浏览器。
- 自动管理邮箱、电商比价下单、自动填表、爬取动态加载网站
- 安装：`hermes skills install official/browser-use`

### 2. 飞书 MCP ⭐9.8/10
国内职场人第一优先级。通过 MCP 协议深度集成飞书所有功能。
- 自动写飞书文档/表格/演示、管理日历、处理任务、批量导出 MD
- 安装：`hermes plugins enable feishu` + 配置 app_id/app_secret

### 3. GitHub MCP ⭐9.7/10
开发者必备，睡觉时替你管 GitHub。
- 自动审查 PR（指出代码问题）、管理 Issue、自动合并符合条件 PR、生成 Release Notes

### 4. Langfuse ⭐9.6/10
重度用户必备，解决"Agent 后台在干嘛我全靠猜"问题。
- 实时监控 Token 消耗、追踪工具调用记录、分析 Agent 性能和成功率

### 5. ComfyUI ⭐9.5/10
v0.12.0 已从可选技能升级为内置默认技能。
- 自然语言生成图像、管理 ComfyUI 模型和节点、批量生成+后处理

### 6. RTK-Hermes ⭐9.4/10
省钱神器，官方测试最高节省 99% Token 消耗，最低也能省 90%。
- 自动过滤无用日志、长文本压缩为结构化短信息、智能缓存重复请求

### 7. Google Workspace ⭐9.3/10
Google 全家桶用户必备，覆盖 Gmail/Calendar/Drive/Sheets/Docs

### 8. Obsidian/SiYuan ⭐9.2/10
用 Hermes+笔记打造第二大脑。
- 自动创建/编辑笔记、总结长文档、智能关联笔记、生成思维导图

### 9. Spotify ⭐9.1/10
v0.12.0 新增内置插件，Hermes 成为专属 DJ。
- 自然语言控制播放、根据心情推荐音乐、创建管理播放列表

### 10. Multi-Agent Kanban ⭐9.0/10
v0.13.0 最重磅更新，持久化多代理协作看板系统。
- 多个工作代理像真实团队协作、任务回收机制（某代理挂了任务自动被接手）、幻觉门控

## 安装使用建议

1. 先安装基础插件（Langfuse、RTK-Hermes），再装功能插件
2. 按需安装，不要装太多影响性能
3. 定期更新插件保持兼容
4. 定期备份 `~/.hermes` 目录

## 相关实体

- [[Hermes-Agent]] — 插件生态所依附的 Agent 框架
- [[MCP协议]] — 飞书/ GitHub MCP 插件的技术基础
