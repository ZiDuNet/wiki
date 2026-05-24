---
type: concept
created: 2026-05-24
updated: 2026-05-24
---

# Git备份（技能）

Skills-Manager 提供的功能：对 skills/ 子目录做 Git 版本历史管理，支持远程 push/pull 与快照恢复。

## 核心能力

| 能力 | 说明 |
|------|------|
| 版本历史 | skills/ 目录的 Git 版本控制 |
| 远程同步 | push/pull 到 GitHub/Gitee 等远程仓库 |
| 快照恢复 | 回滚到任意历史版本 |
| 多机同步 | 通过 Git 远程实现多台机器的技能库同步 |

## 使用方式

在 Skills-Manager 设置中配置 Git 远程仓库，在「我的 Skills」里执行：
- 开始备份
- 同步到 Git

## 注意事项

- 改 Preset 或中央库后，已复制到 Agent 目录的内容不会自动回滚
- CLI 与桌面共用 SQLite，CLI 写入后桌面端需刷新或重启

## 相关实体

- [[Skills-Manager]] — 提供 Git 备份功能

## 相关概念

- [[中央技能库]] — Git 备份的对象
- [[多机同步]] — Git 备份的价值

## 相关文章

- [[Skills装太多怎么办-用Skills-Manager桌面应用统一管理]]