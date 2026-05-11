---
tags: [Hermes, Agent, Claude, API, Python, OpenAI, Skill, OpenClaw]
source: "OhMyAgent"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# Hermes Agent v0.5.0 更新日志

> 来源: [OhMyAgent](https://mp.weixin.qq.com/s?__biz=MzI3MTUyMzA3Mg==&mid=2247484456&idx=1&sn=c6a96e6564b459c9811d411608ed8b90&chksm=eb7c84550508f07a68ea129a018b07f239d2dfcffe8971bf5e9ce0062623f12ad21f4c35c2c6&mpshare=1&scene=1&srcid=0422KC0BsontGzG3BoLYOqeF&sharer_shareinfo=a257ae9261d7eee7b4ab0e98bb513ce0&sharer_shareinfo_first=a257ae9261d7eee7b4ab0e98bb513ce0) | 2026-04-22

## 摘要

2026 年 3 月 28 日
加固版本。新增 Hugging Face provider、/model 命令重构、Telegram 私聊话题、原生 Modal SDK、插件生命周期钩子、GPT 模型工具调用引导、Nix flake、50+ 安全和可靠性修复及供应链审计。
- **Nous Portal 支持 400+ 模型** — 推理门户大幅扩展
- **Hugging Face 一等推理 provider** — 完整集成 HF Inference API，含智能 agent 模型选择器、实时 /models 端点探测、设置向导流程
- **Telegram 私聊话题** — 基于项目的对话，每个话题可绑定独立 skill，在单个 Telegram 聊天中实现隔离工作流
- **原生 Modal SDK 后端** — 用原生 Modal SDK 替代 swe-rex 依赖，消除隧道简化终端后端
- **插件生命周期钩子激活** — pre\_llm\_call、post\_llm\_call、on\_session\_start、on\_session\_end 钩子在 agen...

## 相关实体

[[Anthropic]], [[Docker]], [[OpenAI]], [[OpenClaw]], [[Python]], [[SQLite]]

## 相关概念


