---
tags: [entity, 开源项目, AI新闻, 信息流]
sources:
  - Horizon/Horizon：打造你的专属 AI 新闻雷达.md
created: 2026-05-11
updated: 2026-05-11
---

# Horizon

开源项目（Thysrael/Horizon），AI 驱动的个人新闻雷达。

## 核心功能

- 多源聚合：HN、RSS/Atom、Reddit、GitHub
- AI 评分：0-10 分智能筛选，自定义阈值
- 智能去重：跨平台合并相同报道
- 上下文丰富：自动搜索背景知识
- 社区评论汇总：HN、Reddit 讨论
- 双语输出：中英文简报

## 交付方式

- GitHub Pages（推荐）
- 邮件订阅（SMTP/IMAP）
- Webhook（飞书、钉钉、Slack、Discord）
- MCP 服务

## 自动化

推荐 GitHub Actions 定时任务，每天自动生成简报。

## 相关概念

- [[信息流自动化]] — 多源采集 + AI 过滤
- [[MCP协议]] — 流水线暴露为 MCP 工具
- [[知识管理]] — 信息过滤和沉淀
