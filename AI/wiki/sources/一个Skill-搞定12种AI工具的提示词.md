---
tags: [AI工具, Prompt工程, Skill]
sources: [AI工具/一个Skill，搞定12种AI工具的提示词.md]
created: 2026-05-27
updated: 2026-05-27
type: source
---

# 一个Skill，搞定12种AI工具的提示词

**来源:** AI工具/一个Skill，搞定12种AI工具的提示词.md
**摄入日期:** 2026-05-27
**类型:** 文章

## 摘要

prompt-master 是一个通用提示词生成 Skill，兼容 WorkBuddy、OpenClaw 等 Agent 客户端。通过 12 种提示词模板覆盖主流 AI 工具场景（ChatGPT、Midjourney、Claude Code、ComfyUI 等），并内置 35 种常见错误模式诊断。用户只需描述需求和工具名，Skill 自动匹配合适模板并生成精确提示词。

## 核心观点

- **12种模板覆盖主流AI工具**：RTF、CO-STAR、RISEN、CRISPE、Chain of Thought、Few-Shot、File-Scope、ReAct+Stop Conditions、Visual Descriptor、Reference Image Editing、ComfyUI、Prompt Decompiler
- **35种错误模式自动诊断**：识别"模糊任务动词"、"两个任务混在一起"、"忘记指定文件路径"等问题并给出修复版本
- **推理模型自动识别**：o3、DeepSeek-R1、Qwen3 等内置推理链的模型，自动移除 CoT 指令避免干扰
- **反伪造技术过滤**：MoE（混合专家）、ToT（思维树）、GoT（思维图）等需要多轮执行的技术，在单次 prompt 里是假的，直接过滤
- **安装方式**：GitHub 克隆或手动下载 ZIP，通过 skill-creator 安装

## 涉及实体

- [[WorkBuddy]] — 兼容的 Agent 客户端之一
- [[prompt-master]] — 本 Skill 本身

## 涉及概念

- [[Prompt工程]] — Skill 的核心主题
- [[Skill工程]] — Skill 的设计方法论
- [[推理模型]] — CoT 自动识别的目标模型类型

## 关键洞察

1. **推理模型不该加 CoT**：推理模型内部已有完整"思考-验证-修正"链，外挂 CoT 会让两条推理线互相干扰
2. **MoE/ToT/GoT 单次 prompt 是假的**：这些技术需要多轮交互或外部系统支持，单次 prompt 只能让模型线性生成文本，无法真正启动多专家协作
3. **最好的提示词不是最长的**：每个词都有具体作用，不堆砌看起来专业的废话

## 一句话总结

prompt-master 将 12 种主流 AI 工具的提示词模板和 35 种错误诊断集成为标准化 Skill，让用户告别反复调 prompt 的痛苦。

## 相关链接

- GitHub: https://github.com/nidhinjs/prompt-master