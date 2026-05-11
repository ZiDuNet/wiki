---
tags: [Hermes, Agent, Claude, GitHub, 飞书, Prompt, API, Python]
source: "猿码"
created: 2026-04-27
updated: 2026-05-10
category: Hermes
---

# Hermes 配置项：一张表让你搞懂每个参数怎么配

> 来源: [猿码](https://mp.weixin.qq.com/s?__biz=MzU5MjgxNjAwMQ==&mid=2247488460&idx=1&sn=530e2eb14348864e4e1737f7ad7bc723&chksm=ff8662dddd2765408bbb76c8ef6b4cf94f829601a301fbcd5886ac6408f075051c0aece002f9&mpshare=1&scene=1&srcid=04271M3o8nUIoHtPYlNwOByu&sharer_shareinfo=0dae8f6f71acf7074596358e7c91b2ce&sharer_shareinfo_first=0dae8f6f71acf7074596358e7c91b2ce) | 2026-04-27

## 摘要

先给结论：**不需要逐个设置，开箱即用。**
从 OpenClaw 迁移到 Hermes 后，安装程序会问你是否复用已有配置。如果选"是"，你的模型 API、飞书/微信等渠道配置都会直接带过来，基本不用动。
但有 **5 大类配置**，建议知道它们的存在——不是为了改，而是为了有一天需要的时候知道去哪里找。
Hermes 的配置分布在两个文件里：
| 文件 | 路径 | 存放内容 |
| --- | --- | --- |
| 主配置 | `~/.hermes/config.yaml` | 所有配置项（YAML 格式） |
| 环境变量 | `~/.hermes/.env` | API Key 等敏感信息 |
**三个常用命令：**
这四个配置决定 Hermes 用什么模型、在哪些渠道工作。**迁移过来后通常不用改**。
指定 Hermes 对话使用的大模型。可以是模型名称字符串，也可以是一个完整对象：
**怎么配：**
- 交互式：`hermes model` 按向导选择
- 直接改：`hermes config set model "anthropic/claude-sonnet-...

## 相关实体

[[Anthropic]], [[Claude]], [[Docker]], [[GitHub]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[Python]], [[微信]], [[飞书]]

## 相关概念

[[浏览器自动化]], [[记忆系统]]
