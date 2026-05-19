---
title: HeyGen 开源 HyperFrames：HTML直出视频
type: source-summary
tags: [HeyGen, HyperFrames, 视频制作, AI编程, 开源]
sources: [../微信公众号/HeyGen/15K Star 一夜刷屏！HeyGen 开源 HyperFrames，让 AI 用 HTML 生成视频.md]
created: 2026-05-20
updated: 2026-05-20
---

# HeyGen 开源 HyperFrames：让AI用HTML生成视频

## 摘要

HeyGen开源了HyperFrames视频渲染框架（15K Star），将HTML代码直接渲染为MP4视频，定位为"AI智能体专用视频工具"。

## 核心要点

### 什么是HyperFrames
- 视频渲染引擎：将HTML网页动画一帧帧渲染为MP4
- 项目文件就是HTML本身
- 使用Tailwind CSS控制样式，GSAP/Lottie/Three.js做动画
- 一条命令渲染，无需GUI或时间轴操作

### AI智能体定制设计
- 打包完整的Skills专门给Claude Code、Cursor、Gemini CLI、Codex等AI编程智能体使用
- 提供的斜杠命令：
  - `/hyperframes` - 写画面
  - `/hyperframes-cli` - 预览和渲染流程
  - `/gsap` - 处理时间线动画
- 约束了Tailwind v4浏览器运行时写法、GSAP时间线结构、各动画库适配器

### 快速上手
```bash
# 安装skill
npx skills add heygen-com/hyperframes

# 初始化项目
npx hyperframes init my-video

# 渲染视频
npx hyperframes render
```

### 战略意义
- 视频生产从"人操作"向"AI自主完成"演进
- 未来场景：自动化运营智能体读取产品数据，直接生成适配不同尺寸的推广视频，渲染发布一气呵成
- HeyGen开源底层渲染能力，构建"AI视频工厂"生态

## 相关实体

- [[HeyGen]]
- [[HyperFrames]]
- [[Claude-Code]]
- [[Cursor]]
- [[Codex]]
- [[GSAP]]
- [[Tailwind]]

## 相关概念

- [[视频制作]]
- [[AI编程]]
- [[Skill开发]]
- [[html-ppt-skill]]

## 来源

- 公众号：MinimaxClaw
- 链接：https://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg1Nw==
- GitHub：https://github.com/heygen-com/hyperframes
