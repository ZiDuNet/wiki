---
type: source-summary
title: 把一人企业方法论装进AI：9个Skill帮你从盘点到闭环搭起自己的小生意
sources: ['微信公众号/SkillManager/把_一人企业方法论_装进 AI：9 个 Skill，帮你从盘点到闭环搭起自己的小生意.md']
created: 2026-05-24
updated: 2026-05-24
---

# 把一人企业方法论装进AI：9个Skill

> 📎 来源: [不知名程序员指南](https://mp.weixin.qq.com/s?__biz=MzA3MDM4MTY2NA==&mid=2455509584&idx=1&sn=9a03a2caccf02929e2655db1039d981f) | 时间: 2026-05-24 11:49

## 核心摘要

方糖推出的 **OPC 技能集**，将易仁永澄的《一人企业方法论³》封装为 **9 个可调用的 AI Agent Skill**。这是一条"装上就能跑"的流水线，把已有的能力重组成一个轻资产、可验证、可复用的个人业务。

**一句话概括**：它不是又一个"教你做副业"的课，而是一条"装上就能跑"的流水线。

## 九步建盘流程

| 阶段 | 名字 | 功能 |
| --- | --- | --- |
| 00 | 总编排 | 判断当前步骤，控制节奏，会话续接 |
| 01 | [[资源盘点]] | 按8类（经验/人群/能力/关系/渠道/资产/约束/硬性边界）盘点手上有什么 |
| 02 | [[利基定位]] | "三环合一"找细分市场，6维评分筛候选 |
| 03 | 价值主张 | 拆 Jobs / Pains / Gains，给出多版本对比 |
| 04 | [[商业模式]] | Lean Canvas + 收费结构 + 最高风险假设 |
| 06 | [[MVP设计]] | 决定验证哪个假设、最小形式、成功标准 |
| 07 | [[转化闭环]] | 从触达到承接到成交的完整路径 |
| 08 | 资产沉淀 | 把跑出来的东西沉淀成可复用资产（按需触发） |
| 09 | 经营复盘 | 找当下真实瓶颈，定下一周期唯一重点（按需触发） |

**设计原则**：01 → 07 严格线性，不跳步；08、09 按需触发。

## 真实案例：室内设计师林夏

**背景**：
- 29岁，二线城市，室内全案设计6年
- 公司派单从每月5–8个掉到1–2个，底薪三千
- 不能裸辞：存款只够4–5个月
- 时间窗口：工作日晚9–12点 + 周末1天

**关键节点**：

### 01 资源盘点
- 私域50+深度老客户、200+沉睡咨询
- 高信任老客户5–8个能转介绍/做实景拍摄
- 12–15套高清实景 + 30套施工前后对比
- 硬性边界：不碰公司准客户、不垫资、不接传统全包私单

### 02 利基定位（AI打分）
- A. 报价防坑陪跑（28/30）
- B. 自装翻车救火（24/30）
- C. 预算内高颜值平替设计（24/30）
- 最终选择 **A + C 组合**

### 03 价值主张
> 先帮你守住预算（防坑），再把省下的钱花到最出效果的地方（平替设计）

**理由**：只做降风险会沦为低价审单，只做结果型会被独立设计师红海卷死，两个合一才有壁垒。

### 06 MVP设计（锁死滑回定制苦力）
- 第1单：高信任老客户做校准
- 第2–3单：真实付费客户跑标准包 + 2次答疑
- 成功标准：单客 ≤ 3小时、至少拒绝1次非标需求且客户仍认可、晚12点前收工

### 07 转化闭环
**用表单承接，而不是直接私聊**：过滤白嫖、预收集信息、给自己心理缓冲带。

## 产品力三点

1. **产出是文档，不是聊天记录**
   - inventory.md、three-ring-analysis.md、candidates.md、positioning-statement.md、lean-canvas.md、risky-assumptions.md、mvp-spec.md、conversion-path.md 等
   - 这些是下一步的输入，也是日后复盘的底稿

2. **总编排负责"不让你跳步"**
   - 建盘最常见失败：跳过盘点直接想定位，跳过MVP直接做产品
   - 每次新会话能恢复上次进度

3. **模块可单独使用**
   - 如 `/opc-niche-positioning 分析 Todo 产品的利基市场`
   - 既是一条流水线，也是9个独立工具

## 安装使用

走 Skill 标准协议，Claude Code、CodeX 等支持 Skill 的客户端都能装：

```bash
# 1. 装总编排（必装）
npx skills add https://github.com/easychen/opc-methodology/skills/opc-orchestrator

# 2. 装各阶段 Skill
npx skills add https://github.com/easychen/opc-methodology/skills/opc-resource-audit
npx skills add https://github.com/easychen/opc-methodology/skills/opc-niche-positioning
npx skills add https://github.com/easychen/opc-methodology/skills/opc-value-proposition
npx skills add https://github.com/easychen/opc-methodology/skills/opc-business-model-design
npx skills add https://github.com/easychen/opc-methodology/skills/opc-mvp-designer
npx skills add https://github.com/easychen/opc-methodology/skills/opc-conversion-loop
npx skills add https://github.com/easychen/opc-methodology/skills/opc-asset-ops
npx skills add https://github.com/easychen/opc-methodology/skills/opc-dashboard-review
```

启动命令：
```bash
# Claude Code
/opc-orchestrator

# CodeX
@opc-orchestrator
```

> ⚠️ 注意：非首次运行需清空对话目录下的 `opc-doc` 目录，否则会载入上次数据。

## 核心洞察

1. **AI Skill 形态第一次"真的对不起"方法论**：方法论从书/课传播变成可调用步骤，损耗几乎为零
2. **最值钱的是"拦着你别瞎做"**：AI反复劝退、设边界、定成功标准——这正是个人创业最缺的"外部理性"
3. **适合谁**：手上已有东西（经验/客户/内容/关系），但卡在"怎么重组成一门小生意"的人
4. **不适合谁**：想要"复制粘贴就能赚钱"的项目党——它给骨架，肉得自己长

## 相关链接

- 项目主页：https://opc-skills.ft07.com/
- 视频讲解：B站 BV1JMDQBiEjx
- 方法论原作：易仁永澄《一人企业方法论³》

## 相关实体

- [[一人企业方法论]]
- [[OPC技能集]]
- [[易仁永澄]]

## 相关概念

- [[一人公司]]
- [[利基定位]]
- [[MVP设计]]
- [[资源盘点]]
- [[九步建盘]]
- [[商业模式]]
- [[转化闭环]]
- [[Skill设计]]