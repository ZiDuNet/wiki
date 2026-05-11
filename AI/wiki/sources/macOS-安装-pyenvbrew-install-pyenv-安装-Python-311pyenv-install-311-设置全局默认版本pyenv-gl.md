---
tags: [Hermes, Agent, GitHub, API, Python]
source: "CostaLong"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# macOS 安装 pyenvbrew install pyenv# 安装 Python 3.11pyenv install 3.11# 设置全局默认版本pyenv global 3.11# 验证python3 --version

> 来源: [CostaLong](https://mp.weixin.qq.com/s?__biz=MzA5NzgzNjE1Ng==&mid=2247485784&idx=1&sn=bfe105edcf35830c6fe3f96bb7c5c6ad&chksm=914c243ec657eb839ad4c43ed8347232ed5642204284c25f495892ba66bce662178fbf3e0f9c&mpshare=1&scene=1&srcid=0420BzIgGkslTJKBlKfDsIax&sharer_shareinfo=2126254ac3b2a1964df362ae07cccfe1&sharer_shareinfo_first=2126254ac3b2a1964df362ae07cccfe1) | 2026-04-20

## 摘要

Hermes Agent 安装配置流程图，展示从环境准备到第一个 Agent 运行的全过程
**ℹ️ 📚 系列导航**
本文是《AI Agent 进阶教程》系列第 2/22 篇。
上一篇：[什么是 Hermes Agent：让 AI 从问答升级到替我做事](https://mp.weixin.qq.com/s?__biz=MzA5NzgzNjE1Ng==&mid=2247485773&idx=1&sn=71ce212219d2f8d3a8e40a61829db225&scene=21#wechat_redirect)
下一篇：核心概念：Memory、Tool、Agent Loop
上篇介绍了 Hermes Agent 的概念，这篇直接动手。安装方式是从源码克隆 + uv 安装，不同于常见的 pip install。这篇把安装问题的排查方法整理清楚，帮你 5 分钟搞定。
Hermes Agent 基于 Python 开发，需要 **Python 3.11**。这篇把安装问题的排查方法整理清楚，帮你 5 分钟搞定。
先确认你的版本：
|  |  |
| --- | --- |
|  | b...

## 相关实体

[[GitHub]], [[Hermes]], [[Python]]

## 相关概念

[[AI-Agent]]
