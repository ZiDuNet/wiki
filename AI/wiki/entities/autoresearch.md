---
tags: [entity, 开源项目, AI研究, Karpathy]
sources:
  - AI工具/71k Star 炸裂！Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉.md
created: 2026-05-11
updated: 2026-05-11
---

# autoresearch

[[Karpathy]] 开源的 AI 自主研究项目（71k Star，10.4k Fork）。

## 核心设计

- **三个文件**：prepare.py（只读数据准备）、train.py（AI 可修改的实验场）、program.md（人类写的研究纲领）
- **5 分钟固定实验**：墙钟时间公平对比，一夜约 100 个实验
- **无框架编排**：Markdown 文档即工作流，LLM 本身就是编排器
- **Git 即记忆**：每次实验一次 commit，失败可干净回滚
- **val_bpb**：无歧义目标函数，越低越好

## 设计原则

- 约束产生创造力：AI 只能编辑一个文件
- 简洁性偏好：微小改进如果引入复杂性不值得保留
- 永不停歇：实验循环一旦开始不暂停问人类

## 社区衍生

- Apple Silicon 移植版（MLX）
- Windows RTX 移植版
- Slurm/HPC 集群版

## 相关概念

- [[Agent架构]] — 无框架编排范式
- [[Self-Refinement]] — AI 自主迭代优化
- [[上下文工程]] — 上下文窗口即状态机
