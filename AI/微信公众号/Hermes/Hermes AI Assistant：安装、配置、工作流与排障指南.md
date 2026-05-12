> 📎 来源: [AI拉呱](https://mp.weixin.qq.com/s?__biz=MzI3NDE5MjExOQ==&mid=2650986900&idx=1&sn=61865396ad393fbb9730a24a7a138d79&chksm=f1cc7c6da3259c6ebf5c682ac3327d4642671fdb649c76c07c4c1a47f5b2a4caf64c32ef6717&mpshare=1&scene=1&srcid=0422yClCKLFggzcr7Xzero9l&sharer_shareinfo=8ea71d208dafb4cb0172a76b7eec679e&sharer_shareinfo_first=8ea71d208dafb4cb0172a76b7eec679e) | 时间: 2026-04-22 04:00

---

# Hermes AI Assistant：安装、配置、工作流与排障指南

> 作者：AI拉呱（Errol Yan）
> 定位：AI领域深度内容与实战方法分享

Hermes Agent 是一个可自托管、模型无关（model-agnostic）的 AI 助手：你可以把它跑在本地机器或低成本 VPS 上，通过终端与消息渠道使用，并通过“技能 + 记忆”把重复任务沉淀成可复用能力，让它越用越顺手。

它最有价值的打开方式，不是“偶尔打开一个聊天窗口问两句”，而是把它当作一层长期运行的基础设施：当 Hermes 作为服务稳定运行、并拥有固定的 home 目录之后，你的提示词会越来越像“运维（ops）”，而不是“聊天（chat）”。

## Hermes 是什么？为什么值得做成“长期服务”？

Hermes Agent 是一个开源 AI agent，设计目标是：持久运行、能用工具（终端、文件、网页等），并通过技能与记忆系统持续改进自己的行为。

有两个设计选择特别关键，因为它们决定了你后续的使用方式：

1. 1. **不绑定单一模型厂商**：官方流程支持多种模型提供方，也支持任何 OpenAI-compatible 的端点。切换模型主要通过 

   ```
   hermes model
   ```

    完成，而不是改代码。
2. 2. **清晰区分“对话”和“执行”**：你可以聊很久，但一旦要做事，必须通过显式工具与可配置的执行后端来完成。安全性、可复现性、排障能力主要都在这一层。

成本与许可也很朴素：Hermes Agent 本体是 MIT 许可证的免费软件；如果你用托管模型，成本取决于你的提供方计费；如果你跑本地模型，则可以避免 API 费用。

## 安装 Hermes Agent

Hermes 提供 Linux、macOS、WSL2 的快速安装路径。

### 一行安装

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装完成后，重新加载 shell，再启动 CLI：

```
source ~/.bashrc   # 或 source ~/.zshrchermes
```

安装脚本不只是“薄封装”：它通常会处理依赖、拉取仓库、创建虚拟环境、安装 

```
hermes
```

 命令，并把你带到一个可直接开始对话的状态。

### Windows 与 Android 说明

- 原生 Windows 不支持；推荐使用 WSL2 在 Linux 环境里运行 Hermes。
- Android 支持 Termux 安装路径，Hermes 会识别 Termux 并调整依赖与环境初始化。

## Quickstart：快速跑起来但不要“盲跑”

最快的第一次运行确实是直接 

```
hermes
```

，但一个真正有意义的 quickstart 需要你额外做两件事：

- 选模型提供方与默认模型
- 选择启用哪些工具（toolsets）

### 选择提供方与模型

Hermes 有三个互补入口：

- ```
  hermes model
  ```

  ：选择提供方与默认模型
- ```
  hermes tools
  ```

  ：启用/禁用工具集
- ```
  hermes setup
  ```

  ：交互式向导（覆盖主要配置区域）

最小流程：

```
hermes modelhermes toolshermes
```

### 先验证“工具执行”能否正常工作

在你建立使用习惯之前，建议先做一次工具使用的 smoke test：这既验证终端工具是否能执行，也验证权限提示是否按预期弹出。

示例提示词：

> Show my disk usage and the five largest directories.

如果 Hermes 无法执行终端工具，优先跳到排障部分：终端后端配置问题是最常见原因之一，而且通常看一眼配置就能定位。

## 可扩展的配置方式（避免“昨天还好好的”）

Hermes 的复利主要来自你是否理解：它把配置/状态放在哪、配置优先级怎么解析。

### 配置与状态目录

Hermes 默认把设置和状态放在 

```
~/.hermes
```

 下。常见内容包括：

- ```
  config.yaml
  ```

  ：非敏感配置
- ```
  .env
  ```

  ：密钥等敏感信息
- ```
  auth.json
  ```

  ：OAuth 凭证
- ```
  SOUL.md
  ```

  ：身份设定
- ```
  memories/
  ```

  、

  ```
  skills/
  ```

  、

  ```
  cron/
  ```

  、

  ```
  sessions/
  ```

  、

  ```
  logs/
  ```

   等目录

这件事很重要：

- 排障会变成“机械化”：你知道该看哪里
- 备份更简单：一个目录就能覆盖你关心的大部分状态

### 配置优先级：别把密钥塞进 config.yaml

Hermes 有明确的配置优先级（从高到低）：

1. 1. CLI 覆盖
2. 2. 

   ```
   config.yaml
   ```
3. 3. 

   ```
   .env
   ```
4. 4. 内置默认值

一个很实用的细节是：

```
hermes config set
```

 会把值写到正确文件里：密钥写入 

```
.env
```

，非敏感设置写入 

```
config.yaml
```

。

```
hermes config set model openrouter/meta-llama/llama-3.1-70b-instructhermes config set terminal.backend dockerhermes config set OPENROUTER_API_KEY sk-or-v1-xxxxxxxx
```

Hermes 也支持在 

```
config.yaml
```

 中使用 

```
${VAR_NAME}
```

 做环境变量替换：这对“把敏感信息留在环境里，但仍在结构化配置中引用”非常方便。

## Sandbox 与执行后端（Terminal Backends）

Hermes 支持多种终端后端，决定 shell 命令究竟在哪里执行，例如：

```
local
```

、

```
docker
```

、

```
ssh
```

、

```
modal
```

、

```
daytona
```

、

```
singularity
```

。

一个实用的理解方式：

- ```
  local
  ```

  ：最快最简单，但不隔离
- ```
  docker
  ```

  ：务实的安全 + 可复现层
- ```
  ssh
  ```

  ：把聊天设备与算力机器分离得更干净
- ```
  modal
  ```

   / 

  ```
  daytona
  ```

  ：偏“serverless，但足够持久”的工作方式
- ```
  singularity
  ```

  ：更适合 HPC 场景

一个最小的 Docker 后端示例：

```
# ~/.hermes/config.yamlterminal:  backend: docker  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"  docker_volumes:    - "/home/user/projects:/workspace/projects"  docker_forward_env:    - "GITHUB_TOKEN"
```

如果你把 bash 权限交给 agent，隔离就不是锦上添花，而是必要条件。Docker 后端也通常有更进一步的安全加固选项（例如 drop capabilities、禁用提权）。

## Skills、Memory 与 Profiles：让 Hermes “越用越值钱”

Hermes 有两套会产生复利的机制：

- **Skills（技能）**：过程型记忆。Hermes 能创建/更新/删除技能，并在完成复杂任务后建议把做法固化成 skill。
- **Memory（记忆）**：内置记忆通常以文件形式存在（如 

  ```
  MEMORY.md
  ```

  、

  ```
  USER.md
  ```

  ），也可配置外部 memory provider 做更强的召回。

如果你希望在同一台机器上跑多个互相隔离的 agent，使用 **profiles** 会更合适：每个 profile 有独立目录，包含各自的配置、密钥、记忆、会话、技能、cron、gateway 状态等。

## 典型工作流（把 Hermes 当作“服务工程”）

### 稳定基线

一个不容易“腐烂”的基线流程是：

1. 1. 安装并在 CLI 里完成第一次对话。
2. 2. 用 

   ```
   hermes model
   ```

    选择提供方与模型，并确认成本预期。
3. 3. 配置工具集，并决定终端执行是 

   ```
   local
   ```

    还是 sandbox。
4. 4. 在你用默认 

   ```
   SOUL.md
   ```

    一段时间后再去改它：身份设定往往比大家想象得更影响输出，因为它通常会进入 system prompt 的高权重位置。

### 日常使用（产生复利的节奏）

Hermes 是终端 UI 形态，适合长会话、slash commands、可恢复会话、以及工具输出流式呈现。

一个更“复利型”的节奏是：

- 按项目用命名 session 工作
- 上下文变大时做压缩（compression）
- 让 Hermes 把重复流程沉淀成 skills
- 始终保持“问（ask）”与“做（act）”的边界，让工具执行可审计

### 消息网关（24/7 访问）

消息网关会让 Hermes 更像“助手”而不是“终端应用”：它可以连接多个平台、管理会话、跑 cron、投递消息。

- 通过 

  ```
  hermes gateway setup
  ```

   进行初始化
- 支持前台运行或作为用户服务运行
- 常见子命令：

  ```
  run
  ```

   / 

  ```
  install
  ```

   / 

  ```
  start
  ```

   / 

  ```
  stop
  ```

   / 

  ```
  status
  ```

   / 

  ```
  restart
  ```

安全默认值同样重要：allowlist 与配对（pairing）是为了把工具型 bot 的风险收敛到可控范围。常见的“bot 沉默”并不是坏了，而是授权在按设计工作。

## 更新与维护（尽量别让更新变成事故）

Hermes 的更新是一级命令，常见的更新后小检查可以是：

```
hermes updatehermes doctorhermes gateway status
```

## 排障与诊断

多数 Hermes 故障并不神秘；它之所以看起来神秘，是因为很多人只盯“模型层”，忽视了“运行时层”。

### 快速体检命令

- ```
  hermes doctor
  ```

  ：交互式诊断
- ```
  hermes status
  ```

  ：快速总览
- ```
  hermes dump
  ```

  ：可分享的（可脱敏）配置摘要

日志通常在 

```
~/.hermes/logs
```

 下，可用：

```
hermes doctor --fixhermes statushermes dump --show-keyshermes logs errors -f
```

### 常见安装失败

常见问题包括 Python 版本不符、找不到 

```
uv
```

、以及混用 

```
sudo
```

 安装与用户安装导致的权限问题。修复策略通常是：升级 Python、安装 

```
uv
```

、避免 

```
sudo
```

 并重新安装。

### Provider 与模型问题

- API key 不工作：检查配置，重新运行 

  ```
  hermes model
  ```

  ，或用 

  ```
  hermes config set
  ```

   直接写入 key（注意：key 往往是提供方专属）。
- “model not found”：用 

  ```
  hermes model
  ```

   选择有效标识，必要时用会话级覆盖。
- 429 限流 / 上下文过长：等待、切换提供方/模型、通过压缩或新 session 降低上下文压力。

### 终端后端与网关问题

- 终端命令立刻失败：优先检查后端依赖（例如 Docker 是否在运行、SSH 环境变量是否齐全）。调试时临时回退到 

  ```
  local
  ```

   也很合理。
- 网关“无响应”：很多时候是 allowlist 与 pairing 在按默认安全策略工作。

---

## 关注 AI拉呱

如果这篇内容对你有启发，欢迎关注「AI拉呱」，获取更多 AI 前沿洞察、实战教程与趋势解读。

## 下期在看

下期将继续带来该主题的进阶拆解与实操案例，建议先收藏本文，避免错过更新。
