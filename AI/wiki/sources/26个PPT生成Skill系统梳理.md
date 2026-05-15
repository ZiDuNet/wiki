---
title: 26个PPT生成Skill，我做了一次系统梳理
type: source-summary
tags: [PPT, Skill, AI生成PPT, 工具对比]
sources: [../微信公众号/PPT skill/26个PPT生成Skill，我做了一次系统梳理.md]
created: 2026-05-16
updated: 2026-05-16
---

# 26个PPT生成Skill系统梳理

## 核心摘要

2026 年 Agent Skills Hub 上 PPT & Presentation 分类收录了 25 个项目，总 Star 数超过 7 万。本文对整个赛道做了系统性梳理，按技术路线分为 HTML 网页演示、原生 PPTX、AI 图像驱动、MCP 协议层、垂直场景专用、综合设计平台六大派系，并回答实际问题：**如果你今天要做 PPT，应该用哪一个**。

## 技术路线全景

### HTML 网页演示派
单文件输出、浏览器打开即用。视觉上限极高（CSS 动画、WebGL 特效、Canvas 粒子），但交付后不可编辑。

| Skill | Star | 特点 |
|---|---|---|
| frontend-slides | 17.5k | 12 套视觉预设，"show don't tell"选风格 |
| guizang-ppt-skill | 8.8k | 电子杂志风，5 套主题色，不允许自定义 hex |
| html-ppt-skill | 3.8k | 36 套主题，演讲者模式最突出 |
| apple-bento-grid | 171 | 只做 Apple 风格 Bento Grid 卡片 |
| deepseek-v4-deep-dive | 193 | AI 模型深度解读成品+模板 |

### 原生 PPTX 派
输出真正的 .pptx 文件，文字框/形状/图表可点击编辑，客户拿到能改。

| Skill | Star | 特点 |
|---|---|---|
| ppt-master | 16.6k | SVG→DrawingML，逐字可编辑，模板复刻 |
| ppt-agent-skills | 714 | 软件工程流程，code-driven 框架 |
| mckinsey-pptx | 426 | 40 个麦肯锡模板，AI 解释决策 |
| claude-office-skills | 631 | PPTX/DOCX/XLSX/PDF 全覆盖 |
| slide-deck-ai | 354 | 和 AI 来回打磨，轻量快速 |
| odin-slides | 147 | Word 文档→PPT，专为长报告设计 |
| Mck-ppt-design-skill | 135 | 70 套咨询风格布局 |

### AI 图像驱动派
用 GPT Image 2、NanoBanana 等模型逐页生成视觉图片，视觉效果最好但修改性受限。

| Skill | Star | 特点 |
|---|---|---|
| NanoBanana-PPT-Skills | 2.7k | NanoBanana 模型生成图片+视频 |
| gpt_image_2_skill | 2.1k | 提示词画廊，覆盖科研/海报/UI |
| ppt-image-first | 799 | image-first，跨 Agent |
| gpt-image2-ppt-skills | 557 | 图像级仿版式换内容 |

### MCP/协议层
给 LLM 装上操作 PowerPoint 的手，不直接生成 PPT。

| Skill | Star | 特点 |
|---|---|---|
| Office-PowerPoint-MCP-Server | 1.7k | python-pptx 包装成 MCP Server |
| PPTAgent | 4.4k | Reflective 机制，生成后自检 |
| mcp-server-okppt | 66 | SVG 嵌入 PPTX 保留矢量 |

### 垂直场景专用

| Skill | Star | 特点 |
|---|---|---|
| academic-pptx-skill | 387 | 学术讲座、论文答辩、行动式标题 |
| colloquium | 190 | markdown native，学者直接讲课 |
| fullstack-mkt-skills | 385 | PowerShell，营销内容流水线 |
| ppt-translator | 61 | 翻译保留格式，本地化刚需 |

### 综合设计平台

| Skill | Star | 特点 |
|---|---|---|
| open-design | 40.8k | 设计平台，PPT 是能力出口之一 |

## 选型决策框架

**"出稿"还是"磨稿"？**

- **出稿**（快、能用、能出门）：Gamma（海外）、AI PPT.cn（国内中文办公）、NotebookLM（配 podcast）
- **磨稿**（打磨、有自己的声音、多版迭代）：Codex + 3 款 skill（frontend-slides、guizang-ppt-skill、ppt-master）

**内容类型决定工具**：
- 舞台演讲/发布会 → frontend-slides
- 品牌发布/设计向 → guizang-ppt-skill
- 行业研究/数据驱动 → ppt-master
- 数据可视化/咨询 → ppt-master
- 年度公开演讲/嵌入交互 → Codex

## 相关工具

- [[Claude]] — Agent 载体
- [[Vibe-Coding]] — 开发方式
- [[html-ppt-skill]] — HTML 演示派代表
- [[ppt-master]] — PPTX 派旗舰
