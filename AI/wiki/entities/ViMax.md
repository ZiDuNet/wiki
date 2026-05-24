---
title: ViMax
type: entity
tags: [视频生成, 多智能体协作, GitHub项目]
sources: [多智能体协作视频生成框架.md, 不要错过这10个本周火火火的-GitHub-开源项目.md]
created: 2026-05-24
updated: 2026-05-24
---

# ViMax

> GitHub: https://github.com/HKUDS/ViMax
> 协议: MIT | 语言: Python 3.12

## 简介

港大数据智能实验室（HKUDS）出品的多智能体视频生成框架，把视频制作拆成"剧组"角色协作。

## 四个 AI 角色

1. **Director（导演）** — RAG长脚本生成
2. **Screenwriter（编剧）** — 分镜设计
3. **Producer（制片）** — 多机位模拟
4. **Video Generator** — 并行镜头生成

## 三种模式

- **Idea2Video**: 灵感→完整视频
- **Novel2Video**: 小说→分集视频
- **Script2Video**: 剧本→无限长度视频

## 特色功能

- AutoCameo: 上传照片嵌入角色
- 智能参考图像选择
- 自动化一致性检查
- 支持 MiniMax M2.7（1M 上下文）

## 安装

```bash
git clone https://github.com/HKUDS/ViMax.git
cd ViMax && uv sync
```

## 关联概念

- [[多智能体协作视频生成]]
- [[RAG长脚本生成]]
- [[Idea2Video]]
- [[AutoCameo]]

## 来源文章

- [[多智能体协作视频生成框架]]