---
title: CDP
type: entity
tags: [协议, Chrome, 浏览器]
sources: [browser-harness-592-lines-ai-browser-control.md]
created: 2026-05-29
updated: 2026-05-29
---

# CDP (Chrome DevTools Protocol)

**类型:** 实体
**身份:** 技术协议

## 简介

Chrome DevTools Protocol（CDP）——Chrome 浏览器底层调试协议，允许外部程序通过 WebSocket 与 Chrome 直接通信。

## 核心能力

- 直接操控浏览器 DOM、网络、输入
- 无需中间框架层
- Puppeteer 也走 CDP，但需下载 Chromium（几百兆）
- Browser Harness 直连已装好的 Chrome，开 remote debugging 端口即可

## 对比

| 方案 | CDP 使用 |
|---|---|
| Puppeteer | 需下载 Chromium |
| Browser Harness | 直连已装 Chrome，轻量 |

---

## 相关实体

- [[Browser-Harness]]
- [[Puppeteer]]

## 相关概念

- [[CDP协议]]
- [[浏览器自动化]]