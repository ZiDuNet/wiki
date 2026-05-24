---
title: WebDAV
type: concept
sources: [[开源]本地优先的 Prompt、Skill 与 AI 编程资产工作台，一站式 AI 工具箱.md]
created: 2026-05-25
updated: 2026-05-25
---

# WebDAV

Web-based Distributed Authoring and Versioning。用于 PromptHub 实现跨设备同步，支持坚果云、Nextcloud 等主流服务。

## 在 PromptHub 中的角色

PromptHub 采用"本地优先 + WebDAV 同步"架构：
- 所有数据默认存在本地电脑
- 通过 WebDAV 同步到坚果云、Nextcloud 等服务
- 启动时自动拉取 + 后台定时同步
- 只允许一个活动同步源驱动自动同步，避免多源冲突

## 相关概念

- [[本地优先]]
- [[PromptHub]]

## 数据来源

- [[开源-本地优先的-Prompt-Skill-与-AI编程资产工作台-一站式-AI工具箱]]
