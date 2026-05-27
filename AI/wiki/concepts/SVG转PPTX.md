---
type: concept
created: 2026-05-28
updated: 2026-05-28
---

# SVG转PPTX

**Keywords:** svg, pptx, DrawingML, 中间格式, 转换管线

## 简介

SVG 转 PPTX 是 [[ppt-master]] 的核心技术管线。SVG 作为中间格式，由 AI 生成后转换为原生 DrawingML 形状，实现真正可编辑的 PPTX。

## 工作原理

### SVG 作为中间格式

- **每个 SVG 文件 = PPT 的一页**
- AI 先生成 SVG（定义布局、文字、图形）
- `svg_to_pptx.py` 将 SVG 转换为 DrawingML

### SVG → DrawingML 转换管线

包括：
- **图案填充**
- **饼图弧线端点修正**
- **旋转 pivot 修复**

### PNG+SVG 双模式兼容

如果 `svglib` 的系统级 `cairo` 库装不上：
- `svg_to_pptx.py` 自动用 PNG+SVG 双模式兼容
- 核心功能不受影响

## SVG 编写要点

### 1. XML 转义

SVG 是 XML 格式，`<` 和 `>` 必须转义：

```
< → <
> → >
```

- Python 关系运算符最容易出错：`<`、`>`、`<=`、`>=`
- 忘记转义会导致导出报错

### 2. 中文字体

必须指定支持中文的字体，否则显示为方块：

```svg
font-family="Microsoft YaHei, SimHei, sans-serif"
```

### 3. 文件命名排序

用数字前缀排序，导出时按文件名顺序生成幻灯片：

```
01_cover.svg
02_topic1.svg
03_topic2_1.svg
...
```

### 4. SVG 基本结构示例

```svg
<svg viewBox="0 0 1920 1080">
  <rect width="1920" height="1080" fill="#1a1a2e"/>
  <text x="960" y="540" text-anchor="middle"
        font-size="42" font-weight="bold" fill="#e94560"
        font-family="Microsoft YaHei, SimHei, sans-serif">
    页面标题
  </text>
</svg>
```

## 技术优势

- **原生可编辑**：文字框、图表、图形都是 PowerPoint 对象，点一下就编辑
- **设计自由度**：SVG 定义任意布局，不受模板限制
- **AI 驱动**：AI 生成 SVG，再转标准 PPTX

## 相关实体

[[ppt-master]] [[python-pptx]] [[svglib]]

## 相关概念

[[DrawingML]] [[PDF转PPTX]] [[PPT制作]] [[SVG绘图]]

## Mentioned In

- [[PPT-Master教程-PDF一键转可编辑PPT]] — SVG 编写要点详解
- [[ppt-master-AI-造-PPT的正确姿势]] — SVG → DrawingML 转换管线