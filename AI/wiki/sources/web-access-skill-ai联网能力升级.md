---
title: AI联网能力升级：web-access Skill解决了什么问题
type: source-summary
tags: [Claude, Skill, 浏览器自动化, 联网能力]
sources: [../微信公众号/Claude/AI联网能力升级：这个Skill解决了什么问题.md]
created: 2026-05-16
updated: 2026-05-16
---

# AI联网能力升级：web-access Skill解决了什么问题

## 核心摘要

Claude Code 自带的 WebSearch 和 WebFetch 在面对微信公众号、小红书等反爬严格的平台时直接歇菜——WebSearch 只能拿搜索摘要，WebFetch 无法读取需要登录态的内容，Playwright/Chrome DevTools MCP 配置复杂。**web-access skill** 通过直连用户日常 Chrome 浏览器（带着真实登录态）的方式，让 Agent 能够访问任何"人能看的"页面。

## 关键设计思想

### 1. 浏览哲学而非固定步骤
不写死"第一步搜索、第二步打开"的固定流程，而是教 Agent 像人一样思考：先定义成功标准 → 选最可能直达的方式验证 → 过程中根据反馈实时调整 → 遇到反爬平台直接上浏览器。这个设计解决了"模型一条道走到黑"的问题——让它知道何时该换路径。

### 2. 子 Agent 并行分治
10 个子 Agent 共享同一个 Chrome，各自开后台 tab 互不干扰。主 Agent 只收汇总结果，避免上下文污染。这解决了 Agent 调研多平台时上下文被撑爆的问题。

### 3. 站点经验自动沉淀
首次访问摸索后，操作经验（URL 结构、反爬特征、有效策略）自动记录。下次再访问直接复用，效率提升肉眼可见。

### 4. 不抢浏览器控制权
所有操作在后台 tab 进行，用户正常工作的同时 Agent 默默干活。

## 与自带工具的对比

| 维度 | WebSearch | WebFetch | web-access |
|---|---|---|---|
| 摘要 vs 原文 | 摘要 | 原文（但受限） | 原文（完整登录态）|
| 反爬平台 | 无法处理 | 歇菜 | 直接上浏览器 |
| 上下文污染 | 高 | 中 | 低（子 Agent 分治）|
| 站点经验积累 | 无 | 无 | 有 |

## 安装配置

- Chrome 地址栏输入 `chrome://version`，检查"命令行"是否有 `--remote-debugging-port=9222`
- Mac: `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
- Windows: Chrome 快捷方式目标加 `--remote-debugging-port=9222`
- 安装：`git clone` 地址丢给 Agent 它自己装

## 使用建议

1. **明确告诉 AI 去哪个平台**：不要说"调研一下"，要说"去小红书、微博、知乎上调研"
2. **给 AI 足够时间**：浏览器操作比 API 慢，耐心等
3. **检查登录态**：AI 用你的登录态访问，你没登录它也访问不了

## 相关工具

- [[Claude]] — Agent 载体
- [[浏览器自动化]] — 相关概念
- [[MCP协议]] — 工具调用标准化

## 相关实体

- [[web-access]] — Skill 本身
