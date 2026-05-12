---
tags: [Hermes, Agent, Claude, GitHub, 飞书, RAG, API, Python]
source: "DNOPC"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# npm 一键安装（推荐）npm install -g hermes-web-uihermes-web-ui start# 打开 http://localhost:8648# 一键安装脚本（自动检测 Node.js）bash <(curl -fsSL https://raw.githubusercontent.com/EKKOLearnAI/hermes-web-ui/main/scripts/setup.sh)# Docker Composedocker compose up -d --build hermes-agent hermes-webui# 打开 http://localhost:6060

> 来源: [DNOPC](https://mp.weixin.qq.com/s?__biz=MzY4ODE5Mjc0MQ==&mid=2247483827&idx=1&sn=5de510dce3d57747032cc4046227236e&chksm=f2d6fdeea64fc8c4b7f891ee29f54be4b60590c511ee52c18a15f092c8a2566bfbd1a5b963a1&mpshare=1&scene=1&srcid=04206w5lvqS8vILVxHI8UXMH&sharer_shareinfo=41f377ad09bae87f9ac15bf973eb9b23&sharer_shareinfo_first=41f377ad09bae87f9ac15bf973eb9b23) | 2026-04-22

## 摘要

很多朋友跑着 Hermes Agent，日常操作还是在终端里敲命令——黑底白字，一行一行读输出。
命令行固然很好，Hermes Agent 设计之初就是 terminal-first 的产品。但问题是：**当你需要管理多个会话、配置 Telegram Bot、查看 Token 消耗、设置定时任务时、更优秀的人机交互，终端的效率就开始拖后腿了。**
好消息是，开源社区已经跑出了几套非常成熟的 Web 面板方案。它们不是简陋的 demo，已经是功能覆盖完整、体验对标商业软件的成熟产品。
今天这篇，我们来一次深度横评，把目前 GitHub 上最主流的四套方案全部拆解：**EKKOLearnAI/hermes-web-ui、nesquena/hermes-webui、itq5/OpenClaw-Admin、open-webui/open-webui**。看完你就知道自己该选哪个了。
欢迎关注公众号或加入社区社群微信号:dnhopc，一起探索AI与OPC的更多可能性。
在开始之前，先上一张全局对比表，建立整体认知：
| 维度 | EKKO Web UI | nesquena WebUI | Op...

## 相关实体

[[Anthropic]], [[ChatGPT]], [[Claude]], [[DeepSeek]], [[Docker]], [[GitHub]], [[Hermes]], [[Markdown]], [[Mermaid]], [[Nodejs]], [[OpenAI]], [[OpenClaw]], [[OpenRouter]], [[Python]], [[微信]], [[钉钉]], [[飞书]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[嵌入向量]]
