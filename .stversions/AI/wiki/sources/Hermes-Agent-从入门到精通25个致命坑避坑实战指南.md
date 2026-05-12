---
tags: [Hermes, Agent, Claude, MCP, GitHub, 飞书, Prompt, API]
source: "虾看虾说"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 从入门到精通：25个致命坑避坑实战指南

> 来源: [虾看虾说](https://mp.weixin.qq.com/s?__biz=MzUxNjczOTc4MA==&mid=2247484797&idx=1&sn=e4d2bf7d8bd0226ed2cfd0f1ef720045&chksm=f8539975c2760686144e0fdae8fbc3295c159a1c03c8643a76e748a309c265451264b4390a74&mpshare=1&scene=1&srcid=0420e3uP4RcJ4gouGmXsqEEW&sharer_shareinfo=7475e7140e725d9101e0dd45dd14607f&sharer_shareinfo_first=7475e7140e725d9101e0dd45dd14607f) | 2026-04-20

## 摘要

安装失败？模型失忆？Gateway 启动就崩溃？Token 成本突然暴增？
很多人不是不会用 Hermes Agent，而是很容易在安装、配置和基础使用阶段就卡住，浪费大量 Debug 时间。
我把使用 Hermes Agent 过程中最致命的 **25 个坑**，按阶段分成 5 类，每类 5 个，全部配上触发条件和最小化复现步骤。
很多 AI 爱好者第一次装 Hermes Agent，心态是这样的：
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
跑完，内心OS：好了，装完了，跑一下吧。
然后：
hermes run "你好"
报错。
再试：
hermes gateway start
又报错。
然后就开始漫无目的地搜 Google、刷 GitHub Issues、贴错误日志问社区。一上午过去了，问题还在。
这不是个案。这几乎是每个新手的必经之路。
脚本跑完了，不代表装对了。以下是安装阶段最常见的 5 个坑。
坑1命令装上了，但 P...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Docker]], [[GPT4]], [[GitHub]], [[Hermes]], [[MCP]], [[Nodejs]], [[OpenAI]], [[OpenClaw]], [[Python]], [[飞书]]

## 相关概念

[[MultiAgent]], [[思维链]]
