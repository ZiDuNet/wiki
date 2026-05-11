---
tags: [Hermes, Agent, Claude]
source: "智行问道"
created: 2026-05-06
updated: 2026-05-10
category: Hermes
---

# 我给Hermes配了个日报助理

> 来源: [智行问道](https://mp.weixin.qq.com/s?__biz=MzY4NDE5MDg2OA==&mid=2247486350&idx=1&sn=74278cc3afb406f6ceff0ae658f688ea&chksm=f29040d7f363e904da2a1fba65b085b1df9b2037e595681b725c9db00a9b3c5f63baf601a4a0&mpshare=1&scene=1&srcid=05062kEZMtauxjU2lVKz0CuR&sharer_shareinfo=bd2325176f70f6568dc1a1ac30365800&sharer_shareinfo_first=bd2325176f70f6568dc1a1ac30365800) | 2026-05-06

## 摘要

智行问道 · 五一特辑 Day3
我给 Hermes 配了个
日报助理
每天早上8点，AI热点准时推送到微信
by 深海 | 智行问道 | AI实战
|  |  |  |
| --- | --- | --- |
| 2000字 | 3步操作 | 3分钟阅读 |
**🤔 先问个问题**
每天早上醒来，你做的第一件事是什么？我的是打开微信，看看AI圈有什么热点。但为了那两三条有效信息，每天花5-10分钟翻公众号，一个月就是2.5-5小时。这不是阅读，是信息焦虑。
**💡 所以我想让 Hermes 帮我做这件事**
每天早上8点，搜一遍全网AI热点 → 提炼5条摘要 → 推送到我的微信。我睁眼打开微信，消息列表里已经躺好了。3步搞定，不需要写代码。
**⚡ 第1步：创建日报Agent**
Hermes 里有预设的 OPC 模板：
hermes agent create --template one-person-company --name daily-report
**⚡ 第2步：配 Cron 定时任务**
hermes cron add \
--schedule "0 8 \* \* \...

## 相关实体

[[Claude]], [[Hermes]], [[微信]]

## 相关概念

[[多模态]]
