---
title: PeekDesktop
type: entity
tags: [Windows, 桌面工具, 开源, .NET]
sources: [github-4个star不高但有趣的项目.md]
created: 2026-05-31
updated: 2026-05-31
---

# PeekDesktop

Windows 桌面窗口管理工具，让 Windows 拥有和 macOS Sonoma 一样的窗口透明化体验。

## 基本信息

| 项目 | 信息 |
|---|---|
| GitHub | https://github.com/shanselman/PeekDesktop |
| 开发者 | Scott Hanselman（微软 VP） |
| 技术栈 | .NET |
| 平台 | Windows |

## 功能特点

- 点击桌面空白区域，所有窗口自动收起
- 再点一下或点击任意 App，窗口全部恢复到原位置
- 支持 Fly Away 动画模式（窗口"飞出去"的效果）
- 不需要管理员权限
- 空闲时内存占用 < 5 MB
- 下载 zip 解压即用，**不需要安装 .NET 运行时**
- 自带自动更新功能

## 体积优化

Scott Hanselman 曾专门写文章介绍如何把这个 .NET 程序从 65 MB 压到 1.88 MB，加 LZMA 压缩后甚至能塞进一张软盘。

## 用途场景

需要干净桌面的演示场景、截图场景、或临时聚焦当前任务时使用。