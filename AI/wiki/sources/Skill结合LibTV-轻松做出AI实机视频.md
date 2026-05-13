---
title: "Skill结合哩布哩布LibTV，轻松做出AI实机视频！"
type: source-summary
created: 2026-05-14
updated: 2026-05-14
sources: ["Skill结合哩布哩布LibTV，轻松做出AI实机视频！.md"]
tags: [Skill, LibTV, AI视频, AI游戏, 工作流]
---

# Skill结合哩布哩布LibTV，轻松做出AI实机视频！

## Summary

本文来自「阿真Irene」公众号，介绍如何结合 AI Agent Skill 与 LibTV 平台制作游戏实机效果视频。核心价值：降低了 AI 生成游戏实机视频的门槛，用户只需提供角色描述和风格要求，即可通过 Skill 自动生成完整的提示词文档，再配合 LibTV 平台完成从参考图到分镜图到视频的完整工作流。支持 Claude Code、OpenClaw、Hermes 等 Agent 工具调用。

## Key Claims

1. **Skill 核心功能**：输入角色描述/灵感，输出包含角色四视图、UI规范、6-12个镜头提示词的完整文档
2. **工作流设计三个保证**：角色一致性、UI/HUD一致性、图片+视频提示词配对清晰
3. **工具链组合**：ai-gameplay-pack Skill + LibTV（Lib Image + SeedDance 2.0）
4. **Agent 自动化可能性**：可以通过 Hermes/OpenClaw 等 Agent 自动调用 Skill 和 LibTV，实现提示词到视频全自动产出
5. **LibTV 双入口**：Creator 端适合手动检查，Agent 端适合自动化

## Entities Mentioned

- [[阿真Irene]]（公众号作者）
- [[LibTV]]（AI视频创作平台）
- [[ai-gameplay-pack-skill]]（GitHub: irenerachel/ai-gameplay-pack-skill）
- [[Lib Image]]（LibTV 图片生成模块）
- [[SeedDance-2.0]]（视频生成模型）
- [[Claude-Code]]（可调用 Skill 的 Agent 工具）
- [[Hermes-Agent]]（可调用 Skill 的 Agent 工具）
- [[OpenClaw]]（可调用 Skill 的 Agent 工具）

## Concepts

- [[AI游戏实机视频]]：具有游戏界面感的 AI 生成视频
- [[AI提示词工程]]：为 AI 工具编写高质量提示词的技术
- [[AI视频工作流]]：从创作到成品的 AI 辅助制作流程
- [[Skill-Agent集成]]：Skill 与 Agent 工具的自动化调用

## 工作流步骤

1. **调用 Skill**：在 Agent 工具中说"调用实机游戏视频提示词 Skill"
2. **提供灵感**：描述想要的风格（东方神话/赛博修仙/RPG/国风等）
3. **输出文档**：Skill 生成角色四视图、UI规范、镜头提示词完整包
4. **生成图片**：Lib Image 生成参考图和分镜图
5. **检查细节**：确认人物、UI、场景逻辑正确
6. **生成视频**：SeedDance 2.0 图生视频
7. **合成视频**：LibTV 工作台合成最终成片

## Skill 版本

| 版本 | 用途 | 特点 |
|------|------|------|
| 轻量版（lite） | 聚焦提示词 | 节省 token |
| 完整版 | 详细提示词 | 包含角色锚点、UI规范、时间轴、字幕脚本 |

## Notable Quotes

> "这套设计的骨架是为了保证三个方面：游戏角色不会飘、UI界面和HUD保持一致、每个镜头都使用图片提示词+视频提示词的配对"

> "LibTV 本就不是一个单纯生成视频的工具，我更喜欢把提示词生成和优化、参考图、分镜图、视频节点和最终合成预览都放在它的一个工作台里完成"

## Limitations / Bias

- 依赖 LibTV 平台，跨平台迁移有成本
- 视频生成质量与积分消耗正相关
- 不同模型输出效果有差异，需要手动判断和调整
- 作者立场为创作者分享，实际产出效果因人而异
