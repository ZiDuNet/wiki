---
type: entity
name: UI-TARS Desktop
created: 2026-05-16
updated: 2026-05-16
---

# UI-TARS Desktop

**类型:** 实体（字节跳动开源产品）
**来源:** 字节跳动
**Star:** 33.7k+
**GitHub:** https://github.com/bytedance/UI-TARS-desktop

## 简介

字节跳动开源的桌面级 GUI Agent，能让 AI 像人一样看屏幕、理解界面语义、操作鼠标键盘。核心特点是纯视觉驱动，不依赖固定坐标，与传统 RPA 的固定流程执行形成鲜明对比。

## 架构

- **Operator**：操作员，负责截图和执行（支持 nut-js、WebOperator、MobileOperator）
- **UI-TARS Model**：大脑，多模态大模型，输入截图+任务描述+历史记录，输出动作
- **GUI Agent**：协调员，串联 Operator 和 Model，循环执行直到任务完成

## 相关概念

- [[AI-Agent]] — 上位概念
- [[浏览器自动化]] — 相关场景
- [[RPA]] — 传统方案对比

## 相关来源

- [[UI-TARS-Desktop字节开源33.7k-star]] — 2026-05-16 新摄入
