---
title: 20 个 Agent Skills 盘点：先装这 5 个就够了
type: source-summary
tags: [Skills, Agent, OpenClaw, 工程落地, Skill安装]
sources: [微信公众号/Skills/20 个 Agent Skills 盘点：先装这 5 个就够了.md]
created: 2026-05-24
updated: 2026-05-24
---

# 20 个 Agent Skills 盘点：先装这 5 个就够了

> 📎 来源: [攀云信息科技](https://mp.weixin.qq.com/s?__biz=Mzk1NzY2ODc0MA==&mid=2247484982) | 时间: 2026-05-24

## 核心观点

OpenClaw 生产力翻倍的抓手是 **20 个 skills 的具体组合与执行顺序**，不是泛泛谈"AI 会更强"。核心建议：先装前 5 个，跑通后按场景扩展到 20 个。

## 20 个 Skills 分类

### 1) 发现与规划类

| Skill | 用途 |
|-------|------|
| find-skills | 解决"不会找技能"的入口问题 |
| brainstorming | 创意发散与规划 |
| skill-creator | 创建新 Skill |

### 2) 前端与设计质量类

| Skill | 用途 |
|-------|------|
| vercel-react-best-practices | 约束 React/Next.js 常见性能坑 |
| frontend-design | 提高 UI 质量，减少模板化输出 |
| web-design-guidelines | 补审查标准，避免低级 UX 错误 |
| vercel-composition-patterns | 组件组合模式 |
| vercel-react-native-skills | React Native 开发 |
| sleek-design-mobile-apps | 移动端设计 |
| ui-skills | UI 设计最佳实践 |

### 3) 自动化与内容生产类

| Skill | 用途 |
|-------|------|
| agent-browser | Agent 浏览器自动化 |
| browser-use | 浏览器操作 |
| remotion-best-practices | 视频内容场景提速 |
| pdf | PDF 处理 |

### 4) 后端/平台治理类

| Skill | 用途 |
|-------|------|
| supabase-postgres-best-practices | PostgreSQL 最佳实践 |
| azure-cost-optimization | Azure 成本优化 |
| cloudflare/skills | Cloudflare 配置 |
| redis/agent-skills | Redis 使用 |
| seo-audit | SEO 审计 |
| code-review-expert | 代码审查 |

## 高收益起步组合（前 5 个）

```bash
npx skills add vercel-labs/skills
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices
npx skills add anthropics/skills --skill frontend-design
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
npx skills add remotion-dev/skills --skill remotion-best-practices
```

**选择原因**：
- `find-skills`：先解决"不会找技能"的入口问题
- `vercel-react-best-practices`：直接约束 React/Next.js 常见性能坑
- `frontend-design`：提高 UI 质量，减少模板化输出
- `web-design-guidelines`：补审查标准，避免低级 UX 错误
- `remotion-best-practices`：视频内容场景直接提速

## 3 周落地方案

| 周次 | 重点 Skills | 目标 |
|------|-------------|------|
| 第 1 周 | find-skills + web-design-guidelines | 发现+审查打底 |
| 第 2 周 | vercel-react-best-practices + frontend-design | 前端与设计质量提升 |
| 第 3 周 | agent-browser 或 remotion-best-practices | 自动化扩展 |

每周复盘 3 件事：
1. 这个 skill 是否稳定提升输出质量
2. 是否与现有规则冲突
3. 下周是保留、替换还是淘汰

## 错误 vs 正确做法

| 场景 | 错误做法 | 正确做法 |
|------|----------|----------|
| 首次使用 | 一次装满 20 个 | 先装前 5 个，逐周扩展 |
| 评估效果 | 靠主观感觉 | 每个 skill 绑定 1 个指标（返工率/评审时长/交付时长） |
| 团队协作 | 个人随意加 skill | 统一白名单 + 周度复盘保留/淘汰 |

## 避坑提醒

1. 不要把 skill 当插件收藏夹，要当成**规则资产**
2. 没有验收指标的安装，基本等于没落地
3. "安装量最大"这类描述在没有公开口径时，建议标注为经验判断

## 相关实体

- [[OpenClaw]] — AI Agent 平台
- [[find-skills]] — Skill 发现工具
- [[frontend-design]] — 前端设计 Skill
- [[vercel-react-best-practices]] — React 最佳实践
- [[remotion-best-practices]] — 视频制作 Skill

## 相关概念

- [[Skill安装策略]] — 分批安装、指标绑定、周度复盘
- [[工程场景分类]] — 发现/前端/自动化/后端四类
- [[落地SOP]] — 3 周落地方案