> 📎 来源: [网线那头有只猫](https://mp.weixin.qq.com/s?__biz=MzUyOTg0MDY4Nw==&mid=2247484096&idx=1&sn=f2d51ece399d7e837f3394d7cb3a3d81&chksm=fb480313b6dbe9c1c8d7a22d63033a3ade0760eec9f94426b88edc4706bab2137378b7087f72&mpshare=1&scene=1&srcid=0529Cm1eXnVGCXlWNSueLqmw&sharer_shareinfo=f95e945d7445d53691666146ed75de1e&sharer_shareinfo_first=f95e945d7445d53691666146ed75de1e) | 时间: 2026-05-29 12:55

---

想学 AI Agent，打开 GitHub 一搜，满屏的 awesome list、教程、框架……

看了三天还是不知道从哪开始。

这不是你的问题——AI Agent 领域发展太快，2024 年还没有 Agent 这个词，2025 年已经满天飞了。资料多、路线乱、门槛高，是每个入门者的共同痛点。

今天介绍一个项目，把这件事做清楚了：**awesome-agentic-ai-zh**——一份从零开始的中文 AI Agent 学习地图。

---

## 项目是什么？

**awesome-agentic-ai-zh** 是 GitHub 上一个开源学习路线图项目，目前 **1,743 Stars**，MIT 协议，由开发者 WenyuChiou 主导维护。

它不是简单的资源列表，而是做了三件事：

| 核心 | 内容 | 规模 |
| --- | --- | --- |
| **学习路线图** | 8 个阶段，从 Python 基础到多 Agent 系统 | 8 stages、2 tracks |
| **资源整理** | 240+ 精选项目，每个附星数、适合谁、教什么 | 240+ projects |
| **动手练习** | 每阶段 1-5 个基础练习，70-150 行代码起步 | 23 个练习 |

更贴心的是，**三语完整维护**——繁体中文（主版）、简体中文、英文，不是机翻。

---

## 两套学习路径：你是哪种人？⭐

这个项目最聪明的设计是**按目标分流**，而不是一条路走到底。

### Track A — CLI Power User（8-10 周）

**适合**：不想自己写 Agent，但想用现成工具提效的人。

**路线**：Stage 0-2（基础）→ A1（选一个 CLI Agent）→ A2（建立工作流）→ A3（接入生产环境）

核心内容：7 个主流 CLI Agent 对比（Claude Code、Codex、OpenCode、Gemini CLI 等）、CLAUDE.md 配置、slash command、MCP 接入 CI 自动化。

**目标**：把 CLI Agent 用到极致，成为效率高手。

### Track B — Agent Builder（16-22 周）

**适合**：想从零打造自己 Agent 的人。

**路线**：Stage 0-2（基础）→ 3（Tool Use + ReAct）→ 4（框架学习）→ 5（Claude Code 生态）→ 6（RAG + Memory）→ 7（Multi-Agent）→ 8（Agent Interfaces）

核心内容：function calling、LangGraph/AutoGen/CrewAI 框架、MCP/Skills/Plugins 生态、向量数据库、多 Agent 编排、eval/observability。

**目标**：从 LLM 使用者进化为 Agent 系统构建者。

**两条路不互斥**——大多数人先走 A 把工具用起来，再回到 B 学内部原理。

---

## 8 个阶段，一目了然

| Stage | 主题 | 预估时间 |
| --- | --- | --- |
| 0 | 基础准备（Python/Git/API） | 1-2 周 |
| 1 | LLM 基础（Token/API/各家对比） | 1 周 |
| 2 | Prompt 设计（系统 prompt/few-shot/CoT） | 1-2 周 |
| 3 | 工具使用与第一个 Agent（Function Calling/ReAct） | 2-3 周 |
| 4 | Agent 框架（LangGraph/AutoGen/CrewAI） | 2-3 周 |
| 5 | Claude Code 生态（MCP/Skills/Plugins）⭐ | 3-4 周 |
| 6 | 上下文管理（RAG/Memory/向量数据库） | 2 周 |
| 7 | 多 Agent 与生产化（编排/Eval/Observability） | 2-4 周 |
| 8 | Agent Interfaces（Computer Use/Browser/Sandbox） | 2-3 周 |

**关键设计**：Stage 5 和 Stage 8 是两条路的**共用 Hub**——Track A 和 Track B 都会用到，但学习视角不同。

---

## 三层概念进化

这个项目提出了一个很实用的认知框架：

1. 1. **Prompt Engineering**（Stage 2）→ 单一 prompt 怎么写
2. 2. **Context Engineering**（Stage 3+）→ 动态组合 system prompt + memory + 检索结果 + tool schema
3. 3. **Harness Engineering**（Stage 7）→ agent loop / eval / observability / deploy 完整生产系统

三层递进，从"写好一句话"到"搭建一个系统"，非常清晰。

---

## 五条延伸路线

走完主干后，按角色分流：

| 角色 | 内容 |
| --- | --- |
| 🔬 研究员 | 文献整理、paper 写作、multi-agent review |
| 💻 开发者 | Cursor、Aider、CLI delegation、code review |
| 🎓 教师 | 备课、投影片、学生 feedback、伦理 |
| 📊 知识工作者 | 邮件、会议纪要、报告自动化 |
| 👥 日常使用者 | 写信、学习、隐私场景、CLI 入门 |

---

## 实战亮点

**7 步打造第一个 AI Agent**——一个 Paper Summary Bot，从 Stage 1 一路写到 Stage 7，约 350 行真实代码。同一个项目贯穿所有阶段，学完就知道"为什么需要后面的东西"。

**每个练习都有正确用法**：项目明确提醒——不要直接抄 

```
starter.py
```

 的答案，要自己重写、卡住再对照。这种学习态度很难得。

---

## 资源与结语

- **GitHub**：https://github.com/WenyuChiou/awesome-agentic-ai-zh
- **在线文档**：https://wenyuchiou.github.io/awesome-agentic-ai-zh/
- **协议**：MIT（完全免费）

**一句话总结**：这是目前中文圈最完整的 AI Agent 学习路线图。不是简单的资源堆砌，而是有路线、有练习、有分流的系统化学习方案。如果你想入门 AI Agent，或者想系统梳理已有知识，这份地图值得收藏。

> "240+ 资源不是终点，而是起点。走完这条路，你就知道接下来该去哪了。"
