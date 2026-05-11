---
tags: [Agent, OpenClaw, 企业落地, 知识库, 视频制作, 部署]
sources: ['微信公众号/OpenClaw/“影子 Agent”大爆发：如何排查潜伏在企业内网深处的、那些只有 IP 没有身份的 OpenClaw 实例？.md']
created: 2026-05-10
updated: 2026-05-10
---

# “影子 Agent”大爆发：如何排查潜伏在企业内网深处的、那些只有 IP 没有身份的 OpenClaw 实例？

**Source:** OpenClaw 公众号文章
**Category:** OpenClaw
**Date ingested:** 2026-05-10
**Type:** article

## Summary

> 📎 来源: 快AI慢调 | 时间: 2026-04-24 11:29 周二，一位在某大型制造业做 CISO（首席信息安全官）的朋友给我打了个电话。 他语气里透着一种见鬼了的困惑：“我们内网的防火墙告警疯了。数据中心监控到，行政部有一台平时只用来做登记的破旧台式机，**每天都在往海外疯狂发送数以万计的加密 API 请求。**”

## Key Claims

- 没有恶意代码：** 它运行的可能就是原生的 Python、Node.js 或者 Docker 进程。
- 通信白名单：** 它往外发包的目标地址，往往是 OpenAI、Anthropic、或者你们公司自己采购的云端模型接口。这些地址通常在防火墙的白名单里。
- 行为伪装：** 它的读写动作，在系统看来，就像是一个正常员工在疯狂阅读文档、整理表格。

## Entities Mentioned

- [[OpenClaw]]

## Concepts Covered

- [[Sub-Agent]]
- [[企业落地]]
- [[数据安全]]
- [[本地部署]]
- [[爬虫]]
- [[知识库构建]]
- [[视频制作]]

## Related Sources

- [[OpenClaw文章索引]]
