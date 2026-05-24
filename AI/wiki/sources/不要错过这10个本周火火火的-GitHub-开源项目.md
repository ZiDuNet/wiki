---
title: 不要错过这10个本周火火火的 GitHub 开源项目
type: source
date: 2026-05-24
source: 微信公众号/逛逛GitHub
category: GitHub
url: https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533989
tags: [GitHub, AI开源项目, 热门项目]
entities: [scientific-agent-skills, academic-research-skills, Understand-Anything, codegraph, oh-my-pi, 12-factor-agents, ai-engineering-from-scratch, supertonic, ViMax]
---

# 不要错过这10个本周火火火的 GitHub 开源项目

> 来源：逛逛GitHub | 时间：2026-05-24

## 项目概览

本文盘点10个本周热度攀升最快的GitHub开源AI项目。

---

## 01. scientific-agent-skills — AI科研全家桶

> ⭐ 2.5万+ Star | GitHub: https://github.com/K-Dense-AI/scientific-agent-skills

一套开箱即用的Agent技能包，覆盖科研、科学计算、工程、数据分析、金融和写作6大领域。

### 核心能力

- 覆盖科研全流程的133个技能
- 100+科学数据库统一访问
- 让AI干活有章法，按流程执行

### 适用场景

科研党、数据分析、科学计算相关工作

### 关联

- [[scientific-agent-skills]]
- [[Agent Skills]]

---

## 02. academic-research-skills — 论文写作流水线

> ⭐ ~2万 Star（一周涨1万+）| GitHub: https://github.com/Imbad0202/academic-research-skills

专为Claude Code设计的学术研究技能，把写论文全流程串成管线。

### 核心流程

查资料 → 写 → 审 → 改 → 定稿，一环扣一环自动往下走

### 特点

- 按真实写论文节奏设计
- 需人工干预，非全自动
- 正在熬论文的研究生适用

### 关联

- [[academic-research-skills]]
- [[学术写作管线]]

---

## 03. Understand-Anything — 代码库知识图谱

> ⭐ ~2万 Star | GitHub: https://github.com/Lum1104/Understand-Anything

把代码库变成可交互的知识图谱，支持搜索、提问、可视化浏览。

### 核心能力

- 代码库→知识图谱可视化
- 搜索、提问、点点看看
- 兼容多种AI工具

### 适用场景

读陌生项目、刚进新公司面对历史项目

### 关联

- [[Understand-Anything]]
- [[代码知识图谱]]

---

## 04. codegraph — 给AI提前做功课

> ⭐ ~1.8万 Star（一周涨1.4万+）| GitHub: https://github.com/colbymchenry/codegraph

本周黑马。提前把代码库索引成代码知识图谱，让AI一上来就懂项目结构。

### 核心思路

痛点：每次让AI改代码，都要先啃一遍项目结构，又慢还容易啃错

方案：提前索引成知识图谱喂给AI

### 支持工具

Claude Code、Codex、Cursor、OpenCode

### 性能提升

项目越大，帮助越明显

### 关联

- [[codegraph]]
- [[代码知识图谱]]
- [[MCP Server]]

---

## 05. oh-my-pi — 终端AI编程助手

> ⭐ ~6000 Star | GitHub: https://github.com/can1357/oh-my-pi

终端里的AI编程助手，从Pi分支而来，主打改代码改得准。

### 核心创新：Hashline编辑系统

- 模型用内容哈希锚点定位代码
- 不用重新输入整行
- 解决空白符不匹配导致编辑失败的经典问题
- 减少61% token消耗

### 技术规格

- 32个内置工具
- 40+ LLM Provider
- 13种LSP操作、27种DAP操作
- 约27k行Rust代码
- ripgrep、glob、bash、AST操作、语法高亮全部做进进程内
- 支持8个工具配置导入（Claude Code、Cursor、Windsurf等）

### 关联

- [[oh-my-pi]]
- [[Hashline编辑]]

---

## 06. 12-factor-agents — Agent工程十二条军规

> ⭐ 2.1万 Star | GitHub: https://github.com/humanlayer/12-factor-agents

借鉴经典12-Factor Apps思路，定义构建生产级AI Agent的12条原则。

### 核心理念

- 把LLM当自然语言到工具调用的转换引擎
- 把Agent做成无状态的规约器
- 用确定性代码控制流程

### 资源

- 3个实战工作坊
- 脚手架工具
- 一条命令初始化符合原则的新项目

### 关联

- [[12-factor-agents]]
- [[Agent工程原则]]

---

## 07. ai-engineering-from-scratch — 从零学AI工程

> ⭐ 1.2万+ Star | GitHub: https://github.com/rohitg00/ai-engineering-from-scratch

口号：学会它、造出来、发出去

### 内容规模

- 428节课
- 20个阶段
- 约320小时学习内容
- 从线性代数到自主多智能体系统

### 课程结构

问题 → 概念 → 数学原理实现 → PyTorch/sklearn实现 → AI工件交付

### 四语言实现

Python、TypeScript、Rust、Julia

### 关联

- [[ai-engineering-from-scratch]]

---

## 08. Supertonic — 端侧离线TTS

> GitHub: https://github.com/supertone-inc/supertonic

约99M参数的端侧文本转语音系统，CPU上就能快速推理。

### 核心特性

- 基于ONNX Runtime
- 完全离线，不传云端
- v3支持31种语言
- Expression Tags情感控制（`<laugh>`、`<breath>`、`<sigh>`）

### SDK支持

11个平台：C++、Node.js、Python、Rust、Java、Go、Swift、C#、Flutter、iOS、Web

### 关联

- [[supertonic]]
- [[端侧推理]]
- [[Expression Tags]]

---

## 09. ViMax — 多Agent视频剧组

> GitHub: https://github.com/HKUDS/ViMax

港大HKUDS出品，把视频制作拆成AI剧组角色协作。

### 四个AI角色

导演 → 编剧 → 制片 → 视频生成器

### 三种模式

- Idea2Video：灵感→完整视频
- Novel2Video：小说→分集视频
- Script2Video：剧本→无限长度视频

### 特色功能

- AutoCameo：上传照片嵌入角色
- 六层流水线自动化
- 多机位模拟
- MiniMax M2.7支持（1M上下文）

### 关联

- [[ViMax]]
- [[多智能体协作]]
- [[Idea2Video]]

---

## 核心主题总结

### 概念趋势

1. **Agent工程纪律** — 12-factor-agents定义生产级Agent原则
2. **代码知识图谱** — codegraph、Understand-Anything让AI提前懂项目
3. **多Agent协作** — ViMax把视频制作拆成剧组角色分工
4. **端侧推理** — Supertonic实现完全离线TTS
5. **Skill生态爆发** — scientific-agent-skills、academic-research-skills专业化Skill集

### 热度趋势

- 本周多个项目单周涨星1万+
- Skill相关项目持续火爆
- Agent工程化成为焦点