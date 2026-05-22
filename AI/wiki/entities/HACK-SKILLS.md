---
title: HACK-SKILLS
type: entity
tags: [安全, 渗透测试, Skill, Agent, yaklang, GitHub]
sources: [HACK-SKILLS-Agent黑客武装-101安全技能-14安全领域.md]
created: 2026-05-22
updated: 2026-05-22
---

# HACK-SKILLS

**类型:** 开源 Skill 合集
**作者:** Yaklang 团队
**GitHub:** [yaklang/hack-skills](https://github.com/yaklang/hack-skills)
**协议:** Apache-2.0
**规模:** 101 个深度专题 Skill，14 个安全领域

## 简介

Agent 安全技能知识库，不是 payload 字典，而是给 AI Agent 提供结构化安全知识框架，让 Agent 像有经验的渗透测试员一样思考和行动。

## 核心设计

- **三层路由表模式:** 总入口 → 6个分类入口 → 101个深度专题
- **安装:** `npx skills add yaklang/hack-skills`
- **在线浏览:** https://skills.hackbenchmark.com
- **离线 ZIP:** AES-256 加密，密码 `hack-skills`

## 覆盖领域

Web安全、API安全、认证授权、OS提权（Linux/Windows/macOS）、AD攻击、移动安全、二进制利用（Pwn）、逆向工程、密码学攻击、区块链/智能合约安全、AI/ML/LLM安全、网络协议/横向移动、数字取证

## 知识蒸馏来源

PayloadsAllTheThings、PentesterSpecialDict、Dictionary-Of-Pentesting、Hello-CTF、ctf-wiki、hacktricks、公开CVE公告

## 相关实体

- [[Skill]], [[Agent]], [[GitHub]], [[CTF]]

## 相关概念

- [[渗透测试]], [[Web安全]]
