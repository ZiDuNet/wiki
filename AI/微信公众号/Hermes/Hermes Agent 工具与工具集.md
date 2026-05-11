> 📎 来源: [climbing.top](https://mp.weixin.qq.com/s?__biz=MzA5MTk1OTUxMQ==&mid=2649277478&idx=1&sn=8fb85014e2ef76aa0acf502207e976ce&chksm=8963ce386d0336c89eec73273e354f9ac96d26bd508368aef16100e1d47d177431381136fb62&mpshare=1&scene=1&srcid=0420CGtEmEUaHWz0YtjGA4Pq&sharer_shareinfo=9e494f87432b18910842db246364e6a2&sharer_shareinfo_first=9e494f87432b18910842db246364e6a2) | 时间: 2026-04-20 20:42

---

## Hermes Agent 工具与工具集

> 📖 本教程是 Hermes Agent 中文教程系列第 5 篇

### 目录

• [工具系统概述](#工具系统概述)

• [内置工具分类](#内置工具分类)

• [工具集（Toolsets）](#工具集toolsets)

• [终端后端详解](#终端后端详解)

• [后台进程管理](#后台进程管理)

• [Sudo 支持](#sudo-支持)

• [小结](#小结)

---

### 工具系统概述

Hermes Agent 拥有 40+ 个内置工具，按逻辑分组为"工具集（Toolsets）"，可以按平台启用或禁用。

工具是 Agent 与外界交互的桥梁——搜索网页、执行命令、操作文件、控制浏览器、管理定时任务等。

---

### 内置工具分类

| 类别 | 示例工具 | 说明 |

|------|---------|------|

| 🌐 **网络** | `web_search`, `web_extract` | 搜索网页和提取页面内容 |

| 💻 **终端 & 文件** | `terminal`, `process`, `read_file`, `patch` | 执行命令和操作文件 |

| 🌍 **浏览器** | `browser_navigate`, `browser_snapshot`, `browser_vision` | 浏览器自动化（文本和视觉） |

| 🎨 **媒体** | `vision_analyze`, `image_generate`, `text_to_speech` | 多模态分析和生成 |

| 🧩 **编排** | `todo`, `clarify`, `execute_code`, `delegate_task` | 规划、澄清、代码执行、子代理委派 |

| 🧠 **记忆** | `memory`, `session_search` | 持久记忆和会话搜索 |

| ⏰ **自动化** | `cronjob`, `send_message` | 定时任务和消息投递 |

| 🔌 **集成** | `ha_*`, MCP 服务器工具, `rl_*` | Home Assistant、MCP、RL 训练 |

#### 查看所有可用工具

```
hermes tools
```

这个命令会列出当前可用的所有工具及其状态。

---

### 工具集（Toolsets）

工具集是工具的逻辑分组，可以按需启用/禁用。

#### 常用工具集

| 工具集 | 包含工具 |

|--------|---------|

| `web` | web\_search, web\_extract |

| `terminal` | terminal, process |

| `file` | read\_file, patch |

| `browser` | 浏览器自动化工具 |

| `vision` | 图像分析工具 |

| `image_gen` | 图像生成工具 |

| `tts` | 文字转语音 |

| `memory` | 持久记忆 |

| `session_search` | 会话搜索 |

| `cronjob` | 定时任务 |

| `code_execution` | 代码执行 |

| `delegation` | 子代理委派 |

| `skills` | 技能管理 |

| `todo` | 任务规划 |

| `clarify` | 澄清问题 |

| `homeassistant` | Home Assistant |

#### 启动时指定工具集

```
# 仅使用 web 和 terminal 工具
hermes chat --toolsets "web,terminal"

# 使用所有工具（默认）
hermes chat
```

#### 按平台配置工具集

```
hermes tools   # 交互式配置
```

在交互界面中，你可以为每个消息平台（CLI、Telegram、Discord 等）单独配置启用的工具集。

#### 配置文件方式

```
# ~/.hermes/config.yaml
toolsets:
  cli:
    - web
    - terminal
    - file
    - browser
    - memory
    - session_search
  telegram:
    - web
    - terminal
    - memory
    - cronjob
  discord:
    - web
    - terminal
    - image_gen
```

---

### 终端后端详解

终端工具是 Hermes 最核心的工具之一——它决定了 Agent 的 shell 命令在哪里执行。

#### 六种后端

| 后端 | 运行位置 | 隔离级别 | 适用场景 |

|------|---------|---------|---------|

| **local** | 你的机器 | 无 | 开发、个人使用 |

| **docker** | Docker 容器 | 完全（namespace + cap-drop） | 安全沙箱、CI/CD |

| **ssh** | 远程服务器 | 网络隔离 | 远程开发、强大硬件 |

| **modal** | Modal 云沙箱 | 完全（云 VM） | 无服务器、评估 |

| **daytona** | Daytona 工作空间 | 完全（云容器） | 托管云开发环境 |

| **singularity** | Apptainer 容器 | 命名空间 | HPC 集群、共享机器 |

#### Local 后端（默认）

```
terminal:
  backend: local
```

命令直接在你的机器上运行，无隔离。

> ⚠️ Agent 拥有和你用户账号相同的文件系统访问权限。如需安全沙箱，切换到 Docker。

#### Docker 后端

```
terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  docker_mount_cwd_to_workspace: false
  docker_forward_env:
    - "GITHUB_TOKEN"
  docker_volumes:
    - "/home/user/projects:/workspace/projects"
    - "/home/user/data:/data:ro"
  container_cpu: 1          # CPU 核心数
  container_memory: 5120    # 内存（MB）
  container_disk: 51200     # 磁盘（MB）
  container_persistent: true # 跨会话持久化
```

**安全加固特性**：

• `--cap-drop ALL`，仅保留 DAC\_OVERRIDE、CHOWN、FOWNER

• `--security-opt no-new-privileges`

• `--pids-limit 256`（进程数限制）

• 大小受限的 tmpfs（/tmp 512MB、/var/tmp 256MB、/run 64MB）

• 完整的命名空间隔离

#### SSH 后端

```
terminal:
  backend: ssh
  persistent_shell: true  # 保持长运行的 bash 会话
```

在 `~/.hermes/.env` 中设置：

```
TERMINAL_SSH_HOST=my-server.example.com
TERMINAL_SSH_USER=ubuntu
TERMINAL_SSH_KEY=~/.ssh/id_rsa     # 可选
TERMINAL_SSH_PORT=22                # 可选，默认 22
```

SSH 后端特别推荐用于安全场景——Agent 无法修改自己的代码。

#### Modal 后端（无服务器）

```
# 安装 Modal
uv pip install modal
modal setup

# 配置
hermes config set terminal.backend modal
```

```
terminal:
  backend: modal
  container_cpu: 1
  container_memory: 5120
  container_disk: 51200
  container_persistent: true  # 快照/恢复文件系统
```

Modal 提供无服务器持久化——空闲时环境休眠，按需唤醒，几乎不花钱。

#### Daytona 后端

```
terminal:
  backend: daytona
  container_cpu: 1
  container_memory: 5120
  container_disk: 10240    # 最大 10 GiB
  container_persistent: true # 停止/恢复（而非删除）
```

需要设置 `DAYTONA_API_KEY` 环境变量。

#### Singularity/Apptainer 后端

```
# 预构建 SIF（用于并行 Worker）
apptainer build ~/python.sif docker://python:3.11-slim

# 配置
hermes config set terminal.backend singularity
hermes config set terminal.singularity_image ~/python.sif
```

```
terminal:
  backend: singularity
  singularity_image: "docker://nikolaik/python-nodejs:python3.11-nodejs20"
  container_persistent: true  # 可写覆盖层跨会话持久化
```

使用 `--containall --no-home` 实现完全命名空间隔离。适用于 HPC 集群（共享机器上 Docker 不可用的场景）。

---

### 后台进程管理

#### 启动后台进程

```
terminal(command="pytest -v tests/", background=True)
# 返回: {"session_id": "proc_abc123", "pid": 12345}
```

#### 管理后台进程

```
process(action="list")                          # 列出所有运行中的进程
process(action="poll", session_id="proc_abc123")  # 检查状态
process(action="wait", session_id="proc_abc123")  # 阻塞等待完成
process(action="log", session_id="proc_abc123")   # 查看完整输出
process(action="kill", session_id="proc_abc123")   # 终止进程
process(action="write", session_id="proc_abc123", data="y")  # 发送输入
```

#### PTY 模式

`pty=true` 启用交互式 CLI 工具（如 Codex、Claude Code）：

```
terminal(command="python manage.py shell", pty=True)
```

---

### Sudo 支持

如果命令需要 sudo 权限，Hermes 会提示你输入密码（会话内缓存）。或者在 `~/.hermes/.env` 中设置：

```
SUDO_PASSWORD=your-password
```

> ⚠️ 在消息平台上，如果 sudo 失败，输出会提示你将 `SUDO_PASSWORD` 添加到 `~/.hermes/.env`。

---

### 小结

Hermes 的工具系统分为 8 大类、40+ 个工具，通过工具集机制可按平台灵活启用/禁用。六种终端后本从本地到云端全覆盖，后台进程管理让 Agent 可以并行处理多个任务。

📖 **下一篇**：[06-技能系统](06-技能系统.md)

---

> 📚 官方文档：https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
