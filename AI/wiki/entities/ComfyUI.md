---
type: entity
name: ComfyUI
created: 2026-05-10
updated: 2026-05-11
mentions: 2
tags: [AI绘图, 工作流, 节点编辑器]
---

# ComfyUI

**类型:** 实体
**提及文章数:** 2

## 简介

ComfyUI 是一款开源的基于节点的 AI 图像/视频生成工作流编辑器。用户通过拖拽节点组合 Stable Diffusion、LoRA、ControlNet 等模型组件，构建可复用的图像生成 Pipeline。相比 WebUI（Automatic1111），ComfyUI 以更灵活的节点式架构著称，支持复杂的条件控制、批量生成和工作流导出。

在 Hermes 生态中，ComfyUI 通过 Skill 接入，支持 Agent 直接调用 ComfyUI 生成图像和视频，无需手动操作界面。

## 核心特性

- **节点式工作流**: 可视化拖拽搭建生成流程，支持条件分支、循环等逻辑
- **模型生态**: 支持 Stable Diffusion 1.5/SDXL/Flux、LoRA、ControlNet、IPAdapter 等
- **API 驱动**: 提供 HTTP API，可被外部程序（如 Hermes Agent）调用
- **轻量高效**: 比 WebUI 更省内存，支持队列化批量任务

## 相关概念

[[AI-Agent]], [[工作流自动化]], [[知识管理]], [[自动化测试]]

## 相关文章

- [[Hermes-开源了-ComfyUI-Skill以后出图出视频直接说就行了]]
- [[📦-安装到全局pip-install-e-gimpagentharness-🌍-随处可用clianythinggimp-helpclianythinggimp-]]
