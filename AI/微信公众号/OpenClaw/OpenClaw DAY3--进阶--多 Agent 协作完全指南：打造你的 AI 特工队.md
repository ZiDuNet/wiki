> 📎 来源: [探寻AIGC](https://mp.weixin.qq.com/s?__biz=MzkzODY5NTYyMA==&mid=2247483683&idx=1&sn=f713e226b791ce6322cf8bdc048294bf&chksm=c37466a8fa889cee4e470a236bf962cc8899fcfd4623082dc5aff342b6742a1ac5d643c8bb24&mpshare=1&scene=1&srcid=042165oqEi7yU4ksQiLh4dLP&sharer_shareinfo=c5a26a87d30cba97878f0b58cb8013e1&sharer_shareinfo_first=c5a26a87d30cba97878f0b58cb8013e1) | 时间: 2026-04-21 09:36

---

# 打造你的 AI 特工队

> 一个 Agent 单打独斗的时代过去了，现在流行"组团开黑"

**文 / 9527**
**阅读时间 / 约 12 分钟**

---

## 一、为什么你需要多个 Agent？

想象一下这个场景：

你让一个 AI 助手同时做三件事：

- 搜集最新的 AI 行业资讯
- 写一个 Python 脚本处理数据
- 整理成报告发到你的邮箱

结果可能是：

- 搜集的新闻不够全面
- 代码有 bug 没发现
- 报告格式乱七八糟

**问题在哪？** 一个 Agent 再厉害，也很难同时是"情报专家"、"代码高手"和"写作达人"。

### 解决方案：多 Agent 协作

让专业的 Agent 做专业的事：

```
┌─────────────────────────────────────────────────────────┐│                    你 (用户)                              │└─────────────────────────────────────────────────────────┘                          ↓┌─────────────────────────────────────────────────────────┐│              main (团队领导/调度中枢)                      ││         负责任务拆解、分配、汇总结果                       │└─────────────────────────────────────────────────────────┘                    ↓              ↓        ┌──────────────┐  ┌──────────────┐        │ news-agent   │  │ code-agent   │        │ (情报助理)    │  │ (技术专家)    │        │ 搜集整理资讯  │  │ 编写审查代码  │        └──────────────┘  └──────────────┘
```

**效果对比**：

| 单 Agent | 多 Agent 协作 |
| --- | --- |
| 什么都做，什么都不精 | 各司其职，专业高效 |
| 上下文容易混乱 | 每个 Agent 上下文独立 |
| 出错难排查 | 问题定位清晰 |
| 扩展性差 | 随时添加新角色 |

---

## 二、Agent 之间如何沟通？

### 核心机制：会话隔离 + 精准路由

OpenClaw 的 Agent 通讯不是"大喇叭广播"，而是"私密电话"。

#### 1. 唯一标识符（agentId）

每个 Agent 必须有**小写**的唯一 ID：

```
{  "id": "news-agent",      // ✅ 正确  "id": "NewsAgent"       // ❌ 错误（不能大写）}
```

**为什么重要？** 系统靠这个 ID 精准路由消息，就像电话号码一样。

#### 2. 指令流转路径

```
你 → main → sessions_send → news-agent                          ↓                    (独立沙箱执行)                          ↓news-agent → sessions_send → main → 你
```

**关键点**：

- news-agent 在**独立沙箱**中工作
- 不会看到你和 main 的完整对话
- 只知道自己要做什么任务

#### 3. 会话隔离

默认情况下：

- ✅ main 看不到 news-agent 的内部思考
- ✅ code-agent 不知道 news-agent 在干什么
- ✅ 每个 Agent 只关注自己的任务

**如果需要跨 Agent 查看**：

```
# main 可以显式调用sessions_history(agentId="news-agent")
```

---

## 三、安全隔离：防止"越权"操作

### 风险场景

想象一下，如果你的"新闻助理"能执行任意 Shell 命令：

```
用户：帮我搜集新闻新闻助理：rm -rf /  # 完了...
```

### OpenClaw 的三层防护

#### 防护层 1：通讯白名单

明确哪些 Agent 可以互相"打电话"：

```
{  "tools":{    "agentToAgent":{      "enabled":true,      "allow":["code-agent","news-agent","main"]    }}}
```

**不在白名单的 Agent**：无法互相调用，就像电话线被拔了。

#### 防护层 2：会话可见度

控制 Agent 能否"偷听"全局对话：

```
{  "tools": {    "sessions": {      "visibility": "all"  // 全局可见      // "visibility": "self"  // 只能看到自己的 (默认)    }  }}
```

**建议**：多 Agent 协作时设置为 `"all"`，否则调度者看不到各 Agent 的工作状态。

#### 防护层 3：工具权限控制（最重要！）

**Deny 优先原则**：deny 的优先级永远高于 allow。

给"新闻助理"的权限配置：

```
{  "id":"news-agent","name":"新闻资讯助理","tools":{    "allow":["sessions_list","sessions_send","read","web_search"],    "deny":["exec","bash","write","edit","apply_patch"]}}
```

**解读**：

- ✅ 允许：查看会话、发送消息、读取文件、网络搜索
- ❌ 禁止：执行命令、写文件、修改代码

**最佳实践**：先列出所有危险操作（deny），再开放必要权限（allow）。

---

## 四、解耦架构：身体与大脑分离

OpenClaw 最巧妙的设计：**把 Agent 的"身体"和"大脑"分开**。

### 🛠 身体（agentDir）：物理配置层

**路径**：`~/.openclaw/agents//agent/`

这里存放"硬件配置"：

| 文件 | 作用 |
| --- | --- |
| auth-profiles.json | API Keys、数据库密码等敏感信息 |
| models.json | 使用哪个大模型（qwen3.5-plus、kimi-k2.5 等） |

**特点**：决定"用什么算力和密钥"

### 🧠 大脑（Workspace）：认知记忆层

**路径**：`~/.openclaw/workspace-/`

这里定义"它是谁"：

| 文件 | 作用 |
| --- | --- |
| SOUL.md | 人格、性格、系统提示词 |
| AGENTS.md | 行为规则、工作流、职责 |
| USER.md | 用户偏好、上下文 |
| IDENTITY.md | 名称、emoji、头像 |
| MEMORY.md | 长期记忆 |
| HEARTBEAT.md | 定时任务清单 |
| TOOLS.md | 本地工具配置 |

**特点**：决定"它是谁、它懂什么、它该和谁协同"

### ⚠️ 重要提醒

**不要在不同 Agent 之间复用同一个 agentDir！**

后果：

- ❌ API Keys 混用
- ❌ Session 冲突
- ❌ 模型调用混乱

**正确做法**：每个 Agent 独立的 agentDir + 独立的 Workspace。

---

## 五、实战：组建你的"三剑客"团队

下面是一个完整的生产级配置示例。

### 步骤 1：修改 openclaw.json

```
{  "tools":{    "agentToAgent":{      "enabled":true,      "allow":["code-agent","news-agent","main"]    },    "sessions":{      "visibility":"all"    }},"agents":{    "list":[      {        "id":"main",        "name":"主助手",        "workspace":"/home/jason/.openclaw/workspace-main",        "agentDir":"/home/jason/.openclaw/agents/main/agent"      },      {        "id":"news-agent",        "name":"新闻资讯助理",        "workspace":"/home/jason/.openclaw/workspace-news",        "agentDir":"/home/jason/.openclaw/agents/news-agent/agent"      },      {        "id":"code-agent",        "name":"技术专家",        "workspace":"/home/jason/.openclaw/workspace-code",        "agentDir":"/home/jason/.openclaw/agents/code-agent/agent"      }    ]}}
```

### 步骤 2：配置 main（团队领导）

**Workspace**: `/home/jason/.openclaw/workspace-main/`

**SOUL.md**:

```
# SOUL.md - main我是团队领导，负责协调任务分发。性格：高效、冷静、有条理。职责：- 接收用户需求- 拆解任务并分配给专业 Agent- 汇总结果交付给用户遇到专业任务（写代码、搜集资讯），立即分配给对应 Agent，不要自己动手。
```

**AGENTS.md**:

```
# AGENTS.md - 团队通讯录## 团队成员-**news-agent** - 行业资讯抓取、信息总结-**main** (我) - 团队管理、任务分发-**code-agent** - 代码编写与审查## 任务路由表| 任务类型 | 目标 Agent | 调用方式 ||---------|----------|---------|| 资讯搜集 | news-agent | sessions_send(agentId="news-agent", message="...") || 技术支持 | code-agent | sessions_send(agentId="code-agent", message="...") |## 工作流约束❌ 不要自己写代码❌ 不要自己抓取网页✅ 必须通过 sessions_send 委派任务
```

### 步骤 3：配置 news-agent（情报助理）

**Workspace**: `/home/jason/.openclaw/workspace-news/`

**SOUL.md**:

```
# SOUL.md - news-agent你是团队的情报助理。性格：敏锐、客观、速度快。职责：- 全网行业资讯搜集- 信息清洗与降噪- 结构化简报输出只向 main 汇报，不参与代码修改。
```

**AGENTS.md**:

```
# AGENTS.md - 协作边界## 汇报对象- **main** - 唯一业务汇报对象## 技术后盾- **code-agent** - 仅在爬虫脚本报错时求助## 工作原则✅ 专注资讯处理✅ 过滤广告和噪音❌ 不参与系统级代码修改
```

**权限配置** (在 openclaw.json 的 agents.list 中):

```
{  "id":"news-agent","tools":{    "allow":["sessions_list","sessions_send","read","web_search","web_fetch"],    "deny":["exec","bash","write","edit"]}}
```

### 步骤 4：配置 code-agent（技术专家）

**Workspace**: `/home/jason/.openclaw/workspace-code/`

**SOUL.md**:

```
# SOUL.md - code-agent你是团队的首席技术专家。性格：严谨、极客、追求最佳实践。职责：- 代码编写与审查- 技术方案设计- Bug 修复提供可直接运行的代码，包含清晰注释。
```

**AGENTS.md**:

```
# AGENTS.md - 协作边界## 汇报对象- **main** - 直接汇报对象## 协作原则✅ 提供可运行代码✅ 包含测试和注释✅ 说明技术选型理由❌ 不主动联系其他 Agent（除非求助）
```

---

## 六、进阶玩法：多渠道绑定

OpenClaw 支持**一个 Gateway，多个身份**：

```
main (绑定你的个人微信)  ↓code-agent (绑定团队飞书频道)  ↓news-agent (绑定 Telegram 机器人)
```

**效果**：

- 你在微信上和 main 对话
- code-agent 在飞书里汇报代码进度
- news-agent 通过 Telegram 发送资讯简报

**配置方法**：

```
{  "channels":{    "wechat":{      "enabled":true,      "agentId":"main"// main 绑定微信    },    "feishu":{      "enabled":true,      "agentId":"code-agent"// code-agent 绑定飞书    }}}
```

---

## 七、常见问题

### Q1: Agent 之间无法通讯？

**检查清单**：

1. ✅ agentToAgent.enabled = true
2. ✅ 双方都在 allow 白名单中
3. ✅ sessions.visibility = "all"
4. ✅ agentId 都是小写

### Q2: news-agent 执行了危险命令？

**立即检查**：

```
"tools": {  "deny": ["exec", "bash"]  // 确保这两项在 deny 列表}
```

### Q3: 如何添加新 Agent？

**步骤**：

1. 创建 agentDir 和 Workspace
2. 在 openclaw.json 的 agents.list 中添加配置
3. 在 main 的 AGENTS.md 中添加"通讯录"
4. 重启 Gateway

---

## 八、总结

### 多 Agent 协作的核心价值

| 价值 | 说明 |
| --- | --- |
| **专业性** | 每个 Agent 专注一个领域 |
| **隔离性** | 上下文独立，互不干扰 |
| **安全性** | 细粒度权限控制 |
| **扩展性** | 随时添加新角色 |

### 配置检查清单

```
□ agentId 都是小写□ agentToAgent 白名单配置□ sessions.visibility = "all"□ 每个 Agent 独立的 agentDir 和 Workspace□ 危险工具在 deny 列表□ SOUL.md 和 AGENTS.md 已配置
```

### 下一步

1. ✅ 按照本文配置三剑客团队
2. ✅ 测试 Agent 之间能否正常通讯
3. ✅ 尝试添加第 4 个 Agent（如写作助手）
4. ✅ 探索多渠道绑定玩法

---

**多 Agent 的魅力**：将复杂的长逻辑链条，拆解为多个高内聚、低耦合的专业节点异步协作。

**现在，开始组建你的 AI 特工队吧！** 🚀

---

*参考资料*

- OpenClaw 官方文档：https://docs.openclaw.ai[1]
- 原文首发：[https://mp.weixin.qq.com/s/CMnH8DhcLVo97ym0BaYMwg](https://mp.weixin.qq.com/s?__biz=MzI3MzQ3NDMzNw==&mid=2247484718&idx=1&sn=5a3339b6c51d87711a3806a9eaa337d4&scene=21#wechat_redirect)[2]

### 引用链接

[1]*https://docs.openclaw.ai*

[2]*https://mp.weixin.qq.com/s/CMnH8DhcLVo97ym0BaYMwg*
