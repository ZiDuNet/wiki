---
tags: [Text-to-CAD, CAD, 3D, build123d, OpenCascade]
sources: [Text-to-CAD：用 AI 生成 3D 零件的开源 CAD 技能集，兼容 Codex_Claude_Gemini 等多种 AI Agent！.md]
created: 2026-05-26
updated: 2026-05-26
---

# Text-to-CAD：AI生成3D零件开源CAD技能集

**来源：** Claude/AI开源提效指南
**摄入日期：** 2026-05-26
**类型：** 工具介绍

## 摘要

Text-to-CAD 是开源 AI Agent 驠动的 CAD 建模技能集（3K+ Stars），用自然语言生成 3D 零件。底层基于 build123d（Python CAD 库）和 OpenCascade（开源 CAD 引擎），通过 WASM 和 Agent 技能实现端到端 Text-to-CAD。支持 Codex、Claude Code、Gemini CLI、OpenClaw 等所有主流 Agent。

## 核心观点

### 技术架构

- [[build123d]] — Python 参数化 CAD 库
- [[OpenCascade]] — 开源 CAD 内核
- [[WASM]] — WebAssembly 支持浏览器端渲染
- Agent Skills 标准 — 遵循开放标准

### 七大技能

| 技能 | 功能 |
|------|------|
| CAD Skill（核心） | 生成参数化 CAD 模型，导出 STEP/STL/3MF/DXF/GLB，@cad[...] 几何引用 |
| step.parts Skill | 从 step.parts 查找下载标准件（螺丝螺母轴承电机等） |
| CAD Explorer Skill | 启动浏览器 WebGL 模型查看器，支持 8 种格式 |
| URDF Skill | 生成 URDF XML 机器人描述文件（连杆关节限制） |
| SDF Skill | 生成 SDFormat/SDF XML 仿真模型定义 |
| SRDF Skill | MoveIt2 SRDF 语义定义（逆运动学路径规划） |
| SendCutSend Skill | 激光切割 DXF/STEP 预处理报告 |

### 工作流

1. **描述** — 告诉 Agent 想要的零件/组件/机器人
2. **编辑** — 让 Agent 更新 CAD 源文件
3. **生成** — 创建 STEP/STL/URDF/SDF 输出
4. **检查** — 打开 CAD Explorer 审查模型
5. **引用** — 复制 @cad[...] 句柄精确编辑
6. **提交** — 保存源文件和产物

## 提及实体

- [[text-to-cad]] — earthtojake 开发的 AI 驠动 CAD 建模技能集
- [[earthtojake]] — Text-to-CAD 项目作者

## 涉及概念

- [[Text-to-CAD]] — 用自然语言描述零件，AI 自动生成精确参数化 CAD 模型
- [[参数化CAD]] — 基于参数的 CAD 建模，可通过修改参数调整模型
- [[机器人描述格式]] — URDF/SDF/SRDF 三种机器人/仿真描述标准
- [[CAD-Explorer]] — 基于 WebGL 的浏览器 CAD 模型查看器

## 安装命令

```bash
# 克隆仓库
git clone https://github.com/earthtojake/text-to-cad.git
cd text-to-cad

# Claude Code
./scripts/claude-install.sh

# Codex
./scripts/codex-install.sh

# OpenClaw
./scripts/openclaw-install.sh

# 通用安装（推荐）
npx agent-skills-cli add earthtojake/text-to-cad
```

## 项目地址

- GitHub: https://github.com/earthtojake/text-to-cad
- 官方文档: https://www.cadskills.xyz
- 在线演示: https://demo.cadskills.xyz