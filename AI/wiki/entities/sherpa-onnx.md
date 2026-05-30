---
tags: [ASR, Rust, 推理框架, Kaldi, 开源]
sources: [干掉 Whisper：我把 VoiceVault 迁移到 FunASR，本地转录加总结爽的飞起，已然是一枚离线录音加待办神器.md]
created: 2026-05-31
updated: 2026-05-31
type: entity
---

# sherpa-onnx

**类型:** 开源项目 / 推理框架
**来源:** [[干掉 Whisper：VoiceVault 从 Whisper 迁移到 FunASR]]

## 简介

Daniel Povey（Kaldi 之父）团队的推理框架，把 FunASR 系列模型（SenseVoice、Paraformer）打包成纯 ONNX，提供 C API + 多语言绑定（Python/C++/Rust/Go）。

## 核心优势

- **静态链接**：Rust crate 直接 `cargo add sherpa-onnx --features static`，零运行时依赖
- **多后端**：CPU / GPU / NNAPI / CoreML
- **模型生态丰富**：SenseVoice / Paraformer / Zipformer / Silero VAD / CT-Transformer 标点

## 使用注意

模型不在版本号 tag（v1.12.39 等）下，而是在类型 tag 下：
- `asr-models` — SenseVoice / Paraformer 模型
- `punctuation-models` — 标点恢复模型
- `silero_vad` — 单个 .onnx 文件（200KB），不是压缩包

## 相关

- [[FunASR]] — 提供的模型系列
- [[VoiceVault]] — 使用 sherpa-onnx Rust binding 的实际产品