> 📎 来源: [AI炼金社](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA==&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=975726407f2e6415b216570027722d00671974c034bee3b40f1360e37c481362c5d31da0a999&mpshare=1&scene=1&srcid=0420WK3Q10rE7Dsn5vnXgo07&sharer_shareinfo=413302b6419c52a533c57133c29572c9&sharer_shareinfo_first=413302b6419c52a533c57133c29572c9) | 时间: 2026-04-20 15:46

---

Andrej Karpathy 最近发了一条推文，16 小时内 1600 万次浏览。他说自己不再用 LLM 写代码，而是用来**建知识库**。

核心思路很简单：传统 RAG 每次查询都要从头检索，没有积累。他让 LLM 维护一个持久 Wiki——新增内容自动编译进去，知识复利增长。

这条推文火了之后，Hermes Agent 立刻实现了这个工作流。今天讲两个高级功能：**微信原生集成**和**LLM Wiki 知识库**。

## 一、微信集成：扫码就能用

Hermes Agent 支持**个人微信账号**直连，用的是腾讯 iLink Bot API。不需要公网端点、不需要 Webhook，HTTP 长轮询就够。

### 设置流程（3 步）

### Step 1：运行设置向导

```
hermes gateway setup
```

提示中选择 **Weixin**。向导自动完成：

- 请求二维码 → 显示在终端或提供 URL → 等你扫码 → 手机确认登录 → 保存凭证到 

  ```
  ~/.hermes/weixin/accounts/
  ```

成功后看到：

```
微信连接成功，account_id=your-account-id
```

### Step 2：配置环境变量

QR 登录完成后，在 

```
~/.hermes/.env
```

 设置：

```
WEIXIN_ACCOUNT_ID=your-account-id# 可选：访问控制WEIXIN_DM_POLICY=openWEIXIN_ALLOWED_USERS=user_id_1,user_id_2
```

### Step 3：启动网关

```
hermes gateway
```

适配器恢复凭证，连接 iLink API，开始长轮询接收消息。

### 支持的功能

- 私聊/群聊消息（可配置访问策略）
- 图片/视频/文件/语音媒体支持
- AES-128-ECB 加密 CDN 媒体传输
- Markdown 格式自动适配（标题/表格/代码块转微信可读）
- 智能消息分块（4000 字符以内单条发送）
- "对方正在输入..."提示
- 消息去重（5 分钟滑动窗口）
- 自动重试与退避

**私聊策略**：默认 

```
open
```

（任何人可私聊），可设 

```
allowlist
```

（白名单）、

```
disabled
```

（忽略私聊）、

```
pairing
```

（配对模式）。

**群聊策略**：默认 

```
disabled
```

（忽略群消息，因为个人微信可能在很多群）。

## 二、LLM Wiki：告别 RAG 的无状态检索

传统 RAG 的痛点：每次查询从头检索，没有积累。问一个需要综合五篇文档的问题，LLM 每次都要重新拼凑碎片。**知识不沉淀**。

Karpathy 的思路：让 LLM 维护一个持久 Wiki——新增内容自动编译进去，更新实体页、修订主题摘要、标注矛盾、强化或挑战已有观点。

**Wiki 是持久、复利增长的 artifact。交叉引用已经建好、矛盾已标注、综合已反映所有阅读内容。每加一个来源、每问一个问题，Wiki 都更丰富。**

### 三层架构

```
my-research/├── raw/                    # Layer 1: 不可变原始来源│   ├── articles/│   ├── papers/│   ├── repos/│   ├── data/│   └── images/├── wiki/                   # Layer 2: Agent 生成的 Wiki│   ├── index.md            # 内容目录（每次 ingest 更新）│   ├── log.md              # 时间线日志│   ├── overview.md│   ├── concepts/           # 概念页│   ├── entities/           # 实体页│   ├── sources/            # 来源摘要│   └── comparisons/        # 对比页├── outputs/                # 日期化报告、演示文稿├── CLAUDE.md               # Layer 3: Schema 配置
```

### Layer 1：Raw Sources（不可变）

你的原始文档集合——文章、论文、代码仓库、数据集、图片。LLM 只读，从不修改。这是验证基线：Wiki 里每条声明都能追溯到 

```
raw/
```

 里的文件。

用 **Obsidian Web Clipper** 浏览器扩展可以把网页文章转成 markdown，直接丢进 

```
raw/articles/
```

。

### Layer 2：The Wiki（LLM 生成）

Agent 生成的 markdown 页面，按类型组织：

- ```
  concepts/
  ```

  ：概念页（如 

  ```
  attention-mechanism.md
  ```

  ）
- ```
  entities/
  ```

  ：实体页（如 

  ```
  openai.md
  ```

  ）
- ```
  sources/
  ```

  ：来源摘要（每个摄入文档一条）
- ```
  comparisons/
  ```

  ：对比页（如 

  ```
  rag-vs-fine-tuning.md
  ```

  ）

