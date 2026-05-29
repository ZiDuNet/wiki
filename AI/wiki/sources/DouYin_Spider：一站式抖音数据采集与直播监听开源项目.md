---
tags: [抖音, 爬虫, 部署, Docker, 直播间监听]
sources: ["DouYin_Spider：一站式抖音数据采集与直播监听开源项目.md"]
created: 2026-05-29
updated: 2026-05-29
---

# DouYin_Spider：一站式抖音数据采集与直播监听开源项目

**来源：** DouYin_Spider：一站式抖音数据采集与直播监听开源项目.md
**摄入日期：** 2026-05-29
**类型：** 部署指南

## 摘要

详细介绍 [[DouYin_Spider]]（cv-cat版）的部署方式，包括本地部署和Docker部署。涵盖功能特点、环境准备、依赖安装、.env配置、Cookie获取、直播间监听等。

## 核心内容

- 本地部署：Python 3.7+ / Node.js 18+，pip + npm/pnpm 安装依赖
- Docker部署：提供Dockerfile，docker build/run 一键运行
- Cookie配置：.env文件，分别配置 douyin.com 和 live.douyin.com 的Cookie
- 数据爬取入口：python main.py
- 直播间监听：python dy_live/server.py
- 功能覆盖：作品/用户/评论/搜索/直播间/私信/收藏/导出

## 提及实体

- [[DouYin_Spider]] — cv-cat 维护的抖音数据采集工具

## 涉及概念

- [[爬虫]] — 数据采集技术
- [[抖音]] — 目标平台
