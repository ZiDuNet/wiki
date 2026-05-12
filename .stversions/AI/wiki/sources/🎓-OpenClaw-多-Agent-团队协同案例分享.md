---
tags: [OpenClaw, Agent, GitHub, 飞书, Prompt]
source: "编程老兵学AI"
created: 2026-04-21
updated: 2026-05-10
category: OpenClaw
---

# 🎓 OpenClaw 多 Agent 团队协同案例分享

> 来源: [编程老兵学AI](https://mp.weixin.qq.com/s?__biz=MzA5Njg3MDQzNQ==&mid=2456596671&idx=1&sn=1887f20ca626f157584fb989e0ecc5e8&chksm=86aea4c111a5fc58160b0758f712af11149c217da4a4cb55d9455dd8e8fb0307dce673cdaaf3&mpshare=1&scene=1&srcid=0421SQGs0Kw1hXYZSmsgtayC&sharer_shareinfo=83e47392126aa0e869afef72132126a6&sharer_shareinfo_first=83e47392126aa0e869afef72132126a6) | 2026-04-21

## 摘要

本案例将展示如何使用 OpenClaw 快速搭建一个教学辅助 AI 团队，包含三个不同角色的 Agent，帮助老师减轻教学负担。
- OpenClaw 新手
- 想用 AI 辅助教学的老师
- 对多 Agent 协作感兴趣的同学
- 如何创建第一个 OpenClaw Agent
- 如何配置多 Agent 协同
- 如何将 Agent 接入实际场景
在任意目录创建 `openclaw.json`：
通过飞书发送消息给机器人，体验 Agent 回答。
A: 检查配置是否生效，运行 `openclaw gateway restart`
A: 调整 prompt，使用更具体的指令
A: 参考 OpenClaw 文档配置 Telegram/Discord
- OpenClaw 官方文档[1]
- Lobster 工作流[2]
- 多 Agent 路由[3]
有问题？来 OpenClaw Discord 或 GitHub 提 Issue！
1. **配置路径**：将配置文件放到 `~/.openclaw/agents/main/agent/` 目录，或使用 `-c` 参数指定
2. **重启生效...

## 相关实体

[[GitHub]], [[OpenClaw]], [[飞书]]

## 相关概念

[[MultiAgent]]
