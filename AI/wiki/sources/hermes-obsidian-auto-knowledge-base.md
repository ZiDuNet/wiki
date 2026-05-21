---
title: Hermes+Obsidian自动化知识库
type: source-summary
tags: [Hermes, Obsidian, LLM Wiki, 知识库, BrowserOS, Web Clipper, 自动化]
sources: [收藏 200 篇文章后，我用Hermes+Obsidian搭了一套自动化个人知识库.md]
created: 2026-05-22
updated: 2026-05-22
---

# Hermes+Obsidian自动化知识库

## 核心观点

> 知识不是收藏出来的，是消化出来的。

浏览器书签和微信收藏夹堆积的文章永远不会被阅读。需要的是一个能替你读、替你整理、替你关联知识的系统。

## 整体架构

两条入库路径：
1. **手动摘录**：Obsidian Web Clipper 一键保存文章
2. **自动采集**：BrowserOS 定时抓取关心的资讯

两条路汇到同一个知识库，全流程无人值守。

## 用 Profile 切分独立的 librarian

避免"Agent分裂症"——让写代码的 Hermes 同时管知识库会干扰代码重构。

```bash
hermes profile create librarian
```

配置要点：
- 设置 `WIKI_PATH` 环境变量
- 在 `SOUL.md` 写死职责边界："你是知识库管理员"
- 模型选 DeepSeek-V4-Flash（成本低够用）

切换命令：`librarian chat`

## Obsidian Web Clipper 入库

### 配置三步

1. Obsidian 安装 Web Clipper 插件
2. 浏览器安装扩展（Chrome/Firefox/Safari）
3. 设置保存路径为 `clippers/`

### 特点

- 文件自带 frontmatter（source_url、title、clipped 日期）
- 与 [[LLM Wiki]] 的 raw frontmatter 规范兼容
- 一键保存，无需选目录、填标签

## BrowserOS 定时采集

### 为什么不是爬虫？

- Hacker News 评论需点击展开
- GitHub Trending 需登录看个性化推荐
- 技术博客可能有 Cloudflare 挑战

BrowserOS 是完整 Chromium 浏览器，内置 Agent 能力，处理登录态、JS 渲染、验证码。

### 定时任务示例

| 任务 | 频率 | 采集内容 |
|------|------|----------|
| Hacker News Top 5 | 每天 8:00 | 标题+链接+评分+热门评论摘要 |
| GitHub Trending | 每天 9:00 | 项目名+Star数+描述 |
| 技术博客更新 | 每 12 小时 | 新文章标题+摘要+链接 |
| 行业研报 | 每周一 | 标题+核心观点摘要 |

## 定时 ingest 到知识库

### 设计思路

`clippers/` 是待处理队列，`raw/` 是已入库存档。

- **边界清晰**：中间缓冲区，ingest 出错原文不丢
- **幂等安全**：llm-wiki 的 sha256 机制跳过已处理文件

### 运行效果

每 5 分钟自动检查 `clippers/`，一篇源文章触发 2-5 个 wiki 页面创建或更新——[[LLM Wiki]] 的复利效应。

## 实际效果对比

| 以前 | 现在 |
|------|------|
| 存书签 → 不看 → 搜索 → 读10篇 → 整理2小时 | 点Clipper → 5分钟入库 → 问librarian得综合答案 |

## 来源

- 公众号：专业造轮子
- 原文：[收藏 200 篇文章后，我用Hermes+Obsidian搭了一套自动化个人知识库](https://mp.weixin.qq.com/s?__biz=MzI0OTg0NTk0MA==&mid=2247484283)
- 相关概念：[[Hermes]]、[[Obsidian]]、[[LLM Wiki]]、[[BrowserOS]]、[[Web Clipper]]