---
tags: [Hermes, Agent, Claude, GitHub, Prompt, Skill, OpenClaw]
source: "AgentLab先行者"
created: 2026-05-06
updated: 2026-05-10
category: Hermes
---

# macOS/Linux 一键安装brew install multica-ai/tap/multica# 配置：登录认证 + 启动守护进程multica setup

> 来源: [AgentLab先行者](https://mp.weixin.qq.com/s?__biz=MzYzMzg5MTc3OQ==&mid=2247483786&idx=1&sn=3d2aa8f9ad550cfd395f722834753aba&chksm=f1a8834e82f208803341c421e5d64ad1fef7ecb7fa5f7e1681421b5dc44b23af539a576a6477&mpshare=1&scene=1&srcid=0506jKsUK7dKjG5zeJUIrfAV&sharer_shareinfo=28f0006ed9180cf6f4e3c07318a04cad&sharer_shareinfo_first=28f0006ed9180cf6f4e3c07318a04cad) | 2026-05-06

## 摘要

一个很有意思的趋势正在发生：
图1
AI Agent不再只是"帮你执行命令的工具"，而是正在变成"可以指派任务的同事"。
支撑这个变化的，是一个叫 **Multica** 的开源平台。
图2
传统AI Agent的使用方式是这样的：
你写一段prompt，Agent执行，结果给你。你全程在"喂"它。
Multica想改变这个关系——**让Agent主动认领任务、定期汇报、积累技能**，像一个真正的团队成员。
这句话听起来有点夸张，但实际用起来确实有不一样的感觉。
图3
在Multica里，你不需要给Agent发消息下指令。
你创建一个Issue（比如"优化登录页面的错误处理"），然后把这个Issue**指派给一个Agent**。
Agent会自动：
- **Claim**
这个任务
- 开始执行
- 通过WebSocket实时推送进度
- 完成后更新Issue状态
- 遇到Blocker主动汇报
整个过程，你不需要盯着屏幕。Agent会像同事一样出现在任务面板上。

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub]], [[Hermes]], [[Nextjs]], [[OpenClaw]]

## 相关概念

[[AI-Agent]], [[MultiAgent]]
