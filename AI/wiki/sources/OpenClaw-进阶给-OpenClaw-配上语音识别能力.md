---
tags: [OpenClaw, Python, OpenAI]
source: "檀勤忠"
created: 2026-04-21
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw 进阶：给 OpenClaw 配上语音识别能力

> 来源: [檀勤忠](https://mp.weixin.qq.com/s?__biz=MzYyMzE2MzQ5MQ==&mid=2247484037&idx=1&sn=5dc2f16f6888549f0dbba688ec5d07d9&chksm=fe063845979fe2cc5ced6b2f0725f265f92386c7ccfa449783b485111ff283363241211672b0&mpshare=1&scene=1&srcid=0421G147jQDKfLG4jbk8QHqv&sharer_shareinfo=206156c758528f7ee88d88e34729d0d5&sharer_shareinfo_first=206156c758528f7ee88d88e34729d0d5) | 2026-04-21

## 摘要

OPENCLAW 进阶系列
让你的 AI 助手能听懂语音
基于 SenseVoice 的实时语音识别实战
今天，我们要更进一步 —— 让 AI 听懂 用户说的话。
本文将详细介绍如何集成 **SenseVoice**（阿里开源的多语言语音识别模型），为你的 OpenClaw 工作流添加语音识别能力。
一、ASR 项目选型对比
在选择语音识别方案之前，让我们对比五个主流的 ASR（自动语音识别）项目：
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 项目 | 厂商 | 开源 | 中文支持 | 实时性 |
| SenseVoice | 阿里 | 完全开源 | 极佳 | 实时 |
| Whisper | OpenAI | 开源 | 良好 | 较慢 |
| FunASR | 阿里 | 开源 | 极佳 | 实时 |
| DeepSpeech | Mozilla | 开源 | 一般 | 实时 |
| 讯飞语音 | 科大讯飞 | 商业 | 极佳 | 实时 |
为什么选 SenseVoice？
✓**多语言支持** — 支持中文、英文、粤语、日语、...

## 相关实体

[[OpenAI]], [[OpenClaw]], [[Python]]

## 相关概念


