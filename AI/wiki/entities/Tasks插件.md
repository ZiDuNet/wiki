---
title: Tasks插件
type: entity
created: 2026-05-14
updated: 2026-05-14
sources: ["Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南.md"]
tags: [Obsidian插件, 任务管理, 任务索引, 日期追踪]
---

# Tasks插件

**类型:** 实体/Obsidian插件
**来源:** [[Obsidian任务管理三件套-Tasks-Kanban-Day-Planner完整指南]]

## 简介

Tasks 是 Obsidian 的任务索引插件，在现有笔记基础上给所有复选框装了一个索引系统。通过查询代码块，可以用日期、标签、状态等条件筛选散落在各篇笔记中的任务。

## 核心功能

| 功能 | 说明 |
|------|------|
| 全局任务索引 | 扫描知识库所有 `- [ ]` 复选框 |
| 日期符号 | 📅 到期日、⏳ 计划日、🔁 循环任务 |
| 查询语法 | 日期/状态/标签/路径等多维度筛选 |
| 自动完成记录 | 完成任务自动写入 completion 日期 |

## 日期符号

| 符号 | 名称 | 语法示例 |
|------|------|----------|
| 📅 | due date（到期日） | `- [ ] 任务 📅 2026-05-15` |
| ⏳ | scheduled date（计划日） | `- [ ] 任务 ⏳ 2026-05-10` |
| 🔁 | recurring（循环任务） | `- [ ] 任务 🔁 every Monday` |

## 常用查询条件

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
done date after 2026-05-01  # 完成日期查询
```

## 安装配置建议

- **替换快捷键**：将 `Ctrl/Cmd + Enter` 替换为 `Tasks: Toggle Done`
- **设置全局过滤器**：在 Tasks 设置中填入 `#task`，避免噪音任务进入索引

## 适合人群

多项目并行、任务散落在各篇笔记里、需要在全局视角汇总的人。

## 相关插件

- [[Kanban插件]]：Tasks 的可视化界面
- [[Day-Planner插件]]：Tasks 的日视角补充
- [[Dataview插件]]：Day Planner 依赖插件
