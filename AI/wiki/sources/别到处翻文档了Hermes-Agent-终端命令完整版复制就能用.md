---
tags: [Hermes, Agent, MCP, API, Skill, OpenClaw]
source: "AI新工具实战派"
created: 2026-04-28
updated: 2026-05-10
category: Hermes
---

# 别到处翻文档了！Hermes Agent 终端命令完整版，复制就能用

> 来源: [AI新工具实战派](https://mp.weixin.qq.com/s?__biz=MzkxNjM4NjQ1NQ==&mid=2247484464&idx=1&sn=17fb467c0836908b051241adbf21b1cf&chksm=c0fd0aa9947d14fd21a340a686d4a8f3fa29fe750c2948302f808419b28b15f26a7d23644fc6&mpshare=1&scene=1&srcid=0428sXC4rySLinkoNwplE8sp&sharer_shareinfo=35f31ef77e55e48387c783fb0de92f81&sharer_shareinfo_first=35f31ef77e55e48387c783fb0de92f81) | 2026-04-28

## 摘要

01
全局选项｜前置通用参数
✅ 所有命令都能搭配使用，全局快速控制运行环境
- `hermes --version / -V`
👉 快速查看当前客户端完整版本号
- `hermes -p `
👉 切换指定 Profile 多环境配置，适配多项目隔离使用
- `hermes -r `
👉 精准恢复指定历史会话，接续之前的代理工作进度
- `hermes -c [name]`
👉 一键恢复最近一次会话，无需手动检索会话记录
- `hermes --yolo`
👉 跳过所有高危操作二次确认，适合脚本自动化批量执行场景
- `hermes --tui`
👉 拉起终端可视化交互界面，纯窗口化操作，直观好上手
- `hermes --worktree`
👉 为并行多代理工作流创建独立隔离空间，互不干扰运行
- `hermes --pass-session-id`
👉 将会话ID同步透传给下游代理链路，方便全链路日志溯源排查
02

## 相关实体

[[Hermes]], [[OpenClaw]]

## 相关概念

[[多模态]]
