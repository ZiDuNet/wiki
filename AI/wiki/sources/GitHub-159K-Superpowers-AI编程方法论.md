---
type: source-summary
title: GitHub 159K Superpowers：AI编程方法论
source: 微信公众号/GitHub/GitHub上159K颗星！你的AI编程代理不是能力不够，是不知道怎么干活.md
author: 智能进化Wayen
created: 2026-05-29
updated: 2026-05-29
tags:
  - GitHub
  - AI编程
  - Superpowers
  - Claude-Code
  - Hermes-Agent
  - OpenClaw
  - Skill系统
---

# GitHub 159K Superpowers：AI编程方法论

> 📎 来源: [智能进化Wayen](https://mp.weixin.qq.com/s?__biz=MzkzNDY1NzQ0Mg==&mid=2247488099&idx=1&sn=8cd50b6ffbf3fff9edeb7a0c324aa5a4)

## 核心命题

AI编程代理真正缺的不是能力，而是**怎么干活的方法论**。Superpowers 是一套技能系统，教 AI 编程代理从"接到任务到交付代码"的每一步该干什么、怎么干、干到什么程度算完。

## 关键洞察

**装了和没装的区别：**

| 场景 | 没装 Superpowers | 装了 Superpowers |
|------|------------------|------------------|
| 接任务 | 秒回"好的，我来实现"，直接写代码 | 先问问题：导出格式、数据量、权限要求，给出方案让用户选 |
| 写代码 | 写到一半发现问题，改三轮 | 先写测试再写实现，写完自动 Review |
| Token 消耗 | 一个功能改三轮，烧一万 Token | 一次过，上下文干净 |

**核心差异：一个上来就干，一个想清楚了再干。**

## 14个技能清单

| 技能 | 用途 |
|------|------|
| brainstorming | 接到需求先做头脑风暴，不急着动手 |
| writing-plans | 方案确定后写计划，计划通过后再执行 |
| subagent-driven-development | 拆成子任务，分给多个子 Agent 并行干 |
| test-driven-development | 先写测试，再写代码，红绿循环 |
| requesting-code-review | 代码写完了，主动请求 Review |
| receiving-code-review | 收到 Review 意见，逐条处理 |
| systematic-debugging | 遇到 Bug 不瞎猜，系统化排查 |
| verification-before-completion | 完工之前，逐项验证 |
| using-git-worktrees | 多个任务并行，互不干扰 |
| writing-skills | 自己也能写 Skill，扩展能力 |
| finishing-a-development-branch | 收尾规范化，不留烂摊子 |
| dispatching-parallel-agents | 并行派发子 Agent，提升效率 |
| using-superpowers | Superpowers 使用指南 |
| executing-plans | 按计划执行，不跑偏 |

## 支持工具

**原版官方支持：**
- Claude Code（主力推荐）
- Codex CLI / Codex App（OpenAI）
- Gemini CLI
- OpenCode
- Cursor
- GitHub Copilot CLI
- Factory Droid

**中文增强版 superpowers-zh：**
- 扩展支持 17 款工具，包括 **Hermes Agent** 和 **OpenClaw**
- 完整汉化 + 新增 4 个中国特色技能

## 安装方式

**原版（Claude Code）：**
```bash
/plugin install superpowers@claude-plugins-official
```

**中文增强版（多工具）：**
```bash
npx superpowers-zh
```

**Hermes Agent：**
```bash
cd /your/project
npx superpowers-zh --tool hermes
```

**OpenClaw：**
```bash
cd /your/project
npx superpowers-zh
```

## 核心观点

1. **方法论替代模型调优**：试过 3 个模型、调过十几组参数，发现 Claude 还是那个 Claude。真正决定 AI 编程代理能不能干活的，是"怎么干"的指令。

2. **类比名校程序员**：招了一个名校毕业的程序员，学历好、智商高，但不告诉他项目规范、代码标准、工作流程，一样干不好。

3. **从被动工具到协作者**：AI 编程代理学了这些技能，就不再是"你问它答"的被动工具，而是一个有方法、有节奏、有质量意识的协作者。

4. **替代无方法论程序员**：短期内 AI 不能替代程序员，但 AI + 好方法论可以替代一个没有方法论的程序员。

## 相关链接

- Superpowers 原版：github.com/obra/superpowers
- Superpowers 中文增强版：github.com/jnMetaCode/superpowers-zh

## 相关实体

- [[Superpowers]]
- [[Claude-Code]]
- [[Hermes-Agent]]
- [[OpenClaw]]
- [[Codex]]

## 相关概念

- [[AI编程方法论]]
- [[Skill系统]]
- [[TDD]]
- [[代码审查]]
- [[Multi-Agent]]