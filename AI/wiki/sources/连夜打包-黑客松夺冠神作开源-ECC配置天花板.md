---
tags: [Agent配置, 黑客松, 开源, Claude-Code, ECC]
sources: [微信公众号/Agent/连夜打包！黑客松夺冠神作开源：含38个Agent、156项技能、千级安全测试.md]
created: 2026-05-26
updated: 2026-05-26
---

# 连夜打包！黑客松夺冠神作开源：含38个Agent、156项技能、千级安全测试

**来源：** 微信公众号/Agent/连夜打包！黑客松夺冠神作开源：含38个Agent、156项技能、千级安全测试.md
**摄入日期：** 2026-05-26
**类型：** 文章
**来源公众号：** 壹界点

## 摘要

[[ECC]]（Everything Claude Code）是由 [[Affaan-Mustafa]] 开发的 Claude Code 配置系统，在 Anthropic × Forum Ventures 黑客松中夺冠并获得 $15,000 奖金。该项目在 GitHub 上 7 个月狂揽 18.2 万 Stars，集成 60 个专业 Agent、232 个技能、75 条命令和 1282 种安全隐患检查系统，被称为「AI 编程时代的第一个操作系统」。

## 核心观点

1. **黑客松夺冠故事**：Affaan 用 10 个月打磨的 Claude Code 配置，8 小时手搓出实时协作聊天平台 zenith.chat，一个人干翻全场
2. **安装方式**：推荐通过 Claude Code 插件市场安装，避免与手动安装混用造成技能重复加载
3. **核心命令**：`/ecc:plan`（任务规划分派）、`/code-review`（5路并行检查）、`/security-scan`（安全审计）、`/simplify`（重构清洁）
4. **AgentShield 安全扫描**：三个 Claude Opus 4.6 Agent 扮演攻击者、防御者、审计员进行红蓝对抗，扫描 CLAUDE.md、MCP 配置、Hooks 等
5. **持续学习系统 v2**：通过置信度机制自动学习用户编码习惯，几周后 Claude Code 写出的代码自带个人风格
6. **AI 编程趋势**：核心战场从「模型能力」转向「系统集成」——Agent 编排、安全门禁、记忆持久化、跨会话学习

## 提及实体

- [[ECC]] — Everything Claude Code，Agent 配置天花板开源工作台，18.2万 Stars
- [[Affaan-Mustafa]] — 项目作者，Anthropic 黑客松冠军，Iô 联合创始人
- [[AgentShield]] — ECC 配套安全扫描工具，三 Agent 红蓝对抗
- [[claude-mem]] — 跨会话记忆插件，用 AI 压缩关键上下文存到 SQLite
- [[superpowers]] — 强制规划流程插件，头脑风暴→设计→TDD→两阶段审查
- [[Anthropic]] — 黑客松主办方之一
- [[Forum Ventures]] — 黑客松主办方之一
- [[elizaOS]] — Affaan 参与贡献的开源项目

## 涉及概念

- [[黑客松]] — Anthropic × Forum Ventures 黑客松，2025年9月纽约
- [[持续学习系统]] — ECC 的学习系统 v2，置信度机制自动应用编码习惯
- [[Agent工程]] — 把软件工程方法论编码成 Agent 可执行的规则、技能和 hooks
- [[安全审计]] — AgentShield 的红蓝对抗安全扫描
- [[跨会话记忆]] — claude-mem 解决 Claude Code 每次新会话从零开始的问题

## 关键数据

| 指标 | 数值 |
|---|---|
| GitHub Stars | 18.2万 |
| 专用 Agent | 60个 |
| Skill | 232个 |
| 命令 | 75条 |
| 安全检查 | 1282种 |
| 黑客松奖金 | $15,000 |

## 安装方法

```bash
# 第一步：注册市场地址
/plugin marketplace add https://github.com/affaan-m/ECC

# 第二步：安装插件
/plugin install ecc@ecc

# 第三步：手动拷贝规则文件
git clone https://github.com/affaan-m/ECC.git
mkdir -p ~/.claude/rules/ecc
cp -r rules/common ~/.claude/rules/ecc/
cp -r rules/typescript ~/.claude/rules/ecc/  # 按技术栈选装
```

## 推荐协同工具

```bash
/plugin install claude-mem      # 跨会话记忆
/plugin install superpowers     # 强制规划流程
```