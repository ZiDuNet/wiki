---
title: ai-gameplay-pack-skill
type: entity
created: 2026-05-14
updated: 2026-05-14
sources: ["Skill结合哩布哩布LibTV，轻松做出AI实机视频！.md"]
tags: [Skill, AI游戏, 视频生成, 提示词工程]
---

# ai-gameplay-pack-skill

**类型:** 实体/Skill
**来源:** [[Skill结合LibTV-轻松做出AI实机视频]]

## 简介

ai-gameplay-pack 是一个 AI Agent Skill，用于生成游戏实机效果视频的完整提示词包。用户只需提供角色描述和风格要求，Skill 自动输出包含角色四视图、UI规范、6-12个镜头提示词的完整文档。

## 核心设计原则

1. **角色一致性**：游戏角色不会飘，保持整体一致性
2. **UI/HUD 一致性**：界面元素在所有镜头中保持统一
3. **提示词配对**：每个镜头使用「图片提示词 + 视频提示词」的清晰配对

## 版本

| 版本 | 用途 | 特点 |
|------|------|------|
| 轻量版（lite） | 聚焦提示词 | 节省 token |
| 完整版 | 详细提示词 | 包含角色锚点、UI规范、时间轴、字幕脚本、TTS配音脚本 |

## 输出内容

- 角色四视图提示词
- UI 风格总览
- UI 规范字典
- 进度条状态链表
- 6-12 个镜头的图片 Prompt + 视频 Prompt
- 时间轴（剧情向内容）
- 字幕脚本和 TTS 配音脚本（剧情向）

## 使用方式

1. 安装 Skill 到支持 Skill 的 Agent 工具（Claude Code、OpenClaw、Hermes 等）
2. 输入角色描述或灵感
3. 获得完整提示词文档
4. 复制提示词到 [[LibTV]] 平台生成图片和视频

## GitHub

- 仓库：https://github.com/irenerachel/ai-gameplay-pack-skill

## 相关工具

- [[LibTV]]：视频生成平台
- [[Lib Image]]：图片生成模块
- [[SeedDance-2.0]]：视频生成模型
