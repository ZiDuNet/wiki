---
type: entity
name: prompt-master
sources: [一个Skill-搞定12种AI工具的提示词.md]
created: 2026-05-27
updated: 2026-05-27
mentions: 1
---

# prompt-master

**类型:** 实体 (Skill)
**GitHub:** https://github.com/nidhinjs/prompt-master
**开发作者:** nidhinjs

## 简介

一个标准化提示词生成 Skill，兼容所有支持 skill 加载的 AI 客户端（WorkBuddy、OpenClaw 等）。通过 12 种模板为 ChatGPT、Midjourney、Claude Code、ComfyUI 等主流 AI 工具生成精确、可直接使用的提示词，并内置 35 种错误模式诊断和推理模型自动识别。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| **12种提示词模板** | 覆盖 RTF、CO-STAR、RISEN、CRISPE、CoT、Few-Shot、File-Scope、ReAct+Stop Conditions、Visual Descriptor、Reference Image Editing、ComfyUI、Prompt Decompiler |
| **35种错误模式诊断** | 识别模糊动词、任务混杂、缺少路径等常见问题并给出修复版 |
| **推理模型自动识别** | 自动检测 o3、DeepSeek-R1、Qwen3 等，移除干扰性 CoT 指令 |
| **反伪造技术** | 过滤 MoE、ToT、GoT 等在单次 prompt 里无法真正执行的技术 |

## 设计哲学

**最好的提示词不是最长的，而是每个词都有具体作用的。**

## 安装方式

```bash
# 方式一：GitHub 克隆
git clone https://github.com/nidhinjs/prompt-master.git

# 方式二：手动下载 ZIP + skill-creator 安装
```

## 目录结构

```
prompt-master/
├── SKILL.md              # 核心 skill 定义
├── LICENSE               # MIT 开源协议
└── references/
    ├── templates.md      # 12 种提示词模板完整参考
    └── patterns.md       # 35 种错误模式诊断库
```

## 相关实体

- [[WorkBuddy]] — 兼容的 Agent 客户端

## 相关概念

- [[Prompt工程]] — 核心主题
- [[Skill工程]] — 设计方法论
- [[推理模型]] — 自动识别目标

## 数据来源

- [[一个Skill-搞定12种AI工具的提示词]]