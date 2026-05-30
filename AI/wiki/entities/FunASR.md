---
tags: [ASR, 语音识别, 阿里, 开源, FunAudio]
sources: [干掉 Whisper：我把 VoiceVault 迁移到 FunASR，本地转录加总结爽的飞起，已然是一枚离线录音加待办神器.md]
created: 2026-05-31
updated: 2026-05-31
type: entity
---

# FunASR

**类型:** 开源项目 / ASR 框架
**来源:** [[干掉 Whisper：VoiceVault 从 Whisper 迁移到 FunASR]]

## 简介

阿里达摩院开源的语音识别框架，提供 SenseVoice（多语言）和 Paraformer 模型系列，通过 sherpa-onnx 提供跨语言绑定（Python/C++/Rust/Go）和纯 ONNX 格式。

## 核心模型

| 模型 | 语言 | 特点 |
|------|------|------|
| SenseVoice | 中英日韩粤 | 多语言自动检测，内置标点 |
| Paraformer | 多语言 | 高精度，适合特定场景 |

## 关键优势（vs Whisper）

| 对比项 | Whisper base | FunASR SenseVoice int8 |
|--------|-------------|----------------------|
| 模型大小 | 141 MB | 229 MB（含5种语言）|
| 1分钟中文推理 | ~4s | **~1.2s** |
| 内置标点 | 无 | 有（ITN + CT-Transformer）|
| 内置 VAD | 无 | 有（Silero VAD）|
| 语种检测 | 需手动指定 | 自动检测 |

## 相关技术

- [[sherpa-onnx]] — 推理框架，提供 Rust 绑定
- [[VoiceVault]] — 使用 FunASR 作为后端的实际产品
- [[双后端架构]] — VoiceVault 用 trait object 切换 Whisper/FunASR

## 开源地址

https://github.com/modelscope/FunASR