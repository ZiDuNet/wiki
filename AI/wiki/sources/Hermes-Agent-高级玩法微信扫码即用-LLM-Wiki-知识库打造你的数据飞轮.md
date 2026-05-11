---
tags: [Hermes, Agent, Claude, GitHub, Obsidian, PPT, RAG, API]
source: "AI炼金社"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮

> 来源: [AI炼金社](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA==&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=975726407f2e6415b216570027722d00671974c034bee3b40f1360e37c481362c5d31da0a999&mpshare=1&scene=1&srcid=0420WK3Q10rE7Dsn5vnXgo07&sharer_shareinfo=413302b6419c52a533c57133c29572c9&sharer_shareinfo_first=413302b6419c52a533c57133c29572c9) | 2026-04-20

## 摘要

Andrej Karpathy 最近发了一条推文，16 小时内 1600 万次浏览。他说自己不再用 LLM 写代码，而是用来**建知识库**。
核心思路很简单：传统 RAG 每次查询都要从头检索，没有积累。他让 LLM 维护一个持久 Wiki——新增内容自动编译进去，知识复利增长。
这条推文火了之后，Hermes Agent 立刻实现了这个工作流。今天讲两个高级功能：**微信原生集成**和**LLM Wiki 知识库**。
Hermes Agent 支持**个人微信账号**直连，用的是腾讯 iLink Bot API。不需要公网端点、不需要 Webhook，HTTP 长轮询就够。
提示中选择 **Weixin**。向导自动完成：
- 请求二维码 → 显示在终端或提供 URL → 等你扫码 → 手机确认登录 → 保存凭证到
成功后看到：
QR 登录完成后，在
设置：
适配器恢复凭证，连接 iLink API，开始长轮询接收消息。
- 私聊/群聊消息（可配置访问策略）
- 图片/视频/文件/语音媒体支持
- AES-128-ECB 加密 CDN 媒体传输
- Markdown 格式自动适配...

## 相关实体

[[GitHub]], [[Hermes]], [[Markdown]], [[Obsidian]], [[OpenAI]], [[微信]]

## 相关概念

[[嵌入向量]], [[微调]], [[知识图谱]], [[知识管理]]
