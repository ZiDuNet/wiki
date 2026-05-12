> 📎 来源: [猿码](https://mp.weixin.qq.com/s?__biz=MzU5MjgxNjAwMQ==&mid=2247488460&idx=1&sn=530e2eb14348864e4e1737f7ad7bc723&chksm=ff8662dddd2765408bbb76c8ef6b4cf94f829601a301fbcd5886ac6408f075051c0aece002f9&mpshare=1&scene=1&srcid=04271M3o8nUIoHtPYlNwOByu&sharer_shareinfo=0dae8f6f71acf7074596358e7c91b2ce&sharer_shareinfo_first=0dae8f6f71acf7074596358e7c91b2ce) | 时间: 2026-04-27 21:13

---

# Hermes 配置项：一张表让你搞懂每个参数怎么配

> 从 OpenClaw 迁移 Hermes 后，配置要不要重新折腾？答案是：大部分不用管。本文把每一个配置项掰开讲——是什么、默认值是什么、什么时候需要改、怎么改。

---

## 一、先说清楚一件事：迁移后需要操心配置吗？

先给结论：**不需要逐个设置，开箱即用。**

从 OpenClaw 迁移到 Hermes 后，安装程序会问你是否复用已有配置。如果选"是"，你的模型 API、飞书/微信等渠道配置都会直接带过来，基本不用动。

但有 **5 大类配置**，建议知道它们的存在——不是为了改，而是为了有一天需要的时候知道去哪里找。

---

## 二、配置文件在哪里

Hermes 的配置分布在两个文件里：

| 文件 | 路径 | 存放内容 |
| --- | --- | --- |
| 主配置 | `~/.hermes/config.yaml` | 所有配置项（YAML 格式） |
| 环境变量 | `~/.hermes/.env` | API Key 等敏感信息 |

**三个常用命令：**

```
hermes config       # 查看当前配置hermes config edit # 编辑配置文件（打开编辑器）hermes doctor       # 诊断配置问题（出问题时先跑这个）
```

---

## 三、所有配置项逐个讲

### 3.1 四大核心配置

这四个配置决定 Hermes 用什么模型、在哪些渠道工作。**迁移过来后通常不用改**。

#### model —— 主模型名称

```
model: MiniMax-M2.7
```

指定 Hermes 对话使用的大模型。可以是模型名称字符串，也可以是一个完整对象：

```
model:  name: MiniMax-M2.7  provider: minimax  base_url: https://api.minimaxi.com/anthropic
```

**怎么配：**

- 交互式：`hermes model` 按向导选择
- 直接改：`hermes config set model "anthropic/claude-sonnet-4"`

---

#### model.provider —— 模型服务商

```
model:  provider: minimax
```

指定模型服务商名称。国内常用：`minimax`（MiniMax）、`kimi`（月之暗面）、`openrouter`（海外）。迁移后通常自动继承。

---

#### providers —— 各 provider 的 API Key 引用

```
providers: {}
```

这个字段通常为空，因为 Key 不写在这里——Key 在 `~/.hermes/.env` 文件里。config.yaml 通过**环境变量名**引用 Key。

例如 `.env` 文件里写：

```
MINIMAX_API_KEY=your-key-here
```

config.yaml 里写：

```
model:  provider: minimax
```

Hermes 会自动从环境变量找 Key。**不需要在 config.yaml 里写死 Key**。

---

#### toolsets —— 启用的工具集

```
toolsets:  - hermes-cli
```

决定 Hermes 有哪些工具可用。CLI 模式下默认只有 `hermes-cli`（基本对话），如果需要其他能力要手动开启。

**可用工具集：**

| 工具集 | 包含的能力 |
| --- | --- |
| `web` | 网页搜索、内容抓取 |
| `terminal` | 执行 shell 命令 |
| `file` | 读写文件、搜索文件内容 |
| `browser` | 浏览器自动化控制 |
| `vision` | 图片分析 |
| `image_gen` | 图片生成 |
| `skills` | 技能管理 |
| `tts` | 语音合成 |
| `todo` | 任务管理 |
| `memory` | 记忆管理 |
| `session_search` | 会话历史搜索 |
| `cronjob` | 定时任务 |
| `code_execution` | 代码执行（execute\_code 工具） |
| `delegation` | 启动子 Agent |
| `homeassistant` | 智能家居控制 |

**怎么配：**

```
# 开启多个工具集hermes chat --toolsets "web,terminal,file"
```

或在 config.yaml 里写：

```
toolsets:  - hermes-cli  - web  - terminal  - file
```

---

### 3.2 Agent 行为配置

控制 Hermes 作为 Agent 的核心行为参数。

#### agent.max\_turns —— 最大对话轮次

```
agent:  max_turns: 90
```

单次对话中，Hermes 能调用工具的**最大次数**。90 是很宽松的限制，大多数任务用不到这么多。如果达到上限会自动结束对话并返回当前结果。

**什么时候改：** 复杂的多步骤任务可能需要更多轮次，适当调大。

---

#### agent.gateway\_timeout —— 网关模式无响应超时

```
agent:  gateway_timeout: 1800
```

单位是秒，1800 = 30 分钟。这个配置只在**网关模式**（接飞书、微信等）下生效。控制 Hermes 跑长任务时，多久没动静才判定为超时。

**什么时候改：** 跑需要长时间执行的任务（如批量数据处理）可以调大。

---

#### agent.tool\_use\_enforcement —— 是否强制调用工具

```
agent:  tool_use_enforcement: auto
```

- `auto`：自动判断，GPT/Codex 等模型默认开启
- `true`：强制要求模型调用工具
- `false`：关闭强制

**什么时候改：** 有些模型（如某些开源模型）会"假装在思考"但不真正调用工具，这时可以手动开 `true`。

---

#### agent.verbose —— 详细日志

```
agent:  verbose: false
```

`true` 时 Hermes 会输出更详细的执行日志，包括每轮对话的完整输入输出。

**什么时候改：** 调试特定问题、想看 Hermes 到底在干什么时开。

---

#### agent.reasoning\_effort —— 模型推理深度

```
agent:  reasoning_effort: medium
```

可选：`xhigh` / `high` / `medium` / `low` / `minimal` / `none`。控制模型的推理投入程度——越高越慢越贵，但推理质量通常更好。

**什么时候改：** 简单问答用 `low`，复杂推理任务用 `high` 或 `xhigh`。

---

### 3.3 终端执行配置（terminal）

控制 Hermes 执行 shell 命令的方式和环境。

#### terminal.backend —— 命令执行后端

```
terminal:  backend: local
```

| 值 | 含义 | 适用场景 |
| --- | --- | --- |
| `local` | 在本地执行（默认） | 开发、可信任务 |
| `docker` | 在 Docker 容器里执行 | 隔离、安全 |
| `ssh` | 连接到远程服务器执行 | 沙盒、远程开发 |
| `modal` | 云端无服务器执行 | 弹性扩展 |
| `daytona` | 云沙盒工作区 | 持久远程开发 |

**什么时候改：** 大多数本地用户用 `local` 就够了。需要隔离时换 `docker`。

---

#### terminal.timeout —— 命令超时时间

```
terminal:  timeout: 180
```

单位秒。单个 shell 命令超过这个时间会被强制终止。

**什么时候改：** 跑编译型项目（Gradle/Maven 构建）可以适当调大到 300-600 秒。

---

#### terminal.cwd —— 默认工作目录

```
terminal:  cwd: "."
```

`.` 代表启动 Hermes 时的当前目录。也可指定绝对路径如 `~/projects`。

---

#### terminal.persistent\_shell —— 保持 Shell 状态

```
terminal:  persistent_shell: true
```

开启后，多次命令间能保持同一个 shell 进程——环境变量、shell 变量、工作目录都会保留。关闭则每次命令都是全新的 shell。

**建议：** 保持开启，大多数场景更符合直觉。

---

### 3.4 记忆与上下文配置

这是 Hermes 区别于 OpenClaw 的核心能力区。

#### memory.memory\_enabled —— 开启长期记忆

```
memory:  memory_enabled: true
```

开启后，Hermes 会把学到的知识和技能写入 `~/.hermes/MEMORY.md`，跨会话持久化。**建议保持开启**，这是 Hermes"越用越聪明"的基础。

---

#### memory.user\_profile\_enabled —— 构建用户画像

```
memory:  user_profile_enabled: true
```

开启后，Hermes 会把对你的了解（偏好、习惯、工作内容）写入 `~/.hermes/USER.md`。**建议保持开启**，让 Agent 更快理解你。

---

#### memory.memory\_char\_limit —— 记忆文件最大字符数

```
memory:  memory_char_limit: 2200
```

单个记忆文件的字符上限，约等于 800 个 token。超过后旧的记忆会被压缩。

**什么时候改：** 使用高上下文窗口模型时可以适当调大。

---

#### compression.enabled —— 上下文压缩

```
compression:  enabled: true
```

当对话上下文快满时（达到 threshold 设置的比例），Hermes 自动压缩旧消息，保留近期对话和关键记忆。

**建议：** 保持开启，能显著节省 token 消耗。

---

#### compression.threshold —— 触发压缩的上下文比例

```
compression:  threshold: 0.50
```

上下文用到 50% 时开始触发压缩。可以调低（如 0.30）更早压缩，或调高（如 0.70）更晚压缩。

---

#### context.engine —— 上下文管理引擎

```
context:  engine: compressor
```

可选：`compressor`（内置压缩，默认）或插件名称（如 `lcm` 代表 Lossless Context Management 插件）。

**什么时候改:** 安装了第三方上下文管理插件时才需要改。

---

### 3.5 安全与审批配置

#### approvals.mode —— 危险命令审批模式

```
approvals:  mode: manual
```

| 值 | 行为 |
| --- | --- |
| `manual` | 每次执行危险命令前询问（默认） |
| `smart` | 用 AI 判断低风险直接过，高风险才问 |
| `off` | 直接执行，不问（危险！） |

**什么时候改:** 定时任务（cron）里 `off` 比较方便，但 CLI 对话建议保持 `manual`。

---

#### approvals.timeout —— 审批超时时间

```
approvals:  timeout: 60
```

审批等待秒数。超时后自动拒绝执行。

---

#### security.tirith\_enabled —— 开启安全扫描

```
security:  tirith_enabled: true
```

开启命令预执行安全扫描，检测潜在危险操作。**建议保持开启**。

---

#### security.redact\_secrets —— 日志中隐藏敏感信息

```
security:  redact_secrets: true
```

开启后，日志里的 API Key、Token 等敏感信息会被打码。**建议保持开启**。

---

### 3.6 文件读取与工具输出限制

防止 Hermes 读取或输出超大内容，避免上下文爆炸。

#### file\_read\_max\_chars —— 单次文件读取最大字符

```
file_read_max_chars: 100000
```

默认 10 万字符。超过这个大小的文件读取会报错，提示你用 `offset` + `limit` 参数分批读取。

---

#### tool\_output.max\_bytes —— 终端输出截断字节

```
tool_output:  max_bytes: 50000
```

终端命令输出超过 5 万字符时，只保留头部 + 尾部各一部分，中间截断。这是为了避免超长输出撑爆上下文窗口。

---

#### tool\_output.max\_lines —— read\_file 单次最大行数

```
tool_output:  max_lines: 2000
```

单次 `read_file` 调用最多返回 2000 行。超过需要用 offset+limit 分批读取。

---

### 3.7 显示与人机交互配置

#### display.personality —— Agent 人格

```
display:  personality: kawaii
```

内置人格：`kawaii`（可爱风）、`helpful`（专业助手）、`pirate`（海盗风）。也可以自己定义。

```
personalities:  mybot: "你是一个严谨的技术专家，用词精准，不说废话。"
```

---

#### display.busy\_input\_mode —— Agent 工作时按 Enter 的行为

```
display:  busy_input_mode: interrupt
```

| 值 | 行为 |
| --- | --- |
| `interrupt` | 按 Enter 打断当前任务（默认） |
| `queue` | Enter 把消息加入队列，等当前任务完成后处理 |

---

#### display.streaming —— 流式输出

```
display:  streaming: false
```

`true` 时 AI 回复逐字显示，更实时。`false` 时等完整回复再显示。

---

#### display.show\_reasoning —— 显示推理过程

```
display:  show_reasoning: false
```

`true` 时在回复中显示模型的思考推理过程。调试或学习 AI 推理逻辑时有用。

---

### 3.8 平台接入配置（飞书/微信/Discord 等）

这部分配置控制 Hermes 接入各个消息平台的能力。

#### 飞书配置

```
gateways:  feishu:    app_id: "cli_xxxxx"    app_secret: "${FEISHU_APP_SECRET}"    require_mention: true
```

| 配置项 | 含义 |
| --- | --- |
| `app_id` | 飞书应用 App ID |
| `app_secret` | 飞书应用 App Secret（放 .env） |
| `require_mention` | 群聊是否需要 @ Hermes 才响应 |

---

#### Discord 配置

```
discord:  require_mention: true  auto_thread: true  reactions: true
```

| 配置项 | 含义 |
| --- | --- |
| `require_mention` | 是否需要 @ 机器人 |
| `auto_thread` | 在频道里自动创建线程 |
| `reactions` | 处理消息时显示表情反应 |

---

#### Telegram 配置

```
telegram:  channel_prompts: {}
```

`channel_prompts` 支持为不同会话设置独立的系统提示词。

---

### 3.9 语音配置（TTS / STT）

#### tts.provider —— 语音合成引擎

```
tts:  provider: edge
```

| 值 | 说明 |
| --- | --- |
| `edge` | Microsoft Edge 免费 TTS（默认） |
| `elevenlabs` | ElevenLabs 付费高品质 |
| `openai` | OpenAI TTS |
| `xai` | xAI TTS |
| `minimax` | MiniMax TTS |

---

#### stt.provider —— 语音识别引擎

```
stt:  provider: local
```

| 值 | 说明 |
| --- | --- |
| `local` | 本地 Whisper（免费，需要下载模型） |
| `openai` | OpenAI Whisper API |
| `groq` | Groq 托管 Whisper（便宜快速） |

---

### 3.10 定时任务与日志配置

#### cron.wrap\_response —— cron 结果加包裹

```
cron:  wrap_response: true
```

`true` 时定时任务结果会加上"这是定时任务输出"的提示语。`false` 输出纯净内容，方便程序解析。

---

#### logging.level —— 日志级别

```
logging:  level: INFO
```

可选：`DEBUG` / `INFO` / `WARNING`。级别越低记录越详细。

---

#### sessions.auto\_prune —— 自动清理旧会话

```
sessions:  auto_prune: false  retention_days: 90
```

`true` 时定期自动删除 90 天前的已结束会话记录。**建议开启**，避免 `state.db` 无限膨胀（重用户能涨到几百 MB）。

---

### 3.11 子 Agent 委派配置（delegation）

当 Hermes 需要并行处理多个子任务时，可以用 delegation 启动子 Agent。

#### delegation.model —— 子 Agent 使用什么模型

```
delegation:  model: ""
```

空值 = 继承父 Agent 的模型。也可以指定更便宜更快的模型专门跑子任务。

---

#### delegation.max\_concurrent\_children —— 最大并行子 Agent 数

```
delegation:  max_concurrent_children: 3
```

最多同时启动几个子 Agent。

---

#### delegation.subagent\_auto\_approve —— 子 Agent 危险命令自动审批

```
delegation:  subagent_auto_approve: false
```

**⚠️ 安全警告：**`true` 时子 Agent 可以直接执行危险命令而不需要你确认。仅在你完全信任子 Agent 工作内容时开启（如纯数据处理流水线）。

---

### 3.12 其他配置

#### checkpoints —— 危险操作前自动快照

```
checkpoints:  enabled: true  max_snapshots: 50
```

开启后，首次写文件操作会自动对当前目录打快照。可以用 `/rollback` 命令回滚。**建议保持开启**。

---

#### quick\_commands —— 快捷命令

```
quick_commands:  status:    type:exec    command:systemctlstatushermes-agentgpu:    type:exec    command:nvidia-smi--query-gpu=utilization.gpu,memory.used--format=csv,noheader
```

定义后 `/status` 和 `/gpu` 直接执行对应命令，不需要过 AI 推理。

---

#### timezone —— 时区

```
timezone: ""
```

空值 = 服务器本地时间。也可指定 IANA 时区如 `Asia/Shanghai`。

---

#### code\_execution.mode —— 代码执行模式

```
code_execution:  mode: project
```

| 值 | 含义 |
| --- | --- |
| `project` | 在项目目录执行，能访问项目依赖（默认） |
| `strict` | 隔离环境，只用 Hermes 自带的 Python，无项目依赖 |

---

## 四、配置项关系图

理解配置之间的依赖关系：

```
┌─────────────────────────────────────────────┐│           model + providers                ││         决定用哪个模型、服务商               │└─────────────────┬───────────────────────────┘                  ↓┌─────────────────────────────────────────────┐│              toolsets                       ││         决定有哪些工具可用                   │└─────────────────┬───────────────────────────┘                  ↓┌─────────────────────────────────────────────┐│          terminal.backend                   ││         决定命令在哪里执行                  │└─────────────────┬───────────────────────────┘                  ↓┌─────────────────────────────────────────────┐│       memory + compression                  ││         决定上下文怎么管理                  │└─────────────────┬───────────────────────────┘                  ↓┌─────────────────────────────────────────────┐│        approvals + security                 ││            决定安全边界                     │└─────────────────────────────────────────────┘
```

---

## 五、从 OpenClaw 迁移后的配置差异

| 差异点 | OpenClaw | Hermes |
| --- | --- | --- |
| 配置目录 | `~/.openclaw/` | `~/.hermes/` |
| Skills 目录 | `~/.openclaw/skills/` | `~/.hermes/skills/` |
| 记忆系统 | 无 | 有独立的 `memory.*` 配置 |
| 推理深度 | 无 | 有 `agent.reasoning_effort` |
| 上下文压缩 | 无 | 有 `compression.*` |
| 快照回滚 | 无 | 有 `checkpoints.*` |

---

## 六、配置常见问题

### Q: 改了配置不生效？

```
hermes doctor
```

先跑诊断命令，90% 的配置问题它能直接告诉你原因。

### Q: Hermes 跑着跑着变慢了？

很可能是 `state.db` 太大。开启自动清理：

```
sessions:  auto_prune: true  retention_days: 90
```

或者手动清理：

```
hermes sessions prune
```

### Q: 命令执行报权限错误？

检查 `approvals.mode` 是否为 `manual`，以及当前用户是否有目标目录的读写权限。

### Q: 飞书/微信接入失败？

1. 确认 `app_id` / `app_secret` 填写正确
2. 确认平台后台已配置好 WebSocket 模式
3. 重启网关：`hermes gateway restart`

---

## 总结

Hermes 的配置项虽多，但大多数有合理的默认值，**迁移后直接能用，不需要逐个设置**。

本文的目的不是让你全部记住，而是让你知道：**当有一天需要的时候，知道去哪里找、怎么改**。

需要重点关注的几项：

- `model` / `provider` —— 确认模型配置正确
- `toolsets` —— 需要什么工具自己开
- `memory.enabled` —— 保持开启，Hermes 的核心能力
- `approvals.mode` —— 安全相关，保持 `manual`
- `sessions.auto_prune` —— 建议开启，避免数据库膨胀

> 有问题，先跑 `hermes doctor`。大多数配置问题它能直接告诉你答案。

---

> 欢迎一起学习交流，添加小助手 ysf99918，备注【hermes】。与志同道合的人一起学习，这里总有你答案。

**相关资源：**

- Hermes GitHub：NousResearch/hermes-agent[1]
- 安装脚本：`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

### 引用链接

[1]NousResearch/hermes-agent: *https://github.com/NousResearch/hermes-agent*
