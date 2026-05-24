# academic-research-skills — 学术论文写作全流程管线

> GitHub: https://github.com/Imbad0202/academic-research-skills
> Stars: ~20k (2026-05) | 协议: MIT | 版本: v3.8.0 | 语言: Markdown/Python
> 技术栈: Claude Code Skills、多代理协作、引用审计

## 一句话简介

**专为 Claude Code 设计的学术研究技能套件，把写论文全流程串成管线：查资料→写→审→改→定稿。采用"人机协同而非全自动化"理念，AI处理基础工作，研究者专注于核心决策。**

## 核心特点

- **Deep Research**: 13 个代理 / 7 种模式（含 Socratic 引导、PRISMA 系统综述）
- **Academic Paper**: 12 个代理 / 10 种模式（含风格校准、写作质量检查）
- **Academic Paper Reviewer**: 7 个代理 / 6 种模式（0-100 质量评分）
- **Academic Pipeline**: 10 阶段编排器（含完整性验证门控）
- **反幻觉机制**: 引用审计、跨模型验证、引用-主张一致性审计（v3.8 新增）

## 快速安装

```bash
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

## 架构

```
┌─────────────┐    ┌─────────────┐    ┌──────────────┐
│ Deep Research│───→│Academic Paper│───→│   Reviewer   │
│  13 agents   │    │  12 agents   │    │  7 agents    │
│  7 modes     │    │  10 modes    │    │  6 modes     │
└─────────────┘    └─────────────┘    └──────────────┘
         └──────────────┬──────────────┘
                   Academic Pipeline
                   10-stage orchestrator
                   + integrity gates
```

## 适用场景

- 研究生撰写学术论文全流程辅助
- 系统综述（PRISMA）自动化文献筛选
- 论文投稿前质量审查和引用校验
- 科研团队协作写作规范化

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
