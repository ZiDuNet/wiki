---
tags: [Skills, Agent, GitHub, RAG, Harness, Prompt, API, Skill]
source: "芯火丹师"
created: 2026-04-20
updated: 2026-05-10
category: Skills
---

# 如何写好 Skill：如何正确“蒸馏”同事

> 来源: [芯火丹师](https://mp.weixin.qq.com/s?__biz=MzIwMzIzODcyNA==&mid=2247483678&idx=1&sn=941ee2c1eddc4666dd39ae1df27c3d6b&chksm=97ed28f8626e79cf47dc1acbc94b55a6e3105779141c0ff828887746369d606eda9bdf8d9c19&mpshare=1&scene=1&srcid=0420H5dtIaBmjZEcqoZ42cyk&sharer_shareinfo=fa87b033bc3102df5372972c95a3cc89&sharer_shareinfo_first=fa87b033bc3102df5372972c95a3cc89) | 2026-04-20

## 摘要

AI Agent 工程化，从过往的"提示词工程"、"上下文工程"逐渐走向"Harness 工程"，"Skill 模式"基本是绕不过去的一步。
变化主要在设计重点上，Agent 开始从对话（零散的LLM工具调用）转向组织能力（AgentLoop为主的模块化框架）。同样的基座模型，能不能拉开差距，就看各个模块的评估体系有没有完备、成熟。
这些模块中，其中一块不可或缺的一个，就是今天要聊的 Skill。
Skill 和 Prompt 不在一个层面，它更接近一个标准化的能力封装层。它把能力拆到文件结构里，让这些能力可以被索引、版本化，也可以按需插拔。Skill 主要包含以下内容：
- 标准化文件夹：通常用
格式命名。
- 核心文件
：放在上述的文件夹内，内容包括
头和 Body（具体的 SKILL 内容）
- 脚本
：复杂计算、格式处理这类确定性工作尽量交给脚本。代码是确定的，大模型的理解和输出不是。
- 参考资料（
）：放技术文档、API 指南之类的材料，别把所有东西都塞进主指令里。
- 资源（
）：模板、静态资产或其他复用材料。
YAML头中内容看起来像这样：
大模型在长上下文里会出现"上...

## 相关实体

[[GitHub]], [[Harness]], [[Markdown]], [[OpenClaw]]

## 相关概念

[[AI-Agent]], [[Multi-Agent]], [[Prompt工程]], [[SOP]], [[上下文工程]], [[设计模式]]
