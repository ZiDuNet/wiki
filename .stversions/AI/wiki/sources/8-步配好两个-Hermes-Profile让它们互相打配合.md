---
tags: [Hermes, Agent, Claude, GitHub, API, Skill]
source: "AI赋能说"
created: 2026-05-04
updated: 2026-05-10
category: Hermes
---

# 8 步配好两个 Hermes Profile，让它们互相打配合

> 来源: [AI赋能说](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg==&mid=2247488725&idx=1&sn=60db1ef29da4f479bec67d045a12175d&chksm=ea37fedd36b0b80d9c5db9a6c718f387d4c86f19d6cc4702837e1bc1696e4c08aa5f20a6765e&mpshare=1&scene=1&srcid=0504Lj09uUloWnpTsiFfQLy8&sharer_shareinfo=1510b584cee1d547d0dfea4408d40085&sharer_shareinfo_first=1510b584cee1d547d0dfea4408d40085) | 2026-05-04

## 摘要

昨晚试了一件事。
让两个 Hermes Agent 协作。一个负责查资料，一个负责写文章。各有各的记忆，各有各的工具。跑通之后我盯着屏幕看了好一会。
一个人的电脑上，跑着一支小团队。
这篇教程带你走一遍。8 步，分 3 个阶段。跟着做完，你也能配好「研究员」和「写手」两个 Profile，让它们协作完成一个从调研到成稿的任务。
两个 Profile 各自独立。通过文件系统传递结果。研究员写完调研放到共享目录，写手读取后开始写。
- Hermes 已安装，版本 v0.6.0 或以上
- 终端能跑
命令
- 有一个可用的 API Key（OpenRouter 或其他 provider）
一条命令：
Hermes 会在
下创建独立的配置目录。
验证：
看到
就对了。这个 Profile 有自己的配置空间，不会和默认 Profile 冲突。
同样的操作：
验证：
两个 Profile 创建完毕。各自独立。各自有自己的记忆文件、配置文件、Skill 目录。
编辑研究员的配置：
写入以下内容（根据你的实际情况改 API Key 和模型名）：

## 相关实体

[[Anthropic]], [[Claude]], [[GitHub]], [[Hermes]], [[OpenRouter]]

## 相关概念

[[AI-Agent]], [[MultiAgent]], [[工作流自动化]], [[记忆系统]]
