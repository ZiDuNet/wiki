---
title: "skill自动生成宣传效果图片和可以编辑的ppt"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["skill自动生成宣传效果图片和可以编辑的ppt.md"]
tags: [PPT, AI生成, 设计, 自动化]
---

## Summary

文章介绍如何用 AI Skill 自动生成可编辑的 PPT 和宣传图片。使用 Nano Banana（基于 openrouter 调用 Gemini）生成图片素材；使用 PPT Master 从 .pptx 文件复刻模板（提取主题色、字体、母版/版式结构）并生成可编辑 PPT。相比 NotebookLM 生成不可编辑 PDF 的方案，PPT Master 方案允许用户通过 AI 对话不断修改直到满意，然后保存为私人模板库。

## Key Claims

1. **模板复刻（PPT Master）**：通过 `/create-template` 命令将任意 .pptx 文件复刻成可调用的页面布局，提取主题色、字体、母版/版式结构、复用图片、精灵图裁剪关系；支持公司品牌 deck、客户中标模板等一键变私人模板。
2. **多种风格预置**：官方预置多种风格（年报 / 咨询 / 答辩 / 政府汇报），用户可直接指定风格让 AI 生成。
3. **多源内容生成**：支持从 PDF、DOCX、图片等文件生成 PPT；也支持直接粘贴文字内容生成。
4. **图片生成（Nano Banana）**：使用 openrouter 调用 Nano Banana 生成 ppt 的图片素材，支持换风格、换布局（杂志风格等）。

## Entities Mentioned

- [[PPT Master]] — 模板复刻式 AI PPT 生成 Skill
- [[Nano Banana]] — 基于 openrouter + Gemini 的图片生成工具

## Concepts

- [[PPT制作]] — 使用 AI 辅助生成可编辑 PPT 的工作方式
- [[设计系统]] — 主题色、字体、版式等视觉规范的集合

## Notable Quotes

> "有什么不满意的可以让AI不断修改，而不是黑盒，生成什么就用什么了。"

## Limitations / Bias

- 文章内容较为操作导向，缺少系统性理论框架