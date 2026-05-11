---
tags: [OpenClaw, Agent, Claude, MCP, Prompt, API, OpenAI]
source: "i龙虾"
created: 2026-04-24
updated: 2026-05-10
category: OpenClaw
---

# OpenClaw这次更新后终于重回轻盈

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484443&idx=1&sn=89a6277c9d4cb42dbfb941f981314ccd&chksm=ea0b452709c7649498e169314374719d2c71481c15d0fda4d36a6d929ad2fd83ef8c879e2eef&mpshare=1&scene=1&srcid=0424FGWgRvoyNMQNPcoZLxvY&sharer_shareinfo=d340d0d395a4cca0f01b35fe0d63b6ac&sharer_shareinfo_first=d340d0d395a4cca0f01b35fe0d63b6ac) | 2026-04-24

## 摘要

4月21日到23日，OpenClaw 连出三版。节奏挺快的——三天三次推送，而且不是小修小补，4.20 和 4.22 都是内容量很大的版本。
这次更新后一个最明显的感受是OpenClaw终于又恢复了原先的轻盈。之前某个版本更新后执行openclaw命令就会变卡，CPU飙升，像执行个openclaw docker后就很慢，这次更新后终于正常了。
4.20 的 changelog 大概六七十条，但安全相关的修复集中得很明显，几乎占了三分之一。
**设备配对权限收紧。** 以前非管理员设备能看到其他设备的配对列表，能批准别的设备发来的配对请求。现在非管理员只能管自己的，看不到别人的，也批准不了别人的请求。
**WebSocket 广播加了权限门槛。** 之前配对作用域内的会话能被动接收其他 session 的聊天内容，包括它本不该看到的消息。现在接收对话内容至少需要
，未知类型的广播事件也默认隔离。
**Agent 无法再改网关核心配置。** 这个改动我觉得挺重要的。以前 AI 可以通过
或
指令修改网关配置，现在这条路被堵死了——沙箱设置、插件信任、网关认证、SSRF 策略、MCP 服务器...

## 相关实体

[[Anthropic]], [[Claude]], [[MCP]], [[OpenAI]], [[OpenClaw]]

## 相关概念

[[多模态]]
