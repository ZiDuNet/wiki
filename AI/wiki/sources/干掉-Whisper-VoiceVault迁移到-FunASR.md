---
tags: [ASR, FunASR, Whisper, 语音识别, Rust, VoiceVault]
sources: [干掉 Whisper：我把 VoiceVault 迁移到 FunASR，本地转录加总结爽的飞起，已然是一枚离线录音加待办神器.md]
created: 2026-05-31
updated: 2026-05-31
type: source
---

# 干掉 Whisper：VoiceVault 从 Whisper 迁移到 FunASR

**来源：** 微信公众号/老码小张
**摄入日期：** 2026-05-31
**类型：** 技术文章

## 摘要

作者把 VoiceVault 的转录引擎从 Whisper 迁移到 FunASR（sherpa-onnx），中文识别速度提升 3 倍，模型文件更小，内置标点和 VAD。文章详细记录了迁移过程中的坑：GitHub Release 404、Tauri 白屏、trait object 生命周期、CSP 策略，以及双后端架构设计。

## 核心观点

- **FunASR 优势**：中文推理速度 ~1.2s/min（Whisper ~4s/min），内置标点恢复（CT-Transformer）、内置 VAD（Silero），支持中英日韩粤自动语言检测，零运行时依赖（静态链接）
- **架构演进**：用 trait object 抽象 TranscriptionBackend，迁移只改 ~50 行核心代码，实现 Whisper/FunASR 双后端切换
- **踩坑记录**：sherpa-onnx 模型不在版本号 tag 下，而在类型 tag（asr-models/punctuation-models）下；Silero VAD 是单个 .onnx 文件而非压缩包
- **核心经验**：好的架构是演进出来的，不是预测出来的；不要相信 README 里的下载 URL，用 curl -sI 验证每个 URL

## 涉及实体

- [[VoiceVault]] — 开源离线录音加待办工具
- [[FunASR]] — 阿里达摩院 ASR 框架（SenseVoice/Paraformer）
- [[sherpa-onnx]] — Daniel Povey（Kaldi 之父）团队的推理框架
- [[Whisper]] — OpenAI 语音识别模型

## 涉及概念

- [[双后端架构]] — trait object 抽象实现后端切换
- [[流式转录]] — VAD 分段 + 实时 partial
- [[ONNX 推理]] — 跨平台推理格式
- [[架构演进]] — Phase 1 做 MVP，第五次迭代刚好做重构