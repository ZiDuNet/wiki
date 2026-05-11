---
tags: [Claude, MCP, Skill]
source: "Super话AI"
created: 2026-04-29
updated: 2026-05-10
category: Claude
---

# Part2-【需求开发】OpenSpec实践SDD范式编程&【Git Hooks】配置pre-commit/commit-msg hooks&【安全】审查

> 来源: [Super话AI](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026254&idx=1&sn=9477b9dbfaff52072947961966982191&chksm=8626ec42b992311447781cd3c0eb4883e41729026000080c960f600cdc60bb137a098f12724e&mpshare=1&scene=1&srcid=0429S9SS83cV04qBSzloJrw5&sharer_shareinfo=c7b16e44f736357272b340c0e826249b&sharer_shareinfo_first=c7b16e44f736357272b340c0e826249b) | 2026-04-29

## 摘要

上一篇[(一)ClaudeCode在企业级前端项目上的实践](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026223&idx=1&sn=167f191b35b85a6e77f64759a64f8966&scene=21#wechat_redirect)，主要介绍了Claude Code在前端项目的初始化操作，以及实现【代码审查、规范检查、架构设计、新功能开发、项目源码分析】的能力。
第二篇文章主要回答3个问题：1、我们应该怎么开发一个需求？2、需求开发完了，要提交代码到git时如何触发检查机制？3、最后，提交的代码如何保证没有泄露敏感信息？
我本地使用的是Claude Code（以下简称cc）+deepseek-v4-pro进行演示。
可以参考我之前写的文章[团队老项目落地OpenSpec实践指南](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026198&idx=1&sn=775ee9d9205962bd7f651ccdf3bcb2e0&s...

## 相关实体

[[Claude-Code]], [[Claude]], [[DeepSeek]], [[Node.js]]

## 相关概念

[[CICD]], [[代码审查]]
