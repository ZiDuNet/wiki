---
title: Day Planner插件
type: entity
created: 2026-05-14
updated: 2026-05-14
sources: ["Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南.md"]
tags: [Obsidian插件, 任务管理, 时间规划, 日历同步]
---

# Day Planner插件

**类型:** 实体/Obsidian插件
**来源:** [[Obsidian任务管理三件套-Tasks-Kanban-Day-Planner完整指南]]

## 简介

Day Planner 是 Obsidian 的日视角时间规划插件，将每日笔记渲染成横向时间线，支持状态栏实时显示当前时间点。解决「今天的时间怎么安排」的问题。

## 核心功能

| 功能 | 说明 |
|------|------|
| 时间线视图 | 将时间块渲染成横向时间线 |
| 迷你时间线 | 左下角状态栏实时显示当前时间点 |
| 多日视图 | 同时查看多天的时间块，做周计划 |
| 日历同步 | 通过 ICS 链接导入 Google Calendar/iCloud/Outlook 日历 |

## 依赖要求

**必须先安装 [[Dataview插件]]**，Day Planner 依赖 Dataview 的查询功能。

## 时间块语法

```markdown
- [ ] 09:00 - 10:00 写文章大纲
- [ ] 10:30 - 11:30 客户沟通
- [ ] 14:00 - 15:00 团队周会
```

时间块里的 `- [ ]` 同时也是 Tasks 可索引的任务。

## 与 Tasks 联动

在每日笔记里写：
````tasks
```tasks
not done due today sort by due
```
````

Day Planner 会把今天到期的 Tasks 任务渲染到时间线末尾。

## ICS 日历同步

1. Google Calendar → 设置 → 日历导出 → 复制「公开日历的 ICS 链接」
2. Day Planner 设置 → Calendar Sync → 填入 ICS 链接
3. 日历里的会议自动出现在时间线上

**注意**：ICS 同步有时差，新建日程可能几分钟后才出现。

## 适合人群

有固定日程、需要日视角规划时间、对工具切换有痛感的人。

## 相关插件

- [[Tasks插件]]：Day Planner 的全局任务索引来源
- [[Kanban插件]]：项目进度可视化
- [[Dataview插件]]：Day Planner 的依赖插件
