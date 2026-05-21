---
title: "Zero-to-CAD：从零到CAD生成百万可编辑程序"
type: source-summary
tags: [Zero-to-CAD, CAD, AI, Autodesk, AI-CAD, 机械设计]
sources: ["微信公众号/Zero-to-CAD/Zero-to-CAD_从零到CAD生成百万可编辑程序.md"]
created: 2026-05-21
updated: 2026-05-21
---

# Zero-to-CAD：AI 自主生成可编辑 CAD 程序

## 核心概念

Autodesk 研究部门发布的 **Zero-to-CAD** 解决的核心问题：在没有真实数据（无图片无参考）的前提下，AI 自动写代码、自动画机械零件，生成可编辑的 CAD 程序。

## 以前 vs 现在

### 以前 AI-CAD 的局限

1. 只能照着已有图纸学习，人类没设计过的画不出来
2. 只会画形状不懂逻辑（不懂支吊架、孔位、圆角）
3. 只能做草图，简单拉伸/倒角/剪切
4. 生成的模型无法编辑更改
5. 无法自主纠错

### Zero-to-CAD 的突破

1. **无需参考图纸和数据集**：真正的从零设计
2. **像真实设计师一样操作**：先画体块，拉伸、打孔、倒角等
3. **理解工程语义**：知道支架、孔位、倒角等工程概念
4. **支持 CAD 高级操作**：扫描、阵列、放样等
5. **自主纠错**：AI 自主看报错文档，修改调整/重新画

## 技术实现

- 论文：Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data
- 论文地址：https://arxiv.org/pdf/2604.24479
- 支持操作：拉伸、切除、旋转、布尔剪切、扫描、阵列、放样

## 应用场景

- 土木建筑：支持支架、法兰连接件等从 0 到 1 自主生成
- 机械零件：生成可编辑的 CAD 程序，可更改孔位等参数

## 未来影响

工程师不再是绘图员，而是指挥 AI 干活的人。设计师工作流变为：**提出需求 → AI 出方案 → 画图 → 修改 → 出图 → 设计师验收**。重复劳动大大减少。

## 关联

- [[709-yong-zi-ran-yu-yan-sheng-cheng-ke-bian-ji-can-shu-hua-3D-CAD-mo-xing]] — 自然语言生成可编辑 3D CAD 模型
