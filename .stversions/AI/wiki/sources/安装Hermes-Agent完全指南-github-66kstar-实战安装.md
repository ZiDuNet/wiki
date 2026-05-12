---
tags: [GitHub, Agent, Claude, MCP, Obsidian, 飞书, API, Python]
source: "阿乐的Ale日记"
created: 2026-04-21
updated: 2026-05-10
category: GitHub
---

# 安装Hermes Agent完全指南 github 66kstar 实战安装

> 来源: [阿乐的Ale日记](https://mp.weixin.qq.com/s?__biz=MzYyNDI3ODI4OA==&mid=2247484585&idx=1&sn=1f341bf1cd9d982b302f6978a6a73d5a&chksm=f18393906e0d6ed51cd39f3b36ecb59adeaf273ccc75e8b9b943fad38ffbf604e1f15f9a0339&mpshare=1&scene=1&srcid=0421Osoi5AJVrCQF6Mfy6jBV&sharer_shareinfo=693b7a5d9233b53e05f9ff0c53bc94de&sharer_shareinfo_first=693b7a5d9233b53e05f9ff0c53bc94de) | 2026-04-21

## 摘要

最近在AI社区中，**Hermes Agent** 成为了现象级的热门话题。根据OpenRouter数据，它的token消耗量已跃居日榜第二，仅次于OpenClaw。GitHub上更是收获了66k星标和8.8k Fork，被中国开发者誉为"新一代的OpenClaw"。
对于正在开发微信小程序的我来说，Hermes最吸引人的是它的**微信原生支持**——通过腾讯官方iLink Bot API实现，无需公网服务器和webhook，扫码即可完成配置。这与我当前的小程序项目（微信群消息同步到飞书）高度重叠，可能大大简化开发工作。
Hermes Agent是由Nous Research开发的开源AI智能体框架，**不是单一模型**。它基于Llama/Mistral等开源模型微调，专注于：
- 强大的工具调用（Function Calling）能力
- 结构化输出
- 指令遵循
- 多智能体协作
**架构**：Hermes是多智能体框架，OpenClaw是单智能体框架
**微信支持**：Hermes有原生支持（iLink Bot API），OpenClaw需要webhook配置
**成本优化**：...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]], [[Hermes]], [[Obsidian]], [[OpenClaw]], [[Python]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[Function-Calling]], [[MultiAgent]], [[代码审查]], [[工作流自动化]], [[微调]]
