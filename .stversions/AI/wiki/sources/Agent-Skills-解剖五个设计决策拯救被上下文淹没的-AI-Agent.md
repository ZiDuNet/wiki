---
tags: [Skills, Agent, Claude, MCP, GitHub, Prompt, API, Python]
source: "老郑的AI工具箱"
created: 2026-04-29
updated: 2026-05-10
category: Skills
---

# Agent Skills 解剖：五个设计决策拯救被上下文淹没的 AI Agent

> 来源: [老郑的AI工具箱](https://mp.weixin.qq.com/s?__biz=MzkxNjYyMzIwNQ==&mid=2247484414&idx=1&sn=615907d2caf070b652a63d7d812b8ccd&chksm=c03147c0e19c760f34c5ae934744d18351f06a623dccefc735ddb88ff580dc5fc01e84d0c8ae&mpshare=1&scene=1&srcid=0429mnOTMSsRdRblGwpOfzTu&sharer_shareinfo=062895b16c37f1129a563be2fb0415e8&sharer_shareinfo_first=062895b16c37f1129a563be2fb0415e8) | 2026-04-29

## 摘要

Skill 不是 Python 类，也不是注册的工具。它是磁盘上的一个文件夹，里面放一个 Markdown 文件。
**SKILL.md** 是唯一必需的文件。references 存放 Agent 按需读取的文档。assets 存放模板和品牌文件。scripts 存放 Agent 可以执行的代码。除了 SKILL.md，一切都是可选的。
因为 Skill 就是文件，你可以用 Git 做版本控制。用 Pull Request 做 diff。在项目间复制。发布到 GitHub。**格式即合约**。
同一个 SKILL.md 在 Claude Code、Codex、Gemini CLI、Cursor、Agent Development Kit、LangChain 以及越来越多 Agent 工具和框架中都能用。**一个文件夹，多个运行时**。
打开任何一个 SKILL.md，你首先看到的是 YAML frontmatter 里的两个字段。这两个字段不只是元数据——**它们是搜索索引**。
会话开始时，Agent 加载每个已安装 Skill 的 name 和 description。大约每个 ...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub]], [[LangChain]], [[MCP]], [[Markdown]], [[Python]]

## 相关概念

[[MultiAgent]]
