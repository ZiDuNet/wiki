> 📎 来源: [RowanFYI](https://mp.weixin.qq.com/s?__biz=MzI0NTUyNTM1OQ==&mid=2247485611&idx=1&sn=5e0105f5eb130e001d7cc7c94be40177&chksm=e894713435dfb6d54263a5b04a0b4698e0cff03343c5d13f15b5d6efbcb8112d2a94cda6b56f&mpshare=1&scene=1&srcid=0421kTkr11a97ZXTLFp2PG5x&sharer_shareinfo=4ca9a228a1f1e75a366655763742071d&sharer_shareinfo_first=4ca9a228a1f1e75a366655763742071d) | 时间: 2026-04-21 21:03

---

> 很多人用了 Hermes 一段时间后，最大的抱怨就是："它根本记不住东西"。这通常不是 Bug，而是没有搞清楚它的记忆机制。

---

## 写在前面

本指南默认你已完成 Hermes 的基础安装与配置。我们将直接进入进阶核心内容：

- 🧠 记忆系统
- 🔄 技能自进化
- 🤖 多 Agent 协作
- 🚀 生产化部署
- 🔧 高级调试

---

## 一、记忆系统进阶

### 1.1 为什么它"不记得"？

Hermes 的记忆系统是 \*\*Agent-curated（策展）\*\*的，不是全量记录的。

**核心原因：**

| 原因 | 说明 |
| --- | --- |
| 节省 Token | 如果每轮对话都实时更新记忆，System Prompt 头部会频繁变化，导致无法利用 KV Cache，推理成本大幅增加 |
| 防止记忆污染 | Agent 思考中的"碎碎念"、临时试错、中间结果，不值得长期保留 |

**简单来说：** 实时写入会贵且乱，策展 + 周期性 nudge 是性能与质量的平衡点。

### 1.2 记忆何时会被保留？

Agent 不会把你说的每一句话都写进记忆。通常在以下场景更容易被保留：

✅ 你明确表达了偏好："我喜欢/不喜欢 xxx"
✅ 发现了环境事实："这台机器装了 xxx"
✅ 纠正了 Agent 的错误做法："不要用 sudo，我在 docker 组里"
✅ 完成了一个重要任务里程碑
✅ 你明确要求它记住某件事

**💡 最佳实践：**

```
记住我的偏好：所有代码统一使用 Python 3.11，不要用 3.12 或 3.13。
```

这样更容易让 Agent 把这类信息视为值得长期保留的内容。

### 1.3 核心记忆文件使用方法

| 文件 | 位置 | 用途 | 维护者 |
| --- | --- | --- | --- |
| MEMORY.md | ``` ~/.hermes/memories/ ``` | Agent 的工作笔记、环境事实 | Agent |
| USER.md | ``` ~/.hermes/memories/ ``` | 用户画像、偏好、沟通风格 | Agent |
| SOUL.md | ``` ~/.hermes/ ``` | Agent 的人格、行为准则、固定规则 | 用户 |
| AGENTS.md | 项目根目录 | 项目级行为规范和执行约束 | 用户 |

**⚠️ 铁律：** 不要把应该写在 SOUL.md 里的东西放进 MEMORY.md。

MEMORY.md 会被整理、压缩，甚至替换掉过时内容。你的固定规则应该放在 SOUL.md。

### 1.4 调整记忆频率

打开

```
~/.hermes/config.yaml
```

：

```
memory:
  nudge_interval: 5
```

**推荐值参考：**

| 场景 | 推荐值 |
| --- | --- |
| 小模型、小上下文 | 3~5 |
| 标准模型 | 5~10 |
| 大上下文模型 | 10~15 |

**说明：** 数值越小，Agent 越频繁地进行记忆反思，写入内容更多，但 token 消耗也增加。

### 1.5 跨会话记忆保持方法

**方法一：手动插入 Checkpoint（最简单有效）**

```
当前进度总结：我们已经完成了数据清洗和特征工程，下一步是训练模型。
请把这个进度写入你的记忆，确保后续不会忘记。
```

**方法二：用外部文件作为"任务状态文件"**

```
请在项目目录下创建 TASK_STATUS.md，记录当前任务的完整状态。
每次我们恢复工作时，先读取这个文件。
```

---

## 二、技能自进化

### 2.1 核心机制

**一句话总结：** 记忆解决"记得住"，技能解决"用得高效且可复用"。

Hermes 的技能自生成机制，是把记忆中的重复经验沉淀为**可复用的结构化 Skill**。

| 维度 | 记忆 | 技能 |
| --- | --- | --- |
| 形式 | 事实和经验的记录，相对散乱 | 触发条件 + 操作步骤 + 注意事项 |
| 特点 | 私有的、碎片化的 | 可共享、可积累的"程序性知识" |
| 目的 | 记录"是什么" | 标准化 SOP，降低重复推理负担 |

### 2.2 自动创建 Skill 的触发条件

1. 完成了一个相对复杂的任务
2. 遇到了错误或死路，后来找到了正确路径
3. 用户纠正了它的做法
4. 发现了一个值得复用的非平凡工作流

**💡 主动引导：**

```
我们刚才完成的这个数据处理流程很有价值，请把它保存为一个 Skill，
名字叫 data-pipeline，放在 devops 分类下，
确保包含触发条件、操作步骤、注意事项和验证方法。
```

### 2.3 技能质量标准

判断一个 Skill 质量好不好：

✅ 触发条件清晰：Agent 能准确判断什么时候该用它
✅ 步骤可执行：每一步都有明确操作，而不是空泛描述
✅ 有验证方法：执行完后能判断是否成功
✅ 有注意事项：记录了踩过的坑

---

## 三、多 Agent 协作

### 3.1 Sub-Agent 使用建议

**⚠️ 专家建议：** 并发数不建议超过 3 个。

特别是使用官方 API 时，建议从 2 个起步，防止触发 Rate Limit。

**基本用法：**

```
这个任务可以并行处理：
1. 子任务 A：抓取 A 股今日涨停板数据
2. 子任务 B：分析北向资金流向
3. 子任务 C：生成市场情绪指数

请派生 3 个子 Agent 并行完成这三个子任务，然后汇总结果。
```

### 3.2 子 Agent 的关键限制（必读）

**子 Agent 不会继承主 Agent 的完整历史！**

你必须在 context 里把背景信息传完整：

```
delegate_task(
    goal="修复 api/handlers.py 中的 TypeError",
    context="""
    文件路径：/home/user/myproject/api/handlers.py
    错误信息：第 47 行 TypeError: 'NoneType' object has no attribute 'get'
    原因：parse_body() 在 Content-Type 缺失时返回 None
    项目使用 Python 3.11 + Flask
    """
)
```

**最重要的经验：** 不要假设子 Agent 知道"这个错误""刚才那个文件"是什么。

### 3.3 Profiles 功能实战

Profile 是一个完全隔离的 Hermes 环境。

**创建方式：**

```
# 方式一：全新 Profile（空白）
hermes profile create mybot

# 方式二：克隆配置（复用 API Key 和模型，但记忆和会话独立）
hermes profile create work --clone

# 方式三：完整克隆（包含记忆、会话、技能等更多状态）
hermes profile create backup --clone-all
```

**运行多个独立 Agent：**

```
# 终端 1：运行编码助手
coder chat

# 终端 2：运行投研助手（独立的记忆和技能）
research chat
```

---

## 四、生产化部署

### 4.1 Gateway 长期后台运行

**方式一：Systemd（Linux 生产环境首选）**

```
# 安装为 Systemd 服务
hermes gateway install

# 查看服务状态
systemctl status hermes-gateway
journalctl -u hermes-gateway -f
```

**方式二：Docker Compose**

```
version: "3.8"
services:
  hermes-default:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-default
    restart: unless-stopped
    command: gateway run
    volumes:
      - ~/.hermes:/opt/data
```

### 4.2 ⚠️ 时区警告（最容易踩的坑）

**Hermes 的 Cron 任务严格依赖服务器系统时区！**

```
# 先确认服务器系统时区
timedatectl

# 如果时区不对，修正为上海时间
sudo timedatectl set-timezone Asia/Shanghai
```

国内服务器应显示

```
Asia/Shanghai
```

。若显示

```
UTC
```

，你的定时任务会在半夜"惊喜上线"。

### 4.3 生产化部署 Checklist

在部署到生产环境之前，逐项检查：

- ```
  hermes doctor
  ```

   无明显报错
- API Key 已配置在

  ```
  .env
  ```

   文件中，不是

  ```
  config.yaml
  ```
- 已按需设置

  ```
  GATEWAY_HEARTBEAT=true
  ```
- 已配置用户白名单（如

  ```
  TELEGRAM_ALLOWED_USERS
  ```

  ）
- 审批模式已根据需求设置（

  ```
  approvals.mode
  ```

  ）
- 已安装为 Systemd 服务，或容器设置了自动重启

---

## 五、高级调试技巧

### 5.1 调试工具箱

```
hermes doctor          # 全面健康检查，优先运行
hermes memory status   # 检查记忆系统
hermes mcp status      # 检查 MCP 连接
hermes debug share     # 生成脱敏调试报告
```

### 5.2 常见 Q&A

**Q1：为什么我告诉了 Agent 一件事，它下次还是不记得？**

A：常见原因：会话太短，没有触发记忆整理；或者 Agent 认为这件事不值得长期保存。

**最直接的做法：** 明确说"请把这件事写入你的长期记忆"。

**Q2：Cron 定时任务没有按时触发怎么办？**

A：按以下顺序排查：

1. 运行

   ```
   hermes cron list
   ```

   ，确认任务状态
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

   ，确认任务逻辑本身没问题

**Q3：Tirith 总是拦截我正常的 bash 命令，很烦怎么办？**

A：三个方向：

1. 临时切到更宽松的工作模式
2. 调整

   ```
   approvals.mode
   ```

   ，如从

   ```
   manual
   ```

    变成更灵活的策略
3. 如果版本支持命令白名单，把高频安全命令加入 allowlist

---

## 六、配置速查表

### 生产环境 config.yaml 参考

```
agent:
  max_turns: 90

memory:
  nudge_interval: 10
  provider: mem0  # 或 holographic / honcho 等

approvals:
  mode: smart  # manual | smart | off

terminal:
  backend: docker
  timeout: 60
```

### 生产环境 .env 参考

```
# 核心 API Key
OPENAI_API_KEY=***
ANTHROPIC_API_KEY=***

# Gateway 配置
GATEWAY_PORT=8080
GATEWAY_HEARTBEAT=true

# 平台接入与白名单
TELEGRAM_BOT_TOKEN=123456...ew11
TELEGRAM_ALLOWED_USERS=123456789,987654321

# 外部记忆提供商（按需启用）
MEM0_API_KEY=***
```

---

## 动手实践

### 实践 1：构建你的专属记忆系统

**任务目标：** 配置好基础记忆文件，测试 Agent 的记忆能力。

**操作步骤：**

1. 复制 SOUL.md 模板到

   ```
   ~/.hermes/SOUL.md
   ```
2. 在常用项目目录下创建 AGENTS.md
3. 修改

   ```
   config.yaml
   ```

   ，将

   ```
   nudge_interval
   ```

    设置为 5
4. 开启新对话，告诉 Agent 一条特定偏好
5. 进行 5 轮以上对话，观察是否触发记忆整理

**预期效果：**

- 运行

  ```
  cat ~/.hermes/memories/MEMORY.md
  ```

  ，能看到偏好已被记录
- 开启全新会话，Agent 会自动遵循先前记录的偏好

### 实践 2：训练第一个自动化技能

**任务目标：** 让 Agent 学习并固化一个常用工作流。

**操作步骤：**

1. 找一个重复性任务（如清理 Docker 悬空镜像）
2. 在对话中一步步指导 Agent 完成，纠正错误
3. 发送指令："请把清理流程保存为 Skill，命名为 docker-cleanup"
4. 运行

   ```
   hermes skills list
   ```

    查看是否创建成功

**预期效果：**

- 开启新会话，直接发送

  ```
  /docker-cleanup
  ```
- Agent 能稳定地按照固化的步骤完成任务

---

## 总结

Hermes 最大的差异点不只是"能干活"，而是"**越干越会干**"。

理解技能自生成机制，才能让 Agent 真正进化，而不是每次都从零开始。

**核心要点：**

1. **记忆系统**是 Agent-curated 的，需要明确指令才能保留重要信息
2. **技能系统**把重复经验沉淀为可复用的 SOP
3. **多 Agent 协作**时，必须完整传递上下文给子 Agent
4. **生产部署**时，时区配置是最容易踩的坑

 

如果本文对你有帮助，欢迎：

|  |  |  |
| --- | --- | --- |
| 👍  点赞  给我一点鼓励 | 👀  在看  让更多朋友看到 | ↗️  分享  分享给需要的人 |

💬 互动话题：

你对这个话题有什么看法？

留言区见～

👇 点击写留言，一起聊聊

我是 Rowan，探索 AI 应用与效率提升的实践者。写作是思考的外化，期待在留言区与你相遇。

🚀 关于 Rowan

持续分享 AI 应用与效率提升的实战经验
