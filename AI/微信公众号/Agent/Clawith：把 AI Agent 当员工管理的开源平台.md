> 📎 来源: [Agent开发笔记](https://mp.weixin.qq.com/s?__biz=MzkwMjE4Mzk3MQ==&mid=2247483899&idx=1&sn=186b5b219a5b02b6f7ab2b1afd464c3f&chksm=c176d569b84483c47bf458b9bf3af7c3e3122fa0d40e00a6003562b1e4f19e6f6bdd3f8ba758&mpshare=1&scene=1&srcid=0512VtFIjVdTF0M2nvIM9Pmo&sharer_shareinfo=92cf0c4212a954228336827e3f1665f0&sharer_shareinfo_first=92cf0c4212a954228336827e3f1665f0) | 时间: 2026-05-12 03:50

---

# Clawith：把 AI Agent 当员工管理的开源平台

## 先说清楚这东西是干嘛的

做 Agent 开发的人大概都经历过一个阶段：Agent 跑起来了，能聊天、能调工具，但它本质上还是个"一次性调用"——用户问一句它答一句，关掉对话就什么都没了。

Clawith 想解决的问题是：**让 Agent 变成持续在线的"数字员工"，而不是一个聊天框。**

具体来说：

- Agent 有自己的身份（soul.md 定义人格）
- 有长期记忆（memory.md 跨对话持久化）
- 有独立工作空间（完整文件系统）
- 能自主感知和行动（不是被动等用户发消息）
- 能和其他 Agent 协作（互相发消息、委派任务）
- 有组织级管控（权限分级、审计日志、用量配额）

一句话：**它是 AI Agent 的运行时操作系统 + 组织管理平台。**

## 举个例子就明白了

假设你有一家 20 人的技术团队，想搞几个 AI "员工"：

**场景 1：运营助理 Agent**

你希望它每天早上自动检查公司 Twitter 提及、竞品动态、内部 OKR 进度，然后在飞书群里发一份日报。

在 Clawith 里，你创建一个 Agent，给它配一个 cron 触发器（每天 9:00），绑定 Focus Item "每日运营简报"。到点它自己醒来、调用工具抓数据、生成报告、通过飞书 bot 身份发到群里。没人需要手动触发它。

**场景 2：客户成功 Agent**

客户在飞书/钉钉/Discord 上问问题，Agent 以独立 bot 身份接入渠道，自动响应。它记得每个客户之前聊过什么（长期记忆），遇到搞不定的问题会自动委派给"技术支持 Agent"。

**场景 3：Agent 组队干活**

产品经理 Agent 在"广场（Plaza）"发了一条动态："下周要做用户调研"，研究助理 Agent 看到后自主创建触发器跟进，到时间自动开始收集数据。

这些场景的共同点：**Agent 不是被动响应，而是主动工作；不是一次性的，而是持续运营的。**

## 架构拆解

看过源码后整理的架构全貌：

```
┌─────────────────────────────────────────────────────────────┐│                   Frontend (React 19 + Vite)                 ││            TypeScript · Zustand · TanStack Query             ││                      端口 3008                               │├─────────────────────────────────────────────────────────────┤│                   Backend (FastAPI 单体)                      ││       Uvicorn · WebSocket · JWT/RBAC · 18+ API 模块          ││                      端口 8008                               │├────────────┬────────────────┬───────────────────────────────┤│ PostgreSQL │     Redis      │     Docker Engine              ││  (数据持久) │  (缓存/队列)    │   (Agent 代码执行沙箱)         │└────────────┴────────────────┴───────────────────────────────┘          ↕                              ↕   /data/agents//           各渠道长连接/轮询   ├── soul.md                    ├── 飞书 WebSocket   ├── memory/memory.md           ├── 钉钉 Stream   ├── skills/                    ├── 企微 WebSocket   └── relationships.md           ├── Discord Gateway                                  └── 微信 iLink Poll
```

### 几个关键设计决策

**1. 文件系统即 Agent 状态**

Agent 的人格、记忆、技能全部是 Markdown 文件，存在宿主机 `./backend/agent_data//` 下。好处是：

- 可以直接 cat/vim 调试
- 导入导出就是复制文件夹
- 版本管理可以用 git

**2. Trigger Daemon —— 核心调度引擎**

后端启动时跑一个 asyncio 后台任务，每 15 秒 tick 一次：

```
TICK_INTERVAL = 15      # 秒DEDUP_WINDOW = 30       # 同一 Agent 30秒内不重复唤醒MAX_AGENT_CHAIN_DEPTH = 5  # A→B→A→B→A 最多 5 层
```

支持 6 种触发器：

- `cron` — 定时循环（"每天 9:00"）
- `once` — 单次定时（"明天下午 3 点提醒我"）
- `interval` — 固定间隔（"每 30 分钟检查一次"）
- `poll` — HTTP 端点监控（"这个 API 返回值变了就通知我"）
- `on_message` — 等待特定人/Agent 回复
- `webhook` — 接收外部 HTTP 回调（GitHub、Grafana 等）

每个触发器必须绑定一个 Focus Item（工作记忆），形成 **"关注什么 → 什么时候检查 → 检查完标记完成"** 的闭环。

**3. Autonomy Policy —— 分级权限控制**

不是简单的 allow/deny，而是 L1/L2/L3 三级：

```
autonomy_policy = {    "read_files": "L1",              # 自主执行    "write_workspace_files": "L2",   # 自主但记录    "send_external_message": "L3",   # 需人工审批    "delete_files": "L3",    "financial_operations": "L3",}
```

**4. 渐进披露 Prompt**

技能不全文塞进 System Prompt。只注入索引表（名称 + 描述），Agent 需要时通过 `read_file` 工具自己加载完整内容。省 Token。

**5. 沙箱代码执行**

支持 7 种后端（subprocess/docker/e2b/judge0/codesandbox/self\_hosted/aio\_sandbox），默认用 subprocess + bubblewrap 文件系统隔离。

### 不用 LangChain/LangGraph

这一点值得注意。Clawith 的 LLM 调用是自研的简单封装（`app/services/llm/`），没有用 LangChain 体系。优点是依赖少、可控；缺点是复杂编排（多步推理、条件分支、状态机）需要自己造轮子。

## 部署实操

### 方式一：Docker Compose（推荐）

```
git clone https://github.com/dataelement/Clawith.gitcd Clawith && cp .env.example .envdocker compose up -d
```

等几分钟，打开 `http://localhost:3008`。第一个注册的用户自动成为管理员。

**国内加速：**

```
# Docker 镜像加速sudo tee /etc/docker/daemon.json > /dev/null <<EOF{  "registry-mirrors": [    "https://docker.1panel.live",    "https://hub.rat.dev"  ]}EOFsudo systemctl daemon-reload && sudo systemctl restart docker# pip 加速（构建时）export CLAWITH_PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simpleexport CLAWITH_PIP_TRUSTED_HOST=pypi.tuna.tsinghua.edu.cn
```

### 方式二：裸机部署

```
git clone --depth 1 https://github.com/dataelement/Clawith.gitcd Clawithbash setup.sh        # 自动装依赖、建库、初始化数据bash restart.sh      # 启动前后端
```

环境要求：Python 3.12+、Node.js 20+、PostgreSQL 15+、2核4G30G 磁盘。

### 关键配置项

`.env` 里必须改的：

```
SECRET_KEY=你的随机字符串JWT_SECRET_KEY=另一个随机字符串DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/clawith
```

LLM API 配置在 Web 管理后台设置（支持 OpenAI、Anthropic 等任何 OpenAI 兼容 API）。

## 使用流程

### 1. 创建 Agent

登录后台 → 新建 Agent → 填写：

- 名称、头像
- 角色描述（System Prompt 的一部分）
- 选择 LLM 模型
- 设置权限等级

### 2. 配置 Agent 身份

系统会为 Agent 创建独立工作空间，你可以直接编辑：

- `soul.md` — 定义人格和行为准则
- `memory/memory.md` — 预设长期记忆
- `skills/` — 添加技能文件

### 3. 接入渠道

设置 → 渠道配置 → 填入飞书/钉钉/Discord 等 Bot 凭据。Agent 就能以独立 bot 身份在 IM 里响应了。

### 4. 设置触发器

让 Agent 自主工作的核心。创建 Focus Item → 绑定 Trigger → Agent 到点自动醒来执行。

### 5. 观察 Reflections

专属视图查看 Agent 自主推理过程：什么时间醒来、推理了什么、调用了哪些工具。这是调试和理解 Agent 行为的关键入口。

## 几个注意事项

**Token 消耗问题**

每个 Agent 都有心跳/触发器在定期唤醒，加上长期记忆检索，Token 用量会比普通聊天 Bot 高不少。建议：

- 调大触发器间隔（生产环境别用 5 分钟一次的 poll）
- 善用 `max_tokens_per_day` 配额
- 选便宜的模型做日常巡检，贵的模型做复杂推理

**单体瓶颈**

Trigger Daemon 是后端内的 asyncio task，不是独立进程。Agent 数量上百后 15 秒循环可能跑不完。目前没有分布式调度方案。

**安全问题**

Docker Compose 默认挂载了 docker.sock + SYS\_ADMIN 权限。生产环境建议：

- 限制 Docker socket 访问
- 改 SECRET\_KEY
- 开 HTTPS
- 定期备份 `/data/agents/`

## 和同类平台的横向对比

### 定位差异

| 平台 | 一句话定位 |
| --- | --- |
| **Clawith** | AI 数字员工的操作系统——Agent 有身份、记忆、自主感知，像雇员一样持续工作 |
| **Multica** | AI 编码团队的 Jira——不做 Agent，只调度管理现有编码 Agent CLI |
| **Dify** | LLM 应用开发平台——拖拽式构建 RAG/对话/工作流应用 |
| **CrewAI** | 多 Agent 编排框架——Python 代码定义角色+任务，一次性协作完成目标 |
| **Coze** | 字节的 Bot 构建平台——零代码拖拽做聊天机器人，自带发布渠道 |

### 核心能力对比

| 维度 | Clawith | Multica | Dify | CrewAI | Coze |
| --- | --- | --- | --- | --- | --- |
| **Agent 生命周期** | 持久存在，有身份/记忆 | 任务级（Issue 完就结束） | 无状态（每次请求即一次） | 临时组队，任务完即销毁 | 持久 Bot，但无自主行为 |
| **自主性** | ⭐ 最强：自适应触发器，主动感知行动 | 中：接 Issue 后自主执行 | 弱：被动响应请求 | 中：任务链自动流转 | 弱：被动响应用户消息 |
| **多 Agent 协作** | Agent 互相发消息/委派/感知组织架构 | 通过看板间接协作（人分配） | 不支持（单 App 逻辑） | 原生支持（Role → Task → Crew） | 不支持 |
| **记忆系统** | 长期记忆 + 工作记忆（Focus Items） | 技能沉淀（Skills 复用） | 对话历史 + 向量知识库 | 短期记忆（单次 Crew 内） | 对话历史 + 知识库 |
| **LLM 推理** | 不跑模型，自己组 prompt 调外部 API | 完全不做推理 | 统一封装 LLM 调用 | 通过 LangChain 调 LLM | 内置模型调用 |
| **技术门槛** | 中（需部署，需配 LLM API） | 低（CLI 安装，云服务可用） | 低（Web 拖拽） | 高（纯 Python 代码） | 最低（零代码） |
| **开源** | ✅ Apache 2.0 | ✅ Apache 2.0 | ✅ Apache 2.0 | ✅ MIT | ❌ 闭源 SaaS |
| **渠道集成** | 飞书/钉钉/企微/Discord/微信 | Web 看板 | Web + API | 无（需自己包） | 豆包/飞书/微信/Web |

### 架构层级对比

```
用户触达层        编排/管理层         Agent 执行层        LLM 层             ──────────       ──────────        ──────────        ──────Coze:        多渠道发布   →   零代码工作流编排  →  内置 Bot 运行时  →  字节模型Dify:        Web/API     →   可视化编排器      →  内置执行引擎     →  多 LLM 适配CrewAI:      代码调用     →   Python 角色编排   →  LangChain Agent  →  多 LLM 适配Clawith:     多渠道 IM    →   触发器+组织架构   →  数字员工(持久)   →  多 LLM APIMultica:     Web 看板     →   Issue 调度器      →  外部 CLI Agent   →  各 CLI 自带
```

### 场景选型指南

| 你想做什么 | 选谁 |
| --- | --- |
| 快速做一个客服/FAQ 机器人 | Coze（最快）或 Dify（更可控） |
| 构建 RAG 知识问答应用 | Dify |
| 多角色协作完成一次性复杂任务（研究报告、内容创作） | CrewAI |
| 让 AI 当"持续在线的数字员工"（运营、监控、日报） | **Clawith** |
| 把 Claude Code / Codex 等编码 Agent 纳入开发流程 | Multica |
| 企业内部多 Agent + 权限管控 + 审计 | **Clawith** |
| 需要 Agent 有自主触发、长期记忆、跨对话一致性 | **Clawith** |
| 需要可视化编排 + 低代码 | Dify 或 Coze |
| 纯开发者，偏好代码控制 | CrewAI（Python）或 Multica（CLI） |
| 个人/小团队快速验证 AI 产品想法 | Coze 或 Dify |

### 它们能组合使用吗？

能，不互斥。几种实际组合：

- **Clawith + Dify**：用 Clawith 管理 Agent 生命周期和触发调度，Agent 内部调用 Dify 工作流处理具体业务逻辑
- **Multica + Clawith**：Multica 管开发任务分配，Clawith Agent 作为其中一个 Runtime 执行编码任务
- **CrewAI + Dify**：CrewAI 做多角色编排，单个角色通过 Dify API 获取 RAG 增强的回答

## 值得关注的点

1. 1. **Aware 系统（自适应触发）** 是最大差异化——Agent 不是被动等消息，而是自己管理日程
2. 2. **Focus-Trigger 绑定** 设计精巧，让 Agent 的"注意力"有结构化的表达
3. 3. **文件系统即状态** 的设计对调试非常友好
4. 4. **项目还在早期**（161 Issues、57 PRs），API 和功能可能快速变化

---

**仓库地址：** https://github.com/dataelement/Clawith

**许可证：** Apache 2.0

**最低配置：** 2 核 / 4 GB / 30 GB + 任意 LLM API Key
