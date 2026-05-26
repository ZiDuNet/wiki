---
tags: [Scientific-Agent-Skills, 科研, Claude-Code, Skills]
sources: [科研Skills更新了，Claude Code，Codex和小龙虾都能用.md]
created: 2026-05-26
updated: 2026-05-26
---

# 科研Skills更新了：Claude Code、Codex和小龙虾都能用

**来源：** Claude/ferlich
**摄入日期：** 2026-05-26
**类型：** 工具评测

## 摘要

Scientific Agent Skills（原 Claude Scientific Skills）升级，139 个技能兼容 Claude Code、Cursor、Codex、小龙虾等所有主流 Agents。核心变化：28 个独立数据库技能合并为统一的 `database-lookup`（78 个数据库）；新增 27 个技能（分子动力学、糖基工程等）；删了 40 个过时技能。实测跑文献综述、数据分析、分子计算、文档处理四类任务，给出按场景推荐安装方案。

## 核心观点

### 升级要点

- **更名**：Claude Scientific Skills → Scientific Agent Skills（兼容所有 Agent Skills 标准）
- **技能数**：152 → 139（删 40 过时，加 27 新）
- **database-lookup**：28 个数据库技能合并为 1 个统一接口，覆盖 78 个公开科学数据库
- **搜索拆分**：perplexity-search → exa-search + paper-lookup + paperzilla

### 四类任务实测

| 任务类型 | 评价 | 关键发现 |
|----------|------|----------|
| 文献综述 | **超预期** | 10 数据库并行检索，自动去重，省约 2 天整理时间 |
| 数据分析 | 看你会不会用 | Scanpy 标准流程 OK，细胞类型注释粗糙，需领域判断力 |
| 分子计算 | 能用但需验证 | RDKit 默认参数可能不准，含特殊官能团分子需验证 |
| 文档处理 | **最稳定** | PDF→Markdown、PPTX、XLSX 格式转换确定性最强 |

### 按场景推荐安装

**科研写作**：literature-review + scientific-writing + citation-management + peer-review + latex-posters

**数据分析**：matplotlib + seaborn + statsmodels + scikit-learn + eda

**生物信息学**：scanpy + biopython + pydeseq2 + database-lookup

**药物发现**：rdkit + deepchem + diffdock + datamol + database-lookup

## 提及实体

- [[scientific-agent-skills]] — K-Dense-AI 开发的科研技能集，139 技能覆盖 9 大领域
- [[K-Dense-AI]] — Scientific Agent Skills 开发团队

## 涉及概念

- [[database-lookup]] — 统一的数据库查询技能，覆盖 78 个公开科学数据库
- [[文献综述技能]] — 10 数据库并行检索，按主题分组，标结论差异
- [[跨数据库串联]] — 一句话串联 ChEMBL → RDKit → PubMed，切换成本被抹掉
- [[依赖管理隐性账]] — 139 技能背后的 Python 依赖数量不小，版本冲突风险

## 安装命令

```bash
npx skills add K-Dense-AI/scientific-agent-skills
gh skill install K-Dense-AI/scientific-agent-skills scanpy  # 按需装单个
gh skill install K-Dense-AI/scientific-agent-skills --pin v2.39.0  # 锁定版本
```

**注意**：Windows 需要 WSL2，使用 Python 3.12+

## 项目地址

https://github.com/K-Dense-AI/scientific-agent-skills