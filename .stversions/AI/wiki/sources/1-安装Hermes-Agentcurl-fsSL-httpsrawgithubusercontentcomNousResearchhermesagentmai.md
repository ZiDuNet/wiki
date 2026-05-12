---
tags: [Obsidian, Agent, Claude, MCP, GitHub, 飞书, RAG, Prompt]
source: "飞哥的技术与烟火"
created: 2026-05-06
updated: 2026-05-10
category: Obsidian
---

# 1. 安装Hermes Agentcurl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash# 2. 配置环境变量（~/.hermes/.env）export WIKIPATH="$HOME/wiki"                    # LLMWiki路径export OBSIDIANVAULTPATH="$HOME/wiki"         # Obsidian vault路径export OPENROUTERAPIKEY="sk-xxx"              # 或ANTHROPICAPIKEY等# 3. 运行配置向导hermes setup

> 来源: [飞哥的技术与烟火](https://mp.weixin.qq.com/s?__biz=MzAxNjU3NTY0MA==&mid=2454267765&idx=1&sn=e414be8d4879f9249133a40715bcdd27&chksm=8d0ed44fcb4cc001e85cf1d4258bfd98a6291e13f64fdb72498ef04b8a1f73d4d62bea3b77c9&mpshare=1&scene=1&srcid=0506S7pctFn72v5HRu3wiWgJ&sharer_shareinfo=c1c112da2712267c9217409d9f71ef7b&sharer_shareinfo_first=c1c112da2712267c9217409d9f71ef7b) | 2026-05-06

## 摘要

👇关注我，后续继续分享更多的 AI Agent、技术开发相关的文章.
前段时间在 GitHub 上看到
这个概念，其核心不过是让日积月累的记录"
"起来。趁着五一有空，我把之前
的实践与思考整理了一下，就有了下面的这篇记录。
传统的知识管理方式是「读→记→查」的线性链条，耗时长、易遗忘、难关联。
而 **Hermes Agent[1] + Obsidian[2] + LLM Wiki[3]** 这套组合，直接把知识流变成了「 ingest → synthesize → query → act 」的闭环系统：
- **Hermes Agent**：你的24小时在线的AI助理，能联网、能执行、能记忆、能跨平台工作
- **Obsidian**：双向链接的本地Markdown笔记软件，打造个人知识图谱
- **LLMWiki**：Karpathy推崇的wiki架构，让知识像维基百科一样结构化、可追溯、持续演进
这套组合的终极形态是：**Agent为你吸收信息、整理成体系化的wiki，你随时可以通过对话查询，所有知识沉淀在本地Markdown文件里，永远属于你。**
| 场景 | 输入 | 输...

## 相关实体

[[Anthropic]], [[DeepSeek]], [[GitHub]], [[Hermes]], [[MCP]], [[Obsidian]], [[OpenAI]], [[OpenRouter]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[内容创作]], [[微调]], [[知识图谱]], [[知识管理]]
