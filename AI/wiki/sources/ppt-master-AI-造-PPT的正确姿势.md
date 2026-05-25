---
tags: [PPT-Master, AI-PPT, DrawingML, 可编辑PPTX, 开源]
sources: [PPT Master/PPT Master：AI 造 PPT 的正确姿势.md]
created: 2026-05-25
updated: 2026-05-25
---

# PPT Master：AI 造 PPT 的正确姿势

**来源：** PPT Master/PPT Master：AI 造 PPT 的正确姿势.md
**摄入日期：** 2026-05-25
**类型：** 产品介绍/评测

## 摘要

PPT Master 是一个开源 AI PPT 生成工具（GitHub 19,747 stars），核心差异是生成真正的 DrawingML 形状而非图片式 PPT。文字框、图表、图形都是原生 PowerPoint 对象，点一下就编辑。上线5个月快速迭代，v2.8.0 将 Live Preview 推进主流程，模板架构拆成 brand/layout/deck 三种独立形态。

## 核心观点

- **真正可编辑**：生成原生 DrawingML 形状，而非图像式 PPT（Gamma/美图/Canva 的痛点）
- **成本透明**：工具开源免费，唯一开销是 AI 模型调用费，VS Code Copilot 生成低至 $0.08
- **本地运行**：文件不上传第三方，数据安全
- **v2.8.0 三大更新**：
  - Live Preview 进主流程：生成中浏览器自动打开实时预览，点击标注→说"apply my annotations"→AI 直接改 SVG 并重新导出
  - 模板三段式：brand（品牌色/字体/Logo）+ layout（画布/页面节奏）+ deck（完整复刻），Git 风格冲突处理
  - AI 生图三重锁：rendering × palette × type 三维锁定，Strategist 给出 ≥3 个候选方案

## 技术特点

- **SVG → DrawingML 转换管线**：包括图案填充、饼图弧线端点修正、旋转 pivot 修复
- **多格式输出**：PPT 16:9、小红书、微信朋友圈等 10+ 种格式
- **动画和页面切换**：原生 OOXML 而非嵌入视频
- **语音旁白**：90+ 语种，ElevenLabs/MiniMax 克隆声音，可嵌入 PPTX 导出 MP4
- **开发者友好**：22 个示例项目、309+ 页设计多样性，同一套规则 + 不同 AI 对话

## 开发者价值

- **agent 驱动 workflow**：本质是一套 SKILL.md 工作流跑在 AI IDE 里，零后端、零数据库、零订阅
- **证明两件事**：agent 驱动的 workflow 比 SaaS 更靠谱；"可编辑"这个看似基础的要求，多数产品做不到
- **MIT 协议开源**：GitHub 每周两个版本迭代

## 涉及实体

- [[PPT Master]] — 开源 AI PPT 工具，GitHub 19,747 stars，开发者 Hugo He
- [[Claude Code]] — 主要使用环境，通过对话生成 PPT
- [[Cursor]] — 替代 IDE 选项
- [[VS Code Copilot]] — 低至 $0.08 的成本
- [[DrawingML]] — PowerPoint 原生形状描述语言

## 涉及概念

- [[AI生成PPT]] — 生成真正可编辑的原生 PPTX
- [[DrawingML]] — 真正的 PowerPoint 对象，而非图像
- [[Harness-Engineering]] — agent 驱动的 workflow 比 SaaS 更靠谱
- [[AI办公]] — PPT Master 定位为 AI 办公工具

## 相关链接

- GitHub：https://github.com/hugohe3/ppt-master