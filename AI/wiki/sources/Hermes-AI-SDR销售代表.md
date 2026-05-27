---
tags: [Hermes, AI-SDR, 销售自动化, CRM, Cron任务, 邮件自动化, Lead-Generation]
sources: [用 Hermes Agent 搭一个 AI 销售代表，每天自动找线索、写邮件、跟进客户.md]
created: 2026-05-27
updated: 2026-05-27
---

# Hermes AI SDR — 自动销售代表搭建指南

**来源：** 微信公众号/Hermes/用 Hermes Agent 搭一个 AI 销售代表，每天自动找线索、写邮件、跟进客户.md
**分类：** Hermes
**摄入日期：** 2026-05-27
**作者：** AI赋能说

## 摘要

本文详解如何用 Hermes Agent 构建 AI SDR（Sales Development Representative），实现每天自动找线索、研究潜在客户、写个性化外联邮件、跟进并更新 CRM。整个流程 cron 驱动，一次配置，每天自动跑。麦肯锡数据显示 AI SDR 部署后转化率提升 40%，线索执行速度提升 30%。

## 核心观点

- **AI SDR 定义：** 自动研究潜在客户、写个性化外联邮件、筛选入站线索、更新 CRM、安排跟进
- **效率对比：** 人类 SDR 每天研究 20-30 个潜在客户；AI SDR 可同时研究几百个
- **商业模式：** Hermes SDR 跑在自有 VPS，$5/月 + 模型费，数据不出服务器；传统 SaaS SDR 工具 $900/月起
- **核心优势：** Learning Loop 持续优化，第 6 周邮件质量比第 1 周好 60%
- **成本控制：** 用 smart routing（便宜模型做研究，好模型写邮件）

## SDR 典型日程

| 时间 | 任务 |
|------|------|
| 7:00 | 处理入站队列（新表单、回复） |
| 9:00 | 研究今日外联目标 |
| 10:00 | 发送外联邮件（第一轮） |
| 14:00 | 检查回复，更新 CRM |
| 15:00 | 发送跟进邮件（3天未回复） |
| 17:00 | 生成日报，推送到 Telegram |

## 四阶段搭建路径

### 阶段一：配置邮件接入
- 在 `~/.hermes/config.yaml` 配置 IMAP/SMTP
- 在 `~/.hermes/.env` 存储密码

### 阶段二：创建 SDR Skill
- 创建 `~/.hermes/skills/ai-sdr/SKILL.md`
- 定义 Role（AI Sales Development Representative）
- 定义 Workflow（Inbound Processing + Outbound Sequence）
- 安装社区现成 B2B SDR skill

### 阶段三：设置 Cron 定时任务
- 每天 7:00 检查收件箱新线索，研究公司背景，写邮件草稿，推送 Telegram
- 每天 15:00 检查 3 天前未回复邮件，写跟进邮件草稿

### 阶段四：连接 CRM
- 配置 Notion（v2.0）或 Supabase 作为 CRM
- 第一周开启人工审批（smart/manual 模式）
- 质量稳定后切换 auto 模式自主发送

## 四大坑及避坑

| 坑 | 问题 | 解法 |
|----|------|------|
| 邮件进垃圾箱 | 模板感太强被标记 | 每封邮件必须有独特 hook（公司新闻/招聘信息/融资动态） |
| 忘记退订机制 | 可能违反 CAN-SPAM | Skill Constraints 明确写 "Respect unsubscribe requests immediately" |
| Agent 承诺不存在功能 | agent 过度承诺 | 明确写 "Never promise features that don't exist" |
| 成本失控 | 一个 session 吃掉 50% token | smart routing：Gemini Flash 做研究，Claude/GPT 写邮件 |

## 前提条件

- Hermes Agent v0.14.0 已安装并配置好 provider
- VPS（8GB RAM 够用）或本地机器
- 邮箱（Gmail / Outlook / 自建 SMTP）
- 可选：CRM（Notion / Supabase / HubSpot）

## 提及实体

- [[Hermes Agent]] — 开源自进化 AI Agent 框架
- [[OpenClaw]] — 文中对比提及的开源框架
- [[Notion]] — CRM 选项之一
- [[Supabase]] — CRM 选项之一
- [[DGX Spark]] — 文中提及的跑 Hermes SDR 的平台

## 涉及概念

- [[AI-SDR]] — Sales Development Representative，AI 驱动的销售开发代表
- [[Smart-Routing]] — 智能路由，用便宜模型做研究，好模型写邮件
- [[Learning-Loop]] — Hermes 行为自进化机制，邮件质量持续优化
- [[Cron任务]] — 定时任务驱动 SDR 自动化日程
- [[邮件自动化]] — AI SDR 的核心工作内容
- [[Lead-Scoring]] — 线索评分（BANT：预算/权威/需求/时间线）