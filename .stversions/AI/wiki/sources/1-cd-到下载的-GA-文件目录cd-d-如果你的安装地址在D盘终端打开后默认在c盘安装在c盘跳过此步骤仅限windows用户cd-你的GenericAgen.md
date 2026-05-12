---
tags: [Hermes, Agent, Claude, GitHub, 飞书, Prompt, API, Python]
source: "AI教员"
created: 2026-04-30
updated: 2026-05-10
category: Hermes
---

# 1. cd 到下载的 GA 文件目录cd d:     (如果你的安装地址在D盘，终端打开后默认在c盘,安装在c盘跳过此步骤，仅限windows用户)cd "你的GenericAgent路径"               （示例： cd D:/Document/GenericAgent-main） # 2. 安装最小环境依赖pip install streamlit pywebview# 如果你的 Python 3 对应 pip3，则用：pip3 install streamlit pywebview

> 来源: [AI教员](https://mp.weixin.qq.com/s?__biz=MzY4NTE5Mjg0NA==&mid=2247484575&idx=1&sn=94bc4e6a65112b3fff2f81f8d90db2e8&chksm=f200ae98d000b2ee9ffe577a2f87027d20c3c75a75384d9be446de3a59aa1f4448cfcc7a5e07&mpshare=1&scene=1&srcid=0430OC4655XvFmqBWJ7jN37s&sharer_shareinfo=14e2e6d18e848f29dfba18fb64389025&sharer_shareinfo_first=14e2e6d18e848f29dfba18fb64389025) | 2026-04-30

## 摘要

**Generic Agent**（简称 **GA**）是一个本地运行的 AI 助手框架。与只能聊天的 AI 不同，GA 的核心理念是**替你把事情做完**——它能读取代码、操作文件、调用工具、连接各种平台，自动完成复杂任务。
你可以把它理解为：一个永远在线、听得懂人话、并且真的会动手干活的数字员工。
它不是一个聊天机器人，而是一个**能替你执行任务的 Agent**。
GA 的几个核心特点：
- **本地运行**：代码跑在你自己的电脑上，数据不出本地，更安全。
- **多模型支持**：可以配置 Claude、GPT、DeepSeek、智谱等任意大模型，也可同时配置多个模型做自动切换。
- **工具丰富**：能读文件、写代码、执行命令、管理 Git、安装 Python 依赖，还能接入钉钉、飞书、企业微信、QQ、Telegram 等通讯平台。
- **自动完成任务**：你说一句话，它会自己规划步骤、调用工具、给出结果，不需要你手动一步步操作。
- **持续进化**：GA 能读取自己的代码，自己安装缺失的依赖，自己建立 Git 连接——你的指令越多，它越懂你需要什么。
想象这样一个场景：
...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[DeepSeek]], [[GLM]], [[GPT5]], [[GitHub]], [[OpenAI]], [[OpenClaw]], [[OpenRouter]], [[Python]], [[WorkBuddy]], [[微信]], [[钉钉]], [[飞书]]

## 相关概念

[[Function-Calling]], [[MultiAgent]]
