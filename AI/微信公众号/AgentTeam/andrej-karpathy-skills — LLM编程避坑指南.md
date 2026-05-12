# Karpathy-Inspired Claude Code Guidelines

---

## 📋 中文摘要

### 项目简介
这是一个单文件 `CLAUDE.md`，旨在改进 Claude Code 的行为，灵感来源于 Andrej Karpathy 对 LLM 编程陷阱的观察。

### 核心问题
根据 Karpathy 的观点，LLM 在编程时存在以下问题：
1. **错误假设**：模型会替用户做错误假设并继续执行，不进行检查
2. **不管理困惑**：不寻求澄清、不暴露不一致性、不呈现权衡方案
3. **过度复杂化**：喜欢过度复杂化代码和 API，膨胀抽象，不清理死代码
4. **意外修改**：有时会修改/删除它们不完全理解的注释和代码

### 解决方案：四大原则

| 原则 | 解决的问题 |
|------|-----------|
| **先思考后编码** | 错误假设、隐藏的困惑、缺失的权衡 |
| **简约优先** | 过度复杂化、膨胀的抽象 |
| **精准修改** | 无关编辑、触碰不该触碰的代码 |
| **目标驱动执行** | 通过测试优先、可验证的成功标准 |

### 四大原则详解

#### 1. 先思考后编码
- 明确陈述假设——如果不确定，先问而不是猜测
- 呈现多种解释——存在歧义时不要沉默选择
- 适当时要反驳——如果存在更简单的方法，要说明
- 困惑时停止——指出不明确之处并寻求澄清

#### 2. 简约优先
- 不要添加超出要求的特性
- 不要为单次使用的代码创建抽象
- 不要添加未被请求的"灵活性"或"可配置性"
- 不要为不可能的场景编写错误处理
- 如果 200 行代码可以写成 50 行，那就重写

**测试标准：** 高级工程师会说这太复杂了吗？如果是，那就简化。

#### 3. 精准修改
- 不要"改进"相邻的代码、注释或格式
- 不要重构没坏的东西
- 匹配现有风格，即使你会用不同方式
- 如果注意到无关的死代码，提一下——不要删除它
- 只删除你的修改造成的无用代码

**测试标准：** 每个修改的行都应该能直接追溯到用户的请求。

#### 4. 目标驱动执行
将命令式任务转换为可验证的目标：

| 不要这样做... | 转换为... |
|--------------|-----------|
| "添加验证" | "为无效输入编写测试，然后让它们通过" |
| "修复 bug" | "编写一个能复现它的测试，然后让它通过" |
| "重构 X" | "确保重构前后测试都通过" |

对于多步骤任务，陈述简要计划，每步都有验证检查。

### 安装方式
- **方式 A（推荐）：Claude Code 插件**
- **方式 B：项目级 CLAUDE.md 文件**

### 核心洞察
> "LLM 非常擅长循环直到满足特定目标...不要告诉它做什么，给它成功标准然后看着它执行。"

### 如何知道它在起作用
- diff 中不必要的更改更少
- 由于过度复杂化导致的重写更少
- 在实施之前会提出澄清问题
- 干净、最小化的 PR——没有顺便重构或"改进"

### 权衡说明
这些准则偏向**谨慎而非速度**。对于简单任务，使用判断力——不是每个更改都需要完全的严谨。

---

## 📄 英文原文

# Karpathy-Inspired Claude Code Guidelines

> Check out my new project [Multica](https://github.com/multica-ai/multica) — an open-source platform for running and managing coding agents with reusable skills.
>
> Follow me on X: [https://x.com/jiayuan_jy](https://x.com/jiayuan_jy)

A single `CLAUDE.md` file to improve Claude Code behavior, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

English | [简体中文](./README.zh.md)

## The Problems

From Andrej's post:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."

> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

## The Solution

Four principles in one file that directly address these issues:

| Principle | Addresses |
|-----------|-----------|
| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity First** | Overcomplication, bloated abstractions |
| **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| **Goal-Driven Execution** | Leverage through tests-first, verifiable success criteria |

## The Four Principles in Detail

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

LLMs often pick an interpretation silently and run with it. This principle forces explicit reasoning:

- **State assumptions explicitly** — If uncertain, ask rather than guess
- **Present multiple interpretations** — Don't pick silently when ambiguity exists
- **Push back when warranted** — If a simpler approach exists, say so
- **Stop when confused** — Name what's unclear and ask for clarification

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

Combat the tendency toward overengineering:

- No features beyond what was asked
- No abstractions for single-use code
- No "flexibility" or "configurability" that wasn't requested
- No error handling for impossible scenarios
- If 200 lines could be 50, rewrite it

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting
- Don't refactor things that aren't broken
- Match existing style, even if you'd do it differently
- If you notice unrelated dead code, mention it — don't delete it

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused
- Don't remove pre-existing dead code unless asked

**The test:** Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform imperative tasks into verifiable goals:

| Instead of... | Transform to... |
|--------------|-----------------|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let the LLM loop independently. Weak criteria ("make it work") require constant clarification.

## Install

**Option A: Claude Code Plugin (recommended)**

From within Claude Code, first add the marketplace:
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
```

Then install the plugin:
```
/plugin install andrej-karpathy-skills@karpathy-skills
```

This installs the guidelines as a Claude Code plugin, making the skill available across all your projects.

**Option B: CLAUDE.md (per-project)**

New project:
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

Existing project (append):
```bash
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

## Using with Cursor

This repository includes a committed Cursor project rule ([`.cursor/rules/karpathy-guidelines.mdc`](.cursor/rules/karpathy-guidelines.mdc)) so the same guidelines apply when you open the project in Cursor. See **[CURSOR.md](CURSOR.md)** for setup, using the rule in other projects, and how this relates to Claude Code.

## Key Insight

From Andrej:

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops.

## How to Know It's Working

These guidelines are working if you see:

- **Fewer unnecessary changes in diffs** — Only requested changes appear
- **Fewer rewrites due to overcomplication** — Code is simple the first time
- **Clarifying questions come before implementation** — Not after mistakes
- **Clean, minimal PRs** — No drive-by refactoring or "improvements"

## Customization

These guidelines are designed to be merged with project-specific instructions. Add them to your existing `CLAUDE.md` or create a new one.

For project-specific rules, add sections like:

```markdown
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have tests
- Follow the existing error handling patterns in `src/utils/errors.ts`
```

## Tradeoff Note

These guidelines bias toward **caution over speed**. For trivial tasks (simple typo fixes, obvious one-liners), use judgment — not every change needs the full rigor.

The goal is reducing costly mistakes on non-trivial work, not slowing down simple tasks.

## License

MIT
