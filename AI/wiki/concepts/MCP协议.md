---
title: MCP协议
type: concept
tags: [协议, AI接口, 工具连接]
created: 2026-05-10
updated: 2026-05-24
---

# MCP协议

**Keywords:** mcp, model context protocol, usb接口, AI工具连接

## 定义

MCP（Model Context Protocol）是一种标准化的协议，用于连接 AI Agent 与外部工具和数据源。类比理解：MCP = 给实习生开通公司系统账号，是连接外部工具数据源的万能接头。

## 核心特性

### 通用接口
- 类似 USB 接口的通用性
- 一个协议连接多种工具和数据源
- 语言无关，支持多平台

### 上下文感知
- AI 通过 MCP 感知服务器实时状态
- 提供有上下文的诊断建议
- 不只是聊天，而是真正理解系统状态

## 应用场景

### AI 运维终端
- [[GMSSH]] 通过 MCP 协议感知服务器实时状态
- 预置 50+ 运维技能包（巡检、配置优化、故障排查）
- AI 能查看进程列表、日志，给出具体诊断

### Agent 工具集成
- 连接浏览器自动化工具
- 文件系统操作
- API 调用和数据访问

## Related Entities

[[Claude-Code]] [[Claude-Desktop]] [[Cursor]] [[Codex]] [[Gemini-CLI]] [[MCP]] [[baoyu-skills]] [[Anthropic]] [[GMSSH]]

## Related Concepts

[[Skill设计模式]] [[Harness-Engineering]] [[Skill编排]] [[渐进式披露]] [[Agent开发]] [[PPT制作]] [[运维终端]] [[AI运维]]

## Mentioned In

- [[智能体MCP-Skill到底是啥5句话大白话讲透]] — MCP = 给实习生开通公司系统账号，连接外部工具数据源的万能接头
- [[Agent-Skills-解剖：五个设计决策拯救被上下文淹没的-AI-Agent]]
- [[MCP-与-Skills：AI-Agent-真正走向生产力系统的两块拼图]]
- [[别再手抄设计稿了：我做了个-Skill，把任意网站变成设计文档]]
- [[怎么创建一个真正能干活的-Skills？]]
- [[我给龙虾装上好用的PPT-Skill]]
- [[最值得安装的20个Skills]]
- [[告别传统SSH一款桌面级AI运维终端体验嘎嘎好]] — GMSSH 通过 MCP 感知服务器实时状态，提供有上下文的诊断建议
