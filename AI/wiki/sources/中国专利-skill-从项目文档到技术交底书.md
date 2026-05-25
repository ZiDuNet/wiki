---
title: "中国专利.skill：从项目文档到技术交底书"
type: source-summary
created: 2026-05-25
updated: 2026-05-25
sources: ["中国专利.skill：从项目文档到技术交底书.md"]
tags: [Skill, Patent, Claude-Code, Agent, GitHub, 专利]
---

# 中国专利.skill

## Summary

handsomestWei 开源了 patent-disclosure-skill，一个 Agent Skill，自动完成从项目文档挖掘专利点、检索现有专利、生成技术交底书的完整流程。解决了研发工程师写专利交底书时"挖点难、检索难、写图难、格式难"四大痛点。

## Key Claims

1. 专利交底书四大痛点：挖专利点、检索现有专利、画系统框图/流程图、写成代理可改的格式
2. patent-disclosure-skill 7 步流程：项目扫描→专利点挖掘→查新检索→交底书成稿→自检→迭代管理→交付
3. 查新优先使用国家知识产权局·中国专利公布公告站（epub.cnipa.gov.cn），查不到时降级 WebSearch
4. 输出包含：脱敏交底书模板 + Mermaid 系统框图/流程图（自动转 PNG）+ 可交付 Word 文件
5. 自检逻辑闭环、公式参数一致性检查；迭代管理保留修订对话记录

## Entities Mentioned

- [[patent-disclosure-skill]] — handsomestWei 开源的专利交底书 Agent Skill
- [[handsomestWei]] — GitHub 开源作者
- [[Claude-Code]] — Skill 兼容的 AI 编程环境
- [[Cursor]] — Skill 兼容的 AI IDE
- [[Mermaid]] — 图表绘制语言（自动转 PNG）
- [[Playwright]] — 国知局站精准爬取工具
- [[python-pptx]] — Word 文件生成依赖（文中引用）

## Concepts

- [[专利交底书]] — 技术人和专利代理人之间的桥梁文档
- [[专利点挖掘]] — 从项目代码和文档中分析提取可申请专利点
- [[查新检索]] — 申请前检索现有专利确认创新性
- [[Agent-Skill]] — 兼容 Claude Code/Cursor 的标准 Agent 能力包格式

## Notable Quotes

> "专利交底书是技术人和法律之间的桥梁。以前这座桥全靠人力搭，现在有人帮你用 AI 搭好了。"

## Limitations / Bias

- Skill 主要面向中国专利申请流程，不适用于其他国家和地区
- 自动化图表（Mermaid 转 PNG）效果受模板限制，复杂系统框图可能需手动调整
- 专利点的挖掘质量依赖输入项目文档的完整性
