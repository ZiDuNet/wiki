---
title: 发明Vibe Coding的人说它过时了，我想了很久为什么
type: source-summary
tags: [Vibe-Coding, Agentic-Engineering, AI-编程, Karpathy]
sources: [发明Vibe Coding的人说它过时了，我想了很久为什么.md]
created: 2026-05-20
updated: 2026-05-20
---

# 发明Vibe Coding的人说它过时了，我想了很久为什么

## 核心摘要

Andrej Karpathy 于 2025 年 2 月发明了「Vibe Coding」概念——用自然语言描述需求，让 AI 生成代码，人只管感受"氛围"。一年后，他在红杉资本 AI Ascent 大会上宣布 Vibe Coding 已过时，接替者是 **Agentic Engineering**。

## 关键观点

### Vibe Coding 的局限性

- Vibe Coding 适合原型验证，但无法保障生产级代码安全
- AI 生成代码"看起来对，能跑通过测试"，但缺乏对系统设计风险的理解
- 典型案例：用 Stripe 付款邮箱匹配 Google 登录邮箱来确定用户资金归属——这是危险设计，应使用系统内部 persistent user ID
- Karpathy 将当前 Agent 比喻为"带刺的实体"和实习生：执行能力强但有随机性和不稳定性

### Agentic Engineering 三要素

1. **Spec（规格约束）**：明确定义"哪些事绝对不能做"——如"所有资金必须绑定内部ID而非外部邮箱"
2. **协作流程设计**：将任务拆分给多个 Agent，各司其职、互相检查，而非单一 Agent 全权代理
3. **品味判断**：代码审美和极简主义不在 RL 训练目标内，仍需人类把关

### 核心洞察

> "你可以外包你的思考，但不能外包你的理解。Agent 可以记住所有 API 细节，但你必须理解内存效率；Agent 可以写支付逻辑，但你必须理解资金归属。"

**Vibe Coding 降低了做软件的下限，Agentic Engineering 守住了专业软件的质量上限。**

## 关键引用

- 原文来源：[金技局微信公众号](https://mp.weixin.qq.com/s?__biz=MzE5ODU0NjU0Mg==&mid=2247484953&idx=1&sn=20c4348c6492e2beec791dd1e2a76800&chksm=97ca833d0e99007588a16748ccfbd728b86d4e6706ebfaf813c7c2dbf23c42fde0e15ea97091&mpshare=1&scene=1&srcid=0520gWPXC0CCCsFfAS3fXNEG&sharer_shareinfo=36df27ece93d78cb81ec8d04797aca65&sharer_shareinfo_first=36df27ece93d78cb81ec8d04797aca65)
- 关联：[[Vibe-Coding-如何重塑产品设计和工程研发协同]] | [[从-Vibe-Coding-到-Harness-Engineering注意力时代的软件工程]] | [[vibe-coding会议助手实战]]
- 关联概念：[[Agentic-Engineering]] | [[Harness-Engineering]] | [[Spec]] | [[品味判断]]
