---
title: "skill自动生成宣传效果图片和可以编辑的ppt"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["skill自动生成宣传效果图片和可以编辑的ppt_1.md"]
tags: [PPT, Skill, 图片生成, PPT-Master, Nano-Banana]
---

## Summary

文章介绍如何使用 AI Skill 自动生成宣传效果图片和可编辑 PPT。重点工具为 PPT Master（`/create-template` 复刻任意 .pptx 为模板、Nano Banana 生成图片素材）。核心能力：把任意喜欢的 .pptx 丢给 AI → 一句命令复刻成可编辑模板 → 用 /create-template 保存新模板；使用 openrouter 调用 Nano Banana 生成图片素材注入 PPT。

## Key Claims

1. **模板复刻**：`/create-template` 可将任意 .pptx（公司品牌 deck、客户中标模板）还原为可编辑模板，包含主题色、字体、母版结构、图片裁剪关系
2. **风格灵活切换**：同一内容可换多种风格（科技感、杂志风等），AI 持续修改而非黑盒生成
3. **图片素材生成**：使用 openrouter 调用 Nano Banana 生成 PPT 配图，支持换风格换布局
4. **非 Notion 版本**：直接生成可编辑 PPTX，不依赖 NotebookLM PDF 转 PPT 的会员流程

## Entities Mentioned

- [[PPT Master]]（PPT 生成 Skill）
- [[Nano Banana]]（图片生成工具）

## Concepts

- [[Skill管理]] — PPT 模板复刻的 Skill 化工作流
- [[Prompt管理]] — 图片素材的 AI 生成提示词

## Notable Quotes

> "有什么不满意的可以让 AI 不断修改，而不是黑盒，生成什么就用什么了。"

## Limitations

- 文章较短，属于工具使用心得分享，缺乏系统对比
- 依赖 openrouter API 和 PPT Master 工具可用性
