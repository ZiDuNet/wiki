---
type: project
name: PPT Master
created: 2026-05-10
updated: 2026-05-25
---

# PPT Master

**Type:** project
**Description:** 开源 AI PPT 生成工具，GitHub 19,747 stars，多 Agent 协作生成原生 DrawingML 可编辑 PPTX，MIT 协议

## 核心特性

- **真正的可编辑**：生成原生 DrawingML 形状（文字框、图表、图形），而非图像式 PPT（Gamma/美图/Canva 的痛点）
- **成本极低**：工具开源免费，唯一开销是 AI 模型调用费，VS Code Copilot 生成低至 $0.08
- **本地运行**：文件不上传第三方，数据安全
- **MIT 协议开源**：GitHub 每周两个版本快速迭代

## v2.8.0 更新（2026-05-25）

- **Live Preview 进主流程**：生成过程中浏览器自动打开实时预览，点击任意元素写标注，回聊天框说"apply my annotations"，AI 直接改对应区域的 SVG 并重新导出 PPTX
- **模板三段式架构**：brand（品牌色/字体/Logo）+ layout（画布/页面节奏/SVG结构）+ deck（完整复刻），三者可任意组合，Git 风格冲突处理
- **AI 生图三重锁**：rendering × palette × type 三维锁定系统，Strategist 给出 ≥3 个候选方案而非单一默认选择，Image_Generator 消费固定合约

## 技术管线

- **SVG → DrawingML 转换**：包括图案填充、饼图弧线端点修正、旋转 pivot 修复
- **多格式输出**：画布规格覆盖 PPT 16:9、小红书、微信朋友圈等 10+ 种格式
- **动画和页面切换**：原生 OOXML 而非嵌入视频
- **语音旁白**：90+ 语种，ElevenLabs/MiniMax 克隆声音，可嵌入 PPTX 导出 MP4

## 开发者价值

- **agent 驱动 workflow**：本质是一套 SKILL.md 工作流跑在 AI IDE 里，零后端、零数据库、零订阅
- **22 个示例项目、309+ 页设计多样性**：同一套规则 + 不同 AI 对话跑出来
- **证明两件事**：agent 驱动的 workflow 比 SaaS 更靠谱；"可编辑"这个看似基础的要求，多数产品做不到

## 相关实体

[[Claude-Code]] [[Cursor]] [[html-ppt-skill]] [[GitHub]] [[CodeBuddy]] [[OpenClaw]] [[VS-Code-Copilot]] [[DrawingML]] [[hugohe3]]

## 相关概念

[[Harness-Engineering]] [[PPT制作]] [[AI办公]] [[AI生成PPT]] [[DrawingML]] [[GitHub开源项目]] [[Agent-Teams]] [[PDF转PPTX]] [[SVG转PPTX]]

## Mentioned In

- [[Skills-推荐-·-特别篇｜PPT-Master：让AI组队帮你生成真正可编辑的PPT]] — Skills 推荐 · 特别篇｜PPT-Master：让AI组队帮你生成真正可编辑的PPT
- [[Skill配方｜我终于找到了好用的PPT工具，把已有方案内容自动生成专业可编辑PPTX]] — Skill配方｜我终于找到了好用的PPT工具，把已有方案内容自动生成专业可编辑PPTX
- [[假期结束，打工人上线：5-个做-PPT-的-AI-工具skill，按场景选就够了]] — 假期结束，打工人上线：5 个做 PPT 的 AI 工具skill，按场景选就够了
- [[ppt-master-AI-造-PPT的正确姿势]] — 产品评测：AI 造 PPT 的正确姿势
- [[PPT-Master教程-PDF一键转可编辑PPT]] — 实战教程：PDF 一键转可编辑 PPT

## 相关链接

- GitHub：https://github.com/hugohe3/ppt-master