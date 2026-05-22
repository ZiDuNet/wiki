---
title: "带图PDF 怎么转 Markdown？我终于找到了的最终方案"
type: source-summary
created: 2026-05-23
updated: 2026-05-23
sources: ["带图PDF 怎么转 Markdown？我终于找到了的最终方案.md"]
tags: [PDF转换, Markdown, 知识库, 文档解析]
---

## Summary

作者系统对比了四款 PDF 转 Markdown 工具（markitdown、PyMuPDF、marker-pdf、MinerU），解决了带图表 PDF 在知识库导入场景下的转换难题。核心结论：MinerU 在线服务转换质量最高（完整保留表格、公式、图片），但需 GPU 完整版或在线 API；marker-pdf 适合批量转换作为中间步骤；纯文字 PDF 可用 markitdown 快速处理。最佳实践：批量用 marker-pdf + 人工补充高质量场景直接用 MinerU 在线。

## Key Claims

1. **markitdown（微软开源）**：速度快，几秒出结果；但无法提取图片，图文混排文档不适用。
2. **PyMuPDF（fitz）**：功能强大可提取文本和页面截图，但表格解析效果一般，中文路径需用 glob.glob() 处理。
3. **marker-pdf**：自动识别文字、表格、图片并输出结构化 Markdown，转换速度慢（几十页需近 20 分钟），复杂表格可能简化。
4. **MinerU**：转换质量最高，完整保留 PDF 结构（包括公式、表格、图片），输出干净 Markdown；但完整版需 NVIDIA GPU（占用 10G+ 内存），MacBook 用户只能使用轻量版或在线 API 服务。
5. **最终方案**：批量转换用 marker-pdf 做整体转换 + 人工核对 + MinerU 在线补充；少量高质量直接用 MinerU 在线服务。

## Entities Mentioned

- [[markitdown]] — 微软开源 PDF 转 Markdown 工具
- [[PyMuPDF]] — Python PDF 处理库（fitz）
- [[marker-pdf]] — 专门为 PDF 转 Markdown 设计的转换工具
- [[MinerU]] — 开源 PDF 解析工具，支持云端 API

## Concepts

- [[文档解析]] — 从 PDF 等文档中提取结构化内容的技术
- [[知识库导入]] — 将外部文档摄入知识库的预处理流程

## Notable Quotes

> "MinerU 的转换质量确实比 marker-pdf 更好，表格结构更完整，并且直接把图片里的表格转化为了文字版，图片引用更清晰。"

## Limitations / Bias

- 作者为 MacBook 用户，无法测试 NVIDIA GPU 环境下的完整版 MinerU
- 在线服务依赖网络连接，离线场景受限