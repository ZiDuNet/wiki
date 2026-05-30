---
tags: [Skill, 在线市场, 本地管理, 工具链]
sources: [skill站点与本地管理工具.md]
created: 2026-05-30
updated: 2026-05-30
---

# Skill 生态 — 在线市场与本地管理工具全景

## 在线 Skill 市场

| 站点 | 地址 | 特点 |
|------|------|------|
| skills.sh | skills.sh | 技能索引与发现 |
| ClawHub | clawhub.com | 按下载量排序的 Skill 市场 |
| Skill 中文站 | skill.cn | 中文检索与分类 |

## 本地管理工具

| 工具 | 类型 | 特点 |
|------|------|------|
| [Skill Hub](https://github.com/Backtthefuture/huangshu/raw/main/tools/skill-hub/release/claude-skill-hub.tgz) | 本地 Web UI | 扫描全盘、聚合展示、可视化编辑、自动版本快照 |
| [Skills Manager](https://github.com/xingkongliang/skills-manager) | 桌面应用 | 统一管理 Cursor/Claude Code Skills，多机同步到 Git |
| [PromptHub](https://github.com/legeling/PromptHub) | 一站式平台 | Prompt/Skill/Agent 管理，云同步与版本控制 |

## 完整工作流

```
在线发现（skills.sh / ClawHub / Skill中文站）
    ↓
本地安装（npm install / Git clone / 直接安装）
    ↓
统一管理（Skill Hub / Skills Manager / PromptHub）
    ↓
多机同步（~ /.skills-manager/skills/ → Git 备份）
```

## 涉及概念

- [[Skill生态]]
- [[本地化管理]]
- [[多机同步]]