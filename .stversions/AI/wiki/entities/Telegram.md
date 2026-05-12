---
type: entity
name: Telegram
created: 2026-05-10
updated: 2026-05-10
---

# Telegram

**类型:** 即时通讯平台 / AI Agent 接入渠道
**官网:** telegram.org
**被引用文章数:** 112+

## 简介

Telegram 是一个全球性的即时通讯平台，在 AI Agent 生态中扮演着重要的"消息网关"角色。[[Hermes-Agent]] 和 [[OpenClaw]] 等主流 Agent 框架都原生支持 Telegram 作为消息渠道，使其成为 AI Agent 与用户交互的核心界面之一。

## 在 AI Agent 生态中的角色

### 作为 Agent 消息渠道
Telegram 是 [[Hermes-Agent]] 支持的四大通讯平台之一（其余为 [[微信]]、[[飞书]]、Discord）。Agent 通过 Telegram Bot API 接收用户指令并返回执行结果，实现"随时随地指挥 AI 干活"。

### 多 Agent 协作场景
在 Hermes 的 [[多Agent协作]] 架构中，Telegram 群组可以用作多个 Agent 的协作空间：
- 不同 Agent 以 Bot 身份加入同一群组
- 通过 @mention 指定某个 Agent 处理任务
- Agent 之间在群内自动协调分工

### 定时任务通知
结合 [[Cron定时任务]]，Agent 可以在 Telegram 上：
- 定时推送新闻摘要、数据分析报告
- 任务完成后自动通知
- 监控告警实时推送

## 配置方式

Hermes Agent 接入 Telegram 的配置方式：
- 命令配置：`hermes config set TELEGRAM_BOT_TOKEN your_bot_token`
- 手动编辑配置文件：修改 hermes.config.yaml

## 与其他平台的对比

| 特性 | Telegram | [[微信]] | [[飞书]] |
|------|----------|----------|----------|
| Bot API 开放度 | 高 | 中（个人号限制多） | 高 |
| 群组 Agent 协作 | 原生支持 | 需第三方桥接 | 支持 |
| 消息格式 | Markdown/HTML | 有限 | 富文本 |
| 海外可用性 | 优秀 | 仅国内 | 仅国内 |

## Related Entities

[[Hermes-Agent]] [[Hermes]] [[OpenClaw]] [[微信]] [[飞书]] [[Discord]] [[Termux]]

## Related Concepts

[[多Agent协作]] [[Cron定时任务]] [[Webhook自动化]] [[Agent路由]] [[自进化系统]]

## Related Sources

- [[15-项可能你从未体验过的-Hermes-Agent-功能]] — Telegram 作为 Hermes 功能展示平台
- [[Hermes-Agent-横纵分析报告]] — Hermes Agent 支持 Telegram 作为通讯渠道
- [[让-AI-更好的自动干活Hermes-Agent-定时任务实战指南]] — 定时任务结果推送到 Telegram
- [[装了-Hermes-却只当聊天框用这-15-个功能你大概率没碰过]] — Telegram 相关隐藏功能
- [[深度报告-_-Hermes-Agent会自我进化的开源AI-Agent]] — Telegram 在 Agent 架构中的角色
