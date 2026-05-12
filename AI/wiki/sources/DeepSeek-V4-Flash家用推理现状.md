---
tags: [DeepSeek, 推理, 硬件, RTX5090]
sources: [DGX Spark/5090/【DGX Spark_5090】检索了家用Deepseek v4推理现状，然后继续我们的学习.md]
created: 2026-05-11
updated: 2026-05-11
---

# DeepSeek V4 Flash 家用推理现状

**Source:** DGX Spark/5090/【DGX Spark_5090】检索了家用Deepseek v4推理现状，然后继续我们的学习.md
**Date ingested:** 2026-05-11
**Type:** article

## Summary

截至 2026 年 5 月，DeepSeek V4 Flash（280B MoE）在消费级 Blackwell 硬件（RTX 5090 / DGX Spark）上的推理支持现状：框架层面 vLLM/SGLang 已 Day-0 支持，但 sm_120/121 kernel 兼容性不足。llama.cpp 尚未支持 V4 Flash。KTransformers 提供 CPU/GPU 混合方案。

## Key Claims

- vLLM Day-0 支持但 NVFP4 kernel 有 bug，社区 fork jasl 提供 sm_121 兼容
- SGLang 同样 Day-0 支持但 sm_120 支持严重不足
- KTransformers shared expert 放 GPU、routed expert offload 到 CPU，但 AMX 加速仅 x86
- llama.cpp 尚未支持 V4 Flash

## Entities Mentioned

- [[DeepSeek]] — V4 Flash 模型（280B MoE）

## Concepts Covered

- [[MoE]] — Mixture of Experts 架构
- [[模型推理]] — 消费级硬件推理优化
