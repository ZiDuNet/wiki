---
tags: [Hermes, Agent, Claude, API, OpenAI, Skill, OpenClaw]
source: "云起泊言"
created: 2026-04-26
updated: 2026-05-10
category: Hermes
---

# 你的 Hermes 为什么总是记不住？这篇教你如何给 Hermes 添加长期记忆！

> 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868882&idx=1&sn=5b5c0d470d31c10deeca597314b77526&chksm=86e47c19004a08b7b2e8b0b52feca6734bc968c067c2d1d5a9e039f13acf648ce36e9c68f27f&mpshare=1&scene=1&srcid=04262EPPrvgZGCgMzW7hA66i&sharer_shareinfo=210135d8150d13156080d9b79a03bd6d&sharer_shareinfo_first=210135d8150d13156080d9b79a03bd6d) | 2026-04-26

## 摘要

在使用 Hermes Agent 之前，你是不是也被它强大记忆能力所吸引，然后从 OpenClaw 转到了 Hermes，但是在实际使用过程中，你却经常遇到前几分钟跟它说过的事情，转头就忘了？吐槽最多的就是：“我明明告诉过它，为什么还不记得？”
我之前就是这么跟 Hermes Agent 相处的，每次“失忆”都觉得很郁闷。后来我研究了一下外置的记忆增强工具，才找到了适合自己的方案。
今天我就简单聊聊 Hermes 的内置记忆以及外置记忆工具的优缺点，以及我最终的选择。
Hermes 的内置记忆通常由两个文件组成，存储在 `~/.hermes/memories/` 目录下，如果你是多 Agent，那么记忆目录在各自 Profile 下的 `memories` 目录下。
- **MEMORY.md** 是“工作笔记本”，记录环境配置、项目经验、踩过的坑；针对 MEMORY.md，Hermes 存在 **2200** 字符的系统阈值（硬限制）。
- **USER.md** 是“用户档案”，存着你的偏好、沟通风格、技能水平；针对 USER.md，Hermes 存在 **1375** 字符的系统...

## 相关实体

[[ChatGPT]], [[Claude]], [[DeepSeek]], [[GPT5]], [[Hermes]], [[Notion]], [[OpenClaw]]

## 相关概念

[[MultiAgent]], [[知识图谱]], [[记忆系统]]
