---
type: entity
name: AgentShield
tags: [安全, Agent工具, 开源, 安全扫描]
sources: [GitHub 炸了：19 万星的 Agent 配置天花板，一天涨 2k+星.md, 连夜打包！黑客松夺冠神作开源：含38个Agent、156项技能、千级安全测试.md]
created: 2026-05-26
updated: 2026-05-26
mentions: 2
---

# AgentShield

**类型:** 实体 / 安全工具
**提及文章数:** 2

## 简介

AgentShield 是 [[ECC]] 配套的安全扫描工具，由 [[Affaan-Mustafa]] 开发。它派三个 Claude Opus 4.6 Agent 分别扮演攻击者、防御者和审计员，对 Agent 配置进行红蓝对抗扫描，能发现「单独看没问题、组合起来要命」的漏洞链。

## 扫描范围

- **CLAUDE.md**：是否有硬编码的 API 密钥、可注入的指令
- **settings.json**：权限配置是否有漏洞
- **MCP 配置**：服务器风险（覆盖 25 个以上已知 CVE）
- **Hooks**：注入分析
- **Agent 定义**：Prompt 注入、权限提升风险

## 输出示例

```
Grade: B+
Critical: 0 | High: 2 | Medium: 5 | Low: 3
HIGH: Hardcoded API key in CLAUDE.md:15
Fix: Move to environment variable
```

## 三 Agent 红蓝对抗

| 角色 | 任务 |
|---|---|
| Attacker | 寻找可利用的漏洞链 |
| Defender | 评估现有防御措施 |
| Auditor | 综合双方报告，生成优先级风险清单 |

## CI 集成

可加到 CI 流程里，任何改了 Agent 配置的 PR 都先过 AgentShield 安检。Exit code 2 表示有严重发现，直接卡住构建。

## 相关概念

- [[安全审计]] — AgentShield 的红蓝对抗安全扫描
- [[Agent工程]] — 安全门禁是 Agent 工程的重要组成部分

## 官网

- 仓库：https://github.com/affaan-m/agentshield