两个关键文件：

- ```
  index.md
  ```

  ：内容目录，每次 ingest 更新，LLM 查询时先读这个导航
- ```
  log.md
  ```

  ：时间线日志，记录每个 ingest、每次更新、发现的矛盾

### Layer 3：Schema（CLAUDE.md）

最重要的文件。定义 Wiki 结构、命名约定、页面模板、操作流程。它把通用 LLM 变成**纪律严明的知识管理员**。

## 三、三种核心操作

Karpathy 用编译器类比：

```
raw/
```

 是源码，LLM 是编译器，

```
wiki/
```

 是输出，lint 是测试，query 是运行时。

### Ingest（摄入）

把新来源丢进 

```
raw/
```

，告诉 Agent 处理：

```
> I added a new article to raw/articles/. Please ingest it.
```

Agent 执行：

- 读取文档，讨论关键要点
- 在 

  ```
  wiki/sources/
  ```

   创建摘要页
- 级联更新 10-15 个相关 Wiki 页
- 如需创建新概念/实体页
- 更新 

  ```
  index.md
  ```
- 向 

  ```
  log.md
  ```

   添加记录

单次 ingest 可能触碰几十个 Wiki 页，因为 Agent 要追踪知识图谱里的关联。

### Query（查询）

向 Wiki 提问。Agent 搜索 

```
index.md
```

，读相关页面，综合回答并附 

```
[[wiki-link]]
```

 引用。

**关键洞察：好的回答可以反向写入 Wiki。** 你问的对比、分析、发现的连接——这些有价值，不应消失在聊天历史里。这样你的探索也像摄入来源一样**复利增长**。

### Lint（健康检查）

定期让 Agent 检查 Wiki：

- 页面之间的矛盾
- 过时声明（新来源已覆盖）
- 孤页（没有入链）
- 重要概念被提及但缺独立页
- 缺失交叉引用
- 可用 web 搜索填补的数据缺口

Agent 擅长建议新问题和新来源。这让 Wiki 随增长保持健康。

## 四、RAG vs LLM Wiki：什么时候用哪个

| 维度 | RAG | LLM Wiki |
| --- | --- | --- |
| 数据规模 | 数百万文档 | ~100 文档，~40 万字 |
| 架构复杂度 | 向量数据库 + embedding + chunking + rerank | 纯 markdown + index.md |
| 知识沉淀 | 无（每次从头检索） | 有（编译后持续更新） |
| 可审计性 | 黑盒向量，难以追溯 | 每条声明可追溯到 .md 文件 |
| 维护成本 | 需要专业 infra | Agent 自动维护 |
| 适用场景 | 企业级海量数据 | 个人/团队研究项目 |

Karpathy 的 Wiki 已长到约 **100 篇文章、40 万字**——比大多数博士论文还长——而他**几乎没自己写过**。

## 五、实战演示：从 ArXiv 论文到 Obsidian 图谱

视频演示了完整流程：

1. **创建 Wiki**

   ：

   ```
   hermes wiki init llm-finetuning
   ```
2. **批量摄入论文**

   ：Agent 从 ArXiv 抓取微调相关论文 → 自动提取结构化知识 → 生成交叉引用 Wiki 页
3. **研究命令**

   ：

   ```
   研究防止过拟合的方法
   ```

    → Agent 基于 Wiki 分析 → 生成新 Wiki 页面
4. **多 Wiki 管理**

   ：创建多个 Wiki 无缝切换 → 合并相关 Wiki（演示合并两个 Wiki 得到 27 页知识库）
5. **Obsidian 可视化**

   ：打开 Wiki 目录 → Graph 视图显示交叉引用网络 → 点击节点浏览页面

## 六、数据飞轮：知识复利增长

Karpathy 总结了核心价值：

**"编译一次，持续更新。"**

传统知识库死于维护成本。收集容易，整理困难，规模化维护不可能。

LLM Wiki 把这个不可能变成自动化：

- 你负责 curate（选什么进来）
- Agent 负责 bookkeeping（读、总结、交叉引用、更新索引、标注矛盾）

结果：知识库随时间**复利增长**，而不是随时间腐烂。

## 七、怎么开始

**微信集成**：

```
pip install aiohttp cryptography qrcodehermes gateway setup  # 选择 Weixinhermes gateway
```

**LLM Wiki**：

```
hermes wiki init my-research# 用 Obsidian Web Clipper 把文章丢进 raw/articles/# 然后让 Agent ingest
```

Karpathy 的 Gist：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Hermes Wiki 教程：https://www.aivi.fyi/llms/hermes-wiki

### 最后一句

RAG 是检索，LLM Wiki 是编译。检索每次从头来，编译一次后持续更新。如果你有个人研究项目、团队知识库、或者只是想给读完的书建个 companion wiki——这是目前最优雅的方案。
