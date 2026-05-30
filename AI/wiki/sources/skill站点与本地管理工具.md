---
tags: [Skill, 本地管理, 工具链, 市场]
sources: [微信公众号/SkillManager/Skill 站点与本地管理工具.md]
created: 2026-05-30
updated: 2026-05-30
---

# Skill 生态 — 在线市场与本地管理工具全景

**来源：** 微信公众号/SkillManager/Skill 站点与本地管理工具.md
**摄入日期：** 2026-05-30
**类型：** 文章
**作者：** 天空奇点

## 摘要

本文系统梳理了 Skill 的三类工具体系：三个在线市场（skills.sh / ClawHub / Skill 中文站）用于发现，九个本地工具（Skill Hub / Skills Manager / PromptHub）用于管理，形成完整的"在线找 → 本地装 → 统一管"工作流。

## 在线 Skill 市场

| 站点 | 特点 |
|------|------|
| [skills.sh](https://skills.sh) | 技能索引与发现 |
| [ClawHub](https://clawhub.com) | 按下载量排序的 Skill 市场 |
| [Skill 中文站](https://skill.cn) | 中文检索与分类 |

> 在线站点适合「发现新 Skill」；装到本机后，建议用本地工具做统一管理与同步。

## 本地 Skill 管理工具

### Skill Hub

本地 Web UI，扫描全盘、聚合展示、可视化编辑、自动版本快照。

```bash
npm install -g https://github.com/Backtthefuture/huangshu/raw/main/tools/skill-hub/release/claude-skill-hub.tgz && skill-hub
```

### Skills Manager

统一管理 Cursor、Claude Code 等 AI 编码工具的 Skills。支持从 Git、本地目录、`.zip`/`.skill` 文件或 skills.sh 市场安装，统一存放在 `~/.skills-manager`。多机同步：将 `~/.skills-manager/skills/` 备份到 Git，做版本管理与多机同步。

项目地址：github.com/xingkongliang/skills-manager

### PromptHub

Prompt、Skill、Agent 一站式管理：提示词编辑、Skill 一键分发、Agent 资产云同步与版本管理。

项目地址：github.com/legeling/PromptHub

## 工作流

```
在线发现 → 本地安装 → Skill Hub / Skills Manager / PromptHub 统一管理 → Git 多机同步
```

## 涉及概念

- [[Skill生态]] — 在线市场与本地工具构成的完整 Skill 生命周期管理
- [[本地化管理]] — 版本快照、可视化编辑、多机同步等本地 Skill 管理能力
- [[多机同步]] — 将本地 Skill 目录备份到 Git 实现跨设备同步

## 提及实体

- [[skills.sh]] — Skill 发现与索引平台
- [[ClawHub]] — 按下载量排序的 Skill 市场
- [[Skill中文站]] — 中文 Skill 检索与分类
- [[Skill Hub]] — 本地 Web UI 管理工具
- [[Skills Manager]] — 跨工具统一管理桌面应用
- [[PromptHub]] — 提示词/Skill/Agent 一站式平台