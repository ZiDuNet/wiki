> 📎 来源: [飞哥的技术与烟火](https://mp.weixin.qq.com/s?__biz=MzAxNjU3NTY0MA==&mid=2454267765&idx=1&sn=e414be8d4879f9249133a40715bcdd27&chksm=8d0ed44fcb4cc001e85cf1d4258bfd98a6291e13f64fdb72498ef04b8a1f73d4d62bea3b77c9&mpshare=1&scene=1&srcid=0506S7pctFn72v5HRu3wiWgJ&sharer_shareinfo=c1c112da2712267c9217409d9f71ef7b&sharer_shareinfo_first=c1c112da2712267c9217409d9f71ef7b) | 时间: 2026-05-06 03:43

---

> 字数 2495，阅读大约需 13 分钟

👇关注我，后续继续分享更多的 AI Agent、技术开发相关的文章.

前段时间在 GitHub 上看到 

```
LLM wiki
```

 这个概念，其核心不过是让日积月累的记录"

```
活
```

"起来。趁着五一有空，我把之前

```
Hermes Agent、Obsidian、LLM wiki
```

的实践与思考整理了一下，就有了下面的这篇记录。

## 为什么需要这个组合？

传统的知识管理方式是「读→记→查」的线性链条，耗时长、易遗忘、难关联。

而 **Hermes Agent[1] + Obsidian[2] + LLM Wiki[3]** 这套组合，直接把知识流变成了「 ingest → synthesize → query → act 」的闭环系统：

- **Hermes Agent**：你的24小时在线的AI助理，能联网、能执行、能记忆、能跨平台工作
- **Obsidian**：双向链接的本地Markdown笔记软件，打造个人知识图谱
- **LLMWiki**：Karpathy推崇的wiki架构，让知识像维基百科一样结构化、可追溯、持续演进

这套组合的终极形态是：**Agent为你吸收信息、整理成体系化的wiki，你随时可以通过对话查询，所有知识沉淀在本地Markdown文件里，永远属于你。**

---

## 能用它做什么？

| 场景 | 输入 | 输出 |
| --- | --- | --- |
| **学习笔记** | 「读完这篇Transformer论文」 | 生成  ``` concepts/transformer.md ```  ，链接到  ``` entities/attention.md ```  、  ``` entities/google.md ``` |
| **项目管理** | 「项目A的5次会议记录」 | 生成  ``` entities/project-a.md ```  ，提取决策、责任人、时间线 |
| **研究追踪** | 「每月监控arxiv的cs.CL类别」 | 自动创建  ``` queries/monthly-cl-roundup-2026-05.md ``` |
| **个人CRM** | 「所有微信好友介绍、合影、聊天记录」 | 生成  ``` entities/person-x.md ```  ，标注关系、兴趣、最后一次联系时间 |
| **投资日志** | 「买入XX股票的决策过程」 | 生成  ``` entities/stock-xx.md ```  ，包含基本面、技术面、情绪面分析 |
| **内容创作** | 「我想写一篇关于Agent的文章」 | 先从wiki调取所有相关页面，生成大纲、素材、引用来源 |

---

## 核心组件解析

### Hermes Agent：不止是聊天机器人

Hermes是Nos Research开源的AI Agent框架，特点是：

**多模型支持** — OpenRouter、Anthropic、OpenAI、DeepSeek、本地模型等18+提供商，随你切换。

**跨平台网关** — 一套Agent同时在微信、飞书、QQ Bot、元宝、邮箱等多平台运行，工具全通路。

**自学习能力** — 通过「skills」机制，把复杂任务固化下来，越用越聪明。

**持久记忆** — 记住你的偏好、项目细节、过往决策，上下文不丢。

**子进程 spawned** — 长耗时的任务可以独立进程运行，不阻塞主对话。

### LLMWiki：知识的维基百科

基于Karpathy的wiki模式，核心是三层架构：

```
wiki/├── SCHEMA.md            # 领域定义、规范、标签体系├── index.md             # 内容目录（一句话摘要）├── log.md               # 操作日志（追加式记录）├── raw/                 # Layer 1：原始资料（不可修改）│   ├── articles/       # 网页文章│   ├── papers/         # 论文PDF│   └── transcripts/   # 访谈、会议记录├── entities/           # Layer 2：实体页（人、组织、产品）├── concepts/           # Layer 2：概念页（技术、理论、方法）├── comparisons/        # Layer 2：对比分析页└── queries/            # Layer 2：有价值的问题与答案
```

**关键设计**：

- Raw层是只读的，任何修改都要在wiki页面中「覆盖式更新」并标注来源
- 每个页面必须带YAML frontmatter（title、created、updated、type、tags、sources）
- 使用

  ```
  [[wikilinks]]
  ```

  双向链接，最少2个出站链接
- 索引和日志必须同步更新，否则wiki会退化

### Obsidian：让图谱动起来

Obsidian是本地Markdown笔记软件，天然适配wiki：

- ```
  [[wikilinks]]
  ```

  自动渲染为可点击链接
- Graph View可视化知识网络
- Dataview插件支持YAML frontmatter查询
- 本地存储，数据完全自主

**最佳实践**：把wiki目录直接设为Obsidian vault，改动实时同步。

---

## 从零搭建实操指南

### Step 1：初始化环境

```
# 1. 安装Hermes Agentcurl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash# 2. 配置环境变量（~/.hermes/.env）export WIKI_PATH="$HOME/wiki"                    # LLMWiki路径export OBSIDIAN_VAULT_PATH="$HOME/wiki"         # Obsidian vault路径export OPENROUTER_API_KEY="sk-xxx"              # 或ANTHROPIC_API_KEY等# 3. 运行配置向导hermes setup
```

### Step 2：创建你的LLMWiki

在Hermes对话中执行：

```
请帮我初始化一个LLMWiki，领域是「XXX」，路径使用$WIKI_PATH。
```

Hermes会自动创建：

- ```
  wiki/SCHEMA.md
  ```

  （根据你选择的领域定制标签体系）
- ```
  wiki/index.md
  ```

  （空目录结构）
- ```
  wiki/log.md
  ```

  （第一条创建日志）

**SCHEMA.md关键字段**：

```
## Tag Taxonomy- Models: model, architecture, benchmark, training- People/Orgs: person, company, lab, opensource- Techniques: optimization, finetuning, inference, alignment- Meta: comparison, timeline, controversy, prediction
```

### Step 3：第一次Ingest（信息摄入）

假设你想把一篇关于「Hermes Agent技能系统」的文章加入wiki：

```
我有一篇关于Hermes Agent技能的文章，URL是 https://hermes-agent.nousresearch.com/docs/reference/skills-catalog请帮我把它摄入到wiki的raw/articles/目录，并生成相应的wiki页面。
```

Hermes的执行流程：

1. 1. **抓取原文** → 用

   ```
   web_extract
   ```

   转为Markdown，保存至

   ```
   raw/articles/hermes-agent-skills-2026.md
   ```
2. 2. **分析内容** → 识别出关键实体（Hermes Agent、Skill、Toolset、MCP）和概念（自学习、多平台网关）
3. 3. **查重** → 在

   ```
   index.md
   ```

   和现有文件中搜索，避免重复页面
4. 4. **生成页面**：

- ```
  entities/hermes-agent.md
  ```

  （实体页）
- ```
  concepts/skill-system.md
  ```

  （概念页）
- ```
  concepts/toolset-architecture.md
  ```

  （概念页）

5. 5. **建立链接** → 每个新页面至少2个

   ```
   [[wikilinks]]
   ```
6. 6. **更新索引** → 在

   ```
   index.md
   ```

   的Entities和Concepts区块添加条目
7. 7. **记录日志** → 在

   ```
   log.md
   ```

   追加

   ```
   ## [YYYY-MM-DD] ingest | Hermes Agent技能系统
   ```

### Step 4：查询与检索

```
我们wiki里有哪些关于「多平台网关」的内容？
```

Hermes会：

1. 1. 读取

   ```
   index.md
   ```

   找到相关页面
2. 2. 读取这些页面的完整内容
3. 3. 综合所有信息，用自然语言回答你
4. 4. 如果答案足够重要，自动创建

   ```
   queries/multi-platform-gateway.md
   ```

   存下来

### Step 5：定期Lint（健康检查）

```
运行 wiki lint，检查是否有孤立页面、断链、过时内容。
```

Hermes会扫描整个wiki，输出报告：

```
问题分级：🔴 严重（2个）：  - entities/obsolete-api.md: 断链 [[old-endpoint]] → 目标不存在  - concepts/llm-agents.md: 孤立页面（无入链）🟡 警告（5个）：  - concepts/mcp-protocol.md: 超过200行，建议拆分  - entities/hermes-agent.md: updated=2025-01-01，已有3个新source引用它✅ 通过：索引完整性100%，标签体系合规，log无需轮转
```

---

## 典型应用场景

### 场景1：技术雷达追踪

**需求**：持续追踪AI Agent领域的新工具、新框架

**实现**：

1. 1. 在Hermes中创建定时任务（

   ```
   cronjob
   ```

   ），每天抓取GitHub Trending、Hacker News的AI Agent板块
2. 2. 自动摄入到

   ```
   raw/articles/
   ```

   ，更新

   ```
   entities/ai-agent-tools.md
   ```
3. 3. 通过Obsidian的Graph View观察工具生态的演化脉络

```
hermes cron create "0 9 * * *" --prompt \"抓取今日Hacker News上关于'AI agent'的讨论，摄入到wiki，更新技术雷达。"
```

### 场景2：项目知识沉淀

**需求**：团队新成员快速上手项目

**实现**：

1. 1. 将所有设计文档、会议记录、PR讨论摄入raw/
2. 2. Hermes自动生成：

- ```
  entities/project-x.md
  ```

  （核心组件）
- ```
  concepts/architecture-decisions.md
  ```

  （架构决策）
- ```
  comparisons/storage-options.md
  ```

  （存储选型对比）

3. 3. 新成员提问：「我们为什么选PostgreSQL而不是MongoDB？」→ Hermes直接从wiki找出答案

### 场景3：个人第二大脑

**需求**：读书笔记、学习记录、灵感碎片形成网络

**实现**：

1. 1. 阅读时高亮 → 用Readwise导出 → 投入raw/papers/
2. 2. Hermes定期批量处理：

- 识别关键概念 → 创建/更新concept页面
- 关联已有实体 → 补全[[links]]
- 标记置信度 → 如果是个人观点设为

  ```
  confidence: medium
  ```

3. 3. 复习时提问：「关于注意力机制，我学过哪些？」→ 自动关联多篇笔记

### 场景4：自动化文档

**需求**：API变更时自动更新相关文档

**实现**：

1. 1. 订阅API changelog RSS（用

   ```
   webhook
   ```

   或

   ```
   cron
   ```

   ）
2. 2. 新版本发布 → Hermes抓取说明文档 → 摄入raw/
3. 3. 与现有

   ```
   entities/api-v2.md
   ```

   对比 → 生成

   ```
   comparisons/api-v2-vs-v3.md
   ```
4. 4. 通知你：「有3处破坏性变更，已更新文档，查看[[breaking-changes]]」

---

## 进阶技巧

### Obsidian插件推荐

| 插件 | 用途 |
| --- | --- |
| Dataview | 用JS查询frontmatter，自动生成表格 |
| Obsidian Git | 自动提交wiki变更到Git |
| Kanban | 将log.md的任务转为看板 |
| Calendar | 按日期浏览笔记 |
| Advanced Tables | 便捷编辑对比表格 |

**Dataview示例查询**：

```
TABLE tags, file.day FROM "entities" WHERE contains(tags, "company") SORT file.day DESC
```

### 向量化加速查询

当wiki超过1000页时，全文搜索变慢。安装

```
wiki-vectorization
```

技能：

```
hermes skills install wiki-vectorizationhermes setup memory          # 配置持久化记忆（向量后端）
```

此后，Hermes会：

1. 1. 自动embedding新wiki页面到向量库
2. 2. 查询时先向量检索Top-K页面，再让LLM综合
3. 3. 响应时间从10秒降至2秒

### 多Agent协同

用

```
delegate_task
```

让不同Agent负责wiki的不同部分：

```
# Agent A：负责技术概念 ingestiondelegate_task(goal="将今天arxiv上关于MoE的5篇论文摄入到concept/mixture-of-experts.md")# Agent B：负责实体关系图谱delegate_task(goal="扫描entities/目录，生成一张companies.md的对比表，列出所有AI公司的成立时间、核心产品、开源项目")
```

### Git版本控制

把整个wiki目录初始化成Git仓库：

```
cd ~/wikigit initgit add .git commit -m "Initial wiki commit"# 每次重大更新后提交git commit -am "Update: Add Hermes Agent skills comparison"git tag -a "v2026-05-02" -m "Pre-conference knowledge base"
```

**优势**：

- 可以

  ```
  git diff
  ```

  查看页面变更历史
- 用

  ```
  git blame
  ```

  追溯某句话的来源
- 方便回滚到任一时间点的wiki状态

### 同步到Obsidian Cloud

本地wiki → Obsidian Sync → 手机/平板随时查阅：

1. 1. 在Obsidian客户端开启Sync（付费功能）
2. 2. 将

   ```
   $WIKI_PATH
   ```

   添加到同步 vault 列表
3. 3. 所有设备实时更新
4. 4. 断网时依然可编辑，联网后自动同步

**免费方案**：用

```
git
```

 + 

```
cron
```

定时push到GitHub，手机用Working Copy查看。

---

## 结语

```
Hermes Agent + Obsidian + LLMWiki
```

，本质上是在构建一个**反RAG的系统**：

- RAG每次查询都重新检索、重新生成，知识没有沉淀
- 而这个组合是**一次摄入，永久受益**——知识越积累越值钱，结构越来越清晰，查询越来越准。

更重要的是，**这些文件都在你本地**。不管模型怎么换代、公司怎么倒闭、服务怎么下架，你的知识库永远在。

**你的知识库，从此有了生命。**

👇关注我，后续继续分享更多的 AI Agent、技术开发相关的文章.

---

#### 引用链接

```
[1]
```

 Hermes Agent: *https://hermes-agent.nousresearch.com/docs/*

```
[2]
```

 Obsidian: *https://obsidian.md/*

```
[3]
```

 LLM Wiki: *https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f*
