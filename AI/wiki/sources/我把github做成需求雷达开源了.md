---
type: source-summary
source: 微信公众号/GitHub/我把Github做成需求雷达，开源了.md
author: 极客杰尼
date: 2026-05-28
tags:
  - GitHub
  - 需求挖掘
  - Codex
  - Hermes
  - 独立开发
  - 工具
entities:
  - Codex
  - Hermes-Agent
  - Claude-Code
  - GitHub Demand Radar
concepts:
  - 需求雷达
  - GitHub Issue分析
  - AI自动化研究
  - 需求挖掘
---

# 我把 Github 做成需求雷达，开源了

## 核心内容

作者开源了 **GitHub Demand Radar** 项目——一个从 GitHub 热门项目 Issue/PR 中挖掘真实需求的 Skill。

### 想法起源

找项目最难的不是写代码，而是判断"这个东西值得做"。热门项目的 Issue/PR 藏着大量小众需求：用户留言、讨论、写替代方案。

### 实验案例

扫描 [[Claude-Code]] 项目时发现 **buddy 桌宠功能** 需求热度极高：
- 用户反复提起
- 有人补充具体场景
- 情绪很强
- 需求边界逐渐清楚

后来很多 Claude Code 定制桌宠项目涌现，情绪价值拉满。

### 工具化流程

上个月做成 **Github Demand Radar Skill**：
- 之前：手动翻 Github Trending、搜关键词、看用户留言
- 现在：交给 [[Codex]]，每天早上定时发简报

### 配置方法

1. 打开 Codex 桌面端，下载 `geekjourneyx/github-demand-radar` 项目
2. 输入提示词：
   > 使用 Github Demand Radar 技能，设置一个自动化，每个工作日早上给我一份 Github 简报，扫描 Github Trending，以及 Claude Code / agent skills 相关 topic，从 issue 和 PR 中找到真需求。

### 判断标准

一个小功能背后可能藏着真实需求：
1. 用户反复提起
2. 有人补充具体场景
3. 情绪很强
4. 需求边界逐渐清楚

重点观察数据背后的商业信号。

## 关键洞察

- **需求发现**：从偶然刷到变成每天稳定出现的输入
- **Agent价值**：Agent 帮用户整理线索，但最终判断仍需人的决策
- **时效性**：buddy 功能热度高峰已过，产品化窗口需把握时机

## 相关链接

- 项目地址：geekjourneyx/github-demand-radar
- 作者教程：[Codex 还能定制桌面宠物...（附教程）](https://mp.weixin.qq.com/s?__biz=MzA5Njg4Mzk0NQ==&mid=2649825622&idx=1&sn=960d36504b04cf0df644aa3049d71a84&scene=21#wechat_redirect)

## 相关实体

- [[Codex]] — OpenAI 命令行 AI 编程工具，用于定时推送需求简报
- [[Hermes-Agent]] — 可通过 Skill 实现 GitHub 需求雷达功能
- [[Claude-Code]] — 被扫描的热门项目之一，buddy 功能需求热度高

## 相关概念

- [[需求挖掘]] — 从 GitHub Issue/PR 中发现真实需求的方法论
- [[需求雷达]] — 自动化扫描 GitHub 热门项目获取需求线索的系统
- [[GitHub Issue分析]] — 将 Issue 当用户留言区，PR 当修改方案
- [[AI自动化研究]] — 用 Agent 定时执行需求发现任务