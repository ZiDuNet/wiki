---
type: entity
name: OPC技能集
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# OPC技能集

**类型:** 实体（Skill 项目）
**出品方:** 方糖
**提及文章数:** 1

## 简介

OPC 技能集是方糖团队将易仁永澄《一人企业方法论³》封装成的 **9 个可调用 AI Agent Skill**。这是一条"装上就能跑"的流水线，帮助个人把已有的能力重组成一门小生意。

**核心定位**：不是"教你做副业"的课，而是"装上就能跑"的流水线。

## 9 个 Skill 清单

| Skill 名称 | 功能 | 对应方法论步骤 |
| --- | --- | --- |
| `opc-orchestrator` | 总编排，判断当前步骤，控制节奏 | 00 |
| `opc-resource-audit` | 按8类盘点手上有什么 | 01 |
| `opc-niche-positioning` | "三环合一"找细分市场，6维评分 | 02 |
| `opc-value-proposition` | Jobs/Pains/Gains 分析 | 03 |
| `opc-business-model-design` | Lean Canvas + 收费结构 | 04 |
| `opc-mvp-designer` | 决定验证假设、最小形式、成功标准 | 06 |
| `opc-conversion-loop` | 触达→承接→成交完整路径 | 07 |
| `opc-asset-ops` | 沉淀可复用资产（按需触发） | 08 |
| `opc-dashboard-review` | 找瓶颈，定下周期重点（按需触发） | 09 |

## 安装方式

走 Skill 标准协议，支持 Claude Code、CodeX 等：

```bash
# 总编排（必装）
npx skills add https://github.com/easychen/opc-methodology/skills/opc-orchestrator

# 各阶段 Skill
npx skills add https://github.com/easychen/opc-methodology/skills/opc-resource-audit
npx skills add https://github.com/easychen/opc-methodology/skills/opc-niche-positioning
npx skills add https://github.com/easychen/opc-methodology/skills/opc-value-proposition
npx skills add https://github.com/easychen/opc-methodology/skills/opc-business-model-design
npx skills add https://github.com/easychen/opc-methodology/skills/opc-mvp-designer
npx skills add https://github.com/easychen/opc-methodology/skills/opc-conversion-loop
npx skills add https://github.com/easychen/opc-methodology/skills/opc-asset-ops
npx skills add https://github.com/easychen/opc-methodology/skills/opc-dashboard-review
```

## 启动方式

```bash
# Claude Code
/opc-orchestrator

# CodeX
@opc-orchestrator
```

## 输出文档

每跑完一步，自动落地结构化文件：

- `inventory.md` — 资源盘点结果
- `three-ring-analysis.md` — 三环合一分析
- `candidates.md` — 利基候选
- `positioning-statement.md` — 价值主张
- `lean-canvas.md` — 商业模式画布
- `risky-assumptions.md` — 最高风险假设
- `mvp-spec.md` — MVP规格
- `conversion-path.md` — 转化路径

**注意**：非首次运行需清空 `opc-doc` 目录。

## 产品力特点

1. **产出是文档**：不是聊天记录，是下一步输入和复盘底稿
2. **不让你跳步**：总编排拦住常见失败模式
3. **模块可单独使用**：如 `/opc-niche-positioning 分析 Todo 产品`

## 相关文章

- [[把一人企业方法论装进AI-9个Skill]]

## 相关实体

- [[一人企业方法论]] — 方法论原作
- [[易仁永澄]] — 方法论创始人

## 相关概念

- [[一人公司]]
- [[九步建盘]]
- [[Skill设计]]
- [[Skill编排]]