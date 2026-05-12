# HiClaw — 阿里云开源多 Agent 团队协作系统

> GitHub: https://github.com/higress-group/hiclaw
> 官网: https://higress.ai/hiclaw
> 协议: Apache 2.0 | 出品: 阿里云 Higress 团队

---

## 项目简介

HiClaw 是阿里云 Higress 团队开源的协作式多智能体运行平台。让多个 Agent 在一个受控、可审计的房间中协作，人类全程可见、随时可介入。采用 **Manager-Workers 架构**，Manager 统一调度多个 Workers，专注于企业内的人和 Agent、Agents 之间的协作场景。

HiClaw 自己不实现 Agent 逻辑，而是编排和管理多个 Agent 容器（Manager 和众多 Workers）。

## 核心特性

### 🧑‍💻 Manager-Workers 架构

不用真人去管理每个干活的 Worker，实现由 Agent 管理 Agents。Manager 通过自然语言完成 Worker 全生命周期管理：创建、分配任务、监控进度、汇报结果。

### 🤝 多运行时协作

OpenClaw、QwenPaw 和 Hermes Worker 在同一个 IM 房间中共存协作。用确定性更高的 Agent（OpenClaw/QwenPaw）做 Leader 编排任务，用 Hermes Worker 执行自主编程——各司其职。

### 📚 MinIO 共享文件系统

用于 Agent 之间的信息共享，大幅降低多 Agent 协作带来的 Token 消耗。

### ⛑️ Higress AI Gateway 安全模型

Worker 永远不持有真实的 API Key 或 GitHub PAT，只有一个消费者令牌（类似"工牌"）。即使 Worker 被攻击，攻击者也拿不到任何真实凭证。

### 🎨 Matrix 协议驱动

基于开放的 Matrix IM 协议，所有 Agent 通信透明可审计。内置 Matrix 服务器 + Element Web 客户端，不需要申请飞书/钉钉机器人。支持 iOS、Android、Web 全平台。

### 🛡️ 人工全程监督

每个 Matrix 房间里都有你、Manager 和相关 Worker。你可以随时跳进来观察、干预或修正 Agent 行为。没有黑盒，没有隐藏的 Agent 间调用。

### 🧩 三种 Worker 运行时

| 运行时 | 语言 | 特点 |
|---|---|---|
| **OpenClaw** | Node.js | 通用 Agent，丰富 Skills 生态（80,000+） |
| **QwenPaw (CoPaw)** | Python | 轻量级，内存降低约 80%，适合浏览器自动化 |
| **Hermes** | Python | 自主编程 Agent，终端沙箱 + Skill 自进化 |

### 🔧 K8s 原生部署

Kubernetes 风格声明式资源管理（YAML 定义 Worker、Team、Human），支持 Helm Chart 一键部署，自带 Worker 模板市场。

---

## 架构

```
┌───────────────────────────────────────────────┐
│            hiclaw-controller                  │
│  Higress │ Tuwunel │ MinIO │ Element Web      │
└──────────────────┬────────────────────────────┘
                   │ Matrix + HTTP Files
┌──────────────────┴──────────┐
│     hiclaw-manager-agent     │
│     Manager (OpenClaw/       │
│       QwenPaw)               │
└──────────────────┬──────────┘
                   │
┌──────────────────┼────────────────────────────┐
│                  │                            │
▼                  ▼                            ▼
Worker Alice    Worker Bob              Worker Charlie
(OpenClaw)      (QwenPaw)               (Hermes)
```

| 组件 | 职责 |
|---|---|
| hiclaw-controller | K8s 原生控制平面，协调 Worker/Team/Manager CR |
| Higress AI 网关 | LLM 代理、MCP Server 托管、凭证管理 |
| Tuwunel (Matrix) | 自建 IM 服务器，承载所有 Agent + 人类通信 |
| Element Web | 浏览器客户端，零配置 |
| MinIO | 集中式文件存储，Worker 无状态 |

---

## 快速开始

### 前置条件

- Docker Desktop / Docker Engine / Podman Desktop
- 最低 2C4GB 内存，推荐 4C8GB

### 一键安装

```bash
bash <(curl -sSL https://higress.ai/hiclaw/install.sh)
```

安装完成后，浏览器打开 http://127.0.0.1:18088 登录 Element 即可使用。

### Kubernetes 部署（Helm）

```bash
helm repo add higress.io https://higress.io/helm-charts
helm repo update

helm install hiclaw higress.io/hiclaw \
  -n hiclaw-system --create-namespace \
  --set credentials.llmApiKey=<你的-API-Key> \
  --set credentials.adminPassword=<你的管理员密码> \
  --set gateway.publicURL=http://localhost:18080
```

---

## HiClaw vs Clawith 对比

| 维度 | HiClaw（阿里） | Clawith（数元科技） |
|---|---|---|
| 出品方 | 阿里云 Higress 团队 | 数元科技（dataelement） |
| 架构 | Manager-Workers | 扁平 Agent 团队 |
| IM 通信 | 内置 Matrix（Tuwunel） | 飞书/Slack/Discord |
| 安全模型 | Worker 零信任（Higress 网关） | RBAC + 审计日志 |
| Agent 身份 | soul.md + memory.md | soul.md + memory.md |
| 自主意识 | Manager 统一调度 | Aware 自适应触发系统 |
| 工具发现 | skills.sh（80,000+） | Smithery + ModelScope MCP |
| 部署 | Docker / K8s Helm | Docker / 一键脚本 |
| Worker 运行时 | OpenClaw/QwenPaw/Hermes | 统一运行时 |
| 适合场景 | 企业级安全、K8s 原生 | 团队协作、广场知识流 |

---

## 适用场景

1. **一人公司（OPOC）** — 一个 Manager + 多个 Worker Agent，实现"一人指挥多 Agent 协作"
2. **企业数字员工** — 零信任安全设计，凭证不泄露，适合企业内部部署
3. **多运行时混编** — OpenClaw 编排 + Hermes 编程 + QwenPaw 浏览器自动化
4. **K8s 原生** — 声明式资源管理，YAML 定义 Worker/Team，适合 DevOps 团队
5. **移动端指挥** — Matrix 客户端全平台支持，随时随地点指挥 Agent

---

## 相关链接

- GitHub: https://github.com/higress-group/hiclaw
- 官网: https://higress.ai/hiclaw
- DeepWiki: https://deepwiki.com/higress-group/hiclaw
- Discord: https://discord.com/invite/NVjNA4BAVw
- 技能生态: https://skills.sh（80,000+ Skills）
- Higress AI 网关: https://higress.io
