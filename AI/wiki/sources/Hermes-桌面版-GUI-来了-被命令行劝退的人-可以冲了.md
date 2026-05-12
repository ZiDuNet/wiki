---
title: "Hermes 桌面版 GUI 来了：被命令行劝退的人，可以冲了"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: ["Hermes 桌面版 GUI 来了：被命令行劝退的人，可以冲了.md"]
tags: [Hermes, GUI, 桌面应用, Nous-Research]
---

## Summary

Hermes Desktop是由fathah开发的社区项目，为Hermes Agent提供图形界面，大幅降低使用门槛。核心功能：模型切换（一个下拉框）、聊天界面（SSE流式输出+Token计数器）、22个斜杠命令、消息网关配置（Telegram/Discord/飞书等）、会话管理（SQLite FTS5全文搜索）、技能管理。支持本地和远程两种模式，Windows/macOS/Linux全平台覆盖。

## Key Claims

1. **GUI大幅降低门槛**: 命令行里切模型要改配置重启，GUI里是一个下拉框，点一下就切完。
2. **Token计数器是有价值的功能**: 实时显示token用量，让人自然控制对话长度，避免账单 surprise。
3. **22个斜杠命令保留**: /new, /clear, /web, /image, /browse, /code, /shell, /usage等，GUI化后使用频率明显提高。
4. **SQLite FTS5全文搜索**: 可以搜历史对话，长期使用AI的人这个功能比炫技功能更重要。
5. **消息网关GUI化**: Telegram/Discord/飞书/钉钉等，以前要改配置文件+排查网络，现在填bot token保存测试即可。
6. **本地+远程双模式**: 个人用选本地（数据留本机）；也可以连服务器上的Hermes API。
7. **MIT协议开源免费**，项目还在开发中。

## Entities Mentioned

- [[Hermes Desktop]]（fathah开发，GitHub桌面应用）
- [[Hermes Agent]]（Nous Research开源AI助手，底座）
- [[fathah]]（开发者）
- [[Nous Research]]（Hermes模型系列开发方）

## Concepts

- [[GUI桌面应用]]
- [[消息网关]]
- [[技能管理]]
- [[Token优化]]

## Notable Quotes

- "路径越短，越容易触发。"
- "对于真正长期使用 AI Agent 的人来说，这比多一个炫技功能更重要。"
- "这也是开源社区有意思的地方：有人做底层能力，有人做上层体验，各取所需，然后把门槛一点点降下来。"

## Limitations / Bias

- 项目还在开发中，功能和界面可能继续变化
- 文章对技术细节覆盖较浅
