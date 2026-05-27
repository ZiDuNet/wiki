---
tags: [PPT-Master, PDF转PPTX, 教程, 实战, DrawingML, SVG转PPTX, 扫描版PDF]
sources: [PPT Master/PPT Master 教程：PDF 一键转可编辑 PPT，手把手带你从安装到出片.md]
created: 2026-05-28
updated: 2026-05-28
---

# PPT Master 教程：PDF 一键转可编辑 PPT

**来源：** PPT Master/PPT Master 教程：PDF 一键转可编辑 PPT，手把手带你从安装到出片.md  
**摄入日期：** 2026-05-28  
**原始链接：** [神经达尔加文](https://mp.weixin.qq.com/s?__biz=MzIwODM4ODA1MA==&mid=2247483865&idx=1&sn=946dd867764e608a3c1fd56de85c8292)  
**类型：** 实战教程/教程

## 摘要

一篇完整的 PPT Master 实战教程，以教师视角演示如何将94页扫描版 PDF《2023信息技术宝典手册（Python版）》转换为14页可编辑 PPT。覆盖从安装、环境搭建、项目初始化、SVG 编写、PPTX 导出到 AI 校验的全流程，并总结 PPT Master 的能力边界。

## 核心观点

### 痛点
- 传统 AI PPT 工具生成的 PPT 是"死"的：整页大图改字要重做，或套固定模板排版受限
- PDF 来源多样：扫描件（无文字层）、截图转 PDF、Word 转 PDF，格式保留但改 PPT 需从头排版

### PPT Master 的差异化
- **真正可编辑**：生成原生 DrawingML 形状，每个元素都能独立点击、拖拽、改颜色、改字体
- **agent 驱动 workflow**：跑在 AI IDE（Claude Code/Cursor）里，零后端、零数据库、零订阅

### 能力边界

**擅长场景：**
| 场景 | 说明 |
|------|------|
| Word/Markdown → PPT | 全自动，质量最高 |
| 网页链接 → PPT | 支持微信公众号文章 |
| PDF（可搜索文字）→ PPT | 自动提取文字和结构 |
| 多格式混输入 | PDF+Word+图片一起喂 |

**不擅长场景：**
| 场景 | 说明 |
|------|------|
| 扫描版 PDF → PPT | 需要先 OCR 或人工提取文字 |
| 复杂数据图表 | 图表能力有限，有"伪图表"问题 |
| 独立运行 | 需要在 AI IDE 中对话驱动 |

## 实战流程

### 安装与环境搭建

```bash
# 克隆项目
git clone --depth 1 https://github.com/hugohe3/ppt-master.git

# 国内镜像
git clone --depth 1 https://atomgit.com/hugohe3/ppt-master.git

# 安装依赖
pip3 install python-pptx edge-tts svglib reportlab PyMuPDF \
  mammoth markdownify ebooklib nbconvert openpyxl \
  Pillow numpy requests beautifulsoup4 flask openai

# macOS 需要先装 cairo
brew install cairo
```

### 项目结构

```
projects/baodian_ppt169_YYYYMMDD/
├── exports/          # 导出的 PPTX
├── images/           # 图片资源
├── notes/            # 演讲者备注
├── sources/          # 源文件
├── svg_output/       # 每页 SVG（核心！）
└── templates/        # 模板
```

### SVG 编写要点

1. **XML 转义**：`<` → `<`，`>` → `>`
2. **中文字体**：`font-family="Microsoft YaHei, SimHei, sans-serif"`
3. **文件命名**：数字前缀排序，导出按文件名顺序生成幻灯片

### 导出命令

```bash
python3 skills/ppt-master/scripts/svg_to_pptx.py \
  projects/baodian_ppt169_YYYYMMDD \
  -o ~/Her工作间/信息技术宝典复习概览.pptx
```

## 校验与修正

用 AI 做三件事：
1. **逐页核查知识点**：对照原 PDF 扫描件检查准确性
2. **联网验证关键细节**：如 `math.ceil(-2.3)` 到底是 -2 还是 -3
3. **Python 实际运行验证**：把有疑问的代码直接跑一遍

**核查发现的错误示例：**
| 位置 | 原文 | 正确 | 性质 |
|------|------|------|------|
| 第3页 字符串切片 | `S[5:-1]="022"` | `S[5:]="2"` | 事实错误 |

## 适合人群

- **教师**：把教案、教辅转成课件 PPT
- **职场人**：把方案、报告转成演示文稿
- **学生**：把论文、笔记转成答辩 PPT

## 技术洞察

- **94页扫描版PDF → 14页PPT**：是"理解→重构"的工作方式，按专题重新组织，适合做复习概览
- **如果需要逐页转换**：需 OCR 或人工提取文字，保留原始内容完整性
- **SVG 是核心**：每个 SVG 文件就是 PPT 的一页，AI 先生成 SVG，再转 DrawingML

## 涉及实体

- [[ppt-master]] — 开源 AI PPT 生成工具，开发者 [[hugohe3]]
- [[hugohe3]] — PPT Master 项目作者，GitHub
- [[Claude-Code]] — 主要使用环境
- [[Cursor]] — 替代 IDE 选项

## 涉及概念

- [[PDF转PPTX]] — PDF 到 PPTX 的转换工作流
- [[DrawingML]] — PowerPoint 原生形状描述语言
- [[SVG转PPTX]] — SVG 作为中间格式转 DrawingML
- [[PPT制作]] — AI Agent PPT 生成的核心场景
- [[OCR]] — 扫描版 PDF 处理的前提步骤

## 相关链接

- GitHub：https://github.com/hugohe3/ppt-master
- 在线预览：https://hugohe3.github.io/ppt-master
- 文档：项目内 `docs/zh/` 目录
- 示例：项目内 `examples/` 目录（20+ 个完整示例）
- FAQ：`docs/zh/faq.md`