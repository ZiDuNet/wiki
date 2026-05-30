---
tags: [AI, Skills, 视频分析, 本地工具链]
sources: [分享3个新发现的宝藏Skills.md]
created: 2026-05-31
updated: 2026-05-31
---

# claude-video

**类型:** 实体
**来源文章:** [[分享3个新发现的宝藏Skills]]

## 简介

让 Claude 能直接处理视频内容的 Skill 组合：yt-dlp + ffmpeg + Whisper + Claude 联合分析。

## 工作流程

```
yt-dlp 下载视频 → ffmpeg 抽帧 → Whisper 转文字 → Claude 分析
```

全部本地跑，不需要额外买 API。

## 支持规模

- 支持 1500+ 平台（YouTube、TikTok、B站等）
- 30分钟视频约2分钟分析完

## Claude 输出内容

- 哪几秒是重点
- 节奏怎么安排
- 视觉钩子在哪里

做竞品分析或内容拆解很省事。

## 相关工具

- [[yt-dlp]] — 视频下载工具
- [[ffmpeg]] — 音视频处理工具
- [[Whisper]] — OpenAI 开源语音识别模型