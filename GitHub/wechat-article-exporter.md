# wechat-article-exporter

> 微信公众号文章批量下载工具

GitHub: https://github.com/wechat-article/wechat-article-exporter

在线使用: https://down.mptext.top

文档站: https://docs.mptext.top

## 简介

一款在线的微信公众号文章批量下载工具，支持导出阅读量与评论数据，无需搭建任何环境，可通过在线网站使用，同时也支持 docker 私有化部署和 Cloudflare 部署。

支持下载各种文件格式，其中 HTML 格式可100%还原文章排版与样式。

## 核心特性

- 搜索公众号，支持关键字搜索
- 导出格式：html / json / excel / txt / md / docx（HTML 格式打包图片和样式文件，100%还原文章样式）
- 缓存文章列表数据，减少接口请求次数
- 文章过滤：作者、标题、发布时间、原创标识、所属合集
- 合集下载
- 图片分享消息、视频分享消息
- 导出评论、评论回复、阅读量、转发量等数据（需抓包获取 credentials）
- Docker 部署
- Cloudflare 部署
- 开放 API 接口

## 原理

利用公众号后台写文章时支持搜索其他公众号文章的功能，实现抓取指定公众号所有文章的目的。

## 技术栈

Nuxt 3 + Vue 3 + TypeScript + Tailwind CSS

关键目录结构：

- components/ — Vue 组件（dashboard、grid、preview、search、setting 等）
- composables/ — Vue 组合式函数（批量下载、导出、登录、偏好设置等）
- server/ — Nuxt 服务端 API（代理请求、Cookie 存储等）
- store/v2/ — 文章、资源、评论、HTML 等数据存储
- utils/download/ — 下载器核心（BaseDownloader、Exporter、ProxyManager）
- shared/utils/ — HTML 渲染、请求工具

## 部署方式

### 在线使用
直接访问 https://down.mptext.top

### Docker 部署
```bash
docker run -d -p 3000:3000 wechat-article/wechat-article-exporter
```

### Cloudflare 部署
支持部署到 Cloudflare Workers。

## 许可证

MIT
