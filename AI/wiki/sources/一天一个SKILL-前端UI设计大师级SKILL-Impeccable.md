---
tags: [Impeccable, 前端设计, AI编程, Skill]
sources: [一天一个SKILL——还在用蓝湖_磨刀？不如用用这个前端UI设计大师级SKILL——Impeccable.md]
created: 2026-05-27
updated: 2026-05-27
---

# 一天一个SKILL——前端UI设计大师级SKILL：Impeccable

**来源：** 微信公众号/Impeccable/一天一个SKILL——还在用蓝湖/磨刀？不如用用这个前端UI设计大师级SKILL——Impeccable.md
**分类：** Impeccable
**摄入日期：** 2026-05-27
**作者：** 考拉搞AI

## 摘要

介绍 Impeccable——一个给 AI 注入专业设计品味的 Skill 框架。解决 AI 生成前端代码时普遍存在的"AI 塑料感"问题（Inter 字体、渐变背景、卡片套卡片等）。由 jQuery UI 创造者 Paul Bakaus 创建，GitHub 120K star，4个月内成为 Claude Code 生态最受欢迎设计类 Skill。

## 核心观点

- **问题根源**：大模型知道什么是好设计，但不会主动用，因为没人告诉它——需要具体设计词汇和反模式约束
- **Impeccable 方案**：不是告诉 AI"要做好设计"，而是用明确的设计词汇、命令体系和反模式检测让 AI 自动应用专业决策
- **三大支柱**：7份设计参考文件（字体/色彩/空间/动效/响应式/UX文案）、20条设计命令、25条确定性反模式检测
- **商业价值**：专业设计可将用户可信度提升 75%，跳出率降低 38%；让没设计预算的技术团队也能输出专业界面
- **安装**：一条命令 `npx skills add https://github.com/pbakaus/impeccable --skill impeccable`，自动适配 Claude Code/Cursor/Gemini CLI 等

## 提及实体

- [[Impeccable]] — 设计类 Skill 框架，给 AI 注入专业设计品味
- [[Paul Bakaus]] — Impeccable 创始人，Google Chrome DevTools 前产品负责人，jQuery UI 创造者
- [[Claude Code]] — Anthropic AI 编程工具，Impeccable 生态最受欢迎设计类 Skill
- [[AI-slop]] — AI 生成界面的"塑料感"问题描述

## 涉及概念

- [[AI前端生成]] — 用 AI 自动生成前端代码/界面
- [[设计系统]] — 专业设计的系统性方法论
- [[OKLCH色彩]] — 现代色彩空间，用于高质量配色
- [[反模式检测]] — 明确列出不该做的事，对抗大模型不良习惯
- [[设计命令体系]] — 用具体命令词（/audit /critique /polish）指挥 AI 做设计

## 设计命令示例

| 命令 | 作用 |
|---|---|
| `/teach-impeccable` | 建立设计上下文，保存到 .impeccable.md |
| `/audit` | 可访问性、性能、响应式全面检查 |
| `/critique` | UX 审查：视觉层次、信息架构、情感共鸣 |
| `/polish` | 交付前像素级润色 |
| `/bolder` | 强化过于保守平庸的设计 |
| `/overdrive` | 高级技术野心：WebGL 着色器、弹簧物理动画 |