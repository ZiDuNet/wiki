---
tags: [Agent, Claude, GitHub, PPT, Prompt, API, OpenAI, Skill]
source: "有料黑科技"
created: 2026-05-07
updated: 2026-05-10
category: Agent
---

# 方式 A：Git 克隆git clone https://github.com/mucsbr/ppt-agent-workflow-san.git# 将文件夹放到 skills 目录即可# 方式 B：下载 ZIP# 从 GitHub 下载 zip → 解压 → 放到 skills 目录

> 来源: [有料黑科技](https://mp.weixin.qq.com/s?__biz=MzUxNDAxMzQyMw==&mid=2247496019&idx=1&sn=c00f7eb880ce14060984bb14fcf0bbda&chksm=f85b8f643d20c65253ca75f06df7f244360e54a7b50f31d787b73ffc4af68d5ba4ada546194e&mpshare=1&scene=1&srcid=0507HwmxnsmNbs16J2Slq2Sd&sharer_shareinfo=3ecd52634215f3a70ba128077f7ec144&sharer_shareinfo_first=3ecd52634215f3a70ba128077f7ec144) | 2026-05-07

## 摘要

ppt-agent-workflow-san 是一套开源的 PPT 制作工作流，核心理念是"约束工作流，不约束实现"。它把 PPT 制作拆成 10 个阶段，提供 6 套 prompt 模板，支持从调研简报到最终复核的全流程。本文介绍其核心设计、实际效果和安装使用方式。
GitHub 上有个项目叫 `ppt-agent-workflow-san，`作者 mucsbr 在 Linux.do 论坛分享了一套做 PPT 的思路。
它不是一个"一键生成 PPT"的工具。**它是一套工作流。**
区别在哪？普通的 AI PPT 工具是黑箱——你输入主题，它输出文件，中间发生了什么你不知道，也控制不了。而这个工作流把整个过程拆成了 **10 个阶段，**每一步都有明确的输入和产出，你可以停在任意一层：
| 层级 | 产出 | 适合场景 |
| --- | --- | --- |
| research-brief | 调研简报（关键事实、数据来源、风险点） | 还没想清楚方向 |
| outline | 大纲（JSON 格式，含每页目标） | 已有素材需要结构化 |
| planning-draft ...

## 相关实体

[[ChatGPT]], [[Claude]], [[GitHub]], [[WorkBuddy]]

## 相关概念

[[工作流自动化]]
