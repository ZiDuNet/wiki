---
type: concept
created: 2026-05-28
updated: 2026-05-28
---

# PDF转PPTX

**Keywords:** pdf, pptx, 转换, 扫描版, OCR, 文档转换

## 简介

PDF 转 PPTX 是 AI Agent 办公场景中的常见需求。传统方案存在两大痛点：1) 生成的 PPT 是"死"的（整页大图或固定模板）；2) 扫描版 PDF 无法直接提取文字。

## PPT Master 的 PDF 转 PPTX 工作流

### 可搜索文字 PDF（Word 转 PDF、带 OCR 的 PDF）

```bash
# 自动提取文字并生成大纲
python3 skills/ppt-master/scripts/source_to_md/pdf_to_md.py \
  "/path/to/document.pdf" -o /tmp/output.md
```

- **全自动**：AI 自动提取文字和结构
- **质量最高**：直接生成可编辑 SVG → DrawingML

### 扫描版 PDF（无文字层）

- **必须人工介入**：逐页阅读图片，手动提取核心知识点
- **最耗时环节**：AI 工具都绕不过 OCR 这一步
- **流程**：扫描版 PDF → OCR/人工提取 → SVG → PPTX

## 实战案例

- **94页扫描版 PDF → 14页可编辑 PPT**：
  - 《2023信息技术宝典手册（Python版）》
  - 纯扫描版，每页都是一张图片
  - 输出：按专题重新组织的复习概览 PPT

## 关键洞察

- **不是逐页转换**：是"理解→重构"的工作方式，AI 读完全部内容后按专题重新组织
- **适合做概览**：浓缩精华，不适合需要忠实保留原文的场景
- **逐页转换需要进阶**：需 OCR 或人工提取，保留原始内容完整性

## 相关实体

[[ppt-master]] [[python-pptx]] [[PyMuPDF]] [[Claude-Code]]

## 相关概念

[[OCR]] [[SVG转PPTX]] [[DrawingML]] [[PPT制作]] [[AI办公]] [[文档处理]]

## Mentioned In

- [[PPT-Master教程-PDF一键转可编辑PPT]] — 94页扫描版 PDF 转 14页 PPT 实战教程
- [[ppt-master-AI-造-PPT的正确姿势]] — PDF 转 PPTX 能力边界分析