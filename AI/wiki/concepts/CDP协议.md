---
title: CDP协议
type: concept
tags: [协议, 浏览器, 自动化]
sources: [browser-harness-592-lines-ai-browser-control.md]
created: 2026-05-29
updated: 2026-05-29
---

# CDP协议

**类型:** 概念

## 定义

Chrome DevTools Protocol（CDP）——Chrome 浏览器底层调试协议，通过 WebSocket 与外部程序通信。

## 核心能力

- DOM 操作与事件监听
- 网络请求拦截与模拟
- 输入事件注入
- 页面渲染控制

## 与浏览器自动化关系

传统方案（Selenium/Playwright）：
- 需 xpath/选择器
- 页面结构变化脚本失效
- 维护成本高

CDP 直连方案：
- 直接对话浏览器
- 无中间框架层
- Agent 自适应网页

---

## 相关实体

- [[CDP]] — 协议本体
- [[Browser-Harness]]
- [[Puppeteer]]

## 相关概念

- [[浏览器自动化]]
- [[自愈式自动化]]