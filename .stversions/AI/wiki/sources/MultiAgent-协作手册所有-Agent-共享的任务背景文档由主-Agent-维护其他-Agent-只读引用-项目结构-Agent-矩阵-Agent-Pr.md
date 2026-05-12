---
tags: [Hermes, Agent, 飞书, API, Skill, OpenClaw]
source: "梦朝思夕技术与管理博客"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Multi-Agent 协作手册所有 Agent 共享的任务背景文档。由主 Agent 维护，其他 Agent 只读引用。---## 项目结构### Agent 矩阵| Agent | Profile | 角色 | 核心职责 ||-------|---------|------|----------|| hermes (当前) | `~/.hermes/` | 主控 Agent | 任务调度、跨 Agent 协调、内容发布主流程 || hermes-coder | `~/.hermes/profiles/hermes-coder/` | 开发助理 | 代码开发、技术架构、部署（Aliyun/火山云/DCP） || hermes-dcp | `~/.hermes/profiles/hermes-dcp/` | 运维工程师 | DCP 平台运维、服务管理、ddsv/db/ddns 等 |### 主人信息-工作：小红书内容发布（从凤凰网等链接抓取文章，发布到小红书）-质量标准：正文换行必须是真实换行符 `\n`，不能是字面 `\\n`（已多次强调，必须遵守）-时区：Asia/Shanghai---## 协作规则### 任务分发原则1.代码/架构任务 → `hermes-coder`（通过 `delegatetask` 或 `hermes -p hermes-coder`）2.运维/部署任务 → `hermes-dcp`（通过 `delegatetask` 或 `hermes -p hermes-dcp`）3.内容发布主流程 → 当前 Agent（hermes）直接处理4.复杂任务 → 先计划，列步骤，经确认后再执行### 跨 Agent 通信- 当前 Agent 负责任务分配和结果汇总- 子 Agent 完成工作后，当前 Agent 负责验证和交付- 所有 Agent 共享同一个 `~/.hermes/agents.md` 作为任务背景### 可复用的标准流程参见 `~/.hermes/plans/` 目录下的已存档执行计划。---## 共享资源路径```~/.hermes/├── agents.md              # 本文件 — 跨 Agent 共享任务背景├── plans/                  # 执行计划存档├── profiles/│   ├── hermes-coder/      # 开发助理 profile│   └── hermes-dcp/        # 运维工程师 profile└── skills/                # 全局共享 skills```

> 来源: [梦朝思夕技术与管理博客](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635868&idx=1&sn=6525e66632b77c11f10b982887e12235&chksm=fc57b5ab7568ea6687669915af4aeb9b3f0eeed8ce156852c2b1ee19e88706342c490a13952f&mpshare=1&scene=1&srcid=0420ifsRXgLNcqAMOJ8aXVdB&sharer_shareinfo=97f6f05cc37c3ef5141eece781f09024&sharer_shareinfo_first=97f6f05cc37c3ef5141eece781f09024) | 2026-04-20

## 摘要

看这篇文章的同学，我是默认看过之前的[《Hermes Agent 安装教程》](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635807&idx=1&sn=beb47cbeff028c7f1cf2b6cdf4b6d5aa&scene=21#wechat_redirect)和[《Hermes Agent装好了，还需要做的9件事》，](https://mp.weixin.qq.com/s?__biz=MzI2OTA3MDk4Mw==&mid=2458635852&idx=1&sn=691b2ff3fa150e21ffdcf1cc65252da6&scene=21#wechat_redirect)如果还没有看过，一定要去看看，因为这两篇文章是基础也是前提。
使用过Openclaw或Hermes Agent的同学应该都有所感觉，所有需求都塞给单个 Agent，上下文和记忆难免杂乱。而且一次只能处理一个任务——让 Hermes 做研究的时候想问别的就得等着。
如果你已经有一个跑通的 Hermes Agent，五步就能搭起一个...

## 相关实体

[[Cloudflare]], [[Hermes]], [[小红书]], [[飞书]]

## 相关概念

[[MultiAgent]], [[代码审查]]
