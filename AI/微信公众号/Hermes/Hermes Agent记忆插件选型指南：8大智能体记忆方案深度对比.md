> 📎 来源: [架构师之道](https://mp.weixin.qq.com/s?__biz=MzAxNjk4MzQxNw==&mid=2247490081&idx=1&sn=b9e64b525e5796f5de63871990379602&chksm=9a8ef47a9e4c3d7e9a677fae489c5a2c398fb3b6376569ff5ffb5d464ec75cacb13619837008&mpshare=1&scene=1&srcid=0513GNyfpQJYRvCj5dsDrgVb&sharer_shareinfo=e77d89567e8999c0ac63a1aa103a2062&sharer_shareinfo_first=e77d89567e8999c0ac63a1aa103a2062) | 时间: 2026-05-13 01:54

---

## 1 引言

现代AI助手在对话关闭后便“遗忘”一切，除非用某种机制将信息持久化在上下文窗口之外。**AI智能体记忆提供商**（Agent Memory Providers）正是为此而生——它们作为插件接入智能体框架，实现跨会话的事实与摘要存储，同时保持核心轻量化。

![](assets/img_9e0ad5d25710.jpg)

本指南对比了 **Hermes Agent** 支持的八种外部记忆后端：**Honcho、OpenViking、Mem0、Hindsight、Holographic、RetainDB、ByteRover、Supermemory**。这些提供商也通过社区或官方集成出现在 **OpenClaw** 及其他智能体工具链中。

> ℹ️ Hermes 内置的 MEMORY.md / USER.md 机制与外部提供商**并行运行**，二者是叠加而非替代。同一时间仅能激活一个外部提供商。

## 2 外部依赖的本质：隐私、成本与自托管可行性

**除 Holographic 外**，每个提供商至少需要一次外部服务调用——用于记忆提取的 LLM、用于语义搜索的嵌入模型，或用于存储的数据库（如 PostgreSQL）。这些依赖直接影响：

- **隐私：**

  数据是否离开你的基础设施
- **成本：**

  API 调用费用 + 基础设施维护
- **自托管完整度：**

  能否完全脱离第三方服务运行

若提供商支持 **Ollama 或任何 OpenAI 兼容端点**，可将 LLM 与嵌入调用路由至本地模型，实现完全数据主权。

## 3 在 Hermes Agent 中激活外部记忆

```
hermes memory setup   # 交互式选择器 + 配置向导hermes memory status  # 检查当前激活状态hermes memory off     # 禁用外部提供商
```

或手动编辑 `~/.hermes/config.yaml`：

```
memory:  provider: openviking  # 可选：honcho, mem0, hindsight, holographic, retaindb, byterover, supermemory
```

## 4 提供商核心指标对比

| 提供商 | 存储形态 | 成本模型 | 最小外部依赖 | 完全自托管？ | 独特技术特征 |
| --- | --- | --- | --- | --- | --- |
| **Honcho** | 云 / 自托管 | 付费+免费套餐 | LLM + 嵌入模型 + PostgreSQL/pgvector + Redis | ✅ (Docker/K3s/Fly.io) | 辩证用户建模 + 会话作用域上下文 |
| **OpenViking** | 自托管 | 免费 | VLM + 嵌入模型 | ✅ (本地服务器，Ollama 原生向导) | 文件系统层级 + 分层加载 |
| **Mem0** | 云 / 自托管 | 付费+开源免费 | LLM + 嵌入模型 + 向量库(Qdrant/pgvector) | ✅ (Docker Compose) | 服务端 LLM 自动提取记忆 |
| **Hindsight** | 云 / 本地 | 免费+付费 | LLM + 捆绑 PostgreSQL + 内置嵌入器/重排序器 | ✅ (Docker 或嵌入式 Python) | 知识图谱 + `reflect` 跨记忆综合推理 |
| **Holographic** | 本地 | 免费 | **无** | ✅ (原生，零基础设施) | HRR 代数编码 + 信任评分 |
| **RetainDB** | 云端 | $20/月 | 云端全托管（LLM+检索均在服务端） | ❌ | 增量压缩存储 |
| **ByteRover** | 本地/云 | 免费+付费 | **仅需 LLM** （无需嵌入，无需数据库） | ✅ (默认本地优先) | 基于文件的上下文树 + 全文搜索 |
| **Supermemory** | 云端 | 付费 | LLM + PostgreSQL/pgvector（企业版部署于 Cloudflare） | ⚠️ 仅限企业计划 | 上下文隔离 + 会话图谱导入 |

## 5 各提供商深度解析

### 🔷 Honcho —— 多智能体系统的会话建模

**定位：** 多智能体协作、跨会话上下文、用户-智能体对齐。

Honcho 将对话抽象为“对等方”（peers）之间的消息交换。每个 Hermes 配置文件包含一个用户对等方和一个 AI 对等方，共享同一工作区（workspace）。它构建**双层上下文：**

- **基础层：**

  会话摘要 + 用户表征 + 对等方卡片
- **辩证补充层：**

  LLM 驱动的推理（`dialectic` 机制）

**外部依赖详解：**

- LLM：用于摘要、用户表征推导、辩证推理（支持 OpenAI 兼容端点 → 可接入 Ollama）
- 嵌入模型：用于语义搜索（默认 `openai/text-embedding-3-small`，可通过 `LLM_EMBEDDING_BASE_URL` 替换为本地 vLLM+BGE）
- 存储：PostgreSQL + pgvector + Redis

**关键配置参数：**

```
contextCadence:1      # 基础层刷新所需的最小对话轮次（默认1）dialecticCadence:2    # 辩证推理调用的最小轮次间隔（推荐1-5）dialecticDepth:1      # 每次`.chat()`的传递次数，限制1-3recallMode:hybrid     # hybrid(自动+工具) / context(仅注入) / tools(仅工具)writeFrequency:async  # async / turn / session / N
```

**工具集：** `honcho_profile`, `honcho_search`, `honcho_context`, `honcho_reasoning`, `honcho_conclude`

### 🔷 OpenViking —— 文件系统即记忆

**定位：** 完全自托管的知识管理，结构化浏览。

OpenViking 将记忆存储在**本地文件系统层级**中，采用分层加载策略。无需数据库，所有数据以人类可读形式保存。

**外部依赖：**

- VLM（视觉-语言模型）：语义处理与记忆提取（支持 OpenAI/Anthropic/DeepSeek/vLLM 等）
- 嵌入模型：向量搜索（支持 OpenAI/Jina/Voyage/Ollama）
- `openviking-server init`

  向导可自动检测硬件并推荐 Ollama 模型（如 Qwen3-Embedding 8B + Gemma 4 27B），实现零 API 密钥完全本地化。

**安装配置：**

```
pip install openvikingopenviking-server init   # 交互式向导，自动配置Ollama本地模型openviking-serverhermes memory setup      # 选择 "openviking"echo"OPENVIKING_ENDPOINT=http://localhost:1933" >> ~/.hermes/.env
```

### 🔷 Mem0 —— 零配置的自动记忆管理

**定位：** 开箱即用的自动化记忆提取与去重。

每次 `add` 操作触发 LLM 调用，读取对话内容，提取离散事实，去重后存储。托管云 API 处理一切基础设施；开源版允许完全自托管。

**外部依赖：**

- LLM：记忆提取（默认 `gpt-4.1-nano`，支持 Ollama/vLLM/LM Studio 等 20+ 提供商）
- 嵌入模型：检索（默认 `text-embedding-3-small`，支持 Ollama/HuggingFace 等 10+ 提供商）
- 存储：库模式使用本地 Qdrant (`/tmp/qdrant`)，服务器模式使用 PostgreSQL+pgvector

**完全本地化配置示例：**

```
from mem0 import Memoryconfig = {  "llm": {"provider": "ollama", "model": "llama3.1"},  "embedder": {"provider": "ollama", "model": "nomic-embed-text"},  "vector_store": {"provider": "qdrant", "path": "./qdrant_data"}}mem = Memory.from_config(config)
```

### 🔷 Hindsight —— 知识图谱 + 跨记忆综合推理

**定位：** 实体关系建模，高阶洞察生成。

Hindsight 构建**知识图谱**（实体-关系-记忆），检索时并行运行四种策略：

- 语义搜索（向量）
- 关键词/BM25
- 图谱遍历（相关实体）
- 时序召回

然后使用 **倒数排名融合（RRF, Reciprocal Rank Fusion）** 合并结果，并可选交叉编码器重排序。

**独特工具 `reflect`：** 对多条记忆进行综合推理，生成新洞察（例如：“记忆A和B结合暗示用户更喜欢异步沟通”）。

**外部依赖：**

- LLM：事实/实体提取 + `reflect` 综合推理（支持 Ollama 等，但 `reflect` 需要支持工具调用的模型，如 `qwen3:8b`）
- 嵌入模型与重排序器：**已捆绑**（`hindsight-all` 包内置本地模型）
- PostgreSQL：也捆绑于嵌入式 Python 中，无需外部安装

**完全本地化配置：**

```
hermes memory setup  # 选择 hindsight，模式选 local# 设置环境变量指向本地 Ollamaexport HINDSIGHT_API_LLM_PROVIDER=ollamaexport HINDSIGHT_OLLAMA_BASE_URL=http://localhost:11434
```

### 🔷 Holographic —— 零依赖的纯本地记忆

**定位：** 极端隐私保护，无需任何基础设施。

使用 **HRR（全息降维表示，Holographic Reduced Representations）** 代数对记忆进行编码。HRR 是一种将符号结构表示为高维向量的方法，支持可逆的捆绑（binding）与解绑（unbinding）操作，无需神经网络或嵌入模型。

**核心原理：**

- 每个记忆项编码为一个向量，通过循环卷积（circular convolution）绑定到上下文标签
- 检索时通过相似性（向量点积）召回
- 信任评分：基于记忆的访问频率与 recency 进行指数衰减加权

**零依赖：** 无 LLM、无嵌入、无数据库、无网络。代价是检索质量低于基于语义嵌入的方案，且不支持抽象推理。

**适用场景：** 隐私敏感、离线环境、极简部署（如边缘设备）。

### 🔷 RetainDB —— 增量压缩的云端服务

**定位：** 高频更新场景下的记忆压缩存储。

RetainDB 采用**增量压缩**技术：每次更新时仅存储变更（delta），而非重写整个记忆。检索时混合使用向量 + BM25 + 重排序。

**外部依赖：** 完全托管于 RetainDB 云端（月费 $20）。服务端使用 Claude Sonnet 进行记忆提取。**无自托管选项**，数据必须发送至第三方服务器。

### 🔷 ByteRover —— 人类可读的上下文树

**定位：** 本地优先，审计友好的记忆存储。

ByteRover 将记忆存储为 **Markdown 层级树：** 领域（domain）→ 主题（topic）→ 子主题 → 文件。所有知识以纯文本形式保留，完全可读可编辑。

**技术特点：**

- 无需嵌入模型：检索使用 **MiniSearch** 全文搜索（轻量级倒排索引）
- 无需向量数据库：上下文树即存储
- LLM 仅用于记忆策展（将新内容归类到树的合适位置）及搜索回退

**外部依赖：** 仅需 LLM（18+ 提供商，包括 Ollama）。可选云同步用于团队协作。

**完全本地化示例：**

```
brv providers connect openai-compatible --base-url http://localhost:11434/v1hermes memory setup  # 选择 byterover
```

### 🔷 Supermemory —— 企业级上下文隔离

**定位：** 大型企业的记忆治理。

Supermemory 提供**上下文隔离**（按不同的 context 隔离记忆，避免交叉污染）和**会话图谱导入**（批量导入历史对话）。混合检索（语义+关键词）加用户画像自动构建。

**自托管限制：** 仅作为企业计划附加项，部署于 **Cloudflare Workers**，需要提供 PostgreSQL+pgvector 以及 OpenAI API 密钥（强制）。无 Docker/裸机自托管路径。

## 6 选型决策树

```
你的首要需求是？│├─ 完全自托管 + 无需任何外部服务？│   └─ Holographic（零依赖，但检索质量一般）或 ByteRover（仅需本地 LLM）│├─ 需要知识图谱 + 高阶推理？│   └─ Hindsight（支持 reflect 综合推理）│├─ 需要多智能体协作 + 跨会话用户建模？│   └─ Honcho（辩证建模 + 对等方抽象）│├─ 需要最低配置门槛，自动管理记忆？│   └─ Mem0（自动提取去重）│├─ 希望存储为人类可读文件，便于审计？│   └─ ByteRover（Markdown 树 + 全文检索）│├─ 企业级上下文隔离且接受 Cloudflare 绑定？│   └─ Supermemory│└─ 高频更新 + 接受全托管付费？    └─ RetainDB
```

## 7 技术深度补充：两种值得关注的底层机制

### 1. HRR 代数（Holographic）

HRR 通过向量循环卷积实现符号绑定。给定两个向量 **a** 和 **b**，其绑定结果 **c = a ⊛ b** 定义为：

```
c_k = Σ_i a_i * b_{(k-i) mod n}
```

解绑时使用近似逆卷积。整个操作 O(n log n) 可使用 FFT 加速。Holographic 利用此机制在**无训练、无嵌入**的情况下实现可解释的记忆编码。

### 2. RRF（倒数排名融合，Hindsight 使用）

对于多个检索源的排名列表，RRF 综合分数为：

```
RRF_score(d) = Σ_{s} 1 / (k + rank_s(d))
```

其中 `k` 通常取 60。RRF 无需归一化不同来源的原始分数，对离群值鲁棒，在多策略召回中广泛使用。

## 8 配置实战：将提供商完全本地化

以 **Mem0 + Ollama + Qdrant 本地**为例：

```
# mem0_local_config.pyfrom mem0 import Memoryconfig = {  "llm": {    "provider": "ollama",    "config": {      "model": "llama3.1:8b",      "base_url": "http://localhost:11434",    }  },  "embedder": {    "provider": "ollama",    "config": {      "model": "nomic-embed-text",      "base_url": "http://localhost:11434",    }  },  "vector_store": {    "provider": "qdrant",    "config": {      "path": "./qdrant_data",   # 本地持久化    }  }}memory = Memory.from_config(config)# 添加记忆（自动提取）memory.add("用户喜欢用 Python 处理数据，讨厌 JavaScript", user_id="alice")# 检索results = memory.search("编程语言偏好", user_id="alice")
```

此配置**不调用任何外部 API**，所有模型与向量库运行在本机。

## 9 总结

| 场景 | 推荐 |
| --- | --- |
| 追求最大隐私与控制，接受检索质量折衷 | **Holographic** |
| 需要本地优先、可审计、低依赖 | **ByteRover** |
| 需要知识图谱与高阶记忆推理 | **Hindsight** |
| 需要多智能体与复杂用户建模 | **Honcho** |
| 希望自动管理，愿意投入基础设施 | **Mem0** （自托管） |
| 企业环境，接受 Cloudflare 绑定 | **Supermemory** |
| 不喜欢运维，仅需云端付费 | **RetainDB** |

选择记忆提供商本质是权衡：**隐私 vs 智能、控制 vs 便利、成本 vs 功能**。请根据你的数据主权要求和运维能力做出决策。
