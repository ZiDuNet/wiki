---
type: entity
name: GenericAgent
created: 2026-05-12
updated: 2026-05-12
mentions: 1
---

# GenericAgent

**类型:** 实体
**来源:** [[github-ai热榜-5月11日-genericagent-omlx]]

## 简介

一个让 Agent 自己"长技能"的项目。GitHub: `https://github.com/lsdefine/GenericAgent`

## 核心特性

- **3300 行核心代码 + 9 个原子工具**
- **自进化机制**：用户提出新任务 → Agent 自动安装依赖、逆向接口、写脚本、调试、跑通 → 固化为可复用 Skill → 下次同类请求直接调用
- **震撼案例**：整个 GenericAgent 仓库从安装 Git 到每次 commit，全部由它自己完成
- **Token 优势**：分层记忆架构，消耗不到同类 Agent 的 1/10

## 风险

- 自进化意味着不可控
- 自主结晶的 Skill 质量可能参差
- 建议在沙箱环境使用，定期审查 Skill 树

## 相关概念

[[自进化系统]], [[AI-Agent]], [[记忆系统]], [[Skill开发]]
