---
title: "带图PDF 怎么转 Markdown？我终于找到了的最终方案"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["带图PDF 怎么转 Markdown？我终于找到了的最终方案_1.md"]
tags: [PDF转换, Markdown, MarkItDown, MinerU, 工具对比]
---

## Summary

作者实际折腾了多种带图 PDF 转 Markdown 方案后的经验总结。测试了 markitdown（速度快但丢图）、PyMuPDF（中文路径有坑、表格解析差）、marker-pdf（结构化但速度慢/图片过碎）、MinerU（质量最高但需 GPU）四种工具，最终结论：少量高质量用 MinerU 在线服务，批量用 marker-pdf+MinerU 互补。

## Key Claims

1. **markitdown**：速度快（秒级），但无法提取图片，图文混排文档不适用
2. **PyMuPDF (fitz)**：功能强大，但中文路径需 `glob.glob()` 特殊处理，表格解析效果一般
3. **marker-pdf**：自动识别文字+表格+图片，但速度慢（几十页需 20 分钟），图片可能拆解过细
4. **MinerU**：转换质量最高，表格/公式/图片完整保留，但完整版需 NVIDIA GPU（Mac/Windows 不适用）
5. **最终方案**：少量高质量用 MinerU 在线服务（mineru.net），批量用 marker-pdf 做整体转换 + MinerU 补充复杂表格

## Entities Mentioned

- [[MinerU]]（PDF 解析工具）
- [[markitdown]]（微软开源工具）
- [[PyMuPDF]]（fitz 库）

## Concepts

- [[PDF转换]] — 不同工具的优缺点对比和适用场景
- [[Markdown]] — 带图文档的转换目标格式

## Notable Quotes

> "带图 PDF 想批量转换：先用 marker-pdf 做整体转换，再人工用 MinerU 补充复杂表格。"
> "MinerU 在线地址：https://mineru.net/OpenSourceTools/Extractor"

## Limitations

- 作者为个人经验，工具选择有主观性
- MinerU 在线服务依赖网络和服务器可用性
