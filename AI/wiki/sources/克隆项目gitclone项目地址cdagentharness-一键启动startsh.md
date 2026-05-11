---
tags: [Harness, Agent, GitHub, RAG, Prompt, API, Python]
source: "AI学习的杨同学"
created: 2026-04-20
updated: 2026-05-10
category: Harness
---

# 克隆项目git clone <项目地址>cd agent-harness # 一键启动./start.sh

> 来源: [AI学习的杨同学](https://mp.weixin.qq.com/s?__biz=MzE5ODExMjI3Mw==&mid=2247487831&idx=1&sn=f4d5b3d7f4f94f07d0b8b84a69ff6f50&chksm=9758614dcbbcc5080d69472787ecd9b08c6b1fe2b5f612d7a8fc60a685dff31dfec324606e3c&mpshare=1&scene=1&srcid=0420118c2l0dcKg7jgOA7mR0&sharer_shareinfo=bdcf08c3635123871d32c2518462ad80&sharer_shareinfo_first=bdcf08c3635123871d32c2518462ad80) | 2026-04-20

## 摘要

大家好，我是AI学习的杨同学。当你有多个 AI Agent 需要协同工作时，谁来决定它们的执行顺序？失败了怎么重试？怎么监控整个流程？这就是 Harness 要解决的问题。今天我们一起动手搭建一个Agent Harness，完成多智能体协同工作。
一、为什么需要 Harness
假设你在做一个 AI 驱动的软件开发流程：
每个环节是一个独立的 Agent。问题来了：
• 谁来决定执行顺序？
• 评审不通过时，谁负责把错误信息传回给生成 Agent？
• 最多重试几次？超时了怎么办？
• 整个过程怎么记录和监控？
这些都不是 Agent 自己该操心的事。Agent 只管做好自己的活，编排的事交给 Harness。
Harness 的定位：多 Agent 的编排层，不关心 Agent 内部逻辑，只管把它们按流程串起来、处理失败、记录一切。
二、架构设计
核心模块：
|  |  |
| --- | --- |
| 模块 | 职责 |
| Agent 基类 | 统一接口，继承 run() 即可接入 |
| Pipeline | 定义执行流程（串行/并行/条件/回退） |
| Harness 引...

## 相关实体

[[Docker]], [[GitHub]], [[Harness]], [[Python]], [[SQLite]]

## 相关概念

[[AI-Agent]], [[Multi-Agent]], [[RAG]], [[代码生成]], [[自动化测试]]
