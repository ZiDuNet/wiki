---
title: supertonic
type: entity
tags: [TTS, 端侧推理, GitHub项目]
sources: [闪电般快速的端侧离线TTS.md, 不要错过这10个本周火火火的-GitHub-开源项目.md]
created: 2026-05-24
updated: 2026-05-24
---

# supertonic

> GitHub: https://github.com/supertone-inc/supertonic
> 协议: OpenRAIL-M (模型) / MIT (代码)

## 简介

约 99M 参数的端侧文本转语音系统，基于 ONNX Runtime 完全离线运行，CPU 上即可快速推理。

## 核心特性

- 31 种语言支持
- 完全离线运行
- 约 99M 参数，轻量高效
- Expression Tags 情感控制（`<laugh>`、`<breath>`、`<sigh>`）

## SDK 支持

11 个平台 SDK：
- C++、Node.js、Python、Rust、Java、Go
- Swift、C#、Flutter、iOS、Web (WebGPU/WASM)

## 安装

```bash
pip install supertonic
```

## 关联概念

- [[端侧推理]]
- [[离线TTS]]
- [[ONNX Runtime]]
- [[Expression Tags]]

## 来源文章

- [[闪电般快速的端侧离线TTS]]