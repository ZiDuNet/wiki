---
tags: [Agent, Skill, Dokobot, 网页抓取, 浏览器自动化]
source: "晓来在进化"
created: 2026-05-13
updated: 2026-05-13
category: Agent
---

# 力荐！这个Skill，让你的Agent有了一双真正的眼睛，抓取网页再也不是难事了

> 来源: [晓来在进化](https://mp.weixin.qq.com/s?__biz=MzkyMjMzMzc1Mg==&mid=2247486137&idx=1&sn=dcf93eded476bd8dd1376471dee22351&chksm=c092406fb8023e8de4ae4b7790cac2483b428a0bb3fa09e1fb35c28909f6f3f085a75149e0ac) | 2026-05-13

## 摘要

本文介绍了Dokobot，一个让AI Agent使用真实浏览器读取网页的浏览工具。不同于传统的HTTP请求或爬虫方式，Dokobot直接使用本地浏览器读取渲染后的网页，分析像素，输出对LLM大模型友好的结构化文本。

Dokobot的核心优势在于：支持本地和远程使用，本地使用完全免费、不需要注册、不需要密钥；复用浏览器登录状态，能读取登录墙、JS渲染的网页、内网站点及有反爬机制的网站；支持Claude Code、Codex、OpenCode、OpenClaw、Hermes Agent等主流Agent。安装配置简单：通过Chrome插件安装，配置Node.js环境后安装CLI工具，最后使用`dokobot install-skill`命令为对应Agent配置Skill即可。