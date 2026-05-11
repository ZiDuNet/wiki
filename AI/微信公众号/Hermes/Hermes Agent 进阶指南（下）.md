> 📎 来源: [智客随笔](https://mp.weixin.qq.com/s?__biz=MjM5MjA2MDQxMg==&mid=2448720216&idx=1&sn=7c71c331554b720625cc0f1c2a6605d6&chksm=b32a6ffde58c965d8b780f0b46eec6d01c7da4314e57042e4077f887a5bfd44317944d83b741&mpshare=1&scene=1&srcid=0421jc0Gpu51zFuPKyrBZwZ1&sharer_shareinfo=cc7d8e7bc331bc6155abe11b8df5587c&sharer_shareinfo_first=cc7d8e7bc331bc6155abe11b8df5587c) | 时间: 2026-04-21 23:48

---

多 Agent 协作与生产化部署

> 接上篇。本篇涵盖：多 Agent 协作、生产化部署、高级扩展与疑难解答。

---

## 三、多 Agent 协作：让多个 Agent 一起干活

### 3.1 Sub-Agent 的 spawn 机制

Hermes 对子 Agent 并发做了保护性限制，实战中不建议一上来就把并发拉得太高。

对大多数在线模型场景，**更稳妥的起点仍然是 2~3 个子 Agent**，再根据额度、限流情况和结果质量逐步调整。

**专家建议：在实际使用中，并发数不建议超过 3 个。**

特别是当使用官方 API 时，建议从 2 个起步，以防止触发 API 平台的 Rate Limit 或被封禁 IP，从而影响正常任务的执行。在实战中，追求理论最大并发往往不如控制成本与上下文质量重要。

Hermes 支持主 Agent 通过 

```
delegate_task
```

 等方式派生子 Agent 执行拆分后的任务。

**基本用法（在对话中引导主 Agent）：**

> "这个任务可以并行处理： - 子任务 A：抓取 A 股今日涨停板数据 - 子任务 B：分析北向资金流向 - 子任务 C：生成市场情绪指数

> 请派生 3 个子 Agent 并行完成这三个子任务，然后汇总结果。"

### 3.2 子 Agent 的关键限制（必读）

**子 Agent 往往从一个新的会话上下文开始，它并不会天然继承主 Agent 的完整历史。**

因此，你必须在 

```
context
```

 字段中把子 Agent 所需的背景信息传完整：

```
delegate_task(  goal="修复 api/handlers.py 中的 TypeError",  context="""  文件路径：/home/user/myproject/api/handlers.py  错误信息：第 47 行 TypeError: 'NoneType' object has no attribute 'get'  原因：parse_body() 在 Content-Type 缺失时返回 None  项目使用 Python 3.11 + Flask  """)
```

**最重要的经验：不要假设子 Agent 知道"这个错误""刚才那个文件""上一步那个思路"是什么。**

### 3.3 Profiles：同一台机器运行多个独立 Hermes

Profile 是一个完全隔离的 Hermes 环境。每个 Profile 都有自己独立的配置、记忆、会话和技能。

**创建 Profile 的三种常见方式：**

```
# 方式一：全新 Profile（空白）hermes profile create mybot# 方式二：克隆配置（复用 API Key 和模型，但记忆和会话独立）hermes profile create work --clone# 方式三：完整克隆（包含记忆、会话、技能等更多状态）hermes profile create backup --clone-all
```

**运行多个独立 Agent：**

```
# 终端 1：运行编码助手coder chat# 终端 2：运行投研助手（独立的记忆和技能）research chat
```

每个 Profile 的 

```
memories/
```

、

```
skills/
```

、

```
sessions/
```

 和 

```
logs/
```

 目录通常都是独立的，不会互相读写。

### 3.4 主 Agent 协调多个子 Agent 的技巧

**明确角色分工，通常是最有效的方法。**

你可以在 SOUL.md 或 AGENTS.md 中定义：

```
## 多 Agent 协作规范- **Planner Agent**：负责任务分解和进度追踪，不直接执行- **Executor Agent**：负责具体的数据获取和处理，不做决策- **Reviewer Agent**：负责质量检查和结果验证，不做修改
```

### 3.5 多 Agent 资源分配与冲突避免

**Bot Token 冲突保护**

如果两个 Profile 意外使用了同一个 Bot Token，运行中的 Gateway 往往会产生冲突。因此，最好在各自的 

```
.env
```

 中配置不同的 Token。

**端口冲突**

如果你在本地运行多个 Hermes 实例，最好让它们使用不同端口：

```
# Profile AGATEWAY_PORT=8080# Profile BGATEWAY_PORT=8081
```

---

## 四、生产化部署：让 Hermes 稳定运行

### 4.1 Gateway 长期后台运行

**方式一：Systemd（Linux 生产环境首选）**

```
# 安装为 Systemd 服务hermes gateway install# 查看服务状态systemctl status hermes-gatewayjournalctl -u hermes-gateway -f
```

**方式二：Docker Compose（更适合多 Profile 部署）**

```
version: "3.8"services:  hermes-default:    image: nousresearch/hermes-agent:latest    container_name: hermes-default    restart: unless-stopped    command: gateway run    volumes:      - ~/.hermes:/opt/data  hermes-coder:    image: nousresearch/hermes-agent:latest    container_name: hermes-coder    restart: unless-stopped    command: gateway run    volumes:      - ~/.hermes/profiles/coder:/opt/data
```

**重要提醒：不要同时运行两个容器挂载同一个数据目录，否则共享状态文件可能出问题。**

### 4.2 定时任务、Heartbeat 与通知机制

**❗ 专家级警告：严禁盲目复制模板时区！**

Hermes 的 Cron 任务严格依赖服务器系统时区。配置前必须运行 

```
timedatectl
```

 确认。

- 国内服务器：应显示 

  ```
  Asia/Shanghai
  ```
- 海外服务器：若显示 UTC，请手动执行 

  ```
  sudo timedatectl set-timezone Asia/Shanghai
  ```

   修正，否则你的定时任务会在半夜"惊喜上线"

**Heartbeat 机制（防止静默失败）**

```
echo "GATEWAY_HEARTBEAT=true" >> ~/.hermes/.env
```

**定时任务（Cron）**

```
# 示例：工作日早上 8:30 生成日报hermes cron add "30 8 * * 1-5" "生成今日 A 股市场日报并发送到 Telegram"
```

创建任务后，最好先手动运行一次验证逻辑：

```
hermes cron listhermes cron run 任务名称
```

### 4.3 日志监控与调试方法

日志目录会跟随当前 profile 的 HERMES\_HOME 变化，默认 profile 下通常位于 

```
~/.hermes/logs/
```

。

当你需要向社区或官方反馈问题时，也可以考虑：

```
hermes debug share
```

### 4.4 Tirith 安全模块

Tirith 是 Hermes 的预执行安全扫描模块。

```
approvals:  mode: manual  # manual | smart | off
```

这三种模式可以直接这样理解：

| 模式 | 含义 |
| --- | --- |
| manual | 所有高风险命令都需要人工确认 |
| smart | 由辅助判断做一层风险分级，低风险场景会更顺滑一些 |
| off | 关闭安全检查，仅适合可信环境 |

### 4.5 多平台接入进阶配置

**Telegram 接入**

```
echo "TELEGRAM_BOT_TOKEN=your-bot-token" >> ~/.hermes/.envecho "TELEGRAM_ALLOWED_USERS=your-telegram-user-id" >> ~/.hermes/.env
```

**提醒：如果没有配置允许访问的用户范围，Bot 通常不会处于你预期的安全状态，因此上线前一定要做访问控制。**

### 4.6 生产化部署 Checklist

在将 Hermes 部署到生产环境之前，建议逐项检查：

- [ ] 

  ```
  hermes doctor
  ```

   无明显报错
- [ ] API Key 已配置在 

  ```
  .env
  ```

   文件中，而不是 

  ```
  config.yaml
  ```
- [ ] 已按需设置 

  ```
  GATEWAY_HEARTBEAT=true
  ```
- [ ] 已配置用户白名单（例如 

  ```
  TELEGRAM_ALLOWED_USERS
  ```

  ）
- [ ] 审批模式已根据需求设置（

  ```
  approvals.mode
  ```

  ）
- [ ] 已安装为 Systemd 服务，或容器设置了自动重启

---

## 五、高级扩展与调试

### 5.1 MCP 外部工具链集成实战

MCP（Model Context Protocol）允许你为 Hermes 接入外部工具，例如本地文件系统、数据库、自定义 API 等。

**实战：接入本地文件系统**

```
# 安装 MCP Filesystem Servernpm install -g @modelcontextprotocol/server-filesystem
```

在 

```
$HERMES_HOME/mcp.json
```

 中配置：

```
{  "mcpServers": {    "filesystem": {      "command": "npx",      "args": [        "-y",        "@modelcontextprotocol/server-filesystem",        "/home/ubuntu/projects",        "/home/ubuntu/data"      ]    }  }}
```

配置后，Agent 就更有机会直接通过 MCP 工具读写指定目录，而不必每次都依赖终端命令。

### 5.2 调试工具箱

| 命令 | 作用 |
| --- | --- |
| ``` hermes doctor ``` | 全面健康检查，优先运行 |
| ``` hermes memory status ``` | 检查记忆系统 |
| ``` hermes mcp status ``` | 检查 MCP 连接 |
| ``` hermes debug share ``` | 生成脱敏调试报告 |

---

## 六、疑难解答（Q&A）

### Q1：为什么我告诉了 Agent 一件事，它下次还是不记得？

**A：** 常见原因包括：会话太短，没有触发记忆整理；或者 Agent 认为这件事不值得长期保存。最直接的做法，是明确说 **"请把这件事写入你的长期记忆"**。

### Q2：Cron 定时任务没有按时触发怎么办？

**A：** 按以下顺序排查：

1. 运行 

   ```
   hermes cron list
   ```

   ，确认任务状态是否正常
2. 检查 Gateway 是否在后台运行
3. 运行 

   ```
   timedatectl
   ```

    检查服务器系统时区
4. 手动运行 

   ```
   hermes cron run 任务名
   ```

   ，确认任务逻辑本身没有问题

### Q3：Tirith 总是拦截我正常的 bash 命令，很烦怎么办？

**A：** 可以从三个方向处理：

- 临时切到更宽松的工作模式
- 调整 

  ```
  approvals.mode
  ```

  ，例如从 

  ```
  manual
  ```

   变成更灵活的策略
- 如果你的版本支持命令白名单，再把高频安全命令加入 

  ```
  allowlist
  ```

### Q4：多个 Profile 可以共享同一个 Telegram Bot 吗？

**A：** 通常不建议。多个运行中的 Gateway 最好使用独立 Token，避免冲突。

### Q5：日志文件太大了，怎么清理？

**A：** 先看你当前版本是否已经提供轮转或管理机制；如果没有，再手动清理旧日志文件，并在清理前确认重要问题已经留档。

### Q6：多个子 Agent 并发运行时，API 消耗急剧增长，怎么控制成本？

**A：** 四个办法最有效：

1. 不要一上来就开太多并发，先从 **2~3 个子任务** 试起
2. 让子任务尽量短、上下文尽量清晰，避免反复试错
3. 如果你的版本支持对子 Agent 单独设定模型或轮次上限，可以优先让子任务使用更便宜的模型，并控制最大轮次
4. 如果你在同一 provider 下配置了 Credential Pools，可以利用多 API Key 自动轮转来缓解 429 限流

### Q7：子 Agent 为什么总是说不知道任务背景？

**A：** 因为子 Agent 往往不是从主会话里"复制脑子"过去的，而是从新上下文开始。你必须在 

```
context
```

 字段中把它需要的文件路径、报错信息、项目结构、依赖版本等都明确写出来。

---

## 七、配置速查表

**路径提醒：** 下面的示例默认按默认 profile 编写；如果你正在使用命名 Profile，请把 

```
~/.hermes
```

 路径替换成当前 profile 的 HERMES\_HOME。

### 生产环境参考 config.yaml

```
agent:  max_turns: 90memory:  nudge_interval: 10  provider: mem0  # 或 holographic / honcho / supermemory 等approvals:  mode: smartterminal:  backend: docker  timeout: 60
```

### 生产环境参考 .env

```
# 核心 API KeyOPENAI_API_KEY=sk-xxxANTHROPIC_API_KEY=sk-ant-xxx# Gateway 配置GATEWAY_PORT=8080GATEWAY_HEARTBEAT=true# 平台接入与白名单TELEGRAM_BOT_TOKEN=123456:ABC-DEFTELEGRAM_ALLOWED_USERS=123456789,987654321# 外部记忆提供商（按需启用）MEM0_API_KEY=m0-xxx
```

**说明：** 

```
approvals.mode: smart
```

 在这里是面向生产使用的推荐策略示例，不代表它一定是官方默认值；如果你的环境更强调稳妥与审计，也可以继续使用 

```
manual
```

。

---

*如果你觉得这篇文章有用，欢迎**点赞、收藏、转发**，让更多人也学会！*

*有问题欢迎在评论区留言，看到会一一回复～*
