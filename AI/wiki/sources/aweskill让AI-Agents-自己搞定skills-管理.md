---
tags: [Skills, Agent, Claude, GitHub, API, Skill, OpenClaw]
source: "北野茶缸子"
created: 2026-05-09
updated: 2026-05-10
category: Skills
---

# aweskill：让AI Agents 自己搞定skills 管理

> 来源: [北野茶缸子](https://mp.weixin.qq.com/s?__biz=MzU5ODc3OTA0NQ==&mid=2247492594&idx=1&sn=d89d374d1ba18f68ce04ee33b54bc452&chksm=fff5ab99f1ec3c152cb75b1c7da695d710f97eb8631c94e328f89a56800791234e55008a59d0&mpshare=1&scene=1&srcid=0509D6I49ZQenGmPGCDxjudj&sharer_shareinfo=8bbf767c432ff79c9fa950e8eb7797cd&sharer_shareinfo_first=8bbf767c432ff79c9fa950e8eb7797cd) | 2026-05-09

## 摘要

你同时用好几个 AI 编码工具。Claude Code 做深度重构，Cursor 做快速编辑，Codex 跑自主任务，Gemini CLI 做多模态工作，可能还有 Windsurf 或 Qwen Code。
每个工具有自己的 skill 目录，
放的位置各不相同。每发现一个好用的 skill，你就复制一次。然后再复制一次。再复制一次。
一个月后：一份过期了，一份坏了，一份有谁也记不清的本地改动，没人知道到底哪份才是最新的。
这就是
要解决的问题。
官网：aweskill.webioinfo.top[1]
给一个 agent 装个 skill 很简单，大多数工具都能做到。
难的是之后：
- **哪份是真的？** 同一个
skill 存在于
、
、
。你改哪个？
- **怎么更新？** 上游作者修了个 bug，你得找到每一份副本，逐个替换。
- **怎么组织？** 你有 15 个 skill，有些是后端的，有些是前端的，有些只想在 Codex 里用，有些要全局启用。
- **怎么恢复？** 一个 symlink 断了，一个 agent 更新把你的 skill 目录清空了。怎么办？
- **...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub-Copilot]], [[GitHub]], [[OpenClaw]], [[Qwen]], [[Windsurf]]

- [[Tauri]]
## 相关概念

[[AI-Agent]], [[Multi-Agent]], [[代码审查]], [[多模态]]
