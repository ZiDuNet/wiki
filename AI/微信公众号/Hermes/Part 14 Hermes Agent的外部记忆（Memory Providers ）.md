> 📎 来源: [跨境AI入门指南](https://mp.weixin.qq.com/s/3Hu9iC2h3qhzcxDkLD-ODg) | 时间: 2026-05-05 23:25

---

https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers

### **这一页讲的是：Hermes 内置了 8 个外部记忆提供者插件，在基础 MEMORY.md/USER.md 之上提供知识图谱、语义搜索、自动事实提取等深层记忆能力，且一次只能激活一个外部 provider，与内置 memory 并行运行**

从 Persistent Memory 进入 Memory Providers，学习的焦点从"内置的轻量级记忆系统"转向了"可插拔的外部记忆后端"。这一页的核心是：当内置 memory 的 2,200 + 1,375 字符限制不够用时，Hermes 提供了 8 种不同设计哲学的外部记忆方案来扩展。

---

### **一、这一页的定位：内置 memory 的扩展层，不是替代层**

文档开篇就明确了一个关键设计原则：

### **外部 provider 与内置 memory 并行运行，永不取代内置 memory**

内置的 MEMORY.md 和 USER.md 始终正常工作。外部 provider 是附加的（additive）。这意味着：

- 内置 memory 仍然在 session 启动时注入 system prompt
- 外部 provider 在此基础上额外注入上下文、提供搜索工具
- 两者共存，各有分工

文档还强调：**一次只能激活一个外部 provider**。你不能同时启用 Honcho 和 Hindsight。

---

### **二、外部 provider 的通用工作机制**

当一个外部 memory provider 激活时，Hermes 自动执行 6 件事：

1. **注入 provider 上下文**

   到 system prompt（provider 知道的信息）
2. **预取相关记忆**

   到每次 turn 之前（后台非阻塞）
3. **同步对话轮次**

   到 provider（每次响应后）
4. **在 session 结束时提取记忆**

   （对支持此功能的 provider）
5. **镜像内置 memory 的写入**

   到外部 provider
6. **添加 provider 专属工具**

   ，让 agent 可以搜索、存储和管理记忆

这 6 步构成了一个完整的"读写同步"循环。内置 memory 的写入会自动镜像到外部 provider，所以用户不需要同时管理两套记忆。

---

### **三、8 个 provider 的总体概览**

文档按字母顺序列出了 8 个 provider，每个都有不同的设计哲学和适用场景。先看整体对比：

| Provider | 存储 | 成本 | 工具数 | 独特能力 |
| --- | --- | --- | --- | --- |
| Honcho | 云端 | 付费 | 5 | 辩证用户建模 + 会话范围上下文 |
| OpenViking | 自托管 | 免费 | 5 | 文件系统层级 + 分层加载 |
| Mem0 | 云端 | 付费 | 3 | 服务端 LLM 自动提取 |
| Hindsight | 云端/本地 | 免费/付费 | 3 | 知识图谱 + 跨记忆综合 |
| Holographic | 本地 | 免费 | 2 | HRR 代数 + 信任评分 |
| RetainDB | 云端 | $20/月 | 5 | 增量压缩 |
| ByteRover | 本地/云端 | 免费/付费 | 3 | 预压缩提取 |
| Supermemory | 云端 | 付费 | 4 | 上下文隔离 + 会话图摄取 + 多容器 |

---

### **四、Honcho：最复杂的 provider，辩证用户建模**

Honcho 是文档中篇幅最长的 provider，也是功能最复杂的。它的核心概念是**辩证推理（dialectic reasoning）**——通过多轮 LLM 对话来构建用户模型。

#### **核心架构：两层上下文注入**

Honcho 的上下文注入分为两层：

- **基础层（base layer）**

  ：包含 session summary + user representation + peer card，按 `contextCadence` 刷新
- **辩证补充层（dialectic supplement）**

  ：LLM 推理结果，按 `dialecticCadence` 刷新

基础层存在时使用"warm prompt"（会话范围上下文），不存在时使用"cold-start prompt"（通用用户事实）。

#### **三个正交配置旋钮**

文档特别强调这三个参数独立控制成本和深度：

- `contextCadence`

  ：基础层刷新频率（API 调用频率）
- `dialecticCadence`

  ：辩证 LLM 触发频率（LLM 调用频率）
- `dialecticDepth`

  ：每次辩证调用的 `.chat()` 轮数（1-3，推理深度）

`dialecticDepth` 的 3 轮有明确分工：

- 第 0 轮：cold/warm prompt
- 第 1 轮：self-audit（自我审计）
- 第 2 轮：reconciliation（调和）

#### **多 peer 架构**

Honcho 将对话建模为 peer 之间的消息交换：

- **Workspace**

  ：共享环境，所有 profile 共享同一个用户身份
- **User peer**

  （`peerName`）：人类用户，跨 profile 共享
- **AI peer**

  （`aiPeer`）：每个 Hermes profile 一个，独立构建用户模型

这意味着同一个用户在不同 profile（如 coder vs writer）下，Honcho 会构建不同的用户表征。coder profile 保持代码导向，writer profile 保持编辑导向，即使面对同一个用户。

#### **观察模式（Observation）**

Honcho 支持细粒度的观察控制，每个 peer 有 4 个 toggle：

- `observeMe`

  ：Honcho 是否从此 peer 自己的消息中构建表征
- `observeOthers`

  ：此 peer 是否观察另一 peer 的消息

预设模式：

- `directional`

  （默认）：全部开启，完整双向观察
- `unified`

  ：只有 user 观察自己 + AI 观察 user，形成单观察者池

#### **配置层级**

Honcho 的配置解析顺序是：
`$HERMES_HOME/honcho.json` > `~/.hermes/honcho.json` > `~/.honcho/config.json`

支持多 profile 配置，每个 host block 可以独立覆盖 observation、recallMode、writeFrequency 等设置。

#### **迁移说明**

如果之前用过 `hermes honcho setup`，配置和数据都保留，只需通过 `hermes memory setup` 重新启用或手动设置 `memory.provider: honcho`。

---

### **五、OpenViking：文件系统风格的知识层级**

OpenViking 是字节跳动（Volcengine）的上下文数据库，设计哲学是**结构化浏览**。

#### **核心能力**

- **分层上下文加载**

  ：L0（~100 tokens）→ L1（~2k）→ L2（完整）
- **自动记忆提取**

  ：session 提交时自动提取 6 类信息——profile、preferences、entities、events、cases、patterns
- **`viking://` URI 方案**

  ：支持层级化知识浏览

#### **工具集**

5 个工具：`viking_search`（语义搜索）、`viking_read`（分层阅读）、`viking_browse`（文件系统导航）、`viking_remember`（存储事实）、`viking_add_resource`（摄入 URL/文档）

#### **部署要求**

需要先启动 OpenViking 服务器：

```
pip install openvikingopenviking-server
```

然后配置 Hermes 连接。

---

### **六、Mem0：最省心的自动提取方案**

Mem0 的设计哲学是**免手动管理**——服务端自动完成事实提取。

#### **核心能力**

- 服务端 LLM 自动提取事实
- 语义搜索 + 重排序（reranking）
- 自动去重

#### **工具集**

3 个工具：`mem0_profile`（所有存储的记忆）、`mem0_search`（语义搜索 + 重排序）、`mem0_conclude`（存储逐字事实）

#### **配置**

只需要 API key 和两个标识符：

```
{"user_id":"hermes-user","agent_id":"hermes"}
```

Mem0 是"开箱即用"风格的代表——配置最少，自动程度最高。

---

### **七、Hindsight：知识图谱 + 跨记忆综合**

Hindsight 是唯一提供**跨记忆综合（cross-memory synthesis）**的 provider。

#### **核心能力**

- 知识图谱 + 实体解析
- 多策略检索
- `hindsight_reflect`

  工具：跨记忆综合，其他 provider 没有
- 自动保留完整对话轮次（包括工具调用）
- 会话级文档追踪

#### **部署模式**

支持 cloud 和 local 两种模式：

- Cloud：需要 API key（`hindsight-client`）
- Local：需要 LLM API key（OpenAI、Groq、OpenRouter 等），使用本地嵌入式 PostgreSQL

#### **工具集**

3 个工具：`hindsight_retain`（存储 + 实体提取）、`hindsight_recall`（多策略搜索）、`hindsight_reflect`（跨记忆综合）

#### **配置关键项**

- `recall_budget`

  ：检索彻底度（low/mid/high）
- `memory_mode`

  ：hybrid（上下文+工具）/ context（仅注入）/ tools（仅工具）
- `auto_retain`

  / `auto_recall`：是否自动保留和召回

#### **本地模式 UI**

```
hindsight-embed -p hermes ui start
```

可以启动本地管理界面。

---

### **八、Holographic：零依赖的本地记忆方案**

Holographic 是唯一**不需要任何外部依赖**的 provider——它只依赖 SQLite。

#### **核心能力**

- FTS5 全文搜索
- **信任评分（trust scoring）**

  ：agent 可以对事实标记 helpful/unhelpful，系统据此调整信任度
- **HRR（Holographic Reduced Representations）**

  ：支持组合代数查询

#### **独特工具**

`fact_store` 工具包含 9 个操作：add、search、probe、related、reason、contradict、update、remove、list

其中三个操作是 Holographic 独有的高级能力：

- **probe**

  ：实体特定代数召回——查询关于某个人/物的所有事实
- **reason**

  ：组合 AND 查询——跨多个实体的联合查询
- **contradict**

  ：自动检测矛盾事实

#### **信任评分机制**

- 默认信任分：0.5
- helpful 标记：+0.05
- unhelpful 标记：-0.10

不对称的权重设计（惩罚比奖励重）意味着错误事实的代价更高。

#### **配置**

```
plugins:hermes-memory-store:db_path: $HERMES_HOME/memory_store.dbauto_extract:falsedefault_trust:0.5
```

Holographic 是"本地优先、零依赖、高级检索"的代表。

---

### **九、RetainDB：混合搜索 + 增量压缩**

RetainDB 是付费云服务，$20/月。

#### **核心能力**

- 混合搜索：Vector + BM25 + Reranking
- 7 种记忆类型
- 增量压缩（delta compression）

#### **工具集**

5 个工具：`retaindb_profile`（用户档案）、`retaindb_search`（语义搜索）、`retaindb_context`（任务相关上下文）、`retaindb_remember`（存储 + 类型 + 重要性）、`retaindb_forget`（删除记忆）

---

### **十、ByteRover：CLI 驱动的层级知识树**

ByteRover 的设计哲学是**本地优先、CLI 驱动、可移植**。

#### **核心能力**

- 层级知识树（hierarchical knowledge tree）
- 分层检索：模糊文本 → LLM 驱动搜索
- **预压缩提取**

  ：在上下文压缩丢弃信息之前，先提取关键洞察
- 可选云端同步（SOC2 Type II 认证）

#### **工具集**

3 个工具：`brv_query`（搜索知识树）、`brv_curate`（存储事实/决策/模式）、`brv_status`（CLI 版本 + 树统计）

#### **部署**

需要先安装 ByteRover CLI：

```
curl-fsSL https://byterover.dev/install.sh |sh
```

知识树存储在 `$HERMES_HOME/byterover/`，按 profile 隔离。

---

### **十一、Supermemory：语义记忆 + 上下文隔离 + 多容器**

Supermemory 是功能最丰富的云端 provider 之一。

#### **核心能力**

- 语义相似度搜索
- 用户档案 + 近期上下文
- **上下文隔离（context fencing）**

  ：从捕获的对话轮次中剥离已召回的回忆，防止递归记忆污染
- **会话图摄取**

  ：session 结束时将对话摄入知识图谱
- **多容器模式**

  ：agent 可以跨多个命名容器读写

#### **工具集**

4 个工具：`supermemory_store`（保存显式记忆）、`supermemory_search`（语义搜索）、`supermemory_forget`（按 ID 或最佳匹配删除）、`supermemory_profile`（持久档案 + 近期上下文）

#### **配置关键项**

- `auto_recall`

  ：turn 前自动注入相关记忆
- `auto_capture`

  ：每次响应后存储清理后的对话轮次
- `profile_frequency`

  ：每 N 轮注入一次档案事实
- `capture_mode`

  ：默认跳过微小/琐碎的对话轮次（如"ok"、"thanks"）
- `search_mode`

  ：hybrid / memories / documents

#### **多容器模式**

这是 Supermemory 的独特能力。启用 `enable_custom_container_tags` 后，agent 可以跨多个命名容器读写：

```
{"container_tag":"hermes","enable_custom_container_tags":true,"custom_containers":["project-alpha","shared-knowledge"],"custom_container_instructions":"Use project-alpha for coding context."}
```

自动操作（同步、预取）保持在主容器上，agent 通过工具参数选择其他容器。

#### **Profile 隔离**

使用 `{identity}` 模板可以实现 profile 级别的容器隔离：

```
"container_tag":"hermes-{identity}"
```

→ coder profile 使用 `hermes-coder`，writer profile 使用 `hermes-writer`

---

### **十二、Profile 隔离机制**

文档专门有一节讲 profile isolation，因为每个 provider 的数据隔离方式不同：

- **本地存储 provider**

  （Holographic、ByteRover）：使用 `$HERMES_HOME/` 路径，不同 profile 路径不同
- **配置文件 provider**

  （Honcho、Mem0、Hindsight、Supermemory）：配置存储在 `$HERMES_HOME/`，每个 profile 有自己的凭据
- **云端 provider**

  （RetainDB）：自动派生 profile 范围的项目名
- **环境变量 provider**

  （OpenViking）：通过每个 profile 的 `.env` 文件配置

这意味着即使多个 profile 使用同一个 provider，数据也是隔离的。

---

### **十三、8 个 provider 的选择逻辑**

从文档的对比表和各自描述来看，选择逻辑大致如下：

- **需要最复杂的用户建模**

  → Honcho（辩证推理、多 peer 架构）
- **需要结构化知识浏览**

  → OpenViking（文件系统层级、分层加载）
- **想要最省心的自动管理**

  → Mem0（服务端自动提取，配置最少）
- **需要知识图谱和跨记忆综合**

  → Hindsight（唯一有 reflect 工具）
- **零外部依赖、本地优先**

  → Holographic（SQLite + HRR 代数）
- **已经在用 RetainDB 基础设施**

  → RetainDB（混合搜索 + 增量压缩）
- **想要 CLI 驱动的便携记忆**

  → ByteRover（知识树 + 预压缩提取）
- **需要多容器隔离和上下文防护**

  → Supermemory（上下文隔离 + 多容器）

---

### **14句一句话总结**

1. Memory Providers 是 Hermes 内置 memory 的外部扩展层，一次只能激活一个，与内置 memory 并行运行。
2. 激活后自动执行 6 步：注入上下文、预取记忆、同步对话、提取记忆、镜像写入、添加工具。
3. Honcho 是最复杂的 provider，使用辩证推理和两层上下文注入来构建跨会话用户模型。
4. Honcho 的 peer 架构中，workspace 共享用户身份，每个 Hermes profile 有独立的 AI peer。
5. Honcho 提供三个正交配置旋钮（contextCadence、dialecticCadence、dialecticDepth）独立控制成本和深度。
6. OpenViking 是字节跳动的上下文数据库，使用文件系统风格的知识层级和 L0→L1→L2 分层加载。
7. Mem0 是配置最少的 provider，服务端自动完成 LLM 事实提取、语义搜索和去重。
8. Hindsight 是唯一提供跨记忆综合（hindsight\_reflect）的 provider，支持知识图谱和本地/云端双模式。
9. Holographic 是唯一零外部依赖的 provider，使用 SQLite + HRR 代数 + 信任评分，支持矛盾检测。
10. RetainDB 是付费云服务（$20/月），提供 Vector + BM25 + Reranking 混合搜索和增量压缩。
11. ByteRover 是 CLI 驱动的层级知识树，支持预压缩提取和可选 SOC2 云端同步。
12. Supermemory 提供上下文隔离（防止递归污染）、会话图摄取和多容器跨命名空间读写。
13. 所有 provider 都支持 profile 隔离，通过路径、配置文件、项目名或环境变量实现。
14. 选择哪个 provider 取决于需求：用户建模选 Honcho，零依赖选 Holographic，自动管理选 Mem0，知识图谱选 Hindsight。
