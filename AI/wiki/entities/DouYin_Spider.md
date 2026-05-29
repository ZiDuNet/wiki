---
tags: [抖音, 爬虫, 开源项目, 数据采集]
sources: ["DouYin_Spider：抖音逆向与爬虫实战.md", "DouYin_Spider：一站式抖音数据采集与直播监听开源项目.md"]
created: 2026-05-29
updated: 2026-05-29
---

# DouYin_Spider

**类型:** 实体 — 开源项目
**GitHub:** https://github.com/cv-cat/DouYin_Spider
**维护者:** cv-cat
**技术栈:** Python + Node.js
**最近更新:** 2026-05-15

## 简介

抖音逆向与数据采集开源工具，封装抖音全部API接口，支持数据爬取、直播间监听、私信处理等功能。适合数据分析师、直播间运营、竞品分析、学术研究等场景。

## 核心功能

- 全部API接口封装：登录、用户信息、视频列表、评论
- 直播间实时监听：弹幕、礼物、点赞、进场、关注、房间热度
- 直播间互动：发送弹幕、点赞
- 用户信息采集：主页、作品列表、关注/粉丝列表
- 评论数据采集：含多级评论回复
- 关键词搜索：视频、用户、直播
- 私信处理：WebSocket实时接收、主动发送、会话管理
- 收藏/推荐流数据采集
- 逆向分析：参数构造、签名算法

## 部署方式

- **本地部署**: Python 3.7+ / Node.js 18+，pip install + npm install
- **Docker部署**: 提供Dockerfile，支持挂载数据目录
- **配置**: .env文件填写抖音Cookie（douyin.com + live.douyin.com）

## 数据输出

JSON / Excel / 媒体文件，结构化目录存储

## 相关概念

[[爬虫]], [[抖音]], [[MCP协议]], [[数据采集]]

## 相关文章

- [[DouYin_Spider：抖音逆向与爬虫实战]]
- [[DouYin_Spider：一站式抖音数据采集与直播监听开源项目]]
