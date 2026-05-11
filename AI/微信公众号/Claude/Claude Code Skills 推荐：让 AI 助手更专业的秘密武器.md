> 📎 来源: [超级AI技术](https://mp.weixin.qq.com/s?__biz=MzUyNzA1NDY0MQ==&mid=2247485713&idx=1&sn=c7543f46b267772d79b840a94f7dd71f&chksm=fbec57f04858dc12996859af4771458ca9981aa918aaf64c57d3c3a05f921d2c22816da58b32&mpshare=1&scene=1&srcid=0510DosDPQvwNReAZB0NKxru&sharer_shareinfo=485d94a1a5b7cf0083d6facc1b96c513&sharer_shareinfo_first=485d94a1a5b7cf0083d6facc1b96c513) | 时间: 2026-05-10 15:56

---

> Skills 不是提示词模板，而是可复用的工程方法论。

---

很多人用 Claude Code 时，发现 AI 写的代码"能用但不够专业"——测试不完整、架构混乱、边界情况没考虑。

问题不一定在于 AI 能力不足，更可能在于缺乏引导。Skills 就是用结构化流程引导 AI 按专业标准工作。

这篇推荐两个高质量的 Skills 仓库，覆盖不同场景。

---

## 一、什么是 Skills

Skills 是可复用的知识模块，告诉 AI "如何做"而不仅仅是"做什么"。

### Skills vs CLAUDE.md

| 维度 | CLAUDE.md | Skills |
| --- | --- | --- |
| 作用 | 项目规则 | 工作流程 |
| 加载 | 每次会话 | 按需调用 |
| 内容 | 静态约定 | 动态步骤 |
| 示例 | "用 TypeScript"、"测试覆盖率 80%" | "TDD 工作流"、"代码审查清单" |

### Skills 的典型结构

---

name: test-driven-development

description: 用测试驱动开发。实现逻辑、修复 bug、修改行为时使用。

---

## Overview

[为什么需要这个 skill]

## Workflow

[具体步骤]

## Checklist

[验证清单]

## Rationalizations

[常见借口 + 反驳]

## Red Flags

[危险信号]

**关键设计**：

1. **流程而非散文**——Skills 是工作流，不是参考文档

2. **反合理化表**——列出常见借口并反驳（如"我稍后补测试"）

3. **验证不可协商**——每个 Skill 都有证据要求

---

## 二、agent-skills：生产级工程实践

**仓库**：addyosmani/agent-skills

**定位**：覆盖完整软件开发生命周期，适合追求生产级代码质量的团队。

### 核心理念

DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP

20 个 Skills 映射到开发各阶段，每个阶段都有验证门控。

### 推荐 Skills

#### 1. test-driven-development

**场景**：实现逻辑、修复 bug、修改行为。

**核心流程**：

RED（写失败测试）→ GREEN（写最小代码通过）→ REFACTOR（重构）

**关键原则**：

• **垂直切片，不是水平切片**

```
错误：先写完所有测试，再实现所有代码
  正确：一个测试 → 一个实现 → 循环
```

• **测试行为，不测试实现**——测试重构后应仍然通过

• **Prove-It 模式**——bug 修复必须先写复现测试

**反合理化示例**：

| 借口 | 现实 |
| --- | --- |
| "我稍后补测试" | 你不会。而且事后写的测试测的是实现，不是行为 |
| "这太简单不用测" | 简单代码会变复杂。测试就是文档 |

#### 2. spec-driven-development

**场景**：新项目、新功能、重大变更。

**核心流程**：

SPECIFY → PLAN → TASKS → IMPLEMENT

   ↓        ↓       ↓        ↓

 人工审查  人工审查  人工审查  人工审查

**Spec 六要素**：

1. **Objective**——目标是什么，成功标准

2. **Commands**——构建、测试、lint 命令

3. **Project Structure**——目录结构

4. **Code Style**——代码风格示例

5. **Testing Strategy**——测试框架和覆盖要求

6. **Boundaries**——Always/Ask First/Never 三层

**关键原则**：

• **假设前置**——开始前列出所有假设

• **成功标准可测试**——"Dashboard 更快" → "LCP < 2.5s"

#### 3. code-review-and-quality

**场景**：合并前审查任何变更。

**五轴审查**：

| 轴 | 检查点 |
| --- | --- |
| Correctness | 是否符合需求？边界情况？错误处理？ |
| Readability | 命名清晰？逻辑简单？无过度抽象？ |
| Architecture | 遵循现有模式？无循环依赖？ |
| Security | 输入验证？无密钥泄露？参数化查询？ |
| Performance | N+1 查询？无界循环？分页？ |

**变更大小标准**：

~100 行 → 好

~300 行 → 可接受（单一逻辑变更）

~1000 行 → 太大，拆分

**审查分类标签**：

| 标签 | 含义 |
| --- | --- |
| Critical | 阻塞合并 |
| Nit | 可选，可忽略 |
| Optional/Consider | 建议但不强制 |
| FYI | 仅信息 |

#### 4. debugging-and-error-recovery

**场景**：bug 报告、异常行为、性能回退。

**六阶段诊断**：

Phase 1: 构建反馈循环（最重要！）

Phase 2: 复现

Phase 3: 假设（3-5个排名）

Phase 4: 工具验证（一次改一个变量）

Phase 5: 修复 + 回归测试

Phase 6: 清理 + 复盘

**反馈循环构建优先级**：

1. 失败的测试

2. curl/HTTP 脚本

3. CLI 调用 + 快照对比

4. 无头浏览器脚本

5. 回放捕获的 trace

6. 抛弃式 harness

7. 属性/模糊测试

8. 二分 harness

9. 差分循环

10. 人机交互脚本

**关键洞察**：没有反馈循环，不要开始假设。

### 安装方式

/plugin marketplace add addyosmani/agent-skills

/plugin install agent-skills@addy-agent-skills

---

## 三、skills：高效开发者的工具箱

**仓库**：mattpocock/skills

**定位**：解决 AI 助手的核心失败模式，适合追求效率的个人开发者。

### 核心理念

AI 助手有四个核心失败模式：

1. **没有按你的想法做**——沟通鸿沟

2. **太啰嗦**——没有共享语言

3. **代码不工作**——反馈循环缺失

4. **代码一团糟**——设计被忽视

### 推荐 Skills

#### 1. grill-me / grill-with-docs

**场景**：开始任何变更前，对齐理解。

**核心做法**：

> 面试我，直到我们达成共识。每个分支逐一解决。

**grill-with-docs 增强**：

• 使用项目的领域语言挑战你的计划

• 冲突术语立即指出："你的词汇表定义 'cancellation' 是 X，但你似乎指 Y"

• 决策即时写入

```
CONTEXT.md
```

 和 ADR

**效果**：15 分钟对齐避免数小时返工。

#### 2. tdd

**场景**：任何需要测试的场景。

**与 agent-skills/tdd 的区别**：

• 更简洁，聚焦核心原则

• 强调"测试行为，不测试实现"

• 包含 mocking 指南

**关键原则**：

偏好顺序：

1. 真实实现 → 最高置信度

2. Fake → 依赖的内存版本

3. Stub → 返回固定数据

4. Mock（交互）→ 最少使用

#### 3. diagnose

**场景**：调试困难 bug。

**核心流程**：

构建反馈循环 → 复现 → 假设（3-5个排名）→ 验证 → 修复 → 回归测试

**关键洞察**：

> 反馈循环就是技能本身。如果你有一个快速、确定性的通过/失败信号，你会找到原因。如果没有，盯着代码看再久也没用。

**非确定性 bug**：

目标是提高复现率，不是 100% 复现。50% 概率的 bug 可调试，1% 的不行——持续提高概率直到可调试。

#### 4. improve-codebase-architecture

**场景**：代码库变成泥球时。

**核心概念**：

• **模块**：有接口和实现的任何东西

• **深度**：小接口背后的行为量。深 = 高杠杆

• **缝隙**：接口所在的地方

**深度化测试**：

> 想象删除这个模块。如果复杂性消失，它只是透传。如果复杂性分散到 N 个调用者，它在赚取价值。

**流程**：

1. 探索——找出摩擦点

2. 展示候选——编号列表

3. 烤问循环——逐一决策

#### 5. caveman

**场景**：节省 token。

**效果**：压缩 ~75% token，保持完整技术准确性。

**做法**：去掉填充词，保持技术准确。

### 安装方式

npx skills@latest add mattpocock/skills

然后在 Claude Code 中运行

```
/setup-matt-pocock-skills
```

。

---

## 四、两个仓库对比

| 维度 | agent-skills | skills (mattpocock) |
| --- | --- | --- |
| Skills 数量 | 20 | 11 |
| 覆盖范围 | 完整 SDLC | 核心问题 |
| 风格 | 企业级、流程驱动 | 实用主义、问题驱动 |
| 学习曲线 | 较陡 | 平缓 |
| 验证严格度 | 高（门控） | 中（实用） |
| 适合场景 | 团队、生产项目 | 个人、快速迭代 |

### 选择建议

**选 agent-skills 如果**：

• 追求生产级代码质量

• 团队协作，需要统一标准

• 完整项目周期，从需求到上线

**选 skills (mattpocock) 如果**：

• 快速迭代，不想过度流程

• 个人项目，追求效率

• 解决特定问题（调试、对齐、架构）

**两者可以混用**：

• 用

```
grill-with-docs
```

 对齐需求

• 用

```
spec-driven-development
```

 写规格

• 用

```
tdd
```

 写代码

• 用

```
diagnose
```

 调试

• 用

```
code-review-and-quality
```

 审查

---

## 五、如何使用 Skills

### 调用方式

/tdd

/grill-me

/spec-driven-development

"用 TDD 方式实现用户认证"

### 最佳实践

1. **按需调用**——不要一次加载所有 Skills

2. **组合使用**——grill → spec → tdd → review

3. **定期更新**——Skills 会迭代改进

4. **自定义**——根据项目调整 Skill 内容

### 自定义 Skills

Skills 是纯 Markdown，可以修改：

---

name: my-tdd

description: 我的 TDD 工作流，适配团队规范

---

## Workflow

1. 写测试前先写测试名

2. ...

---

## 六、总结

Skills 把资深工程师的工作方法编码成可复用的流程。

| 场景 | 推荐 Skill |
| --- | --- |
| 需求不清晰 | ``` grill-me ```   /   ``` grill-with-docs ``` |
| 新功能开发 | ``` spec-driven-development ```   +   ``` tdd ``` |
| Bug 调试 | ``` diagnose ``` |
| 代码审查 | ``` code-review-and-quality ``` |
| 架构改进 | ``` improve-codebase-architecture ``` |
| 发布前检查 | ``` shipping-and-launch ``` |

**记住**：AI 助手默认走最短路径。Skills 强制它走正确的路径。

---

## 资源链接

• agent-skills - Addy Osmani 的生产级 Skills
 https://github.com/addyosmani/agent-skills

• skills - Matt Pocock 的高效工具箱
 https://github.com/mattpocock/skills

• Claude Code Skills 文档
 https://code.claude.com/docs/en/skills
