---
tags: [ASR, Rust, 开源, 离线工具, 语音转文字]
sources: [干掉 Whisper：我把 VoiceVault 迁移到 FunASR，本地转录加总结爽的飞起，已然是一枚离线录音加待办神器.md]
created: 2026-05-31
updated: 2026-05-31
type: entity
---

# VoiceVault

**类型:** 开源项目 / 桌面应用
**来源:** [[干掉 Whisper：VoiceVault 从 Whisper 迁移到 FunASR]]

## 简介

Rust + Tauri 开发的离线录音加待办工具，支持实时流式字幕、全文搜索、LLM 行动项提取。13MB 二进制，全部离线开源。

## 技术架构

- **前端**：Tauri（Rust 后端 + WebView）
- **转录引擎**：双后端架构（Whisper / FunASR 可切换），通过 `TranscriptionBackend` trait 抽象
- **流式转录**：VAD 检测静音边界 → 定时发 partial 预览 → 超时强制 commit → 音频归一化 → 事件分发

## 迁移到 FunASR 的效果

| 指标 | Whisper (base) | FunASR (SenseVoice int8) |
|------|----------------|-------------------------|
| 模型下载 | 141 MB | 305 MB（+标点+VAD）|
| 1分钟中文推理 | ~4s | ~1.2s |
| 标点 | 无 | 自动恢复 |
| 首次启动速度 | 800ms | 200ms |

## 相关

- [[FunASR]] — 当前使用的后端
- [[Whisper]] — 原后端
- [[双后端架构]] — 架构设计模式

## 开源地址

https://github.com/coder-brzhang/voicevault