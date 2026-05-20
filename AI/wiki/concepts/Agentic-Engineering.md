---
title: Agentic Engineering
type: concept
tags: [AI编程, Agent, 软件工程, Karpathy]
sources: [发明Vibe Coding的人说它过时了，我想了很久为什么.md]
created: 2026-05-20
updated: 2026-05-20
---

# Agentic Engineering

> Agentic Engineering 是 Andrej Karpathy 在 2026 年提出的新范式，用于取代 Vibe Coding。它强调人类在 AI 辅助编程中的不可替代职责：定义约束、设计流程、把控品味。

## 核心定义

Agentic Engineering 要求人类承担三项 AI 无法外包的工作：

1. **Spec（规格约束）**：定义"哪些事绝对不能做"
2. **协作流程设计**：拆分任务给多个 Agent，各司其职、互相检查
3. **品味判断**：代码审美和极简主义仍需人类把关

## 与 Vibe Coding 的对比

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 核心理念 | "AI帮你做，你不用懂" | "AI帮你做，但你必须比它更懂什么不能做" |
| 人类角色 | 感受"氛围"，验收结果 | 定义约束、判断品味、识别"能跑但有毒"的代码 |
| 代码质量 | 下限（让不会写代码的人也能做东西） | 上限（确保做出来的东西不会在生产环境出事） |
| 适用场景 | 原型验证、个人小工具 | 生产级系统、支付逻辑、数据安全 |

## 关键洞察

> "你可以外包你的思考，但不能外包你的理解。Agent 可以记住所有 API 细节，但你必须理解内存效率；Agent 可以写支付逻辑，但你必须理解资金归属。"

**Spec 的重要性**：AI 生成代码"看起来对，能跑通过测试"，但缺乏对系统设计风险的理解。例如用 Stripe 付款邮箱匹配 Google 登录邮箱来确定用户资金归属——这是危险设计，应使用系统内部 persistent user ID。

## 相关实体

- [[Andrej-Karpathy]] — Vibe Coding 和 Agentic Engineering 的提出者
- [[MenuGen]] — Karpathy 提到的演示应用
- [[Stripe]] — 被提及的危险设计案例中的支付平台
- [[Google]] — 被提及的危险设计案例中的登录平台

## 相关概念

- [[Vibe-Coding]] — Agentic Engineering 的前身，已被宣布过时
- [[Harness-Engineering]] — 类似的"门禁不能靠AI自判"工程思想
- [[Spec]] — Agentic Engineering 第一要素：定义约束
- [[品味判断]] — Agentic Engineering 第三要素：代码审美

## 来源

- [[发明Vibe-Coding的人说它过时了-我想了很久为什么]]（金技局，2026-05-20）
