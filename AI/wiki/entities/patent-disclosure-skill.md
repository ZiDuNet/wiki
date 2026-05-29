---
tags: [开源, 专利, AI工具, Python, Mermaid]
sources: [patent-disclosure-skill-716星专利交底书.md]
created: 2026-05-30
updated: 2026-05-30
---

# patent-disclosure-skill

**类型:** 开源工具/Skill
**Star:** 716+
**GitHub:** handsomestWei/patent-disclosure-skill

## 简介

专利技术交底书自动生成 Skill。把研发配合写专利的时间从 3 天缩短到 30 分钟。扫描本地代码仓库或设计文档，自动挖掘专利点，输出符合国知局标准、带高清图表的 Word 版技术交底书。适用于软件/硬件专利申请。

## 核心功能

- **原材料自动清洗**：将 .docx/.pptx 等 Office 二进制文件转换为 Markdown 纯文本，避免 AI 解析混乱
- **硬核查新**：用 Playwright 爬国知局官方专利公告网站，降级方案 Google Patents
- **图示自动化渲染**：大模型输出 Mermaid 代码，调用 Node.js 渲染引擎生成 PNG，嵌入 Word
- **LaTeX 公式一致性闭环**：扫描公式在 Word 里的兼容性，检查前后参数一致性
- **多轮修订和审计追踪**：增量合并，维护修订对话记录，追溯每轮修改来龙去脉

## 相关概念

[[专利技术交底书]], [[AI文档自动化]], [[Mermaid]], [[Playwright]]