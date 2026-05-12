---
tags: [Skills, Agent, Claude, GitHub, Prompt, API, Skill, OpenClaw]
source: "零壹界点"
created: 2026-04-24
updated: 2026-05-10
category: Skills
---

# AI Skill 碎片化的解法来了：一个中央库统一管理 27 个平台

> 来源: [零壹界点](https://mp.weixin.qq.com/s?__biz=MzIxMzk1MzQ0Ng==&mid=2247483789&idx=1&sn=07df8e95841cf8087b98e90da5efb7b2&chksm=969718384b6d718c1992160a1d7cc58f48eba483a6383806dfd4355798b6109be863855b14ae&mpshare=1&scene=1&srcid=0424twXpqNODJQdpRYcRIdJc&sharer_shareinfo=00aa8e0558cddf6f20062601e17f951d&sharer_shareinfo_first=00aa8e0558cddf6f20062601e17f951d) | 2026-04-24

## 摘要

你花了一下午写了一个好用的 Skill——某个处理代码审查的提示模板，或者一套调试 SQL 的操作流程。然后你发现，它只在 Claude Code 里有。打开 Cursor，没有。切到 Windsurf，没有。换 Copilot，还是没有。你开始手动复制，改路径，粘贴，保存。第二天你优化了这个 Skill，又来一遍。
这不是极端情况，这是今天同时使用多个 AI 工具的用户每天都在面对的现实。
`skills-manage` 是经过独立开发者志辉打磨两周后于 2026 年 4 月 20 日开源的一个 Tauri 桌面应用，核心思路只有一句话：**以 `~/.agents/skills/` 为单一事实来源，通过软链接把技能分发到所有平台**。你在中央库里写一次，它帮你装到你指定的每一个工具里；你改一次，所有平台同步更新；你卸载某个平台，只删软链接，中央库丝毫不动。
目前它支持的平台有 27 个，从 Claude Code、Cursor、Windsurf、Copilot、Gemini CLI，到 OpenClaw、Hermes、OpenCode、Augment，乃至 Kiro、OB1、Amp...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub]], [[Hermes]], [[Markdown]], [[Nodejs]], [[OpenClaw]], [[React]], [[SQLite]], [[Windsurf]], [[WorkBuddy]]

## 相关概念

[[代码审查]]
