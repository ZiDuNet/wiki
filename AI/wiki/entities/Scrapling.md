---
title: Scrapling
type: entity
tags: [Python, 爬虫, Web-Scraping, 开源工具, GitHub]
sources: [Scrapling-自适应Web爬虫框架-绕Cloudflare-自适应解析-Spider.md]
created: 2026-05-22
updated: 2026-05-22
---

# Scrapling

**类型:** 工具/框架
**作者:** Karim Shoair (D4Vinci)
**GitHub:** [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
**协议:** BSD-3-Clause
**版本:** v0.4.8

## 简介

自适应 Web 爬虫框架，从单个请求到大规模爬取全搞定。解析器能学习网站变化并自动重新定位元素，内置反反爬能力可绕过 Cloudflare Turnstile。

## 核心能力

- **三种抓取模式:** Fetcher（纯HTTP）、DynamicFetcher（Playwright/JS渲染）、StealthyFetcher（反爬/绕CF）
- **自适应解析:** 网站改版后自动重新定位目标元素（auto_save + adaptive）
- **Spider 框架:** 类 Scrapy，支持并发、多 Session、暂停/恢复、自动代理轮换
- **MCP Server:** 配合 [[Claude]] / Cursor 等 AI 工具使用
- **CLI 命令行:** 不用写代码直接抓网页

## 性能

解析速度比 [[BeautifulSoup]] 快 700+ 倍，与 [[Parsel]]/[[Scrapy]] 持平。

## 相关实体

- [[Playwright]] — DynamicFetcher 的浏览器引擎
- [[Cloudflare]] — StealthyFetcher 可绕过其 Turnstile 验证
- [[MCP]] — Scrapling 内置 MCP Server
- [[Scrapy]] — Spider 模式的设计参考
- [[Python]] — 开发语言

## 相关概念

- [[Web Scraping]]
- [[反反爬虫]]
- [[浏览器自动化]]
