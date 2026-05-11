---
tags: [OpenClaw, Agent, GitHub, 飞书, API, Python, OpenAI, Skill]
source: "前沿AI运维"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# Linux / macOS / WSL2curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

> 来源: [前沿AI运维](https://mp.weixin.qq.com/s?__biz=MzY5NzI4MjU1NA==&mid=2247483684&idx=1&sn=895e29a075f942822455828c76ef0ff7&chksm=f53a02285cc43300ac92270f37f631967ca757339502a15562f559225e49a3b45bbd92f0e9d2&mpshare=1&scene=1&srcid=0423Z7LI85vRbNHutqBm2dDY&sharer_shareinfo=bd5bb203434036fde1d1247165adba25&sharer_shareinfo_first=bd5bb203434036fde1d1247165adba25) | 2026-04-23

## 摘要

先说结论：**两者是互补关系，不是替代关系。**
| 对比项 | Hermes | OpenClaw |
| --- | --- | --- |
| **定位** | 🚀 Agent 执行引擎 + API 网关 | 🎛️ Agent 管理平台 |
| **核心能力** | 会话管理、OpenAI 兼容 API、插件执行 | Skills 生态、任务编排、可视化界面 |
| **部署方式** | 轻量，支持远程部署 | 必须本地 Gateway |
| **适合场景** | 远程接入、多设备管理、API 集成 | 本地调试、复杂任务、多工具协同 |
| **上手难度** | ⭐⭐ 简单 | ⭐⭐⭐ 稍复杂 |
**我的建议**：多任务用 OpenClaw，专项任务用 Hermes，想同时操控一把抓就用 OpenClaw-Admin。
**一行命令安装**：
安装完成后，重新加载 shell：
验证安装：
**初始化配置**：
**WSL2 方式（推荐）**：
**原生 Windows 方式（有坑，不推荐）**：
如果一定要在 Windows 原生环境运行，可以手动安装：
**Window...

## 相关实体

[[GitHub]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[Python]], [[钉钉]], [[飞书]]

## 相关概念

[[SOP]]
