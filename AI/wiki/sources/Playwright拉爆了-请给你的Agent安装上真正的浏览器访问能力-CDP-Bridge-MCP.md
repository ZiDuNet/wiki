---
tags: [Agent, MCP, 浏览器自动化, CDP]
sources: [Agent/Playwright拉爆了！请给你的Agent安装上真正的浏览器访问能力——CDP Bridge MCP.md]
created: 2026-05-10
updated: 2026-05-10
---

# Playwright拉爆了！请给你的Agent安装上真正的浏览器访问能力——CDP Bridge MCP

**Source:** Agent/Playwright拉爆了！请给你的Agent安装上真正的浏览器访问能力——CDP Bridge MCP.md
**Date ingested:** 2026-05-10
**Type:** article

## Summary

三黄工作室开源的 [[CDP-Bridge-MCP]] 项目，通过 Chromium 扩展桥接 MCP 客户端与真实浏览器会话，让大模型可以直接操作用户已登录的浏览器页面。与 [[Playwright]] MCP 和 Chrome DevTools MCP 不同，它连接的是真实浏览器会话而非新开实例，可以复用登录态、Cookie 和页面状态。

## Key Claims

- Playwright MCP 和 Chrome DevTools MCP 偏向自动化测试和新开浏览器实例，CDP Bridge MCP 则让 LLM 直接接管正在使用的真实浏览器
- 核心优势：复用真实登录态、适合日常浏览器协作、页面内容更适合 LLM 消费、启动链路轻量
- browser_scan 对页面 HTML 做简化，过滤脚本样式和不可见元素，减少 token 浪费
- 支持 browser_get_tabs、browser_scan、browser_execute_js、browser_switch_tab、browser_navigate、browser_screenshot、browser_cookies 共 7 个工具
- 安装方式：加载 Chromium 扩展 + MCP 客户端配置 `uvx cdp-bridge@latest`
- 支持 [[Claude-Code]]、[[Codex]]、opencode 等 MCP 客户端

## Entities Mentioned

- [[Playwright]] — 对比对象，偏向自动化测试的新开浏览器实例
- [[Claude-Code]] — 支持的 MCP 客户端之一
- [[Codex]] — 支持的 MCP 客户端之一
- [[MCP]] — 核心协议，CDP Bridge MCP 是一个 MCP Server

## Concepts Covered

- [[浏览器自动化]] — 让大模型操作真实浏览器页面
- [[MCP协议]] — CDP Bridge 作为 MCP Server 暴露工具
- [[Agent架构]] — LLM 直接接管真实浏览器会话的架构模式
- [[企业落地]] — 复用真实登录态，适合企业内部已登录的 Web 应用
