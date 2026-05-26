---
type: entity
tags: [CAD, 3D建模, Agent-Skills, GitHub项目]
sources: [Text-to-CAD-AI生成3D零件开源CAD技能集.md]
created: 2026-05-26
updated: 2026-05-26
---

# text-to-cad

> GitHub: https://github.com/earthtojake/text-to-cad
> Stars: 3k+ (2026-05)
> 作者: earthtojake

## 简介

开源 AI Agent 驠动的 CAD 建模技能集，用自然语言生成 3D 零件，专为 CAD 建模、机器人和硬件设计而生。

## 技术架构

- **build123d** — Python 参数化 CAD 库
- **OpenCascade** — 开源 CAD 内核
- **WASM** — WebAssembly 支持浏览器端渲染
- Agent Skills 标准 — 遵循开放标准

## 七大技能

| 技能 | 功能 |
|------|------|
| CAD Skill（核心） | 生成参数化 CAD 模型，导出 STEP/STL/3MF/DXF/GLB |
| step.parts Skill | 从 step.parts 查找下载标准件 |
| CAD Explorer Skill | 浏览器 WebGL 模型查看器（8 格式） |
| URDF Skill | 生成机器人 URDF XML 描述 |
| SDF Skill | 生成仿真 SDF XML 定义 |
| SRDF Skill | MoveIt2 语义定义 |
| SendCutSend Skill | 激光切割预处理 |

## 支持格式

**CAD 格式**：STEP、STL、3MF、DXF、GLB
**机器人格式**：URDF（ROS）、SDF（Gazebo/Isaac）、SRDF（MoveIt2）

## 多 Agent 支持

Codex、Claude Code、Gemini CLI、OpenClaw 全部支持。

## 安装

```bash
# 通用安装
npx agent-skills-cli add earthtojake/text-to-cad

# Claude Code
./scripts/claude-install.sh
```

## 相关概念

- [[Text-to-CAD]] — 自然语言生成 CAD 模型
- [[参数化CAD]] — 基于参数的可编辑建模
- [[机器人描述格式]] — URDF/SDF/SRDF 标准

## 来源文章

- [[Text-to-CAD-AI生成3D零件开源CAD技能集]]