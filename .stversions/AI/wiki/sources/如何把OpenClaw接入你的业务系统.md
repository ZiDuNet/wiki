---
tags: [OpenClaw, Agent, GitHub, 飞书, Prompt, API, OpenAI, Skill]
source: "i龙虾"
created: 2026-04-24
updated: 2026-05-10
category: OpenClaw
---

# 如何把OpenClaw接入你的业务系统

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484106&idx=1&sn=66bce0ae104e19f3852fd4a15fead99b&chksm=eae2d11551ac3a5d3eab54cab6906821d53bdebfa95a15ac65c8aecf3aea759d35996ed2a63b&mpshare=1&scene=1&srcid=0424RLmiHp33wVli5nrGzVP1&sharer_shareinfo=c2af37068de5e80753e6d104d357761a&sharer_shareinfo_first=c2af37068de5e80753e6d104d357761a) | 2026-04-24

## 摘要

文章比较长，建议先收藏再看。
如果你只是想让龙虾响应外部事件，看前半部分就够了。如果想把OpenClaw 对接自己的业务系统——比如工单触发 AI 分析、合同上传自动审查——后半部分专门讲这个，包括结果怎么回传。
OpenClaw 的 Webhook 挂在网关上，默认端口 18789，路径默认 `/hooks`。在 `openclaw.json` 配置文件里加这几行开启：
{
"hooks": {
"enabled": true,
"token": "your-shared-secret",
"path": "/hooks"
}
}
的时候
是必填的，没有 token 根本启不来。认证方式官方推荐用请求头：
也支持 `x-openclaw-token: `
最轻量的触发方式，请求体只有两个字段：
{ "text": "收到新邮件", "mode": "now" }
是事件描述，作为系统行写进主会话队列。
有两个值：
立即触发心跳，
等下次定期检查再处理。
适合场景：外部脚本监控某个目录，出现新文件就通知龙虾处理。逻辑简单、不需要隔离运行环境时用这个。

## 相关实体

[[GitHub]], [[OpenAI]], [[OpenClaw]], [[飞书]]

## 相关概念

[[CICD]], [[MultiAgent]]
