---
tags: [浏览器自动化, Agent, Claude, MCP, GitHub, Python, Skill]
source: "比特片场"
created: 2026-04-15
updated: 2026-05-10
category: 浏览器自动化
---

# 创建持久会话/persistent-terminal create my-browser-server# 在会话中启动服务器/persistent-terminal exec my-browser-server "python3 src/browser-chrome-agent/scripts/server.py --port 9009"

> 来源: [比特片场](https://mp.weixin.qq.com/s?__biz=MzAwMTIwNzE1Mw==&mid=2247485702&idx=1&sn=f128f7506abb12897be7fd28908ffa88&chksm=9b3b73ef923805ca4a52e62ed99e6a41d4859b63f5bca7485715a3971a5166ffc076eceb40c4&mpshare=1&scene=1&srcid=0415jPf8FCZytLB8aokNOvct&sharer_shareinfo=64707912352ffe0733d9eb4be6fd01b3&sharer_shareinfo_first=64707912352ffe0733d9eb4be6fd01b3) | 2026-04-15

## 摘要

本期分享内容：**【浏览器自动化技能】**【原创】
上一期聊了持久化终端技能，解决了 Claude Code 终端会话不持久的问题。这期要聊的浏览器自动化工具，正是基于此持久化终端才能跑起来的——因为 WebSocket 服务器需要一直运行。
想让 AI 帮你操作浏览器？现在有几个选择，但都不太理想：
**Claude Code 官方的浏览器功能**
- 需要订阅才能用（付费门槛）
- 使用很麻烦：必须先建立专门的标签页组
- 限制多：只能操作特定标签页组内的页面，不能随意切换
**传统自动化工具（Selenium/Playwright）**
- 需要启动一个独立的浏览器实例
- 无法操控你正在使用的浏览器
- 需要重新登录账号、配置环境
- 调试不方便，看不到实时操作过程
我想要的很简单：**免费、简单、能直接操控我正在用的 Chrome**。
后来发现了 Browser MCP 这个项目，它通过 Chrome 插件 + WebSocket 的方式实现了这个想法：
- ✅ 完全免费开源
- ✅ 直接操控当前浏览器
- ✅ 不需要标签页组限制
- ✅ 保持登录状态，不需要重新配置
但它...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]], [[MCP]], [[Markdown]], [[Node.js]], [[Python]]

## 相关概念

[[浏览器自动化]]
