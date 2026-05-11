---
tags: [Hermes, Agent, MCP, Prompt, API, Python, Skill]
source: "未知变量X"
created: 2026-04-24
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 从入门到精通：8个实战技巧让AI真正记住你

> 来源: [未知变量X](https://mp.weixin.qq.com/s?__biz=MzIwOTUyMjYxMg==&mid=2247484826&idx=1&sn=8c9d7dad533ff3f8980a59fb44e925f8&chksm=96598577fff374dc9417e588954bc7a612feca88b0a0d09af266a60d582b9afd1d7becbacb87&mpshare=1&scene=1&srcid=0424mxDFt4guQHUhIBngwD0B&sharer_shareinfo=c43cf553451c8cf063fcdf03c5c9d084&sharer_shareinfo_first=c43cf553451c8cf063fcdf03c5c9d084) | 2026-04-24

## 摘要

作者: AI实验室
你是不是也遇到过这种情况：
跟Hermes聊了半天需求和偏好，下次新会话一开，它问：“你是谁来着？”
别急着骂它记性差。真相是：**Hermes的记忆系统有很明确的设计逻辑，你可能一直用错了方法。**
本文适合已完成基础配置的同学，直接上进阶干货。
很多人踩坑的根源在于：把Hermes当成了“全量记录仪”。
实际上，它的记忆系统是**内置记忆 + 外部提供商 + 运行时上下文**的三层组合。理解这个架构，你才能真正用活它。
存放在
目录下的两个文件：
- **MEMORY.md** — 类似Agent的工作笔记，保存环境事实、项目约定。硬限制2200字符，建议维持在1800字符左右。
- **USER.md** — 类似用户画像，保存你的偏好和沟通风格。硬限制1375字符，建议维持在1100字符左右。
**关键概念：冻结快照。**
这两个文件在每次会话开始时作为**冻结快照**注入上下文。会话中写入的记忆，通常要到后续会话才能体现。
这种设计的核心目的是**保持前缀稳定**，从而提升KV Cache命中并降低推理成本。
外部提供商是对内置记忆的补充，不是替代。Her...

## 相关实体

[[Hermes-Agent]]
[[Claude]]

## 相关概念

[[上下文管理]]
