---
title: "PDF 处理 Skill：让 Agent 真正会读、会拆、会抽取 PDF"
type: source-summary
created: 2026-05-25
updated: 2026-05-25
sources: ["PDF 处理 Skill：让 Agent 真正会读、会拆、会抽取 PDF.md"]
tags: [Agent, PDF, Skill, 办公自动化, Claude]
---

# PDF 处理 Skill

## Summary

PDF 是办公室里最像"黑盒"的文件：表格错位、扫描件无法提取、合同风险项找不到。PDF 处理 Skill 通过"判断类型→选择方法→输出可复查结果"的固定流程，让 Agent 真正做到可交付的 PDF 处理，而不只是写几句空泛的总结。

## Key Claims

1. PDF 处理的核心不是 AI 能力，而是流程设计：判断类型→渐进式加载规则→输出自检
2. 合同初筛 Skill 的价值在于输出可复查的风险清单（带页码、风险说明、修改建议），而不是一句"建议请法务确认"
3. 报价单抽取最重要的是标出"未识别项"，而不是假装全部成功
4. PDF Skill 和普通提示词的根本区别：普通提示词靠临场发挥，Skill 靠固定流程交付
5. Skill 调度采用渐进式加载：合同任务只加载合同清单，不一次性加载所有规则

## Entities Mentioned

- [[pdf-processing-skill-zh]] — 中文增强版 PDF 处理 Skill
- [[python-pptx]] — 用于 PPTX 文件处理的 Python 库（文中引用）
- [[Mermaid]] — 图表绘制语言（文中引用）
- [[Playwright]] — 浏览器自动化工具（文中引用）

## Concepts

- [[PDF-处理流程]] — 判断类型→选择方法→输出可复查结果的固定流程
- [[Skill-调度模式]] — 渐进式加载，避免一次性加载所有规则
- [[合同初筛]] — 定位合同风险条款并给出修改建议的 Agent Skill 场景
- [[表格-异常检测]] — 报价单/BOM 等表格抽取时标记未识别单元格
- [[Agent-Skill]] — 包含 SKILL.md 和可选 scripts/references/assets 的能力包

## Notable Quotes

> "普通提示词靠临场发挥，Skill 靠固定流程交付。"

> "PDF Skill 不会假装全都识别成功，而是把'不确定项'标出来，这对真实工作非常重要。"

> "Skill 的关键是设计一套'判断—加载—执行—检查'的流程，不是写一堆提示词。"

## Limitations / Bias

- 作者立场偏向办公场景（合同/报价单），技术报告/学术论文场景未覆盖
- PDF Skill 是初筛工具，不是法律意见，不能替代专业律师判断
- 扫描件 PDF 需要 OCR 或视觉识别，Skill 默认处理的是文字 PDF
