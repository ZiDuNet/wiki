---
tags: [Vibe Coding, Agent, Claude, MCP, GitHub, Prompt, API, Skill]
source: "蒜是哪根葱"
created: 2026-04-29
updated: 2026-05-10
category: Vibe Coding
---

# Claude Code（推荐）

> 来源: [蒜是哪根葱](https://mp.weixin.qq.com/s?__biz=MzI1MzQ3NzcwNg==&mid=2247484664&idx=1&sn=73f9d744198c75527e95b8bb967e4136&chksm=e85247e0dd132ce4784dd0d469ef0fbbd9123cefffe31d21bb0f14b0038e9affb61e65625bc7&mpshare=1&scene=1&srcid=0429VpRUOhJ2H5JELOvIDrvo&sharer_shareinfo=0fca845847c76b0e5b86402815a8c46d&sharer_shareinfo_first=0fca845847c76b0e5b86402815a8c46d) | 2026-04-29

## 摘要

Addy Osmani的agent-skills项目概念图：从Vibe Coding到Production-grade的进化
这破玩意，相信做过正经项目的人都懂——让 Claude 或 Cursor 帮你写代码，速度确实快，三下五除二就能搞出一个能跑的 demo。但等你要上线的时候，问题全来了：没有测试、没有安全审查、commit 历史一团糟、API 设计随手一拍、部署流程约等于手动 scp。
这就是所谓的 **Vibe Coding**——氛围到了，代码就出来了，但质量嘛……
Addy Osmani（对，就是那个在 Google 当工程总监的 Addy Osmani，Chrome DevTools 和 Lighthouse 背后的人）在 GitHub 上开源了一个项目叫 **agent-skills**，专门解决这个问题。
agent-skills的六阶段开发生命周期：DEFINE→PLAN→BUILD→VERIFY→REVIEW→SHIP
整个项目的核心思路是把软件开发拆成六个阶段，每个阶段有对应的 Skill。Agent 必须按阶段走，不能跳步。
每个阶段都有对应的斜杠命令：
-...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub-Copilot]], [[GitHub]], [[MCP]], [[Windsurf]]

## 相关概念

[[AI-Agent]], [[TDD]], [[Vibe-Coding]], [[上下文工程]], [[代码审查]], [[工作流自动化]]
