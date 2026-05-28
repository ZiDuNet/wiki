---
type: concept
name: Skill系统
created: 2026-05-28
updated: 2026-05-28
tags: [Skill, 员工技能手册, 知识积累]
sources: [[Claude-code使用笔记怎样用MCPSkillHarness搭建一个AI公司]]
---

# Skill系统

**类型:** 概念

## 定义

Claude Code 中的 Skill 类比「员工技能手册」，告诉 AI 怎么做某件具体的事。好的 Skill 包含三层：知识层 + 流程层 + 工具调用层。

## Skill 三层结构

| 层级 | 内容 |
|-----|------|
| 知识层 | 知道什么是好的结构、SEO 规范、平台差异 |
| 流程层 | Step 1 → Step 6 的执行步骤 |
| 工具调用层 | 读文件、调脚本、处理配图 |

## 关键特性：积累

Skill 会积累，越用越懂用户：
- 记得用户偏好（镜头节奏、字幕风格）
- 不需要每次重新解释背景
- 像老员工而非新员工

## 全局 vs 项目

| 放全局 | 放项目 |
|-------|-------|
| 通用能力（humanizer、文档处理） | 业务绑定（geo-blog、dealer-content） |
| 所有项目都可能用到 | 特定品牌/受众/规范 |

**核心原则**：业务 Skill 永远放项目，80% 混乱问题解决。

## 相关文章

- [[Claude-code使用笔记怎样用MCPSkillHarness搭建一个AI公司]]

## 相关概念

- [[Harness]]
- [[MCP]]
- [[AI操作系统]]