---
tags: [Claude, Agent, GitHub, Prompt, Python, OpenAI, Skill]
source: "图情充电站"
created: 2026-04-23
updated: 2026-05-10
category: Claude
---

# 文献分析 Skill  ## 元数据 Name: literature-analysis Description: 当用户需要分析学术文献、提取关键信息或生成文献综述时使用  ## 指令 你是一位图书情报学领域的资深研究者。在分析文献时:  1. 信息提取标准:    - 研究问题/目标    - 理论框架    - 研究方法(定性/定量/混合)    - 核心发现    - 研究局限    - 未来研究方向  2. 分析维度:    - 时间维度:研究主题的演进脉络    - 方法维度:不同研究方法的应用趋势    - 理论维度:主要理论框架的发展  3. 输出格式:    - 使用 Markdown 表格呈现结构化信息    - 关键概念用加粗标注    - 提供简明的综述性段落  4. 学术规范:    - 保持客观中立的学术语言    - 准确引用原文观点    - 明确区分描述性总结和批判性分析

> 来源: [图情充电站](https://mp.weixin.qq.com/s?__biz=MzIwMjk1NzI3Ng==&mid=2247485507&idx=1&sn=2ca70534ca9b1dbc5ce71450070cd856&chksm=97d6fb5836b565a67a4db2a24218d6927470178280e82d5a89f7622fa9accd20fb91fcf3ceab&mpshare=1&scene=1&srcid=0423umuCpYxP2TXHoXIwFXNw&sharer_shareinfo=c28e283dc73d5077ebf63d4ad4cfa469&sharer_shareinfo_first=c28e283dc73d5077ebf63d4ad4cfa469) | 2026-04-23

## 摘要

作为一名图书情报专业的研究生，你可能正面临着论文撰写、数据挖掘、课题申报等多重挑战。而 Agent Skills 的出现，正在改变科研工作者与 AI 的协作方式。这篇文章将带你从零开始，掌握如何用 Skills 提升科研效率。
很多人第一次接触 Skills 时会困惑：这不就是把提示词写长一点吗？
**答案是：完全不同。**
传统的提示词就像你给 ChatGPT 发一段指令，它只能“说”不能“做”。而 Skills 是给 **Agent**（智能代理）用的技能包，Agent 不仅能对话，还能**动手干活**——读取文件、调用工具、执行脚本、生成图表，甚至在遇到问题时自己调试解决。
用一个比喻来说明：
- **传统提示词** = 你给助手口头交代任务，助手只能回答“好的，您可以这样做……”，剩下的活还得你自己干
- **Agent Skills** = 你给助手一本操作手册，助手看完后自己完成整个任务流程，遇到问题还能自己解决
一个标准的 Skill 包含：
1. **元数据（Metadata）**：告诉 Agent 这个技能是干什么的、什么时候该用
2. **指令（Instructio...

## 相关实体

[[Anthropic]], [[ChatGPT]], [[Claude-Code]], [[Claude]], [[GLM]], [[GitHub]], [[Markdown]], [[Python]]

## 相关概念

[[代码生成]]
