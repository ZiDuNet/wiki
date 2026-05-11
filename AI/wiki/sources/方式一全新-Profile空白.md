---
tags: [Hermes, Agent, Claude, MCP, Prompt, API, Python, OpenAI]
source: "RowanFYI"
created: 2026-04-21
updated: 2026-05-10
category: Hermes
---

# 方式一：全新 Profile（空白）

> 来源: [RowanFYI](https://mp.weixin.qq.com/s?__biz=MzI0NTUyNTM1OQ==&mid=2247485611&idx=1&sn=5e0105f5eb130e001d7cc7c94be40177&chksm=e894713435dfb6d54263a5b04a0b4698e0cff03343c5d13f15b5d6efbcb8112d2a94cda6b56f&mpshare=1&scene=1&srcid=0421kTkr11a97ZXTLFp2PG5x&sharer_shareinfo=4ca9a228a1f1e75a366655763742071d&sharer_shareinfo_first=4ca9a228a1f1e75a366655763742071d) | 2026-04-21

## 摘要

本指南默认你已完成 Hermes 的基础安装与配置。我们将直接进入进阶核心内容：
- 🧠 记忆系统
- 🔄 技能自进化
- 🤖 多 Agent 协作
- 🚀 生产化部署
- 🔧 高级调试
Hermes 的记忆系统是 \*\*Agent-curated（策展）\*\*的，不是全量记录的。
**核心原因：**
| 原因 | 说明 |
| --- | --- |
| 节省 Token | 如果每轮对话都实时更新记忆，System Prompt 头部会频繁变化，导致无法利用 KV Cache，推理成本大幅增加 |
| 防止记忆污染 | Agent 思考中的"碎碎念"、临时试错、中间结果，不值得长期保留 |
**简单来说：** 实时写入会贵且乱，策展 + 周期性 nudge 是性能与质量的平衡点。
Agent 不会把你说的每一句话都写进记忆。通常在以下场景更容易被保留：
✅ 你明确表达了偏好："我喜欢/不喜欢 xxx"
✅ 发现了环境事实："这台机器装了 xxx"
✅ 纠正了 Agent 的错误做法："不要用 sudo，我在 docker 组里"
✅ 完成了一个重要任务里程碑
✅ 你明确要求它记...

## 相关实体

[[Docker]], [[Hermes]], [[MCP]], [[Python]]

## 相关概念

[[Multi-Agent]], [[SOP]], [[自进化系统]], [[记忆系统]]
