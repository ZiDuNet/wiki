---
type: concept
name: AI-SDR
created: 2026-05-27
updated: 2026-05-27
---

# AI SDR

**Type:** Concept（AI销售自动化）
**来源:** Hermes-AI-SDR销售代表.md

## 定义

AI SDR（Sales Development Representative）= AI 驱动的销售开发代表。自动执行：研究潜在客户、写个性化外联邮件、筛选入站线索、更新 CRM、安排跟进。

## 核心数据

- 人类 SDR 每天研究 20-30 个潜在客户；AI SDR 可同时研究几百个
- McKinsey 数据：AI SDR 部署后转化率提升 40%，线索执行速度提升 30%
- 传统 SaaS SDR 工具 $900/月起；Hermes SDR $5/月 + 模型费

## 工作流程

### Inbound Processing
1. 检查收件箱新线索（表单/回复）
2. 研究公司（规模/行业/最近新闻）
3. 线索评分（BANT：预算/权威/需求/时间线）
4. 合格则起草个性化回复；不合格则礼貌拒绝 + 归档

### Outbound Sequence
1. 研究目标公司和联系人
2. 找个性化 hook（最近新闻/招聘/融资/技术栈）
3. 起草邮件（hook + 价值主张 + 软 CTA）
4. 3 天无回复安排跟进

## 典型日程（Contabo 教程）

| 时间 | 任务 |
|------|------|
| 7:00 | 处理入站队列 |
| 9:00 | 研究今日外联目标 |
| 10:00 | 发送第一轮外联邮件 |
| 14:00 | 检查回复，更新 CRM |
| 15:00 | 发送跟进邮件 |
| 17:00 | 生成日报，推送 Telegram |

## 四大坑

1. **邮件进垃圾箱** — 每封必须有独特 hook（公司新闻/招聘/融资）
2. **忘记退订机制** — Skill 必须写 "Respect unsubscribe requests immediately"
3. **Agent 承诺不存在功能** — 写 "Never promise features that don't exist"
4. **成本失控** — 用 smart routing（Gemini Flash 研究 / Claude 写邮件）

## 相关实体

- [[Hermes-Agent]] — 搭建 AI SDR 的框架
- [[Notion]] — 可选 CRM
- [[Supabase]] — 可选 CRM
- [[DGX-Spark]] — 可部署平台

## 相关概念

- [[Lead-Scoring]] — 线索评分机制
- [[Smart-Routing]] — 智能路由节省成本
- [[Learning-Loop]] — Hermes 持续优化邮件质量
- [[Cron任务]] — 定时驱动 SDR 日程