> 📎 来源: [百码山庄](https://mp.weixin.qq.com/s?__biz=MzAwMTAzMzkzOQ==&mid=2647791746&idx=1&sn=7d06ae4df7a1b1e21cea88b6b7e033b1&chksm=83fa4360a47e40b7de089782e78e37dd0512a3400de54429db0849596602d2f55dead38052da&mpshare=1&scene=1&srcid=0422SoBXnz8ufQ3rGWkA5xgq&sharer_shareinfo=c750ad244157a60d90b7a15722e0f1fc&sharer_shareinfo_first=c750ad244157a60d90b7a15722e0f1fc) | 时间: 2026-04-22 04:00

---

> The agent that grows with you — 由 Nous Research 打造的自我进化 AI Agent

---

## 一、技术介绍

### 1.1 概述

Hermes Agent 是 Nous Research 开发的开源自主 AI Agent（MIT 协议），当前版本 v0.10.0。它不是 IDE 中的代码补全工具，也不是简单的聊天机器人包装——它是一个自我进化的自主 Agent，运行在你的服务器上，跨会话记忆学习，越用越强。

核心定位：

- 内置学习循环（Learning Loop）：从经验中创建技能，使用中自我改进
- 全平台触达：CLI、Telegram、Discord、Slack、WhatsApp 等 15+ 平台
- 灵活部署：$5 VPS、GPU 集群、或 Serverless（Daytona/Modal）

GitHub 数据： 104k+ Stars, 14.8k Forks, 521+ Contributors

### 1.2 核心架构

```
┌─────────────────────────────────────────────────────────┐
```

三个入口：

| 入口 | 用途 |
| --- | --- |
| CLI | 交互式终端 UI |
| Gateway | API 服务器，连接消息平台 |
| ACP | 编辑器集成（VS Code / Zed / JetBrains），通过 stdio/JSON-RPC |

核心循环（AIAgent）：

1. 用户输入 → 构建系统提示词
2. 解析运行时 Provider → 发送 API 请求
3. 处理 Tool Calls → 执行工具
4. 返回响应 → 持久化会话

### 1.3 关键子系统

| 子系统 | 说明 |
| --- | --- |
| Prompt System | 组装系统提示词：人格(SOUL.md) + 记忆 + 技能 + 上下文 + 工具说明 |
| Provider Resolution | 统一的 Provider 解析器，支持 18+ 提供商，处理 OAuth、密钥池、别名 |
| Tool System | 47 个工具，19 个工具集，自注册模式，支持 6 种终端后端 |
| Session Persistence | SQLite + FTS5 全文搜索，支持会话血缘追踪 |
| Plugin System | 三个发现源：用户目录、项目目录、pip entry points |
| Cron Scheduler | 一等公民的定时任务，支持自然语言配置，投递到任意平台 |

### 1.4 设计原则

- Prompt 稳定性：系统提示词不会在对话中途变化
- 可观察执行：每个工具调用对用户可见
- 可中断：API 调用和工具执行可随时取消
- 平台无关核心：一个 AIAgent 类服务所有入口
- 松耦合：可选子系统使用注册表模式
- Profile 隔离：每个 profile 独立的配置、记忆、会话

### 1.5 支持的 LLM Providers

无锁定，可自由切换 `hermes model` 或 `/model provider:model`：

- Nous Portal（官方端点）
- OpenRouter（200+ 模型）
- OpenAI / Anthropic
- NVIDIA NIM / Nemotron
- Ollama（本地模型）
- Hugging Face
- Kimi / Moonshot
- MiniMax / z.ai / GLM
- 小米 MiMo
- 或自定义端点

---

## 二、安装指南

### 2.1 一键安装（推荐）

Linux / macOS / WSL2：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Android (Termux)：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装器自动检测 Termux 环境。

> Windows 原生不支持，需先安装 WSL2。

安装器自动处理：

- Python 3.11、Node.js v22、uv、ripgrep、ffmpeg
- 仓库克隆、虚拟环境创建
- 全局 hermes 命令注册
- LLM Provider 配置向导

安装后：

```
source ~/.bashrc
```

### 2.2 手动安装

```
# 1. 克隆仓库
```

### 2.3 Nix / NixOS

项目提供 Nix Flake，支持声明式 NixOS module 和容器模式。

### 2.4 配置目录结构

```
~/.hermes/
```

### 2.5 常用管理命令

```
hermes config          # 查看配置
```

---

## 三、热门玩法

### 3.1 多平台消息 Agent

通过 Gateway 将 Hermes 连接到所有你的通讯平台，一个 Agent 统一服务：

```
hermes gateway setup    # 配置平台（Telegram/Discord/Slack 等）
```

支持 18 个平台适配器，包含语音转写、图片识别、文件处理、线程对话等能力。

实用场景：

- 在 Telegram 中用自然语言指挥服务器运维
- 通过 Discord 群组提供 AI 助手服务
- WhatsApp 接收每日自动化报告

### 3.2 定时自动化任务

内置 Cron 调度器，用自然语言配置定时任务并投递到任意平台：

```
/cron add "每天早上9点发送项目状态报告到 Telegram"
```

适用场景：每日站报、夜间备份、周报生成、监控告警。

### 3.3 自主技能创建与进化

Hermes 在完成复杂任务后会自主创建技能（Skill），下次遇到类似任务时直接调用：

```
# 浏览已有技能
```

技能遵循 agentskills.io 开放标准，社区共享，渐进式加载节省 Token。

### 3.4 子 Agent 并行任务

通过 `delegate_task` 和 `execute_code` 实现并行工作流：

- 生成独立的子 Agent 处理并行任务
- 编写 Python 脚本通过 RPC 调用工具
- 将多步流水线压缩为零上下文成本的单轮操作

示例： 同时搜索多个代码库、并行分析多个日志文件、批量处理数据。

### 3.5 六种终端后端灵活部署

| 后端 | 适用场景 |
| --- | --- |
| Local | 本地开发 |
| Docker | 容器化隔离 |
| SSH | 远程服务器 |
| Daytona | Serverless 持久化 |
| Modal | Serverless 云端 |
| Singularity | HPC 高性能计算 |

空闲时环境休眠，按需唤醒，最低成本运行。

### 3.6 浏览器自动化

内置浏览器工具集，支持网页导航、截图、视觉分析：

```
帮我打开 GitHub trending 页面，截图分析今天有什么热门项目
```

### 3.7 智能家居控制

通过 Home Assistant 集成，用自然语言控制智能设备：

```
把客厅灯调暗一点
```

### 3.8 研究与训练（RL）

面向研究者的高级用法：

- 批量轨迹生成（Batch Runner）
- Atropos RL 环境集成
- 轨迹压缩生成训练数据
- ShareGPT 格式输出

### 3.9 MCP Server 扩展

连接任意 MCP Server 扩展工具能力，无需修改 Agent 源码：

```
# config.yaml
```

### 3.10 记忆系统深度使用

- 持久记忆：跨会话记住项目上下文和用户偏好
- FTS5 全文搜索：回溯任意历史对话
- Honcho 辩证用户建模：越用越懂你
- 主动遗忘：可清除不再相关的记忆

---

## 四、快速上手示例

```
# 安装
```

---

## 五、相关资源

| 资源 | 链接 |
| --- | --- |
| GitHub | https://github.com/NousResearch/hermes-agent |
| 官方文档 | https://hermes-agent.nousresearch.com/docs/ |
| 官网 | https://hermes-agent.nousresearch.com/ |
| Skills Hub | https://agentskills.io |
| Discord 社区 | Nous Research Discord |
| WebUI | https://github.com/nesquena/hermes-webui |

---

*文档整理于 2026-04-20*
