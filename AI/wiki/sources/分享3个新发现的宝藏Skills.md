---
tags: [AI, Skills, GitHub, 视频生成, 项目架构, AI编程]
sources: [分享3个新发现的宝藏Skills.md]
created: 2026-05-31
updated: 2026-05-31
---

# 分享3个新发现的宝藏Skills

**来源：** 微信公众号/Skills/分享3个新发现的宝藏Skills.md
**作者：** Ai扫街笔记
**摄入日期：** 2026-05-31
**类型：** 文章
**分类：** Skills

## 摘要

本文分享了3个 GitHub 上的宝藏 AI Skills，覆盖视频生成、项目架构审查和视频内容分析，帮助独立开发者和 AI 编程用户提效。

## 核心观点

1. **Higgsfield AI Skills**：AI 视频生成一键搞定，Marketing Studio + Virality Predictor + Soul + product-photoshoot 四个工具，Claude Code/Cursor 用户友好安装，10分钟出片
2. **advise-project-approach**：项目启动前先跑一遍，对比真实案例告诉你哪些坑可以避开，适合独立开发者选技术栈、项目中期架构审查、上线前最后一轮检查
3. **claude-video系列**：让 Claude 能"看"视频，yt-dlp → ffmpeg → Whisper → Claude 分析，1500+ 平台支持，30分钟视频2分钟分析完

## 涉及实体

- [[Higgsfield-AI]] — AI 图像和视频生成平台，提供 Marketing Studio、Virality Predictor、soul、product-photoshoot 等 Skills
- [[advise-project-approach]] — 项目启动与架构审查 Skill，帮助独立开发者避免技术选型坑
- [[claude-video]] — 视频内容分析 Skill 组合：yt-dlp + ffmpeg + Whisper + Claude 本地分析
- [[npx-skills]] — Skills 安装工具（npx skills add）
- [[Whisper]] — OpenAI 开源语音识别模型
- [[ffmpeg]] — 音视频处理工具
- [[yt-dlp]] — 视频下载工具，支持 1500+ 平台

## 涉及概念

- [[AI视频生成]] — 用 AI 生成营销视频、产品展示图的工作流
- [[项目架构审查]] — 在项目启动和中期进行技术选型与架构合理性评估
- [[视频内容分析]] — 用 AI 分析视频结构、重点、节奏、视觉钩子
- [[本地AI工具链]] — 不依赖云服务 API，全部本地跑的工具组合

## 详细内容

### Higgsfield AI Skills（01）

Higgsfield AI 用于图像和视频生成，这套 Skill 把能力打包成实用工具：

- **Marketing Studio**：营销素材自动生成
- **Virality Predictor**：爆款预测
- **Soul**：角色一致性保持
- **Product Photoshoot**：产品摄影

安装命令：`npx skills add higgsfield-ai/skills`

做营销视频或产品展示图能省大量时间，30秒产品介绍视频从半天缩短到10分钟。

### advise-project-approach（02）

项目启动前跑一遍，拿项目对比真实案例和文档，告诉你哪些坑可以避开。

典型场景：
- 独立开发者选技术栈（如 solo app 硬上 Kafka 的坑）
- 项目中期架构审查
- 上线前的最后一轮检查

相当于有个资深工程师帮你把关，避免走弯路。

### claude-video 系列（03）

让 Claude 能直接处理视频内容，完整流程：

```
yt-dlp 下载视频 → ffmpeg 抽帧 → Whisper 转文字 → Claude 分析
```

全部本地跑，不需要额外买 API。支持 1500+ 平台（YouTube、TikTok、B站等），30分钟视频2分钟分析完。

Claude 输出：
- 哪几秒是重点
- 节奏怎么安排
- 视觉钩子在哪里

做竞品分析或内容拆解很省事。