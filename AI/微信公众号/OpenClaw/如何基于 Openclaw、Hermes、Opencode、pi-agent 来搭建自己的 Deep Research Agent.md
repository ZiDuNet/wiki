> 📎 来源: [即心的AI笔记](https://mp.weixin.qq.com/s?__biz=MzkzNDkyNDU2NQ==&mid=2247484041&idx=1&sn=8b79fe3ea1724e015ea50a8cb71b969b&chksm=c3e94d4843d883e6c281868ed05fc51d8d1983da58e96702af32e5e33c482f8696b0b00ea295&mpshare=1&scene=1&srcid=0526bDLqhufgExZ9IxYBNZvt&sharer_shareinfo=4c4ca0a24dfda2b87b198a462bb0cb1c&sharer_shareinfo_first=4c4ca0a24dfda2b87b198a462bb0cb1c) | 时间: 2026-05-26 12:42

---

**基于这些现有框架搭建 Deep Research Agent 的可行性与具体路径**（2026 年现状）：

这些框架主要偏向**持久化、自主执行型 Agent**（尤其是 coding/personal assistant），而非纯研究型。但它们高度可扩展，通过 **MCP（Model Context Protocol）**、自定义 skills/tools 和 multi-agent 机制，完全可以改造成强大的 Deep Research Agent。核心优势是**持久内存 + 长期运行 + 真实行动能力**（文件、shell、浏览器），这对“迭代研究 + 保存成果 + 持续跟踪”非常友好。

### 1. 框架快速对比（针对 Deep Research 适配性）

- **OpenClaw**：最成熟的“always-on”个人 Agent 运行时。持久 workspace/memory、heartbeat 调度、多渠道交互（Telegram/WhatsApp 等）。底层用 **Pi**。适合搭建“长期研究助手”（能自主跑几天、跟踪主题、生成报告并通知你）。
- **Pi-agent**：极简核心（仅 4 个基础工具：read/write/edit/bash），高度可扩展。通过 MCP 接入外部工具。适合作为底层 harness，自定义 research-specific skills。
- **Hermes Agent**（Nous Research）：**最推荐用于 Deep Research**。自带 closed learning loop（从经验创建/改进 skills、持久记忆、跨会话 recall、用户建模）。支持从 OpenClaw 迁移。自主性强，适合“越用越懂你的研究偏好”的 Agent。
- **OpenCode**：更偏 coding，但支持 Primary Agents（Plan/Build）+ Subagents、多模型混合、MCP。适合研究中需要**代码执行、数据分析、图表生成**的部分（如文献处理、数据爬取后分析）。

**推荐组合**：以 **Hermes 或 OpenClaw (Pi)** 作为主运行时 + OpenCode 处理 coding-heavy 子任务 + MCP 统一工具层。

### 2. 搭建 Deep Research Agent 的具体步骤

#### **步骤 1: 基础部署与配置**

- 安装 OpenClaw / Hermes（推荐 VPS 或本地 Mac Mini 持久运行）。
- 配置多模型：强推理模型（Claude 4 / o-series / Gemini）做 Planner/Synthesizer；更快模型（Gemini Flash / 本地）做检索/总结。
- 启用持久内存（MEMORY.md、SQLite/FTS5、全会话 recall）。Hermes 在这点上原生更强。
- 设置 Heartbeat / Scheduler：让 Agent 定期醒来检查新信息、继续未完研究。

#### **步骤 2: 核心组件改造（Multi-Agent 架构）**

使用框架内置的 **Agent / Subagent / Skill 系统**：

- **Planner Agent**（Lead）：分解查询 → 生成研究计划（子问题、关键词、优先级）。
- **Researcher Agents**（多个并行 Subagents）：执行搜索、浏览、验证。
- **Critic / Verifier Agent**：评估来源可信度、找矛盾、识别缺口。
- **Synthesizer Agent**：整合成带引用的 Markdown/PDF 报告 + 视觉化。
- **Coder / Analyzer Agent**（用 OpenCode）：处理数据清洗、可视化、代码复现。

在 **Hermes/OpenClaw** 中通过定义 **Skills**（可复用 workflow）实现；Pi 则通过扩展工具/MCP adapter。

#### **步骤 3: 集成关键工具（MCP 是关键）**

- **搜索与浏览**：Tavily / Perplexity / Firecrawl MCP server（深度页面抓取 + 总结）。
- **学术**：Semantic Scholar / arXiv API / Google Scholar tools。
- **多模态**：YouTube 分析、PDF 阅读、图像/图表理解。
- **执行**：Browser automation（Playwright）、代码执行（OpenCode 集成）、文件系统（保存中间结果）。
- **外部 MCP**：DeepWiki（GitHub 探索）、Parallel Search 等。Pi 和 OpenCode 原生支持 MCP。

注册这些工具到 Agent 的 tool calling 系统中，Planner 动态决定调用顺序。

#### **步骤 4: 实现迭代与反思循环**

- **Self-Reflection**：在 Skill/Prompt 中加入 Critique 步骤（“检查信息缺口、潜在偏差、下一步行动”）。
- **迭代**：用状态机或循环（LangGraph 风格，但在这些框架中用 event-driven messaging 或 cron + memory）。
- **Grounding**：强制每步输出来源 + 引用追踪。Hermes 的 learning loop 可自动把成功的研究 pattern 转成 reusable Skill。
- **Human-in-the-loop**：关键决策点通过 chat app 通知你审核。

#### **步骤 5: 输出与持久化**

- 生成结构化报告（带 inline citations、TOC、executive summary）。
- 保存到 workspace：research\_project/ 目录（raw sources、summaries、final.md）。
- 通知 + 归档：完成后通过 Telegram 发送摘要，并把新 Skill 加入库。

#### **步骤 6: 优化与生产化**

- **Observability**：加 logging、Langfuse 或自定义 dashboard。
- **Cost Control**：分层模型 + 总结压缩上下文。
- **Eval**：定期用 LLM Judge 测试事实准确性、覆盖度。
- **Scaling**：多 Agent Army（一个总管 + 多个专题 Researcher）。

### 3. 实践Tips与潜在挑战

- **从简单开始**：先做一个“单主题研究 Skill”（输入 query → 输出报告），然后扩展成 multi-step。
- **迁移优势**：Hermes 可直接 import OpenClaw 配置，降低切换成本。
- **挑战**：
  - 上下文管理：用总结 + RAG 避免爆炸。
  - Hallucination：强制 multi-source verification + Critic Agent。
  - 安全性：尤其是 shell/browser 工具，严格 sandbox + approval 机制（OpenClaw 支持）。
- **基准参考**：参考开源 DeepResearchAgent 项目或 MCP-powered workshop，复用其 tool 定义。

这些框架的**持久化 + 自主执行**特性，反而比纯 LangGraph/CrewAI 更适合“真实世界长期研究”（例如跟踪行业趋势、文献综述更新）。Hermes 的 learning loop 是最大亮点，能让你的 Deep Research Agent 随时间显著变强。
