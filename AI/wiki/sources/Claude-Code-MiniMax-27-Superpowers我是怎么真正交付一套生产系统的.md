---
tags: [Claude, Agent, MCP, GitHub, Harness, Prompt, API, OpenAI]
source: "feifeirun"
created: 2026-04-29
updated: 2026-05-10
category: Claude
---

# Claude Code + MiniMax 2.7 + Superpowers：我是怎么真正交付一套生产系统的

> 来源: [feifeirun](https://mp.weixin.qq.com/s?__biz=MzIxMjM0ODY3Ng==&mid=2247484222&idx=1&sn=49e096a3c3a0eb794a1d2101f5e5b2f4&chksm=9657180e099503e7ff8bad49ace29e7291be50edf04e533d8a4bb51a939ae0efd6fe980722c4&mpshare=1&scene=1&srcid=0429IRLTAe26bYFHhEBw1BvS&sharer_shareinfo=f4c4a37dc69856d8492325c53d053455&sharer_shareinfo_first=f4c4a37dc69856d8492325c53d053455) | 2026-04-29

## 摘要

我用Claude Code + MiniMax 2.7  + SuperPowers完成了用于生产环境的微服务架构的原型设计->需求确认->代码开发工作，已在内部系统部署验证。尝试通过约束、文档分层、技能工作流和工程化方法，让 Coding Agent 真正可控地参与交付。
1、在电脑用户目录的 `.claude` 文件夹下创建 `CLAUDE.md` 文件，用来约束 claude code 的全局行为。我的配置可参考：
或者参考：
andrej-karpathy-skills(https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md[1])
2、安装skill
- superpower(https://github.com/obra/superpowers[2])
用途：在开发新模块和处理复杂 bug 时，它提供了一套行之有效的工作流程，用来保证效果。
安装方法：在claude code里执行：
- planning-with-files (https://github.com/OthmanA...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]]
[[Matt-Pocock]]

## 相关概念

[[Vibe-Coding]], [[上下文工程]], [[代码生成]], [[微服务]]
[[Skill设计模式]]
