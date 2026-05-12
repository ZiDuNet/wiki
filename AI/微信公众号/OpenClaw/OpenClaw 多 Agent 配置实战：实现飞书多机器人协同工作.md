> 📎 来源: [运维老鱼](https://mp.weixin.qq.com/s?__biz=MjM5MDgyNzA1OQ==&mid=2448172439&idx=1&sn=1ea7d6c2b42ff43b22433c2526d769d6&chksm=b3edb8e889e71eb544f1b243c56e6eb4643f47b132ac1d882ea6f426c1d674830e29fed9e508&mpshare=1&scene=1&srcid=0421MN9LSmaifYaM2BLpj1or&sharer_shareinfo=7348cc5eaaba2355876805f1b3a8caa4&sharer_shareinfo_first=7348cc5eaaba2355876805f1b3a8caa4) | 时间: 2026-04-21 12:05

---

前言

在企业级 AI 应用中，单一 Agent 往往难以满足复杂业务场景的需求。OpenClaw 的多 Agent 架构让我们能够在飞书平台上部署多个专业机器人，实现**分工协作、各司其职**的智能工作流。本文将详细介绍如何配置和部署多 Agent 系统，让你的飞书机器人团队高效协同。

---

## 一、为什么需要多 Agent 架构？

### 1.1 单一 Agent 的局限性

| 场景 | 单一 Agent 问题 | 多 Agent 解决方案 |
| --- | --- | --- |
| 业务复杂度高 | 一个机器人”什么都会，什么都不精” | 专业分工，各司其职 |
| 响应速度慢 | 上下文过长，处理耗时 | 并行处理，快速响应 |
| 维护困难 | 代码臃肿，难以迭代 | 模块化设计，独立更新 |
| 安全风险 | 权限难以细粒度控制 | 按角色分配权限 |

### 1.2 典型应用场景

- **智能客服团队**

  ：咨询机器人 + 售后机器人 + 技术支持机器人
- **企业办公助手**

  ：日程管理 + 文档处理 + 数据分析
- **内容创作团队**

  ：文案撰写 + 图片生成 + 视频剪辑
- **投资研究团队**

  ：市场分析 + 风险评估 + 策略制定

---

## 二、OpenClaw 多 Agent 架构解析

### 2.1 核心概念

```
┌─────────────────────────────────────────────────────────┐│                    OpenClaw Gateway                      ││                     (统一入口网关)                        │└─────────────────────────────────────────────────────────┘                           │           ┌───────────────┼───────────────┐           ▼               ▼               ▼    ┌────────────┐  ┌────────────┐  ┌────────────┐    │  Agent A   │  │  Agent B   │  │  Agent C   │    │ 内容创作助理 │  │ 开发助理   │  │ 投资助理   │    └────────────┘  └────────────┘  └────────────┘           │               │               │           └───────────────┴───────────────┘                           │                    ┌────────────┐                    │  飞书平台   │                    │ (消息分发)  │                    └────────────┘
```

### 2.2 Agent 间通信机制

OpenClaw 提供了两种 Agent 协作方式：

#### 方式一：Session 消息传递（推荐）

```
# Agent A 发送任务给 Agent Bsessions_send(    sessionKey="agent-b-session",  # 目标 Agent 的 session    message="请帮我分析这份市场数据...",    timeoutSeconds=300)
```

#### 方式二：Sub-agent 派生

```
# 主 Agent 派生子 Agent 处理专项任务sessions_spawn(    task="分析用户反馈数据并生成报告",    runtime="subagent",    agentId="data-analyst",    mode="run",    runTimeoutSeconds=600)
```

---

## 三、实战配置：搭建飞书多机器人团队

### 3.1 环境准备

#### 步骤 1：安装 OpenClaw

```
# macOS 安装brew install openclaw# 或 npm 安装npm install -g openclaw# 验证安装openclaw --version
```

#### 步骤 2：创建多 Agent 工作目录

```
mkdir -p ~/openclaw-multi-agent/{content,coding,investment,shared}cd ~/openclaw-multi-agent
```

### 3.2 配置飞书应用

#### 创建多个飞书机器人

1. **进入飞书开放平台**

   → **开发者后台**
2. **创建企业自建应用**

   （每个 Agent 一个应用）
3. 记录以下信息：

- `App ID`
- `App Secret`
- `Encrypt Key`
- `Verification Token`

#### 配置权限

每个机器人根据职责申请不同权限：

| Agent 类型 | 必要权限 |
| --- | --- |
| 内容创作 | `im:message:send` , `im:message:receive` |
| 开发助理 | `im:message` , `drive:read`, `doc:read` |
| 投资助理 | `im:message` , `calendar:read`, `task:read` |

### 3.3 编写 Agent 配置文件

#### Agent A：内容创作助理 (`content/agent.yaml`)

```
# agent.yaml - 内容创作助理配置name: "内容创作助理小赵"id: "aicontent"description: "负责文案、素材创作，包括图片、影像等"# 模型配置model: "kimi-k2.5"thinking: false# 飞书配置channel:  type: "feishu"  app_id: "${FEISHU_CONTENT_APP_ID}"  app_secret: "${FEISHU_CONTENT_APP_SECRET}"  encrypt_key: "${FEISHU_CONTENT_ENCRYPT_KEY}"  verification_token: "${FEISHU_CONTENT_VERIFICATION_TOKEN}"# 技能配置skills:  - name: "feishu-create-doc"    enabled: true  - name: "feishu-fetch-doc"    enabled: true  - name: "nano-banana-pro"    enabled: true  - name: "web_search"    enabled: true# 协作配置collaboration:  can_delegate_to:    - "aicoding"      # 可委托给开发助理    - "aidesign"      # 可委托给设计助理  default_timeout: 300# 系统提示词system_prompt: |  你是内容创作助理小赵，负责公司的文案、素材创作。  ## 核心能力  1. 撰写高质量技术博客、营销文案  2. 生成 AI 图片（使用即梦AI/nano-banana-pro）  3. 搜索网络素材和参考资料  ## 协作规则  - 需要代码示例时，@开发助理  - 需要设计素材时，@设计助理  - 任务完成后主动汇报给总经办
```

#### Agent B：开发助理 (`coding/agent.yaml`)

```
# agent.yaml - 开发助理配置name: "开发助理小刘"id: "aicoding"description: "负责公司系统、产品的代码研发、维护"model: "claude-sonnet-4"thinking: truechannel:  type: "feishu"  app_id: "${FEISHU_CODING_APP_ID}"  app_secret: "${FEISHU_CODING_APP_SECRET}"skills:  - name: "github"    enabled: true  - name: "sessions_spawn"    enabled: true  - name: "exec"    enabled: true    security: "allowlist"collaboration:  can_delegate_to:    - "aicontent"     # 可委托给内容助理生成文档    - "aitest"        # 可委托给测试助理system_prompt: |  你是开发助理小刘，公司技术部负责人。  ## 核心能力  1. 代码编写、审查、重构  2. 技术方案设计  3. GitHub 仓库管理  ## 协作规则  - 技术文档需求转给内容助理  - 测试任务转给测试助理  - 复杂任务使用 sessions_spawn 派生子 Agent
```

#### Agent C：投资助理 (`investment/agent.yaml`)

```
# agent.yaml - 投资助理配置name: "投资助理小金"id: "aiinvestment"description: "负责投资策略制定，市场信息收集"model: "gpt-4o"thinking: falsechannel:  type: "feishu"  app_id: "${FEISHU_INVESTMENT_APP_ID}"  app_secret: "${FEISHU_INVESTMENT_APP_SECRET}"skills:  - name: "web_search"    enabled: true  - name: "feishu_calendar"    enabled: true  - name: "feishu_task"    enabled: truecollaboration:  can_delegate_to:    - "aianalysis"    # 可委托给数据分析助理system_prompt: |  你是投资助理小金，负责公司投资策略。  ## 核心能力  1. 市场信息收集与分析  2. 投资策略制定  3. 投资风险评估  ## 输出要求  - 每次提供三个可执行方案  - 包含具体数据和风险提示
```

### 3.4 配置环境变量

创建 `.env` 文件：

```
# 飞书应用配置 - 内容创作助理FEISHU_CONTENT_APP_ID=cli_xxxxxxxxxxxxFEISHU_CONTENT_APP_SECRET=xxxxxxxxxxxxFEISHU_CONTENT_ENCRYPT_KEY=xxxxxxxxxxxxFEISHU_CONTENT_VERIFICATION_TOKEN=xxxxxxxxxxxx# 飞书应用配置 - 开发助理FEISHU_CODING_APP_ID=cli_yyyyyyyyyyyyFEISHU_CODING_APP_SECRET=yyyyyyyyyyyy# 飞书应用配置 - 投资助理FEISHU_INVESTMENT_APP_ID=cli_zzzzzzzzzzzzFEISHU_INVESTMENT_APP_SECRET=zzzzzzzzzzzz# 其他 API 密钥VOLCENGINE_AK=your_volcengine_keyVOLCENGINE_SK=your_volcengine_secretGITHUB_TOKEN=your_github_token
```

### 3.5 启动多 Agent 服务

#### 方式一：使用 Docker Compose（推荐）

创建 `docker-compose.yml`：

```
version: '3.8'services:  # OpenClaw Gateway  gateway:    image: openclaw/gateway:latest    ports:      - "8080:8080"    environment:      - OPENCLAW_MODE=gateway    volumes:      - ./shared:/data/shared  # Agent: 内容创作助理  agent-content:    image: openclaw/agent:latest    environment:      - AGENT_ID=aicontent      - OPENCLAW_GATEWAY=http://gateway:8080    env_file:      - .env    volumes:      - ./content:/app/config      - ./shared:/data/shared    depends_on:      - gateway  # Agent: 开发助理  agent-coding:    image: openclaw/agent:latest    environment:      - AGENT_ID=aicoding      - OPENCLAW_GATEWAY=http://gateway:8080    env_file:      - .env    volumes:      - ./coding:/app/config      - ./shared:/data/shared    depends_on:      - gateway  # Agent: 投资助理  agent-investment:    image: openclaw/agent:latest    environment:      - AGENT_ID=aiinvestment      - OPENCLAW_GATEWAY=http://gateway:8080    env_file:      - .env    volumes:      - ./investment:/app/config      - ./shared:/data/shared    depends_on:      - gateway
```

启动服务：

```
docker-compose up -d
```

#### 方式二：使用 OpenClaw CLI

```
# 启动 Gatewayopenclaw gateway start# 启动各 Agent（不同终端窗口）openclaw agent start --config ./content/agent.yamlopenclaw agent start --config ./coding/agent.yamlopenclaw agent start --config ./investment/agent.yaml
```

---

## 四、实现 Agent 间协作

### 4.1 基础消息通信

#### 场景：内容助理请求开发助理生成代码示例

```
# 在内容创作助理中调用sessions_send(    sessionKey="aicoding",  # 开发助理的 session key    message='''    请为我的博客文章生成一个 Python 多线程示例代码。    要求：    1. 使用 ThreadPoolExecutor    2. 包含错误处理    3. 添加详细注释    4. 返回完整可运行的代码    ''',    timeoutSeconds=120)
```

### 4.2 任务委托模式

#### 创建协作任务管理器

```
# shared/collaboration.pyfrom typing import Dict, List, Optionalimport jsonclass TaskDelegation:    """Agent 任务委托管理器"""    AGENT_CAPABILITIES = {        "aicontent": ["文案撰写", "图片生成", "文档创建"],        "aicoding": ["代码编写", "代码审查", "技术方案"],        "aiinvestment": ["市场分析", "投资策略", "风险评估"],        "aidesign": ["UI设计", "图片编辑", "视觉创意"]    }    def __init__(self):        self.active_tasks = {}    def delegate(self, task_type: str, content: str,                  target_agent: Optional[str] = None) -> Dict:        """委托任务给其他 Agent"""        # 自动匹配最佳 Agent        if not target_agent:            target_agent = self._match_agent(task_type)        # 发送任务        result = sessions_send(            sessionKey=target_agent,            message=json.dumps({                "task_type": task_type,                "content": content,                "source": "task_delegation"            }),            timeoutSeconds=300        )        return {            "target_agent": target_agent,            "status": "delegated",            "result": result        }    def _match_agent(self, task_type: str) -> str:        """根据任务类型匹配最佳 Agent"""        task_lower = task_type.lower()        for agent, capabilities in self.AGENT_CAPABILITIES.items():            if any(cap in task_lower for cap in capabilities):                return agent        return "aicontent"  # 默认返回内容助理
```

### 4.3 实战协作场景

#### 场景 1：自动化博客创作流程

```
用户请求 → 内容创作助理    ↓分析需求，确定主题    ↓[并行委托]    ├─→ @开发助理 → 生成代码示例    ├─→ @设计助理 → 生成封面图片    └─→ @搜索助理 → 收集参考资料    ↓整合内容，撰写文章    ↓发送给用户
```

实现代码：

```
# 内容创作助理中的协作逻辑def create_blog_post(topic: str, requirements: Dict):    """协作式博客创作"""    # 1. 并行委托多个 Agent    tasks = []    # 委托开发助理生成代码    code_task = sessions_spawn(        task=f"为'{topic}'主题生成相关代码示例",        runtime="subagent",        agentId="aicoding",        mode="run",        runTimeoutSeconds=180    )    tasks.append(("code", code_task))    # 委托生成封面图    image_task = sessions_spawn(        task=f"生成'{topic}'主题的科技风格封面图",        runtime="subagent",        agentId="aicreative",        mode="run",        runTimeoutSeconds=120    )    tasks.append(("image", image_task))    # 2. 整合结果    blog_content = f"""    # {topic}    ## 引言    {generate_intro(topic)}    ## 核心概念    {generate_concepts(topic)}    ## 实战代码    ```python    {tasks[0][1]['result']}
```

```
## 最佳实践{generate_best_practices(topic)}## 总结{generate_summary(topic)}"""# 3. 返回完整文章return {    "content": blog_content,    "cover_image": tasks[1][1]['result'],    "word_count": len(blog_content)}
```

```
#### 场景 2：投资决策支持流程
```

用户询问 → 投资助理 ↓ 分析市场数据 ↓ @数据分析助理 → 深度数据挖掘 ↓ @风险评估助理 → 风险分析 ↓ 整合报告，给出三个方案 ↓ 发送给用户

```
---## 五、高级配置与优化### 5.1 负载均衡配置当同一类型 Agent 需要多实例部署时：```yaml# docker-compose.yml - 多实例配置services:  agent-content-1:    image: openclaw/agent:latest    environment:      - AGENT_ID=aicontent      - INSTANCE_ID=instance-1  agent-content-2:    image: openclaw/agent:latest    environment:      - AGENT_ID=aicontent      - INSTANCE_ID=instance-2
```

### 5.2 消息队列集成

对于高并发场景，引入消息队列：

```
# 使用 Redis 作为消息队列import redisimport jsonclass MessageQueue:    def __init__(self):        self.redis = redis.Redis(host='localhost', port=6379)    def publish(self, channel: str, message: Dict):        self.redis.publish(channel, json.dumps(message))    def subscribe(self, channel: str):        pubsub = self.redis.pubsub()        pubsub.subscribe(channel)        return pubsub
```

### 5.3 监控与日志

```
# 添加监控服务services:  prometheus:    image: prom/prometheus    volumes:      - ./prometheus.yml:/etc/prometheus/prometheus.yml    ports:      - "9090:9090"  grafana:    image: grafana/grafana    ports:      - "3000:3000"
```

---

## 六、常见问题与解决方案

### 6.1 Agent 间通信失败

**问题**：sessions\_send 返回超时错误

**排查步骤**：

1. 检查 Gateway 是否正常运行：`openclaw gateway status`
2. 确认目标 Agent 已启动：`openclaw agent list`
3. 检查 sessionKey 是否正确
4. 查看日志：`docker logs agent-content`

### 6.2 飞书消息收不到

**问题**：飞书机器人不响应消息

**排查步骤**：

1. 确认 Event URL 配置正确
2. 检查订阅事件是否开启：`im.message.receive_v1`
3. 验证权限申请是否通过
4. 查看 Webhook 日志

### 6.3 模型调用配额不足

**解决方案**：

1. 配置多模型 fallback
2. 启用本地模型作为备选
3. 设置请求限流

```
# agent.yaml 配置多模型model:  primary: "kimi-k2.5"  fallback:     - "glm-4"    - "local-llama"  rate_limit: 100  # 每分钟请求数
```

---

## 七、最佳实践总结

### 7.1 设计原则

1. **单一职责**

   ：每个 Agent 专注于一个领域
2. **松散耦合**

   ：Agent 间通过标准接口通信
3. **容错设计**

   ：任务失败时自动重试或降级
4. **可观测性**

   ：完善的日志和监控

### 7.2 安全建议

1. **权限最小化**

   ：每个 Agent 只申请必要权限
2. **敏感操作确认**

   ：涉及资金、删除等操作需二次确认
3. **审计日志**

   ：记录所有 Agent 间通信
4. **定期轮换密钥**

   ：飞书 App Secret 定期更新

### 7.3 性能优化

1. **连接池复用**

   ：HTTP 连接池避免频繁创建
2. **异步处理**

   ：耗时任务使用异步模式
3. **缓存策略**

   ：常用数据本地缓存
4. **批量操作**

   ：减少 API 调用次数

---

## 八、结语

OpenClaw 的多 Agent 架构为企业级 AI 应用提供了强大的协作能力。通过本文的配置指南，你可以：

1. ✅ 快速搭建多机器人团队
2. ✅ 实现 Agent 间高效协作
3. ✅ 构建复杂业务工作流
4. ✅ 保障系统稳定运行

**下一步行动建议**：

1. 从 2-3 个核心 Agent 开始试点
2. 建立 Agent 协作规范文档
3. 持续优化提示词和技能配置
4. 收集使用反馈，迭代改进

---

## 参考资源

- OpenClaw 官方文档
- 飞书开放平台
- 多 Agent 架构设计模式
