> 📎 来源: [豆爸AI](https://mp.weixin.qq.com/s?__biz=MzcwMjIwMDk2Mg==&mid=2247483881&idx=1&sn=65724676b9ee3a993c14ae72235a7c0d&chksm=f54acc8555a269e9067130c2444fec5ead42d3b86361329dc98f0f99bcd4b52a29bd16bc0c81&mpshare=1&scene=1&srcid=0424c1qrJZecsqWD12spmfKu&sharer_shareinfo=8ac752344a04f20b8a8e88c2f3829df5&sharer_shareinfo_first=8ac752344a04f20b8a8e88c2f3829df5) | 时间: 2026-04-24 00:20

---

AI Agent 架构深度解析

🐠 小鱼技术笔记 • 2026年4月14日 • 15分钟阅读

**核心观点：**Hermes Agent 和 OpenClaw 代表了 AI Agent 架构的两个极端方向——前者是「会学习的个人助手」，后者是「可控的企业级多智能体平台」。选择哪个框架，取决于你要解决的是「效率问题」还是「规模问题」。

1

## Hermes Agent：从代码看自进化架构

Hermes Agent 由 Nous Research 开源，GitHub 上已获得 **57,200+ stars**，核心代码 run\_agent.py 约 9,200 行，是一个真正意义上的**「自我进化型」AI Agent**。它的核心哲学是：Agent 应该像人类一样，通过经验积累不断变强。

### 🏛️ 五层架构体系

Hermes Agent 架构图

Layer 1

🚪 多入口接入层

CLI (~10K行) | Gateway (18+平台) | ACP (IDE适配)

↓

Layer 2

🤖 AIAgent 核心引擎 (~9,200行)

Prompt Builder | Provider Resolver | Tool Dispatch | Context Compress

↓

🎯 Skills

渐进式披露 (3级)

🧠 Memory

三层记忆架构

🛠️ Tools

47+ 工具 / 20 工具集

↓

Layer 4

🔄 自进化学习闭环

执行 → 评估 → 提取 → 精炼 → 复用

↓

Layer 5

☁️ 终端执行后端

Local | Docker | SSH | Daytona | Modal | Singularity

### 🔑 三大核心技术亮点

🎯

渐进式技能披露 (Progressive Disclosure)

Skills 采用三级加载策略：L0 仅加载技能列表(~3K tokens) → L1 加载具体内容 → L2 加载引用文件。避免上下文爆炸。

🧠

三层记忆架构

Session 记忆 + MEMORY.md(2.2K字符) + USER.md(1.375K字符)。SQLite + FTS5 全文搜索，支持跨会话召回。

🔄

自进化学习闭环

复杂任务(5+工具调用)后自动提取 Skill，通过 skill\_manage 工具创建。Skills 在使用过程中自我精炼。

☁️

Serverless 执行

支持 6 种终端后端：Local、Docker、SSH、Daytona、Modal、Singularity。Daytona/Modal 支持休眠唤醒，成本极低。

### 💡 代码级实现细节

**1. 核心对话循环**

🐍run\_agent.pyPython

```
# AIAgent 核心循环 (~9,200行)class AIAgent:    def run_conversation(self):        # 1. 构建系统提示词        system_prompt = prompt_builder.build()                # 2. 解析 Provider        provider = runtime_provider.resolve()                # 3. 执行工具调用循环        while not complete:            response = llm.chat_completion(messages, tools)            if response.tool_calls:                results = model_tools.handle_calls(response.tool_calls)                messages.extend(results)                # 4. 上下文压缩        if token_count > threshold:            context_compressor.compress(messages)
```

**2. Skill 自动提取机制**

当 Agent 完成一个复杂任务（通常涉及 5+ 次工具调用）后，会通过 

```
skill_manage
```

 工具自动创建 Skill：

⚡skill\_manage 工具调用Python

```
skill_manage(    action="create",    name="competitor-analysis-workflow",    content="""    # Competitor Analysis Workflow        ## When to Use    When researching competitor content strategy...        ## Procedure    1. Use browser tool to capture screenshots    2. Run vision analysis on key pages    3. Extract pricing and feature data    4. Generate comparison table        ## Pitfalls    - Don't rely on cached pages older than 7 days    - Verify pricing in multiple regions    """)
```

**3. 记忆管理**

使用 SQLite + FTS5 实现全文搜索，通过触发器自动同步 messages 表到 messages\_fts：

🗄️hermes\_state.pySQL

```
CREATE TRIGGER messages_fts_insert AFTER INSERT ON messages BEGIN    INSERT INTO messages_fts(rowid, content)     VALUES (new.id, new.content);END;
```

2

## OpenClaw：企业级多智能体框架

OpenClaw（又称 Clawdbot）是一个 TypeScript/Node.js 编写的企业级 AI Agent 框架，核心设计理念是**「可控、可观测、可扩展」**。与 Hermes 的单体 Agent 不同，OpenClaw 采用 **Gateway-Centric 四层架构**（Gateway → Session → Agent Runtime → Tools），强调多 Agent 协作和严格的安全边界。

### 🏗️ 核心架构特点

🌐

Gateway 中心控制

WebSocket 网关作为唯一控制平面，管理所有会话、工具执行和消息路由。支持多平台接入（Telegram、Discord、Slack 等）。

📦

Skills Hub 生态

OpenClaw 内置 53 个 bundled skills，ClawHub 提供额外技能下载。Skill 是静态的、可审计的，不会自主变化。

🔒

安全审计工具

提供 

```
openclaw security audit
```

 命令检查配置风险。支持 allowlist 和 exec 审批，但默认关闭（需手动启用）。设计为个人助手信任模型。

🔌

MCP 协议支持

通过安装 MCPorter 等技能，可连接 Model Context Protocol 服务器，扩展能力边界。

### ⚡ 与 Hermes 的关键差异

核心哲学

Hermes Agent

深度自学习

OpenClaw

广度可控制

Skills 来源

Hermes Agent

自主创建 + 精炼

OpenClaw

人工编写 + Hub

记忆机制

Hermes Agent

Agent 自主管理

OpenClaw

结构化 MEMORY.md

多 Agent 支持

Hermes Agent

Delegate 子代理

OpenClaw

原生多 Agent 编排

技术栈

Hermes Agent

Python

OpenClaw

TypeScript/Node.js

GitHub Stars

Hermes Agent

57,200+

OpenClaw

335,000+

🔒

## 安全特性深度对比（重要更正）

**⚠️ 重要说明：**经过深入代码和官方文档调研，发现之前的安全对比存在严重错误。实际情况与直觉相反：

- **Hermes Agent** 默认开启多层安全防护（危险命令审批、容器强化）
- **OpenClaw** 默认配置较为开放（

  ```
  security="full", ask="off"
  ```

  ），需手动加固

### 🛡️ Hermes Agent 七层安全模型

👤

1. 用户授权

通过 allowlists 和 DM pairing 控制谁可以与 Agent 交互，支持平台级和全局白名单

✅

2. 危险命令审批（默认开启）

内置 30+ 种危险模式检测（rm -rf, curl | sh 等），支持 manual/smart/off 三种模式，默认 manual 需用户确认

🐳

3. 容器隔离

Docker/Singularity/Modal 后端使用 --cap-drop ALL、--read-only、no-new-privileges、PID 限制 256

🔐

4. MCP 凭证过滤

环境变量隔离，防止 MCP 子进程访问敏感凭证，阻断密钥泄露

📝

5. 上下文文件扫描

自动检测 prompt injection 攻击，扫描项目文件中的恶意注入模式

🔒

6. 跨会话隔离

会话间数据完全隔离，cron job 存储路径加固防止路径遍历攻击

🧹

7. 输入消毒

终端工具后端的工作目录参数通过白名单验证，防止 shell 注入

### ⚠️ OpenClaw 安全模型

**默认配置警告：**

- 默认 

  ```
  security="full", ask="off"
  ```

   - 工具执行无需审批
- 官方文档明确说明：这是为"个人助手"体验设计的，不是漏洞
- 需要手动运行 

  ```
  openclaw security audit
  ```

   并配置 allowlist 才能加固
- **不适用于**多租户或对抗性用户场景

### 📊 安全特性对比表

| 安全特性 | Hermes Agent | OpenClaw |
| --- | --- | --- |
| **危险命令审批** | ✅ 默认开启 | ⚠️ 默认关闭 |
| **容器隔离** | ✅ 强化（cap-drop ALL, read-only） | ⚠️ 可选（需手动配置） |
| **安全审计工具** | ❌ 无 | ✅   ``` openclaw security audit ``` |
| **Prompt Injection 防护** | ✅ 内置扫描 | ❌ 无 |
| **适用场景** | 开箱即用的安全 | 需手动加固的个人助手 |

**结论：**如果你重视**开箱即用的安全性**，Hermes Agent 是更好的选择。如果你愿意投入时间手动配置安全策略，OpenClaw 也提供相应的工具（security audit、allowlist）。

💰

## Token 成本深度对比：为什么 Hermes 更省钱

Token 成本是 AI Agent 长期运营中最容易被忽视但又最致命的因素。根据社区实测数据，两者的成本差异可能达到 **10-20 倍**。

### 📊 真实成本数据对比

| 成本维度 | Hermes Agent | OpenClaw |
| --- | --- | --- |
| **典型日均成本** | $0.5 - $3 | $10 - $65+ |
| **长会话成本增长** | ✅ 线性增长（压缩后） | ⚠️ 指数增长（完整历史） |
| **基础设施成本** | ✅ $5 VPS 即可 | ⚠️ 需要更多资源 |
| **Serverless 选项** | ✅ Daytona/Modal 休眠免费 | ❌ 无原生支持 |

### 🔧 Hermes 的三大省 Token 机制

**1️⃣ 核心杀手锏：三级渐进式懒加载**

这是两者成本差异的**最主要来源**：

- **OpenClaw 的"全量加载"模式：**默认加载所有已安装技能的完整定义。即使只是问"今天天气如何"，也必须把成百上千个技能的完整说明书全部塞进上下文
- **数据：**OpenClaw 单次请求中，高达 **73% 的 Token 是固定开销**（工具定义占 46%，系统提示词占 27%），上下文窗口往往超过 10 万 Token
- **Hermes 的"按需加载"模式：**
  - **平时：**只加载技能的名称和简短描述（约 3K tokens）
  - **用时：**只有判断需要执行某个技能时，才加载完整内容
  - **结果：**技能库从 40 个增长到 200 个，基础上下文成本几乎不变

🤖

2. 智能模型编排（Auxiliary Models）

分工明确：图像分析、网页提取、技能匹配等"脏活累活"分配给轻量级模型（Gemini Flash）。只有核心推理才调用 Claude、DeepSeek 等昂贵模型。

🗜️

3. 双重上下文压缩 + Prompt Caching

Gateway 层(85%阈值) + Agent 层(50%阈值)双重压缩，可用便宜模型(GPT-4.1 Nano $0.10/M tokens)。Anthropic Prompt Caching 降低多轮对话成本 ~75%。

### ⚠️ OpenClaw 的高成本根源

**为什么 OpenClaw 更贵？**

- **73% 固定开销：**每次请求中，工具定义(46%) + 系统提示词(27%) = 73% 的 Token 是固定成本，与任务复杂度无关
- **全量技能加载：**无论是否需要，都加载所有 Skills 的完整定义，技能越多成本越高
- **完整对话历史：**每次请求发送整个会话历史，Token 数随会话长度线性增长
- **无原生压缩：**依赖外部工具或手动清理，没有内置的上下文压缩机制

**用户实测：**有用户报告使用 OpenClaw 日均消耗 $65+，而 Hermes 在相同工作量下仅需 $3-5，成本差异达 **10-20 倍**。

### ⚡ 成本优势缩小的例外情况

**注意：以下情况 Hermes 的成本优势可能会缩小**

- **任务极度复杂：**如果任务迫使 Hermes 加载大量技能详情并进行深度推理，Token 消耗自然会上升
- **配置不当：**手动关闭懒加载或强制使用最高级模型（如 Opus）处理简单任务

3

## 企业级选型指南（2026 版）

### 🎯 按组织类型选择

| 组织类型 | 推荐方案 | 关键考量 |
| --- | --- | --- |
| **银行/医院/大型国企** 强合规、需厂商兜底 | 商业版 OpenClaw (如 PowerClaw) 或私有化 Hermes | • 原生 Hermes：安全强但需自建维护 • 商业版 OpenClaw：RBAC + 审计日志 + 本地化 • CIO/CTO 首选商业版，技术团队可选原生 |
| **研发团队/AI 公司** 技术驱动、需护城河 | Hermes Agent | • Skill 自我进化构建产品护城河 • RL 训练管线持续优化 • 适合构建"越用越强"的 AI 原生应用 |
| **跨境电商/互联网运营** 多平台连接、快速部署 | OpenClaw | • 原生支持 20+ 平台（WhatsApp、Shopify、Slack、飞书） • 最好的"连接器"生态 • 标准化高并发任务更稳定 |
| **个人开发者/小团队** 预算有限、快速验证 | Hermes Agent | • $5 VPS 即可运行 • 开箱即用的安全（危险命令审批） • Serverless 后端（Daytona/Modal）成本极低 |

### ⚠️ 关键场景补充说明

**金融/医疗合规的特殊考量**

技术架构上 Hermes 更安全（七层安全模型、默认审批），但企业采购层面：

- **原生 Hermes**：适合有技术实力的团队自建，安全性极高但需维护 Linux/Docker 环境
- **商业版 OpenClaw（PowerClaw）**：国内厂商提供企业级 RBAC、审计日志、本地化部署，CIO/CTO 更省心

**重复性业务自动化的细分**

Hermes "自主性" vs OpenClaw "稳定性"：

- **复杂/非标准化任务**（写代码、报表分析）→ **Hermes**，Skill 自我进化持续提升效率
- **高并发/极度标准化任务**（10万+次/天发票录入）→ **OpenClaw**，线性工作流更稳定、更易审计，避免 Hermes "想太多"的波动

### 📊 核心能力速查表

| 能力维度 | Hermes Agent | OpenClaw |
| --- | --- | --- |
| **开箱即用安全** | ✅ 七层安全、默认审批 | ⚠️ 默认开放，需手动加固 |
| **多 Agent 协作** | ⚠️ Delegate 子代理 | ✅ 原生编排 |
| **平台连接能力** | ⚠️ 14+ 平台 | ✅ 20+ 平台 |
| **自我进化能力** | ✅ Skill 自动生成 | ❌ 静态 Skills |
| **部署成本** | ✅ $5 VPS 起 | ⚠️ 需更多资源 |

### 🏢 企业级应用场景

| 场景类型 | 推荐框架 | 理由 |
| --- | --- | --- |
| **金融/医疗合规** | Hermes ✅ | 默认开启危险命令审批、强化容器隔离、七层安全模型 |
| **多 Agent 协作平台** | OpenClaw ✅ | 原生多 Agent 编排、Gateway 统一调度 |
| **个人效率助手** | Hermes ✅ | 越用越懂你的习惯、自动学习工作流 |
| **重复性业务自动化** | Hermes ✅ | Skill 自我进化、执行效率持续提升 |
| **客服/运维机器人** | OpenClaw ✅ | 行为可控、响应可预测、团队协作 |
| **研究/创意工作** | Hermes ✅ | 跨会话记忆、个性化风格、知识积累 |

4

## 决策流程图：如何选择？

选型决策流程

Step 1

需要多 Agent 协作编排？

↓

✅ 是 → **OpenClaw**

✓ 推荐 OpenClaw

原生多 Agent 支持

❌ 否 → 继续 Step 2

↓

Step 2

对安全合规要求高？

金融/医疗/审计场景

↓

✅ 是 → **Hermes**

✓ 推荐 Hermes

原生安全、开箱即用

或考虑商业版 OpenClaw
（如 PowerClaw）

❌ 否 → 继续 Step 3

↓

Step 3

任务是否高度重复？

希望 Agent 自我学习优化

↓

✅ 是 → **Hermes**

✓ 推荐 Hermes

自进化、越用越聪明

❌ 否 → **OpenClaw**

✓ 推荐 OpenClaw

稳定可控、生态丰富

**核心逻辑：**多 Agent 或高合规 → OpenClaw | 重复任务需优化 → Hermes | 其他 → OpenClaw

5

## 未来展望：融合趋势

有趣的是，两个框架正在互相靠拢：

- **Hermes** 已经支持从 ClawHub 安装社区 Skills，并提供了 

  ```
  hermes claw migrate
  ```

  命令方便 OpenClaw 用户迁移
- **OpenClaw** 社区正在讨论引入「记忆学习」机制，虽然不会达到 Hermes 的自主程度

**我的预测：**2026 年底，我们会看到结合两者优势的新框架——既具备 Hermes 的自学习能力，又拥有 OpenClaw 的企业级管控。对于现在的选型，关键是理解自己的核心需求是「效率」还是「控制」。

附

## 技术实现规范说明

本文在排版和可视化方面的设计规范，供后续文章参考。

### 🎨 代码片段展示规范

**结构要求：**

- **容器化设计**：使用 

  ```
  .code-container
  ```

   包裹整个代码块，包含圆角阴影
- **头部标题栏**：显示语言图标、文件名、语言标签（如 Python/SQL）
- **语法高亮**：使用 CSS 类区分注释(绿色)、关键字(粉色)、字符串(黄色)、函数(蓝色)
- **pre + code 结构**：保持原始格式，避免自动换行导致的错乱
- **深色主题**：背景 #1a202c，文字 #e2e8f0，确保对比度

### 🌳 决策流程图设计规范

**结构要求：**

- **线性步骤**：Step 1 → Step 2 → Step 3，避免嵌套分支导致的视觉混乱
- **问题节点**：黄色背景(#fef3c7)，明确标注步骤序号
- **分支展示**：左右并排显示「是/否」两个路径，用箭头明确指向
- **结果节点**：OpenClaw 用绿色(#f0fdf4)，Hermes 用紫色(#f5f3ff)
- **提前终止**：如果某一步已得出结果，直接显示推荐，不再继续后续步骤
- **底部总结**：用一句话概括核心逻辑，方便读者快速记忆

### ✅ 数据准确性检查清单

**发布前必须验证：**

- GitHub Stars 数据（通过官网或 API 验证）
- 代码行数（通过 GitHub 文件详情页验证）
- 工具/技能数量（通过官方文档验证）
- 架构术语（使用官方文档中的标准术语，避免自创）
- 版本号（确认是最新稳定版本）

**参考来源：**

- Hermes Agent GitHub: github.com/NousResearch/hermes-agent
- Hermes Agent 官方文档: hermes-agent.nousresearch.com
- OpenClaw 官方文档: docs.openclaw.ai
- The New Stack: Persistent AI Agents Compared

— 本文由小鱼技术笔记原创出品，转载请注明出处 —
