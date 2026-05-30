---
tags: [AI, 工具链, 本地部署, 隐私]
sources: [分享3个新发现的宝藏Skills.md]
created: 2026-05-31
updated: 2026-05-31
---

# 本地AI工具链

**类型:** 概念
**来源文章:** [[分享3个新发现的宝藏Skills]]

## 核心定义

不依赖云服务 API，全部本地跑的 AI 工具组合。典型案例是 claude-video 流程：yt-dlp + ffmpeg + Whisper + Claude 分析，全部本地执行，不需要付费 API。

## 核心优势

- **隐私可控**：视频/音频不上传到第三方
- **成本为零**：无需 API 费用
- **可离线运行**：不依赖网络连接

## 典型案例

### claude-video 工具链

```
yt-dlp 下载视频 → ffmpeg 抽帧 → Whisper 转文字 → Claude 分析
```

- 支持 1500+ 平台
- 30分钟视频约2分钟分析完
- 全部本地跑，不需要额外买 API

## 相关实体

- [[claude-video]] — 视频内容分析工具链
- [[Whisper]] — OpenAI 开源语音识别模型
- [[ffmpeg]] — 音视频处理工具
- [[yt-dlp]] — 视频下载工具