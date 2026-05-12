---
title: "WordOllama 2.0 更新：为 Word/WPS 增加 Agent 能力"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: [给Word_WPS增加Agent能力！_ WordOllama 2.0 更新！.md]
tags: [WordOllama, AI插件, Word, WPS, Agent, SKILL]
---

# WordOllama 2.0 更新：为 Word/WPS 增加 Agent 能力

## 摘要

WordOllama 是为 Word/WPS 增加 AI 能力的免费开源插件（支持本地模型、ChatGPT、国产大模型）。2.0 版本正式引入 Agent 功能：打开 Agent 面板后，AI 会自动规划任务、调用 Word 能力操作文档，默认用修订模式完成修改方便审查。Agent 可调用 Skill，支持静默审查（保存时自动检查段落问题）。

## 主要更新

### Agent 任务面板

- 打开左侧【Agent任务】按钮，进入 Agent 面板
- 输入任务描述，AI 自动规划并开始执行
- 暴露"理论上够用"的各类 Word 能力，AI 根据任务需要自主调用
- **修订模式**：默认用修订模式完成修改，改完有修改面板统一查阅
- **危险动作门禁**：重要节点/危险操作需用户批准；AI 无法确认时主动询问

### SKILL 功能

- 支持导入符合标准的 Skill（Zip 包或直接文件夹）
- 两种使用方式：
  1. 让 AI 根据任务需要自己选择 Skill
  2. 通过斜杠 `/` 指令手动指定 Skill
- 支持带 Python 等代码的功能性 Skill（WordOllama 提供终端能力）

### 静默审查

- 默认关闭（会多调用 AI，建议按需开启或选小模型）
- 保存文档时自动审查修改段落是否存在问题
- 发现问题时在 Agent 面板提示

## 安装

官网：`https://www.wordollama.com`

一行脚本安装（管理员终端）：
```powershell
iex(irm 'https://download.wordollama.com/WordOllamaInstaller.ps1')
```

旧版用户建议重新安装以获取更新。

## 作者简介

李伯阳律师 — 北京市隆安(广州)律师事务所，《法律人ChatGPT应用指南》作者，WordOllama 作者。

## 实体

- [[WordOllama]]
- [[李伯阳]]

## 概念

- [[AI-Agent]]
- [[Skill开发]]
- [[Skills技能系统]]

## 来源

> [[给Word_WPS增加Agent能力！_ WordOllama 2.0 更新！]]
