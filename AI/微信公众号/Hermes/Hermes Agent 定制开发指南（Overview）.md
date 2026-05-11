> 📎 来源: [智能思辨录](https://mp.weixin.qq.com/s?__biz=MzY5NzIwOTg4MQ==&mid=2247483790&idx=1&sn=f613d0cf8b37898f6534700223564f6c&chksm=f5f2260398b21c1f818afbe5d8ea0086a06135d78e5dbffa1d3251183d96e53ee33f03d624d2&mpshare=1&scene=1&srcid=0421zp5815pO8LUnQ5QRJpNr&sharer_shareinfo=57eaf6ae12f869696bc2f484f0822823&sharer_shareinfo_first=57eaf6ae12f869696bc2f484f0822823) | 时间: 2026-04-21 23:48

---

这篇文章是给想深入了解 Hermes Agent 的小伙伴看的（不讲怎么安装和使用），初心是我想从工程上深入学习一下 AI Agent。为什么是 Hermes 而不是 OpenClaw，主要是因为我觉得 Hermes 的工程架构更加清晰、门槛较低一些。我后续准备做一个系列将 Agent 所学的部分和大家分享讨论。

这篇文章准备从一个宏观的角度去看看如果开发者拿到这么一个项目，我们应该如何启动，能够快速上手。

下面从开发环境、架构、功能地图、定制开发、配置、测试、调试几个部分，将这个项目拆分开来。

## ▍ 开发环境

##

## 从 git 上拉到远程仓库，使用 uv 安装依赖：

```
git clone  hermes-agent && cd hermes-agentuv venv venv --python 3.11 && source venv/bin/activateuv pip install -e ".[all,dev]"hermes doctor  # 验证
```

▍ 架构概要

Hermes Agent 的核心是一个工具调用循环。整个流程如下：

```
用户输入消息
```

▍ 功能地图

核心的功能模块：

```
run_agent.py (AIAgent)          # 核心编排：对话循环、工具分发、会话管理
```

模块的依赖关系如下：

```
┌─────────────────────────────────────────────────────┐
```

快速定位：

|  |  |
| --- | --- |
| 想改什么 | 去哪里 |
| 核心对话循环 | `run_agent.py` → `AIAgent` |
| 系统提示词 | agent/prompt\_builder.py |
| 上下文压缩 | agent/context\_compressor.py |
| 工具注册机制 | tools/registry.py |
| 工具集分组 | toolsets.py  toolset\_distributions.py |
| 工具发现/分发 | model\_tools.py |
| 某个工具的实现 | tools/.py |
| 某个平台网关 | gateway/platforms/.py |
| 网关会话管理 | gateway/session.py |
| 技能解析 | agent/skill\_utils.py |
| 定时任务 | cron/scheduler.py  cron/jobs.py |

▍ 定制开发

1、添加工具

**Step 1** ：在 `tools/` 下创建文件：

```
# tools/my_tool.py
```

**Step 2** ：

```
在 model_tools.py 的 _discover_tools() 中添加
```

`Step 3（可选）： `

```
若创建了新工具集，在 toolsets.py 中注册：
```

``
``

2、添加消息平台

在 `gateway/platforms/` 下创建适配器，继承 `base.py` 中的抽象基类：

```
# gateway/platforms/my_platform.py
```

然后在 `gateway/config.py` 的 `Platform` 枚举中注册。

3、创建技能

技能放在 `~/.hermes/skills/<类别>/<技能名>/SKILL.md`：

```
---
```

技能会在 prompt 构建时被扫描索引，匹配后注入系统提示词。

参考：`agent/skill_utils.py`、`agent/prompt_builder.py` 中的 `build_skills_system_prompt()`。

4、MCP 工具集成

在 `~/.hermes/config.yaml` 中声明 MCP 服务器，工具会自动注册：

```
mcp:
```

5、终端执行后端

通过策略模式切换（`tools/environments/`），实现 `base.py` 的抽象基类即可添加新后端：

```
tools/environments/├── base.py            # 抽象基类├── local.py           # 本地 Shell├── docker.py          # Docker├── ssh.py             # SSH├── modal.py           # Modal├── daytona.py         # Daytona├── singularity.py     # Singularity└── persistent_shell.py
```

通过 `config.yaml` 中 `terminal.env_type` 切换。

▍ 配置

配置目录：`~/.hermes/`（可通过 `HERMES_HOME` 环境变量覆盖）

```
~/.hermes/├── config.yaml     # 主配置├── .env            # API 密钥├── skills/         # 技能├── memories/       # 记忆├── state.db        # 会话数据库├── cron/           # 定时任务└── profiles/       # 多配置隔离
```

关键配置项：

```
model:default:"anthropic/claude-sonnet-4-20250514"provider:"openrouter"# openrouter/anthropic/openai/custombase_url:null# 自定义端点terminal:env_type:"local"# local/docker/ssh/modal/daytona/singularitycompression:enabled:truethreshold:0.5# token 使用率阈值agent:max_turns:50system_prompt:null# 追加自定义提示词delegation:max_iterations:20default_toolsets: [terminal, file, web]toolsets:enabled: [web, terminal, file, skills, memory, cron, delegate]disabled: [browser, vision]skills:disabled: [social-media/xitter]external_dirs: [/path/to/custom/skills]memory:provider:"builtin"# builtin/mem0/honcho/...
```

▍ 测试

```
pytest tests/ -v                          # 全部
```

测试目录与源码对应：`tests/agent/`、`tests/gateway/`、`tests/hermes_cli/`、`tests/plugins/` 等。需要 API 的工具用 `unittest.mock` 模拟。

▍ 调试

```
HERMES_LOG_LEVEL=DEBUG hermes   # 详细日志HERMES_LOG_API=1 hermes         # 查看 API 请求
```

```
# 检查工具注册
```
