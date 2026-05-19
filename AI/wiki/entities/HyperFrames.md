---
title: HyperFrames
type: entity
tags: [视频渲染, 开源, GitHub, AI工具]
sources: [../微信公众号/HeyGen/15K Star 一夜刷屏！HeyGen 开源 HyperFrames，让 AI 用 HTML 生成视频.md]
created: 2026-05-20
updated: 2026-05-20
mentions: 1
---

# HyperFrames

**类型:** 实体（开源项目）
**提及文章数:** 1

## 简介

HyperFrames是HeyGen开源的视频渲染框架（15K Star），将HTML代码直接渲染为MP4视频，定位为AI智能体专用视频工具。

## 核心能力

- **输入**: HTML + CSS动画代码
- **输出**: MP4视频文件
- **特点**: 无需GUI，命令行即可完成渲染

## 技术栈

- HTML作为项目文件格式
- Tailwind CSS v4（浏览器运行时写法）
- GSAP（时间线动画）
- Lottie（矢量动画）
- Three.js（3D动画）

## AI智能体集成

提供Skills供以下AI编程工具使用：
- Claude Code
- Cursor
- Gemini CLI
- Codex

### 斜杠命令
- `/hyperframes` - 写画面
- `/hyperframes-cli` - 预览和渲染流程
- `/gsap` - 处理时间线动画

## 安装使用

```bash
# 安装skill
npx skills add heygen-com/hyperframes

# 初始化项目
npx hyperframes init my-video

# 渲染视频
npx hyperframes render
```

## 相关实体

- [[HeyGen]]
- [[Claude-Code]]
- [[Cursor]]
- [[Codex]]
- [[GSAP]]
- [[Tailwind]]

## 相关概念

- [[视频制作]]
- [[AI编程]]
