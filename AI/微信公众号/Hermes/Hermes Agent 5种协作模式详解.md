> 📎 来源: [怪兽打奥凸曼](https://mp.weixin.qq.com/s?__biz=MzY5MzE3NjA4OA==&mid=2247483653&idx=1&sn=6b09711bb3299ed25f2a71035f9a24e4&chksm=f58ad9599f53b8af19b01b25496836221c6f66165caafd9dc5024ff9f96b36ecffa182d1ff73&mpshare=1&scene=1&srcid=0423HHjGRGi1Ys0QPOdScRjW&sharer_shareinfo=297500c5e940edc9084ab98628ff3c49&sharer_shareinfo_first=297500c5e940edc9084ab98628ff3c49) | 时间: 2026-04-23 21:24

---

#

---

## 📋 5种协作模式概览

| 编号 | 模式名称 | 英文 | 核心特点 | 使用场景 |
| --- | --- | --- | --- | --- |
| 01 | 🤖 单代理模式 | Single Agent | 逻辑集中，简单快速 | 简单问答、文本生成、小脚本编写、快速原型 |
| 02 | 🔗 顺序协作模式 | Sequential | 流水线串行，上下游传递 | 数据采集→清洗→分析、需求→开发→测试、文档→翻译→校对 |
| 03 | ⚡ 并行协作模式 | Parallel | 多Agent同时执行，最多3路 | 多源信息检索、批量内容生成、多角度分析、分支任务处理 |
| 04 | 👑 主从模式 | Manager-Worker | 智能任务分配与调度 | 项目规划执行、复杂问题求解、自动化工作流、多模块开发 |
| 05 | 🔄 评审反馈模式 | Critic-Refiner | 生成→评审→迭代优化闭环 | 代码审查优化、文章写作打磨、策略方案评估、高质量内容生产 |

---

## 🔧 详细配置指南

### 模式1：单代理模式 Single Agent

**使用场景**：简单任务、快速响应、低成本

**配置步骤**：

```
# 1. 创建空配置文件hermes profile create myagent# 2. 进入配置myagent setup# 3. 编辑 SOUL.md 定义角色echo "You are a helpful assistant." > ~/.hermes/profiles/myagent/SOUL.md# 4. 启动对话myagent chat
```

**关键文件**：

- ```
  config.yaml
  ```

   - 模型和工具配置
- ```
  SOUL.md
  ```

   - 个性和指令设定
- ```
  .env
  ```

   - API密钥

---

### 模式2：顺序协作模式 Sequential

**使用场景**：流水线任务、数据处理、多步骤流程自动化

**配置步骤**：

```
# 1. 创建多个Agent（按流水线顺序）hermes profile create collector --clone# 采集hermes profile create analyzer --clone# 分析hermes profile create reporter --clone# 报告# 2. 配置各Agent职责# collector/SOUL.md: 负责数据采集# analyzer/SOUL.md: 负责数据分析# reporter/SOUL.md: 负责生成报告，接收analyzer输出# 3. 配置交接合同# ~/.hermes/profiles/handoffs/collector-to-analyzer.md# 定义输出格式、验证门禁、失败动作
```

**目录结构**：

```
~/.hermes/profiles/├── collector/    # 采集Agent├── analyzer/     # 分析Agent├── reporter/     # 报告Agent└── handoffs/     # 交接合同目录
```

---

### 模式3：并行协作模式 Parallel

**使用场景**：高并发、任务拆分、多源检索、批量生成

**⚠️ 注意**：最多建议3路并发，避免资源竞争

**配置步骤**：

```
# 1. 创建并行的多个Agenthermes profile create research1 --clone# 搜索技术文档hermes profile create research2 --clone# 搜索行业报告hermes profile create research3 --clone# 搜索竞品分析hermes profile create aggregator --clone# 汇总Agent# 2. 各Agent配置独立任务域（SOUL.md）# research1/2/3 分别负责不同领域的信息收集# aggregator 负责整合所有研究成果# 3. 并行启动hermes -p research1 chat &hermes -p research2 chat &hermes -p research3 chat &# 4. aggregator 收集并整合结果hermes -p aggregator chat
```

---

### 模式4：主从模式 Manager-Worker

**使用场景**：复杂任务、多步骤推理、项目规划、自动化系统

**配置步骤**：

```
# 1. 创建 Manager 和多个 Workerhermes profile create manager --clone# 协调员（核心）hermes profile create coder --clone# 写代码hermes profile create tester --clone# 测试hermes profile create writer --clone# 文档# 2. 配置 Manager 职责（任务拆解与调度）# ~/.hermes/profiles/manager/SOUL.md角色：任务协调员职责：- 分析用户需求- 将复杂任务拆解为子任务- 分配给合适的Worker执行- 收集并汇总Worker结果# 3. 配置 Worker 职责# ~/.hermes/profiles/coder/SOUL.md角色：代码工程师职责：执行具体的编码任务# 4. 配置权限级别（策略门禁）# coder: 审核级 - 可读代码库、运行测试、写功能分支# manager: 关键级 - 唯一批准合并的权限
```

**目录结构**：

```
~/.hermes/profiles/├── manager/      # 协调员（核心大脑）├── coder/        # 代码工程师├── tester/       # 测试工程师└── writer/       # 文档工程师
```

---

### 模式5：评审反馈模式 Critic-Refiner

**使用场景**：高质量输出、反复优化、代码审查、策略优化

**配置步骤**：

```
# 1. 创建生成和评审Agenthermes profile create generator --clone# 生成者hermes profile create critic --clone# 评审者# 2. 配置 Generator（生成者）# ~/.hermes/profiles/generator/SOUL.md角色：内容生成专家职责：高质量输出初稿# 3. 配置 Critic（评审者）# ~/.hermes/profiles/critic/SOUL.md角色：质量评审专家职责：严格评审，给出改进建议评审标准：- 准确性- 完整性- 格式规范- 逻辑连贯# 4. 配置迭代收敛条件最大迭代次数：3次收敛标准：评审评分 ≥ 90分# 5. 评审反馈循环while 评分 < 90 and 迭代 < 3:    output = generator.generate(input)    score = critic.evaluate(output)    if score < 90:        input = critic.suggest_improvements(output)        迭代 += 1
```

---

## 📊 模式选择对照表

| 场景复杂度 | 推荐模式 | 命令示例 |
| --- | --- | --- |
| 简单问答 | 单代理 | ``` myagent chat ``` |
| 流程清晰 | 顺序 | ``` collector → analyzer → reporter ``` |
| 效率优先 | 并行 | ``` agent1 & agent2 & agent3 ``` |
| 复杂任务 | 主从 | ``` manager ```   调度多个   ``` worker ``` |
| 质量优先 | 评审 | ``` generator ```   +   ``` critic ```   迭代 |

---

## 🛠️ 核心命令速查

```
# 创建配置文件hermes profile create            # 空白hermes profile create  --clone# 克隆配置# 使用配置文件hermes -p  chat                 # 指定profile对话hermes profile use              # 设为默认hermes profile list                   # 列出所有profile# 管理hermes profile delete           # 删除hermes profile show             # 查看详情hermes profile rename       # 重命名# 配置myagent setup                        # 交互式配置myagent doctor                       # 健康检查myagent gateway start                # 启动网关
```

---

## 📁 Profile 目录结构

每个配置文件完全隔离，包含：

```
~/.hermes/profiles//├── config.yaml      # 模型、提供者、工具集├── .env# API密钥、机器人令牌├── SOUL.md          # 个性和指令├── memories/        # 记忆文件├── sessions/       # 会话历史├── skills/          # 技能└── cron/           # 定时任务
```

---
