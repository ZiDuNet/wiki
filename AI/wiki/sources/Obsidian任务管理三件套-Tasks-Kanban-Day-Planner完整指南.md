---
title: "Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南"
type: source-summary
created: 2026-05-14
updated: 2026-05-14
sources: ["Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南.md"]
tags: [Obsidian, 任务管理, Tasks插件, Kanban插件, Day-Planner插件, 效率工具]
---

# Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南

## Summary

本文来自「ITKEE」公众号，系统介绍了 Obsidian 三款任务管理插件的功能和组合工作流。Tasks 解决跨笔记任务索引，Kanban 提供可视化看板，Day Planner 实现日视角时间规划。三者互补覆盖全局/项目/日三个维度，结合 Templater 模板可实现自动化日常记录。

## Key Claims

1. **Tasks 核心价值**：全局任务索引——散落在各篇笔记的任务，通过查询代码块统一汇总
2. **Kanban 核心价值**：Markdown 驱动的看板——数据仍为纯文本，导出无锁定
3. **Day Planner 核心价值**：时间线视角——日视角规划+日历同步
4. **推荐起步顺序**：今天只装 Tasks → 明天加 Kanban → 后天加 Day Planner
5. ** Templater 模板价值**：新建每日笔记时自动生成时间块格式，减少重复操作

## Entities Mentioned

- [[ITKEE]]（公众号来源）
- [[Tasks插件]]（Obsidian 任务索引插件）
- [[Kanban插件]]（Obsidian 看板插件）
- [[Day-Planner插件]]（Obsidian 时间线插件）
- [[Dataview插件]]（Day Planner 依赖插件）
- [[Templater插件]]（模板自动化插件）

## Concepts

- [[Obsidian-任务管理]]：在 Obsidian 中管理任务的完整方案
- [[Tasks查询语法]]：Tasks 插件的日期/状态/标签筛选语言
- [[Markdown看板]]：纯文本驱动的看板实现
- [[ICS日历同步]]：通过 ICS 协议导入外部日历到 Obsidian

## 三个插件对比

| 插件 | 核心功能 | 适用场景 | 数据格式 |
|------|----------|----------|----------|
| Tasks | 全局任务索引+日期追踪 | 多项目并行、任务散落各笔记 | 查询结果动态生成 |
| Kanban | Markdown看板可视化 | 项目阶段管理、拖拽切换状态 | 纯 Markdown |
| Day Planner | 日时间线+日历同步 | 日视角规划、会议+任务统一 | 时间块 Markdown |

## Tasks 日期符号

| 符号 | 名称 | 含义 | 示例 |
|------|------|------|------|
| 📅 | due date | 到期日 | `📅 2026-05-15` |
| ⏳ | scheduled date | 计划日 | `⏳ 2026-05-10` |
| 🔁 | recurring | 循环任务 | `🔁 every Monday` |

## Tasks 常用查询条件

```tasks
not done                    # 未完成任务
done                        # 已完成任务
due before 2026-05-15      # 到期日晚于指定日期
due after today             # 今天之后才到期
starts before today         # 计划日已到但未完成
tag contains #项目           # 包含特定标签
path includes 项目A         # 在特定文件夹
sort by due reverse        # 按到期日倒序
group by filename           # 按所属笔记分组
```

## Kanban 代码块语法

````
```kanban
- [ ] 待办
- [ ] 进行中
- [x] 已完成
```
````

## 组合工作流

- **早上**：Day Planner 做日计划 → 时间线显示全天节奏
- **白天**：Kanban 管项目进度 → 拖拽卡片更新状态
- **随时**：Tasks 查全局汇总 → 周报素材 5 秒生成

## Notable Quotes

> "Tasks 解决「有哪些任务」，Kanban 解决「项目进度如何」，Day Planner 解决「今天的时间怎么安排」"

> "Tasks 在你现有笔记基础上，给所有复选框装了一个索引系统"

> "三个插件不要同时装。按顺序来：今天只装 Tasks，在旧笔记里找一条带日期的任务，测试查询——这是整个工作流的起点"

## Limitations / Bias

- Kanban 目前在寻找新维护者，长期维护有不确定性
- ICS 日历同步有时差，新建日程可能几分钟后才出现
- 作者推荐最小起步方案（Tasks first），但未讨论与其他插件（如 Dataview）的更深度整合
