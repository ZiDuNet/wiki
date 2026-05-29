---
title: Browser-Harness
type: entity
tags: [浏览器自动化, CDP, 自愈系统, GitHub]
sources: [browser-harness-592-lines-ai-browser-control.md]
created: 2026-05-29
updated: 2026-05-29
---

# Browser-Harness

**类型:** 实体
**身份:** 开源项目
**Stars:** 7.8k
**出品方:** browser-use 团队

## 简介

592 行 Python 代码，让 AI 像人一样操控浏览器。核心创新是 **自愈式自动化**——出 bug 时 AI 自己写代码打补丁。

## 核心特性

| 特性 | 说明 |
|---|---|
| **代码量** | 592 行 Python |
| **技术基础** | Chrome DevTools Protocol（CDP） |
| **连接方式** | WebSocket 直连 Chrome，无中间框架 |
| **自愈机制** | 发现缺函数 → 自己写 helper → 继续跑 |

## 设计哲学

- 不给 AI 设轨道，直接给 AI 一辆车
- 路没了自己修——self-healing
- 对比传统：Selenium/Playwright 需人跟 DOM 死磕

## 使用方式

```bash
# 粘到 Claude Code 或 Codex
Set up https://github.com/browser-use/browser-harness for me.
Read `install.md` first to install and connect this repo to my real browser.
Then read `SKILL.md` for normal usage.
```

---

## 相关实体

- [[browser-use团队]] — 出品方
- [[何三]] — 推文作者

## 相关概念

- [[自愈式自动化]]
- [[CDP协议]]
- [[浏览器自动化]]
- [[Agent-Harness]]