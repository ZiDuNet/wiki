---
tags: [entity, person, AI大神]
sources:
  - LLM Wiki/Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？.md
  - AI工具/71k Star 炸裂！Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉.md
created: 2026-05-11
updated: 2026-05-11
---

# Karpathy

AI 领域知名人物，前 Tesla AI 总监，OpenAI 联合创始人之一。

## LLM Wiki

Karpathy 提出的 LLM Wiki 方法论（GitHub Gist，5000+ Star）：

- 不是 RAG 替代品，而是 RAG 缺失的知识预编译层
- 核心思路：资料进入知识库时先让 LLM 加工成结构化 Markdown Wiki
- 三层架构：Raw Sources → Structured Wiki Pages → Query Layer
- 知识形态：摘要页、实体页、概念页、综合页、索引页
- 配套概念：index.md（目录）、log.md（操作记录）、lint（健康检查）

## autoresearch

Karpathy 开源的 AI 自主研究项目（71k Star）：

- 给 AI 真实 LLM 训练环境，自主实验循环
- 三个文件：prepare.py + train.py + program.md
- 核心理念：人类写 program.md（研究纲领），AI 改 train.py（实验执行）
- 固定 5 分钟实验，一夜约 100 个实验
- 无框架编排：Markdown 即工作流，LLM 即编排器
- Git 即记忆和撤销机制

## 核心观点

> 传统 RAG 是提问时临时找材料，LLM Wiki 是资料进入时先做知识编译。

> autoresearch 证明最好的智能体编排可能就是没有编排框架——一份写得好的自然语言指令可以替代大量工程基础设施。

## 相关概念

- [[RAG]] — LLM Wiki 是 RAG 的预编译补充层
- [[知识库构建]] — LLM Wiki 方法论
- [[知识管理]] — Agent 持续维护知识库
- [[autoresearch]] — AI 自主研究项目
- [[Self-Refinement]] — 自主实验循环
- [[Agent架构]] — 无框架编排范式
