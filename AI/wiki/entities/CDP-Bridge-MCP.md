---
tags: [MCP, 浏览器工作流自动化, 开源项目]
sources:
  - Agent/Playwright拉爆了！请给你的Agent安装上真正的浏览器访问能力——CDP Bridge MCP.md
created: 2026-05-10
updated: 2026-05-10
---

# CDP Bridge MCP

CDP Bridge MCP 是三黄工作室开源的一个 MCP Server，通过配套的 Chromium 扩展桥接 MCP 客户端与真实浏览器会话，让大模型可以直接操作用户已登录的浏览器页面。

## 核心特点

- **复用真实登录态**：连接已打开、已登录的浏览器标签页，直接使用现有 Cookie、登录状态和页面上下文
- **页面内容优化**：browser_scan 过滤脚本、样式和不可见元素，保留对模型有用的正文和结构，减少 token 浪费
- **启动轻量**：`uvx cdp-bridge@latest` 即可启动，浏览器端加载扩展即可连接
- **7 个核心工具**：browser_get_tabs、browser_scan、browser_execute_js、browser_switch_tab、browser_navigate、browser_screenshot、browser_cookies

## 与 Playwright MCP 的区别

- [[Playwright]] MCP 适合可脚本化的自动化测试，新开浏览器实例
- CDP Bridge MCP 适合 LLM 在用户当前页面上做交互式任务，复用真实会话

## 支持的 MCP 客户端

- [[Claude-Code]]：`claude mcp add cdp-bridge uvx cdp-bridge@latest`
- [[Codex]]：`codex mcp add cdp-bridge uvx cdp-bridge@latest`
- opencode：在配置文件中添加

## 相关概念

- [[MCP协议]] — 作为 MCP Server 暴露工具
- [[浏览器自动化]] — 让大模型操作真实浏览器
- [[Agent架构]] — LLM 接管真实浏览器会话的架构模式
