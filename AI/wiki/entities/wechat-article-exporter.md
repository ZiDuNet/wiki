---
tags: [开源项目, 微信公众号, 文章下载]
sources: [GitHub/wechat-article-exporter.md]
created: 2026-05-26
updated: 2026-05-26
---

# wechat-article-exporter

开源的微信公众号文章批量下载工具。

## 基本信息

- **GitHub:** https://github.com/wechat-article/wechat-article-exporter
- **在线使用:** https://down.mptext.top
- **文档站:** https://docs.mptext.top
- **许可证:** MIT
- **技术栈:** Nuxt 3 + Vue 3 + TypeScript + Tailwind CSS

## 核心能力

- 搜索公众号（关键字搜索）
- 6 种导出格式：HTML / JSON / Excel / TXT / MD / DOCX
- HTML 格式100%还原文章排版与样式
- 缓存文章列表，减少接口请求
- 文章过滤：作者、标题、发布时间、原创标识、所属合集
- 合集下载、图片分享消息、视频分享消息
- 导出评论、评论回复、阅读量、转发量（需抓包 credentials）
- 开放 API 接口

## 工作原理

利用公众号后台写文章时"搜索其他公众号文章"的功能，实现抓取指定公众号所有文章。

## 部署方式

- **在线：** 直接访问 down.mptext.top
- **Docker：** `docker run -d -p 3000:3000 wechat-article/wechat-article-exporter`
- **Cloudflare：** 支持部署到 Cloudflare Workers

## 技术架构

- `components/` — Vue 组件（dashboard、grid、preview、search、setting）
- `composables/` — 组合式函数（批量下载、导出、登录、偏好设置）
- `server/` — Nuxt 服务端 API（代理请求、Cookie 存储）
- `store/v2/` — 文章、资源、评论、HTML 数据存储
- `utils/download/` — 下载器核心（BaseDownloader、Exporter、ProxyManager）

## 关联

- [[微信公众号文章抓取]] — 该工具的核心使用场景
- [[文章格式还原]] — HTML 格式100%还原能力
