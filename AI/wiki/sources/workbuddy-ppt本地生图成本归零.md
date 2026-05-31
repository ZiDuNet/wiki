---
title: WorkBuddy升级PPT技能，本地生图成本归零
type: source-summary
tags: [WorkBuddy, PPT, 本地生图, PyInstaller, AI辅助]
sources: [微信公众号/WorkBuddy/Workbuddy升级PPT技能，本地生图，成本归零，高效_快速_稳定.md]
created: 2026-05-31
updated: 2026-05-31
---

# WorkBuddy升级PPT技能，本地生图成本归零

**来源：** 微信公众号/WorkBuddy/Workbuddy升级PPT技能，本地生图，成本归零，高效_快速_稳定.md
**公众号：** 8点虾聊AI
**摄入日期：** 2026-05-31

## 摘要

作者用 Playwright + Python 开发了本地生图工具，然后将其集成到 WorkBuddy 的 PPT 生成技能中，实现"云端转本地、成本归零"的升级。记录了完整过程和踩坑解决方案。

## 核心流程

1. **改技能**：修改 `ppt-nano-master` 的 SKILL.md，把云端生图 API 调用替换为本地 CLI 命令
2. **对话生成大纲**：WorkBuddy 根据需求生成 PPT 大纲（8页，秒出），作者评审后让 AI 改进
3. **踩坑**：沙箱环境 Python 无法访问外网，`pip install Pillow` 超时失败
4. **解决方案**：用 PyInstaller 把生图工具打包成独立 exe（172MB），沙箱直接调用 exe 不依赖 Python 环境
5. **成功出图**：不到1分钟生成完整 PPT，白板风格，配图全部本地生成

## 关键决策

| 决策 | 原因 |
|---|---|
| 本地生图 > 云端生图 | 云端限流/收费、不稳定、无法商用 |
| 打包 CLI > 装依赖 | 沙箱隔离无法 pip install，本地工具打包后不依赖环境 |

## 核心观点

1. **工具复利**：昨天开发的生图工具，今天成为 PPT 技能的生图引擎。明天 PPT 技能可能变成"公众号配图自动生成"的零件

2. **角色反转**：以前是"人写、AI 改"，现在是"AI 写大纲、人评审"——笔杆子反转

3. **CLI 打包**：沙箱跑不通就打包成独立 exe，别在环境问题上耗太久

## 涉及实体

- [[WorkBuddy]] — AI 助手产品，支持对话生成 PPT
- [[ppt-nano-master]] — PPT 生成 Skill，调用生图工具
- [[PyInstaller]] — Python 打包工具，将脚本转换为独立 exe
- [[playwright-gen-image]] — 作者自研本地生图 CLI 工具

## 涉及概念

- [[本地AI工具链]] — 不依赖云服务 API 的本地 AI 工具组合
- [[AI辅助PPT生成]] — AI 生成大纲 + 人类评审的协作模式
- [[CLI打包方案]] — 沙箱隔离环境下的依赖问题解决方案
- [[工具复利]] — 早期开发的工具成为后续功能的组件