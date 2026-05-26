---
tags: [微信公众号, 文章下载, 批量导出, 开源工具]
sources: [GitHub/wechat-article-exporter.md]
created: 2026-05-26
updated: 2026-05-26
---

# wechat-article-exporter

**来源：** GitHub/wechat-article-exporter.md
**摄入日期：** 2026-05-26
**类型：** 开源项目

## 摘要

一款在线的微信公众号文章批量下载工具，支持导出阅读量与评论数据。无需搭建环境，可通过在线网站使用，也支持 Docker 和 Cloudflare 部署。HTML 格式可100%还原文章排版与样式。

## 核心观点

- 利用公众号后台"搜索其他公众号文章"接口实现全量抓取
- 支持 6 种导出格式（HTML/JSON/Excel/TXT/MD/DOCX），HTML 格式100%还原样式
- 支持导出评论、阅读量、转发量等互动数据（需抓包 credentials）
- 三种部署方式：在线 / Docker / Cloudflare Workers
- Nuxt 3 + Vue 3 + TypeScript 技术栈，开放 API 接口

## 提及实体

- [[wechat-article-exporter]] — 微信公众号文章批量下载开源工具
- [[Nuxt-3]] — Vue.js 全栈框架
- [[Cloudflare-Workers]] — 边缘计算托管平台

## 涉及概念

- [[微信公众号文章抓取]] — 利用公众号后台接口批量获取文章
- [[文章格式还原]] — HTML 打包图片和样式文件，100%还原原始排版
