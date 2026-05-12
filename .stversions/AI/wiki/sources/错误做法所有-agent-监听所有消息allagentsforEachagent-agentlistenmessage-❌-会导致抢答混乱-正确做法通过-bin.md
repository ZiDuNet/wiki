---
tags: [OpenClaw, Agent, RAG]
source: "AI Hour"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# 错误做法：所有 agent 监听所有消息allagents.forEach(agent => agent.listen(message))  # ❌ 会导致抢答混乱# 正确做法：通过 bindings 精准路由targetagent = bindings.route(message.channel, message.accountid)targetagent.handle(message)  # ✅

> 来源: [AI Hour](https://mp.weixin.qq.com/s?__biz=MzY4ODAxMDc5MQ==&mid=2247484282&idx=1&sn=7ee707cf374b9c4bfa89b7eb4a182fd8&chksm=f273fde5d273c11faf2be21b0c3a5a9fdd707aa0541f1ea9d9496c169407323d2568c471fb56&mpshare=1&scene=1&srcid=04237RFy6XuVz4csAbsJBEQQ&sharer_shareinfo=e58417eba94d66f563cbe58093e4aa93&sharer_shareinfo_first=e58417eba94d66f563cbe58093e4aa93) | 2026-04-23

## 摘要

大多数人理解的"多 Agent"：开 5 个 bot，各聊各的。
**这不叫多 Agent，这叫多个单机器人。**
真正的多 Agent 系统有组织、有协议、有记忆隔离 —— 像一个团队在协作，而不是五个人在各自对着墙说话。
这篇文章拆解的是我用 OpenClaw 搭建的 5 角色协作系统的完整架构。从路由层到记忆系统，从会话隔离到群聊编排，每一层都是真实踩坑后的工程决策。不是 demo，不是概念验证，是正在跑的系统。
先看全貌：
**为什么选择单 Gateway？**
三个理由：
1. 1. **运维集中** —— 一个进程管理所有角色，不用开 5 个服务
2. 2. **配置统一** —— 一份总配置文件，不用到处同步
3. 3. **协作基础** —— 同一运行时才能高效通信，跨进程通信的复杂度不是你想踩的坑
**5 个角色的职责划分：**
- **总指挥** —— 态势感知、任务拆解、派工、收口
- **军师** —— 策略分析、方案评估、风险预判
- **工程师** —— 技术执行、代码实现、系统维护
- **创作官** —— 内容创作、表达优化、对外输出
- **智库** ...

## 相关实体

[[OpenClaw]]

## 相关概念

[[MultiAgent]], [[内容创作]], [[记忆系统]]
