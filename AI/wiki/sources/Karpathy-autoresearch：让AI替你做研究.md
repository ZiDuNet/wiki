---
tags: [AI研究, Karpathy, 开源项目, 自动化实验]
sources: [AI工具/71k Star 炸裂！Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉.md]
created: 2026-05-11
updated: 2026-05-11
---

# Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉

**Source:** AI工具/71k Star 炸裂！Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉.md
**Date ingested:** 2026-05-11
**Type:** article

## Summary

[[Karpathy]] 开源的 autoresearch 项目（71k Star），让 AI 自主进行机器学习研究实验。核心：给 AI 一个真实 LLM 训练环境，自主修改代码→训练 5 分钟→看结果→保留或回滚，无限循环。人类只写 program.md（研究纲领），AI 负责 train.py（实验执行）。

## Key Claims

- autoresearch 只有三个核心文件：prepare.py（只读数据准备）、train.py（AI 可修改的实验场）、program.md（人类写的研究纲领）
- 固定 5 分钟墙钟时间是最精妙设计：公平对比、自动适配硬件、快速反馈
- 没有使用 LangGraph/CrewAI 等编排框架——"智能体循环是用英语实现的"
- val_bpb 目标函数完全无歧义，把研究变成定义清晰的优化问题
- Git 就是 AI 的记忆和撤销机制，不需要外部向量数据库
- 约束产生创造力：AI 只能编辑一个文件、不能修改评估工具
- 社区已涌现 Apple Silicon 移植版、Windows RTX 版、Slurm/HPC 集群版

## Entities Mentioned

- [[Karpathy]] — 项目作者，前 Tesla AI 负责人、OpenAI 联合创始人
- [[Claude]] — 可作为 AI 编码智能体运行 autoresearch
- [[Claude-Code]] — 推荐的运行环境
[[Codex]] — 推荐的运行环境
- [[GitHub]] — 项目托管，10.4k Fork
- [[OpenAI]] — Karpathy 联合创立

## Concepts Covered

- [[Agent架构]] — 无框架编排：Markdown 文档即工作流
- [[Agent工程化]] — 自主实验循环的设计模式
- [[上下文工程]] — 上下文窗口即状态机
- [[经验蒸馏]] — program.md 蒸馏研究策略
- [[Self-Refinement]] — AI 自主迭代优化
