---
tags: [Agent, Agent路由, Claude, Gateway, Hermes Agent, MCP, OpenClaw, Skill]
sources: ['微信公众号/OpenClaw/OpenClaw & Hermes 深度使用（一）—— 部署 Hermes.md']
created: 2026-05-10
updated: 2026-05-10
---

# OpenClaw & Hermes 深度使用（一）—— 部署 Hermes

**Source:** OpenClaw 公众号文章
**Category:** OpenClaw
**Date ingested:** 2026-05-10
**Type:** article

## Summary

> 📎 来源: 规则变量 | 时间: 2026-04-21 09:34 最近被Hermes刷屏了，很多文章和视频都在拿Hermes和OpenClaw做对比，为了吸引眼球多数文章都是踩OpenClaw，捧Hermes。这种AI注水文章的同质化很高，只讲“概念”，不展示实际使用场景。咱作为OpenClaw深度用户，从今天开始我将并行使用这个项目，后续将以「OpenClaw & Hermes 深度使用」作为系列文章，分享我对Hermes的使用过程和“踩坑”记录，同时将深入对比Hermes和OpenClaw两者架构、性能、适用场景。 本着“有图有真相”的原则，先贴出我正在使用的Hermes环境，这绝对...

## Key Claims

- 依赖：大量 Linux 原生库（某些在 Windows 上编译困难）
- 设计目标：跨平台（Linux/macOS 优先，Windows 通过 WSL2 支持）
- 依赖兼容性 — Hermes 依赖的某些 Python 包（如语音处理、向量数据库）在 Linux 上维护最好
- 部署一致性 — 服务器环境通常是 Linux，开发环境用 WSL2 可以减少"在我机器上能跑"的问题
- 开发效率 — Nous Research 团队主要用 Linux/macOS，优先优化这些平台

## Entities Mentioned

- [[Claude]]
- [[Claude-Code]]
- [[GitHub]]
- [[Hermes-Agent]]
- [[MCP]]
- [[OpenClaw]]
- [[Telegram]]
- [[飞书]]

## Concepts Covered

- [[Agent路由]]
- [[Skill开发]]
- [[Token优化]]
- [[本地部署]]
- [[视频制作]]
- [[记忆系统]]

## Related Sources

- [[OpenClaw文章索引]]
