---
title: scientific-agent-skills
type: entity
tags: [Agent Skills, 科研自动化, GitHub项目]
sources: [AI科研全家桶133个技能包.md, 不要错过这10个本周火火火的-GitHub-开源项目.md, 科研Skills更新-Claude-Code-Codex-小龙虾都能用.md]
created: 2026-05-24
updated: 2026-05-26
---

# scientific-agent-skills

> GitHub: https://github.com/K-Dense-AI/scientific-agent-skills
> Stars: 25k+ (2026-05)
> 开发团队: K-Dense-AI

## 简介

将 AI 编程助手转化为"AI科学家"的技能包集合，原名 Claude Scientific Skills，2026 年升级更名兼容所有 Agent Skills 标准。

## 版本变化（152 → 139 技能）

- **database-lookup 统一接口**：28 个独立数据库技能合并为 1 个，覆盖 78 个公开科学数据库
- **删除过时技能**：删了 40 个过时技能
- **新增技能**：加 27 个新技能（分子动力学模拟、糖基工程、RNA velocity 分析等）
- **搜索拆分**：perplexity-search → exa-search + paper-lookup + paperzilla

## 核心能力

- 139 个科研技能（从 152 优化）
- 78 个科学数据库统一访问（database-lookup）
- 70+ Python 包优化（RDKit、Scanpy、PyTorch Lightning）
- 多平台兼容（Claude Code、Cursor、Codex、Gemini CLI、OpenClaw、WorkBuddy）

## 9 大领域

1. 生物信息学
2. 化学信息学
3. 临床研究
4. 机器学习
5. 材料科学
6. 地球与地理空间科学
7. 药物发现
8. 科学计算
9. 学术写作

## 安装

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

## 关联概念

- [[Agent Skills]]
- [[科研自动化]]
- [[科学数据库]]
- [[多代理协作]]

## 来源文章

- [[AI科研全家桶133个技能包]]