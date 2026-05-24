---
title: Honcho：AI Agent记忆库，3年打磨让Agent真正认识用户
type: source-summary
tags: [Agent, 记忆系统, Honcho, Plastic Labs, 用户画像, 持续学习]
sources: [3.3K Star！做了3年的 AI 记忆库 Honcho：让你的 Agent 真正_认识_用户.md]
created: 2026-05-24
updated: 2026-05-24
---

# Honcho：AI Agent记忆库，3年打磨让Agent真正认识用户

## 核心定位

**一句话定位**：为 AI Agent 提供持久记忆，让 Agent 真正理解并记住每个用户。

Plastic Labs 开发的开源记忆库，2023年9月开始开发，当前版本 **v3.0.6**，**3,333 Stars**（截至 2026-05-08）。

仓库：https://github.com/plastic-labs/honcho

## 为什么值得关注

大多数"AI记忆"方案只是把对话塞进 Context Window，或简单做个 RAG 检索。Honcho 做的不同：

1. **持续学习**，不只是存储——用户画像随时间演化
2. **自然语言查询**，不需要写检索代码——直接问问题
3. **多实体支持**，不只记住用户——任何实体都可以有记忆
4. **做了3年**，不是两周出来的玩具——v3.0.6 经过了大量打磨

## 核心概念：4个基本单元

| 单元 | 说明 |
| --- | --- |
| **Workspace** | 应用容器，一个 App 对应一个 Workspace |
| **Peer** | 任何实体，可以是用户、Agent、群组、想法 |
| **Session** | 一次对话上下文 |
| **Messages** | 对话内容本身 |

设计理念：记忆不只是属于"用户"，任何有意义的实体都可以拥有记忆。

## Benchmark 数据

| Benchmark | Honcho 得分 |
| --- | --- |
| LongMem S | **90.4%** |
| LoCoMo | **89.9%** |
| BEAM 100K | **0.630** |

完整测评：evals.honcho.dev

## 技术架构：Deriver 组件

Honcho 后台运行 **Deriver** 组件，持续处理 session 数据：

- 生成用户摘要
- 构建用户表征（Representation）
- 管理"梦境"任务（离线深度推理）

支持**本地 Representation 和全局 Representation 的区分**——同一个用户，在不同 session 中的表征可以不同。

## SDK 支持

Python 和 TypeScript SDK：

```bash
pip install honcho-ai       # Python
npm install @honcho-ai/sdk  # TypeScript
```

官方文档：https://docs.honcho.dev

## 部署方式

**托管服务**：app.honcho.dev，注册送 **$100 免费额度**。

**自托管**：PostgreSQL + pgvector + FastAPI，走 Docker 或 uv 直接跑。

```bash
git clone https://github.com/plastic-labs/honcho.git
cd honcho && uv sync
uv run fastapi dev src/main.py
uv run python -m src.deriver  # 后台推理进程
```

## 代码示例

```python
from honcho import Honcho

# 初始化
honcho = Honcho(workspace_id="my-app")
alice = honcho.peer("alice")
tutor = honcho.peer("tutor")

# 存对话
session = honcho.session("session-1")
session.add_messages([
    alice.message("能帮我做数学作业吗？"),
    tutor.message("没问题，把题发过来！"),
])

# 自然语言查询用户画像
response = alice.chat("这个用户最容易接受哪种学习方式？")

# 获取带摘要的上下文，直接传给 OpenAI
context = session.context(summary=True, tokens=10_000)
openai_messages = context.to_openai(assistant=tutor)
```

`alice.chat("这个用户最容易接受哪种学习方式？")` 这一行是重点——**用自然语言问关于用户的问题**，不用写 SQL，不用手动维护向量索引。

## 关联实体

- [[Honcho]] — Plastic Labs 开发的 Agent 记忆系统
- [[Plastic-Labs]] — Honcho 的开发团队

## 关联概念

- [[记忆系统]] — Agent 的持久化记忆机制
- [[用户画像]] — Agent 对用户的理解和表征
- [[Agent工程原则]] — Agent 工程化方法论

## 来源

> 📎 来源: [杰克王聊AI](https://mp.weixin.qq.com/s?__biz=MzI2NjI1OTQ1MA==&mid=2247492358&idx=1&sn=37e0356f6fb1b392406fc84c1d867b2b) | 时间: 2026-05-24 12:31