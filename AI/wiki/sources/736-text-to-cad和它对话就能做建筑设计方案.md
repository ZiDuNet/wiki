---
title: "text-to-cad：和它对话就能做建筑设计方案"
type: source-summary
created: 2026-05-18
updated: 2026-05-18
sources: [text-to-cad：和它对话就能做建筑设计方案.md]
tags: [text-to-cad, CAD, AI生成, 建筑设计, 参数化设计]
---

## Summary

text-to-cad 是一款开源的 CAD 模型生成框架，用户通过自然语言描述即可生成建筑设计方案。核心工作流：描述建筑需求（层数、尺寸、材料）→ 生成体块模型 → 深化设计（加楼板、窗户）→ 添加细节（阳台、屋顶、车位）。支持方案阶段多方案比选，导出 CAD 深化。

使用方式：线上试用（需要 Google 账号）或本地部署（需要 Python 环境 + API key）。提示词需要英文输入。

## Key Claims

1. text-to-cad 实现了自然语言到 CAD 模型的直接转换，降低了建筑设计门槛
2. 深化设计可以逐步添加（楼层线、窗户网格、入口、屋顶），每次添加一个功能避免复杂失败
3. 应用场景：方案阶段多方案比选，导出 CAD 后做深化设计

## Entities Mentioned

- [[text-to-cad]] — 本文核心产品：自然语言驱动的 CAD 设计框架
- [[OpenSCAD]] — text-to-cad 底层使用的参数化 CAD 引擎
- [[建筑设计]] — text-to-cad 的目标应用领域

## Concepts

- [[参数化设计]] — 通过变量和公式定义几何关系，修改参数自动更新
- [[AI生成设计]] — 自然语言描述生成建筑模型
- [[CAD深化]] — 方案比选后导出 CAD 做详细设计

## Related Pages

- [[Zero-to-CAD]] — Zero-to-CAD 系列文章
- [[AI技术]] — 更广泛的 AI 生成应用
