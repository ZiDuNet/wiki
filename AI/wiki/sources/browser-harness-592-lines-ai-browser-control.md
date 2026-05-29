---
title: Browser Harness：592 行代码让 AI 操控浏览器，自愈式自动化
type: source-summary
tags: [浏览器自动化, CDP协议, 自愈系统, AI-Coding]
sources: [browser-harness-592-lines-ai-browser-control.md]
created: 2026-05-29
updated: 2026-05-29
---

# Browser Harness：592 行代码让 AI 操控浏览器

> 来源: 何三笔记 | 时间: 2026-05-29

## 项目概述

**7.8k Star**。一个只有 **592 行 Python 代码** 的项目，让 AI 像人一样操控浏览器。出 bug 了怎么办？它自己写代码给自己打补丁。

**Browser Harness**，browser-use 团队出品。

---

## 传统浏览器自动化的痛点

| 框架 | 问题 |
|---|---|
| Selenium | 页面改 class 名脚本就废，不停修 xpath、修选择器、修等待时间 |
| Playwright | 同样要跟 DOM 树死磕，网页一改就得跟着改 |

本质：拿头跟 DOM 树死磕。

---

## Browser Harness 的颠覆思路

### 核心设计

- 只有 **592 行 Python**
- 基于 **Chrome DevTools Protocol（CDP）** 直接跟浏览器对话
- **没有框架、没有 recipes**——WebSocket 直连 Chrome，中间什么都不隔
- 直接连已装好的 Chrome，开个 remote debugging 端口就行

### 自愈式工作流

LLM 操作浏览器时发现缺东西（如要上传文件但没有上传函数）→ 在 `agent-workspace/` 目录下自己写 helper 函数 → 自己写，自己用，继续跑。

> 以前是你写代码让机器跑，现在是机器发现缺代码，自己写出来继续跑。
> 这已经不是自动化的范畴了，这是 **self-healing**。

---

## 设计哲学对比

| 方案 | 思路 |
|---|---|
| 传统自动化框架 | 给 AI 设轨道，让它在轨道上跑 |
| Browser Harness | 直接给 AI 一辆车，说"你去吧，路没了自己修" |

---

## 使用方式

装好后，把这段粘到 Claude Code 或 Codex：

```
Set up https://github.com/browser-use/browser-harness for me.
Read `install.md` first to install and connect this repo to my real browser.
Then read `SKILL.md` for normal usage.
```

AI 会自己读文档、自己装依赖、自己连浏览器。只需在 Chrome 开一个 remote debugging。

---

## 同类对比

| 工具 | 思路 |
|---|---|
| Playwright codegen | 记录回放 |
| Selenium IDE | 记录回放 |
| **Browser Harness** | 自愈式 AI 操控 |

真正同类的是 **AutoGPT** 那种 Agent 框架，只不过专注在浏览器场景。

---

## 相关实体

- [[Browser-Harness]] — 本项目
- [[browser-use团队]] — 出品方
- [[何三]] — 作者
- [[CDP]] — Chrome DevTools Protocol

## 相关概念

- [[自愈式自动化]] — 核心创新
- [[CDP协议]] — 技术基础
- [[浏览器自动化]] — 领域背景
- [[Agent-Harness]] — 更广义概念

---

## 项目链接

- **GitHub**: https://github.com/browser-use/browser-harness