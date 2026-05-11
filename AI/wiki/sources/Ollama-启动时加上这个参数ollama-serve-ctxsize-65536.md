---
tags: [Hermes, Agent, Claude, MCP, GitHub, API, Python, OpenAI]
source: "楮墨的AGI世界"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Ollama 启动时加上这个参数ollama serve --ctx-size 65536

> 来源: [楮墨的AGI世界](https://mp.weixin.qq.com/s?__biz=MzY4MzEzODI2MQ==&mid=2247483973&idx=1&sn=d7a7a15c3843197c734672241586ffb8&chksm=f2d8e1bf55545154a805130b24142418eb7a42f390f2892d56463e135b933df559f1fb390948&mpshare=1&scene=1&srcid=0420k7ikJHWqdO0YM4KssMJc&sharer_shareinfo=e8851edd23ad0b347bdfc593ca0688d1&sharer_shareinfo_first=e8851edd23ad0b347bdfc593ca0688d1) | 2026-04-20

## 摘要

昨天写了一篇关于Open Claw与Hermes Agent对比的文章，好多朋友看完后，私下跟我说，Hermes Agent大概看懂了是个什么东西，但如何安装和使用呢，我突然意识到，最近GitHub上非常火爆的开源Agent原来还有好多人不知道，那我们今天就来讲讲它的安装和使用。
如果你也是刚听说这个工具，或者试过但装不上，这篇指南就是为你写的。我们从零开始，手把手，保证你能跑起来。
在说安装之前，先简单介绍一下这是个什么东西，方便你判断"这玩意儿值不值得装"。
Hermes Agent 是由 **Nous Research**（就是那个做羊驼系列模型的研究机构）开源的一个 AI Agent 命令行工具。简单来说，它就是一个跑在终端里的 AI 助手，但你可以通过它真正操控你的电脑——搜索网页、读写文件、执行命令行操作、接入 Telegram 或 Discord 聊天、设置定时任务。
**它能做的事**（举几个例子）：
- "帮我查一下今天 Hacker News 上 AI 相关的新闻，整理成摘要"
- "把我桌面上的所有 PDF 文件按时间排序"
- "帮我写一个部署脚本，然后执行它"...

## 相关实体

[[Anthropic]], [[Claude]], [[DeepSeek]], [[Docker]], [[GPT-4]], [[Gemini]], [[GitHub]], [[Hermes]], [[Llama]], [[MCP]], [[Node.js]], [[OpenAI]], [[OpenRouter]], [[Python]], [[Qwen]]

## 相关概念

[[AI-Agent]], [[MCP协议]], [[代码审查]], [[浏览器自动化]], [[记忆系统]]
