---
tags: [Hermes, Agent, API, Skill]
source: "怪兽打奥凸曼"
created: 2026-04-23
updated: 2026-05-10
category: Hermes
---

# ---

> 来源: [怪兽打奥凸曼](https://mp.weixin.qq.com/s?__biz=MzY5MzE3NjA4OA==&mid=2247483653&idx=1&sn=6b09711bb3299ed25f2a71035f9a24e4&chksm=f58ad9599f53b8af19b01b25496836221c6f66165caafd9dc5024ff9f96b36ecffa182d1ff73&mpshare=1&scene=1&srcid=0423HHjGRGi1Ys0QPOdScRjW&sharer_shareinfo=297500c5e940edc9084ab98628ff3c49&sharer_shareinfo_first=297500c5e940edc9084ab98628ff3c49) | 2026-04-23

## 摘要

| 编号 | 模式名称 | 英文 | 核心特点 | 使用场景 |
| --- | --- | --- | --- | --- |
| 01 | 🤖 单代理模式 | Single Agent | 逻辑集中，简单快速 | 简单问答、文本生成、小脚本编写、快速原型 |
| 02 | 🔗 顺序协作模式 | Sequential | 流水线串行，上下游传递 | 数据采集→清洗→分析、需求→开发→测试、文档→翻译→校对 |
| 03 | ⚡ 并行协作模式 | Parallel | 多Agent同时执行，最多3路 | 多源信息检索、批量内容生成、多角度分析、分支任务处理 |
| 04 | 👑 主从模式 | Manager-Worker | 智能任务分配与调度 | 项目规划执行、复杂问题求解、自动化工作流、多模块开发 |
| 05 | 🔄 评审反馈模式 | Critic-Refiner | 生成→评审→迭代优化闭环 | 代码审查优化、文章写作打磨、策略方案评估、高质量内容生产 |
**使用场景**：简单任务、快速响应、低成本
**配置步骤**：
**关键文件**：
- ```
config.yaml
...

## 相关实体

[[Hermes]]
[[Hermes-Agent]]

## 相关概念

[[多Agent协作]]
[[Agent架构]]
