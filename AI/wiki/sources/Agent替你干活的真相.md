---
title: Agent 替你干活的真相，比你想象的简单十倍
type: source-summary
tags: [Agent, LLM, 工具调用, 架构, 记忆系统]
sources: [../微信公众号/Agent/Agent 替你干活的真相，比你想象的简单十倍_1.md]
created: 2026-05-16
updated: 2026-05-16
---

# Agent 替你干活的真相

## 核心摘要

大模型（LLM）本身**一行代码都没执行过**——它不会上网、不会读文件、不会发邮件，它只会预测下一个 token。Agent 的"自主"来自一个简单循环：**LLM 输出 JSON（工具调用），你的代码执行，结果返回 LLM**。大脑是 LLM，手脚是你的代码。

## Agent vs 普通 LLM 的本质区别

| | 普通 LLM | Agent |
|---|---|---|
| 行为 | 被动回答 | 主动探索 |
| 信息 | 依赖训练数据 | 实时获取 |
| 执行 | 无 | 通过工具循环执行 |

Agent 的核心循环：**感知 → 思考 → 行动 → 观察 → 再思考**，每步结果决定下一步方向。

## Agent 四个核心零件

### 1. 大脑：模型选型
- **Claude Opus 4.7**：编程和复杂推理最强
- **GPT-5.5**：最大特点是耐力好，能连续自主运行 31 小时不崩
- **Gemini 3.1 Pro**：杀手锏是 200 万 token 上下文窗口

### 2. 手：工具描述（Tool Description）
LLM 不能上网/读文件/发邮件，工具接入的核心是**写清楚描述**，必须包含：工具能做什么、返回什么、参数怎么填。

工具调用底层流程：LLM 判断该用哪个工具 → 返回 JSON → 代码执行 → 结果返回 LLM → 判断继续调还是直接回答。（OpenAI 叫 Function Calling，Anthropic 叫 Tool Use，Google 也叫 Function Calling）

**MCP（Model Context Protocol）** 是解决工具描述标准化的方案——写一次，所有支持 MCP 的 AI 应用都能用，相当于 USB-C 之于充电口。

### 3. 记忆：两层设计
- **短期记忆**：当前对话内容，每调一次工具结果拼进记录，窗口有大小限制
- **长期记忆**：跨会话信息，存数据库，启动时检索自动调整

### 4. 规划：两种方式
- **ReAct（边走边看）**：做一步看结果决定下一步，像走迷宫，灵活但可能绕路
- **Plan-and-Execute（先画地图）**：列完整计划再执行，像开导航，高效但中途封路就傻眼

**实战策略**：大方向 Plan-and-Execute 驱动，遇意外切 ReAct。

## Agent 的不可靠性与防御

三个导致不可靠的原因：LLM 概率性（同样输入今天和昨天不同）、错误滚雪球（一步跑偏后面全歪）、不知道自己错了（继续往错误方向狂奔）。

四层防御：Prompt 自纠错 → 调低 temperature → 加护栏规则引擎验证 → 人类审批。

## 成本控制策略

- 规划用强模型（贵但值），执行用轻量模型（Claude Opus 4.7 做规划，Haiku 4.5 做信息提取，后者成本不到十分之一）
- 相同查询走缓存
- 发现跑偏果断终止

## 何时用 Agent

**适合**：步骤不确定、需要推理判断的任务（"分析架构问题""排查报错原因"）
**不适合**：步骤明确、逻辑固定的任务（批量处理文件、定时同步数据），用传统脚本更稳更便宜

## 核心代码示例（十几行 Agent Loop）

```python
def agent_loop(user_goal):
    messages = [{"role": "system", "content": AGENT_PROMPT},
                {"role": "user", "content": user_goal}]
    while steps < MAX_STEPS:
        response = llm.chat(messages, tools=tools)
        if response.has_tool_calls():
            for call in response.tool_calls:
                result = execute_tool(call.name, call.arguments)
                messages.append(tool_result_to_message(result))
        else:
            break
    return response.content
```

## 相关概念

- [[MCP协议]] — 工具描述标准化
- [[记忆系统]] — 短期+长期记忆设计
- [[Prompt工程]] — 自纠错 Prompt
- [[AI-Agent]] — 上位概念
