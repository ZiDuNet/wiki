---
tags: [Claude, Agent, Prompt, API, Skill]
source: "AI步步通"
created: 2026-05-01
updated: 2026-05-10
category: Claude
---

# 拆解 Claude Code 的大循环机制

> 来源: [AI步步通](https://mp.weixin.qq.com/s?__biz=MzY4NTE4OTYzNg==&mid=2247483884&idx=1&sn=02644e6607865ae3d111125b48b61120&chksm=f216a8307d183e19f22cba7b8851942c1997bd08da355f25d5b33ae64ec79ed94519e0ab3aa7&mpshare=1&scene=1&srcid=0501RDNIXGS0E4Z01BhV0hYF&sharer_shareinfo=f492ef4d77e1a06c421f477fa9d08a99&sharer_shareinfo_first=f492ef4d77e1a06c421f477fa9d08a99) | 2026-05-01

## 摘要

如果只把终端 Agent 看作一个“会调用工具的聊天框”，就会把它简化成一次问答。用户输入一句话，模型读文件、改代码、跑测试，最后给出结果。这个表面体验很顺，背后支撑它的是一个长时间运行、持续决策的循环系统。
Claude Code 的核心是一套持续推进的 Agentic Loop：模型判断当前状态，发起工具调用，运行时执行动作，把结果重新喂回模型，再进入下一轮判断。复杂任务能跑几十轮，靠的是循环本身对上下文增长、权限拦截、工具失败、API 限流和用户中断的承载能力。
这套机制把错误也纳入了循环。文件不存在、命令失败、权限被拒绝、API 短暂不可用，这些异常不会天然等于 CLI 崩溃。它们会被截住、归类、转译成模型和 UI 都能理解的反馈，让下一轮决策可以继续发生。
Claude Code 的大循环可以拆成四层：QueryEngine 负责推进 turn，Tool System 负责执行动作，Permission / Hook 负责拦截边界，React + Ink 负责把状态变化渲染成终端体验。
Claude Code Persistent Agentic Loop上下文、动作、结果、...

## 相关实体

[[Claude-Code]], [[Claude]], [[React]]

## 相关概念


