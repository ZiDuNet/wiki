---
title: "Obsidian官方同步贵？在NAS上自建服务器，实现多端笔记完美同步"
type: source-summary
tags: [Obsidian, NAS, Fast-Note-Sync, 同步, 私有化部署]
sources: ["微信公众号/Obsidian/Obsidian官方同步贵？在NAS上自建服务器，实现多端笔记完美同步.md"]
created: 2026-05-21
updated: 2026-05-21
---

# Fast Note Sync：NAS 上的 Obsidian 多端同步方案

## 问题背景

Obsidian "本地优先"设计带来隐私安全，但多端同步困难。官方同步服务收费且服务器在海外，国内访问不友好。

## 解决方案：Fast Note Sync

一款免费开源、可私有化部署的 Obsidian 多端实时同步插件。

### 项目信息

- 插件地址：https://github.com/haierkeys/obsidian-fast-note-sync
- 服务端：https://github.com/haierkeys/fast-note-sync-service
- 技术栈：Golang + WebSocket + SQLite + React

### 核心特性

1. **毫秒级实时同步**：WebSocket 协议，支持文本、图片、视频、音频
2. **完整配置同步**：除笔记外，还同步 `.obsidian` 配置（主题、插件、快捷键）
3. **私有化部署**：可部署在 NAS、软路由、云服务器
4. **极简配置**：插件端粘贴服务端生成的配置即可
5. **Web 管理后台**：网页端查看、编辑笔记、管理用户
6. **笔记历史版本 & 回收站**：查看完整修改记录，支持恢复误删

## 部署架构

```
┌─────────────────┐     WebSocket      ┌──────────────────────┐
│  Obsidian 插件   │ ←───────────────→  │  Fast Note Sync      │
│  (客户端)        │                    │  Service (服务端)     │
└─────────────────┘                    │  - 存储               │
                                        │  - 版本管理           │
┌─────────────────┐                    │  - 配置同步           │
│  手机/平板客户端 │ ←───────────────→  │  (NAS 私有化部署)     │
└─────────────────┘                    └──────────────────────┘
```

## 部署要点

1. NAS 上通过 Docker Compose 部署服务端（端口 9100）
2. 需要外网访问：公网 IP + Lucky 反向代理（启用 WebSocket）
3. 无公网 IP：需 Tailscale 等支持 WebSocket 的内网穿透方案
4. 节点小宝 P2P 直连不支持 WebSocket，外网同步会失败

## 客户端配置

1. 第三方插件 → 关闭安全模式
2. 拖入插件文件夹 → 启用插件
3. 服务端网页授权 → "一键授权到 Obsidian"
4. 远端配置自动导入 → 显示"服务已连接"

## 关联

- [[Hermes+Obsidian+LLM-Wiki-da-jian-ben-di-zhi-shi-ku]] — 搭配 Hermes Agent 和 LLM Wiki 使用
