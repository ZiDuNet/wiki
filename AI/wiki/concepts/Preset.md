---
type: concept
created: 2026-05-24
updated: 2026-05-24
---

# Preset（预设）

Preset 是 Skills-Manager 提出的概念：可复用的 Skill 分组，用于一键给 Agent 挂上/卸下整组 Skill。

## 核心特性

| 特性 | 说明 |
|------|------|
| 命名技能组 | 如「前端套件」「安全审计套件」 |
| 批量激活 | 在工作区点 Preset 标签一键激活 |
| 一次性复制 | 激活 = 把这一组复制到 Agent 目录，**非实时订阅** |
| 可管理 | 改 Preset 后需按应用内流程再操作，不会自动回滚 |

## 使用场景

- **前端套件**: vercel-react-best-practices + frontend-design + web-design-guidelines
- **安全审计套件**: seo-audit + code-review-expert
- **视频制作套件**: remotion-best-practices + agent-browser

## 与中央库的关系

Preset 是中央库中定义的技能组配置，激活时从中央库复制到指定 Agent 目录。

## 相关实体

- [[Skills-Manager]] — 实现 Preset 功能的桌面应用

## 相关概念

- [[中央技能库]] — Preset 的来源
- [[技能分发]] — Preset → Agent 的分发过程

## 相关文章

- [[Skills装太多怎么办-用Skills-Manager桌面应用统一管理]]