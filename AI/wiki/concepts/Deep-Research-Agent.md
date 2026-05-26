---
type: concept
tags: [Deep-Research, Multi-Agent, Hermes]
sources: [如何基于Openclaw-Hermes-Opencode-pi-agent搭建Deep-Research-Agent.md]
created: 2026-05-26
updated: 2026-05-26
---

# Deep-Research-Agent

**来源文章:** [[如何基于Openclaw-Hermes-Opencode-pi-agent搭建Deep-Research-Agent]]

## 定义

深度研究智能体，能长期跟踪主题、迭代研究、生成结构化报告。与普通 Agent 的区别：持久化 + 自主执行 + 真实行动能力。

## 框架适配性

| 框架 | 适配度 | 说明 |
|------|--------|------|
| [[Hermes Agent]] | **最推荐** | 自带 learning loop，越用越懂研究偏好 |
| [[OpenClaw]] | 高 | always-on 运行时，能自主跑几天 |
| [[Pi-agent]] | 中 | 极简核心，需自定义 research skills |
| [[OpenCode]] | 中 | 偏 coding，适合数据分析子任务 |

## 六步搭建法

1. **基础部署** — VPS 持久运行，多模型配置
2. **Multi-Agent 架构** — Planner → Researcher → Critic → Synthesizer → Coder
3. **MCP 工具集成** — 搜索/学术/多模态/浏览器自动化
4. **迭代反思循环** — Self-Reflection + Grounding
5. **输出持久化** — 结构化报告 + 通知归档
6. **优化生产化** — Observability + Cost Control + Eval

## 核心特点

- **持久内存** — 记住之前研究内容
- **长期运行** — 能自主跑几天跟踪主题
- **真实行动能力** — 文件、shell、浏览器操作
- **闭环学习** — 成功 pattern 转成 reusable Skill

## 相关概念

- [[Multi-Agent架构]] — 五角色分工协作
- [[Learning-Loop]] — Hermes 的闭环学习系统
- [[MCP工具层]] — 统一的 Agent 工具接口

## 相关实体

- [[Hermes Agent]] — 最推荐的 Deep Research 框架
- [[OpenClaw]] — always-on 运行时框架