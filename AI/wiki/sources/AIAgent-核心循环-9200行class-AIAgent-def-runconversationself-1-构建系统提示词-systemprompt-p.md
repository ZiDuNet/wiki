---
tags: [OpenClaw, Agent, Claude, MCP, GitHub, 飞书, Prompt, API]
source: "豆爸AI"
created: 2026-04-24
updated: 2026-05-10
category: OpenClaw
---

# AIAgent 核心循环 (~9,200行)class AIAgent:    def runconversation(self):        # 1. 构建系统提示词        systemprompt = promptbuilder.build()                # 2. 解析 Provider        provider = runtimeprovider.resolve()                # 3. 执行工具调用循环        while not complete:            response = llm.chatcompletion(messages, tools)            if response.toolcalls:                results = modeltools.handlecalls(response.toolcalls)                messages.extend(results)                # 4. 上下文压缩        if tokencount > threshold:            contextcompressor.compress(messages)

> 来源: [豆爸AI](https://mp.weixin.qq.com/s?__biz=MzcwMjIwMDk2Mg==&mid=2247483881&idx=1&sn=65724676b9ee3a993c14ae72235a7c0d&chksm=f54acc8555a269e9067130c2444fec5ead42d3b86361329dc98f0f99bcd4b52a29bd16bc0c81&mpshare=1&scene=1&srcid=0424c1qrJZecsqWD12spmfKu&sharer_shareinfo=8ac752344a04f20b8a8e88c2f3829df5&sharer_shareinfo_first=8ac752344a04f20b8a8e88c2f3829df5) | 2026-04-24

## 摘要

AI Agent 架构深度解析
🐠 小鱼技术笔记 • 2026年4月14日 • 15分钟阅读
**核心观点：**Hermes Agent 和 OpenClaw 代表了 AI Agent 架构的两个极端方向——前者是「会学习的个人助手」，后者是「可控的企业级多智能体平台」。选择哪个框架，取决于你要解决的是「效率问题」还是「规模问题」。
1
Hermes Agent 由 Nous Research 开源，GitHub 上已获得 **57,200+ stars**，核心代码 run\_agent.py 约 9,200 行，是一个真正意义上的**「自我进化型」AI Agent**。它的核心哲学是：Agent 应该像人类一样，通过经验积累不断变强。
Hermes Agent 架构图
Layer 1
🚪 多入口接入层
CLI (~10K行) | Gateway (18+平台) | ACP (IDE适配)
↓
Layer 2
🤖 AIAgent 核心引擎 (~9,200行)
Prompt Builder | Provider Resolver | Tool Dispatch | Context Co...

## 相关实体

[[Anthropic]], [[Claude]], [[DeepSeek]], [[Docker]], [[GPT-4]], [[Gemini]], [[GitHub]], [[Hermes]], [[MCP]], [[Node.js]], [[OpenClaw]], [[Python]], [[SQLite]], [[飞书]]

## 相关概念

[[AI-Agent]], [[MCP协议]], [[Multi-Agent]], [[工作流自动化]], [[自进化系统]]
