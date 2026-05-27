---
type: concept
created: 2026-05-10
updated: 2026-05-10
---

# PPT制作

**Keywords:** ppt, 幻灯片, pptx, slide, 演示文稿

## 简介

PPT制作是 AI Agent 生态中最热门的应用场景之一。随着 AI 工具的发展，PPT 的制作方式正在经历从传统 Office 工具到 AI 驱动的自动化生成的转变，尤其以 HTML-based PPT 和 Skill 驱动的 PPT 生成为代表。

## 主流 AI PPT 方案

### 1. HTML-based PPT（PPT 2.0）
AI 时代 PPT 的未来形态可能是 HTML。通过 [[html-ppt-skill]] 等工具，将 PPT 做成 HTML 格式：
- 每页都是独立的 HTML，完全可编辑
- 支持动画、交互、响应式布局
- 不依赖 [[python-pptx]] 等传统库
- 可通过浏览器直接展示

### 2. PPT-Master（传统 PPTX 方案）
[[ppt-master]] 方案能将任何文档转换为本地可编辑的 PPTX：
- 输入 Markdown/文档，输出标准 .pptx 文件
- 保持传统 Office 兼容性
- 适合需要交付给非技术人员的场景

### 3. Skill 驱动的 PPT 生成
通过 Agent + Skill 组合实现全流程自动化：
- [[OpenClaw]] + PPT Skill：一句话生成 PPT
- [[Hermes]] + PPT Skill：从"想到"到"做到"的全流程实操
- [[Claude-Code]] + PPT Skill：结合飞书、微信实现端到端生成

## 关键洞察

- **不要指望一次性生成完美 PPT**：AI 生成 PPT 需要分步骤、迭代优化
- **信息整合能力是核心**：PPT 考验对信息的整合和精简提炼能力，一页一个核心观点
- **流程比工具重要**：先确定内容框架，再交给 AI 生成视觉，最后人工微调
- **HTML PPT 是趋势**：AI 生成的 HTML PPT 比 PPTX 更灵活、更可控

## 按场景选择工具

| 场景 | 推荐方案 | 说明 |
|------|----------|------|
| 快速汇报 | [[OpenClaw]] + PPT Skill | 一句话生成，适合日常汇报 |
| 精美展示 | [[html-ppt-skill]] | HTML 格式，视觉表现力强 |
| 正式交付 | [[ppt-master]] | 标准 PPTX，兼容性好 |
| 学术演示 | [[Claude-Code]] + Skill | 结合 [[Obsidian]] 知识库 |

## Related Entities

[[Claude-Code]] [[Cursor]] [[Codex]] [[Windsurf]] [[MCP]] [[ppt-master]] [[html-ppt-skill]] [[baoyu-skills]] [[Hermes]] [[OpenClaw]]

## Related Concepts

[[Skill设计模式]] [[Harness-Engineering]] [[Skill编排]] [[Agent开发]] [[MCP协议]] [[AI编程]] [[内容创作]] [[数据可视化]] [[PDF转PPTX]] [[SVG转PPTX]]

## Mentioned In

- [[AI时代，PPT的未来是HTML，一个神奇的-Skills-推荐]] — AI 时代 PPT 的未来是 HTML
- [[AI时代，PPT的未来是HTML，一个神奇的-Skills-推荐]] — PPT Master 推荐
- [[Skills商店来了：5w+人在用的热门Skills，我试了一遍]] — Skills 商店 PPT 相关评测
- [[Skill配方｜我终于找到了好用的PPT工具把已有方案内容自动生成专业可编辑PPTX]] — PPT 工具配方
- [[一句话生成架构图！这个开源-Skill-让你告别熬夜画图]] — 一句话生成架构图
- [[假期结束，打工人上线：5-个做-PPT-的-AI-工具skill，按场景选就够了]] — 5 个 PPT AI 工具按场景选择
- [[分享6个宝藏Skills]] — 宝藏 Skills 推荐
- [[告别AI-PPT1.0，带你沉浸式体验AI-PPT2.0的科技感，进入万物皆可PPT的时代]] — AI PPT 2.0 体验
- [[PPT-Master教程-PDF一键转可编辑PPT]] — PDF 一键转可编辑 PPT 实战教程
