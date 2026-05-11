---
tags: [OpenClaw, Agent, Claude, GitHub, API, OpenAI]
source: "云起泊言"
created: 2026-04-27
updated: 2026-05-10
category: OpenClaw
---

# 给你的 Hermes & OpenClaw 安装这个工具，能让 Token 消耗立省60%

> 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868887&idx=1&sn=e7186e3b129602043b723a3096674d30&chksm=8630dc17f8aa8261d1e62221932e542dc137de502b57322e0cd389ea9774202093f4c9474cff&mpshare=1&scene=1&srcid=0427hVjbXyUCqHEiisoDozhv&sharer_shareinfo=ce25204eff1846276bebe8b64f493b28&sharer_shareinfo_first=ce25204eff1846276bebe8b64f493b28) | 2026-04-27

## 摘要

如果你正在使用 **OpenClaw**、**Hermes Agent** 或者 **Claude Code** 等Agent工具，是不是经常在用的很爽的时候，又在一直担心 Token 的消耗？
每次一条命令的输出动不动就几万 Token，你让它查个 `git status` 它能给你唠出一篇小作文。本来上下文窗口就宝贵，这些冗余信息一塞，模型推理能力变差不说，你的 API 费用也跟着蹭蹭往上涨。
今天给大家推荐一款工具——**RTK (Rust Token Killer)**：Rust 开发的一款**零依赖 CLI 代理**，能智能过滤/压缩 `ls`、`git status`、`cargo test` 等终端输出，直接减少 60-90% Token。
**这到底是个啥玩意？**
它可以理解成在 Hermes 和你的命令行之间加了一层 **"过滤器"**——过滤掉注释、空行、重复日志、模板代码这些噪音，只把真正有用的核心信息喂给大模型。
举个例子你就明白了。你让 Hermes 执行 `npm test`，假设跑了 100 个测试只挂了 2 个，原始输出可能有 25000 Token，...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[DeepSeek]], [[GPT-5]], [[Gemini]], [[GitHub-Copilot]], [[GitHub]], [[Hermes]], [[OpenClaw]], [[VS-Code]], [[Windsurf]]

## 相关概念

[[Function-Calling]]
