---
type: concept
tags: [CAD, 自然语言生成, 3D建模]
sources: [Text-to-CAD-AI生成3D零件开源CAD技能集.md]
created: 2026-05-26
updated: 2026-05-26
---

# Text-to-CAD

**来源文章:** [[Text-to-CAD-AI生成3D零件开源CAD技能集]]

## 定义

用自然语言描述零件或机构，AI 编程代理（如 Codex、Claude Code）自动生成参数化 CAD 模型。

## 技术底层

- **build123d** — Python 参数化 CAD 库
- **OpenCascade** — 开源 CAD 内核
- **WASM** — WebAssembly 浏览器端渲染

## 工作流

1. **描述** — 告诉 Agent 想要的零件/组件/机器人
2. **编辑** — 让 Agent 更新 CAD 源文件
3. **生成** — 创建 STEP/STL/URDF 输出
4. **检查** — 打开 CAD Explorer 审查模型
5. **引用** — @cad[...] 几何句柄精确编辑
6. **提交** — 保存源文件和产物

## 支持格式

**CAD 格式**：STEP、STL、3MF、DXF、GLB
**机器人格式**：URDF、SDF、SRDF

## 应用场景

- 机械零件设计
- 机器人模型生成
- 硬件创客设计
- 仿真模型定义

## 相关实体

- [[text-to-cad]] — 实现 Text-to-CAD 的技能集
- [[build123d]] — Python CAD 库
- [[OpenCascade]] — CAD 内核

## 相关概念

- [[参数化CAD]] — 可通过修改参数调整模型
- [[机器人描述格式]] — URDF/SDF/SRDF 标准