---
type: entity
name: WebDAV
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# WebDAV

**类型:** 实体（协议/技术）
**提及文章数:** 1

## 简介

WebDAV（Web-based Distributed Authoring and Versioning）是一种远程文件同步协议。简单理解的话，可以把 WebDAV 当成\"远程文件夹\"。很多 NAS、云盘甚至服务器都支持 WebDAV。

## 核心定位

在 Obsidian 同步方案中，WebDAV 是 [[Remotely-Save]] 插件的后端协议，连接 Obsidian 与坚果云或 NAS。

## 同步结构

```
Obsidian
    ↓
Remotely Save 插件
    ↓
WebDAV 协议
    ↓
坚果云 / NAS / 私有服务器
```

## 支持平台

| 平台类型 | 示例 |
|---|---|
| 云盘 | 坚果云（国内推荐） |
| NAS | 极空间、群晖、飞牛、威联通 |
| 私有服务器 | 自建 WebDAV 服务 |

## 特性

- **远程文件夹**：像操作本地文件夹一样操作远程文件
- **多平台支持**：NAS、云盘、服务器均可提供 WebDAV 服务
- **协议标准**：基于 HTTP 扩展的开放标准

## 在 Obsidian 同步中的角色

### 坚果云 WebDAV 方案
**Remotely Save + 坚果云 WebDAV**

这是目前国内用户最推荐的免费组合：
- 坚果云国内速度快
- 免费版有流量限制（上传 1GB/月，下载 3GB/月）
- 配置难度适中

### NAS WebDAV 方案
**Remotely Save + NAS WebDAV**

终极方案之一：
- 数据完全在自己手里
- 局域网同步速度非常快
- 无流量限制

## 与其他协议对比

| 协议 | 特点 | 适用场景 |
|---|---|---|
| WebDAV | 远程文件夹，标准协议 | Obsidian 同步、文件管理 |
| Git | 版本控制，适合纯文本 | 程序员、版本管理需求 |
| iCloud/OneDrive | 系统集成 | 轻量用户、单生态 |

## 相关概念

- [[云盘同步]]
- [[同步冲突处理]]
- [[本地优先]]

## 相关实体

- [[Remotely-Save]]
- [[坚果云]]
- [[NAS]]
- [[Obsidian-Sync]]

## 相关文章

- [[Obsidian怎么同步-4套方案深度对比-2026最新版]]