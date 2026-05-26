---
tags: [AI前端, 设计系统, Skill, Claude-Code]
sources: [一天一个SKILL——还在用蓝湖_磨刀？不如用用这个前端UI设计大师级SKILL——Impeccable.md]
created: 2026-05-27
updated: 2026-05-27
mentions: 1
---

# Impeccable

**类型:** 工具/Skill框架
**创始人:** Paul Bakaus（前 Google Chrome DevTools 产品负责人，jQuery UI 创造者）
**GitHub:** 120K+ stars

## 简介

给 AI 注入专业设计品味的 Skill 框架。不是组件库或 CSS 框架，而是一套让 AI 生成代码时自动应用专业视觉系统的命令体系和设计规范。解决 AI 生成前端的"塑料感"问题（Inter 字体、渐变背景、卡片套卡片等）。

## 三大支柱

1. **7份设计参考文件**：字体排印、OKLCH 色彩、空间布局、动效交互、响应式设计、UX 文案
2. **20条设计命令**：/teach-impeccable、/audit、/critique、/polish、/bolder、/overdrive 等
3. **25条确定性反模式检测**：禁止默认 Inter 字体、禁止纯黑配色、禁止卡片套卡片等

## 解决的问题

AI slop（AI 塑料感）：大模型知道什么是好设计，但不会主动用——因为没人用具体词汇告诉它。Impeccable 用明确的设计词汇和反模式约束让 AI 自动执行专业决策。

## 商业价值

专业设计将用户可信度提升 75%，跳出率降低 38%。让没有设计预算的技术团队也能输出专业级界面。

## 安装

```bash
npx skills add https://github.com/pbakaus/impeccable --skill impeccable
```
自动适配 Claude Code、Cursor、Gemini CLI、Codex CLI、VS Code Copilot 等。

## 相关概念

[[AI前端生成]], [[设计系统]], [[OKLCH色彩]], [[反模式检测]], [[Claude Code]]

## 来源

- [[一天一个SKILL-前端UI设计大师级SKILL-Impeccable]]