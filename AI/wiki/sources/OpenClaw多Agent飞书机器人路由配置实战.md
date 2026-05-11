---
tags: [OpenClaw, Agent, 飞书, Skill]
source: "不灭的传说"
created: 2026-04-21
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw多Agent飞书机器人路由配置实战

> 来源: [不灭的传说](https://mp.weixin.qq.com/s?__biz=MzA3ODk4OTU4Mg==&mid=2454625893&idx=1&sn=59c5e3a95f02600e7e1d75acbe077547&chksm=891ed41d337189fd0ffd149283636bec0fee7a78549659b09dba577735adc5e645cde04d2de0&mpshare=1&scene=1&srcid=0421XAV4lTLoblrPbBxk2NmJ&sharer_shareinfo=458e8019740036df5116a0ac71be361e&sharer_shareinfo_first=458e8019740036df5116a0ac71be361e) | 2026-04-21

## 摘要

最近在部署OpenClaw多Agent系统时，遇到了一个棘手的问题：我们配置了3个飞书机器人，分别对应3个不同的AI专家Agent（总指挥、编程大师、投资顾问）。但所有用户发送给这些机器人的消息，都被错误地路由到了总指挥Agent。
问题现象：
- 用户向编程大师机器人发送技术问题 → 总指挥回复
- 用户向投资顾问机器人发送财经咨询 → 总指挥回复
这完全打乱了我们的多Agent协作架构！
检查飞书开放平台配置
✅-所有机器人APPID和APP Secret配置正确，事件订阅方式均为"使用长连接接收事件"（WebSocket模式）
检查OpenClaw配置文件~/.openclaw/openclaw.json✅
agent配置
渠道飞书机器人配置
检查Gateway日志✅
WebSocket连接都已建立,消息能被正确接收
但路由决策错误：所有消息都路由到agent:commander
通过阅读OpenClaw官方文档《Multi-Agent Routing》，发现了关键信息：
核心要点：
1. 多Agent路由必须配置bindings
2. accountId是路由的关键标识
3. ...

## 相关实体

[[OpenClaw]], [[飞书]]

## 相关概念

[[Agent架构]], [[Multi-Agent]]
