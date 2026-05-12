---
tags: [Hermes, Agent, Claude, GitHub, Prompt, API, Python, OpenAI]
source: "DNOPC"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Hermes Agent Self-Evolution：开启Agent自我进化之路

> 来源: [DNOPC](https://mp.weixin.qq.com/s?__biz=MzY4ODE5Mjc0MQ==&mid=2247483772&idx=2&sn=2de37474b79cd10d615ca5d7ae3f4fb8&chksm=f20f0e5399966be6e982d1b8879ffb63edd88fcb6f3979c96d7b717495c38747efea1d2c861e&mpshare=1&scene=1&srcid=0420HWElypF0qLFMFW6iy5rm&sharer_shareinfo=b22e31a23c477c55c20ffac9780b9be5&sharer_shareinfo_first=b22e31a23c477c55c20ffac9780b9be5) | 2026-04-20

## 摘要

训练一个模型需要 GPU、算力和大量数据。一个训练好的模型（比如 Claude、GPT-4）部署为 AI Agent后，能力上限往往不是模型本身，而是**提示词、工具描述、技能文件的质量**。
这些文本在 AI Agent架构中无处不在：
- 系统提示词（System Prompt）决定Agent行为模式
- 技能描述（Skill descriptions）决定Agent知道哪些工作流
- 工具定义（Tool descriptions）决定Agent能调用哪些能力
传统做法是人工撰写、人工 Review、人工迭代。问题在于：
1. **人工调优靠直觉**
，没有系统性的评估手段
2. **反馈周期长**
，改一版提示词可能需要几十次对话才能判断好坏
3. **规模扩展差**
，技能从 10 个扩展到 100 个，人工维护成本指数增长
Hermes Agent Self-Evolution 的出发点就是解决这三个问题。
Self-Evolution 的方法论分为三个步骤：**读 → 变 → 选**。
**读**：系统读取当前技能文件或提示词，同时读取该技能的**执行轨迹（executio...

## 相关实体

[[Claude-Code]], [[Claude]], [[GPT4]], [[GitHub]], [[Hermes]], [[Python]], [[微信]]

## 相关概念

[[AI-Agent]], [[Agent架构]], [[代码审查]]
