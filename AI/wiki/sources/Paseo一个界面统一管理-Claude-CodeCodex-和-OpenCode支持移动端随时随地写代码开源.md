---
tags: [Claude, Agent, MCP, GitHub, OpenAI, Skill]
source: "物联网星球"
created: 2026-04-13
updated: 2026-05-10
category: Claude
---

# Paseo：一个界面统一管理 Claude Code、Codex 和 OpenCode，支持移动端，随时随地写代码【开源】

> 来源: [物联网星球](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0MjE3Mg==&mid=2247501703&idx=1&sn=aa4807d426f38bbf35fc94eddf5937a9&chksm=c3558543f3d3cbc119587c760e3280bb51b34eec0704c54990ffded743262b4bd097f3c80680&mpshare=1&scene=1&srcid=0411MF8mLtW6RxRSXazjwzyx&sharer_shareinfo=86964d55cdda4b22c2f4562989e402ef&sharer_shareinfo_first=86964d55cdda4b22c2f4562989e402ef) | 2026-04-13

## 摘要

做AI编程的，现在手上至少有两三个不同的代码智能体：Claude Code、Codex、OpenCode……每个都有自己的命令行，各自为政，切来切去烦死人。
最近 GitHub 上有个开源项目叫 **Paseo**，正好解决这个问题——一个界面统一管理所有主流AI编程智能体，手机、桌面、CLI 都能用。
Paseo 不是又一个AI编程工具，而是一个**编排层**。
它自己不写代码，而是帮你管理 Claude Code、Codex、OpenCode 这些底层智能体。你可以：
•从手机远程启动家里的 Claude Code 跑任务
•同时在多个代码库并行跑不同的智能体
•用语音给智能体下指令
•在桌面端和移动端无缝切换
一句话：**把分散的AI编程能力，整合到一个统一的控制界面。**
Paseo 的核心是一个本地守护进程（daemon），运行在你的机器上：
**关键点：**
•**Self-hosted**：智能体在你的机器上运行，用你的开发环境、你的工具链、你的配置
•**无遥测**：不开源的项目天天传数据，Paseo 零追踪、零强制登录
•**跨设备**：iOS、Android、桌面、...

## 相关实体

[[Claude-Code]], [[Claude]], [[GPT-5]], [[GitHub]]

## 相关概念

[[代码生成]], [[数据可视化]]
