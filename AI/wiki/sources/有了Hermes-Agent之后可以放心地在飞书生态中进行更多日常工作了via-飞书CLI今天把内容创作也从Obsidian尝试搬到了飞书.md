---
tags: [Hermes, Agent, GitHub, Obsidian, 飞书, API, Python, Skill]
source: "Draco正在VibeCoding"
created: 2026-04-13
updated: 2026-05-10
category: Hermes
---

# 有了Hermes Agent之后，可以放心地在飞书生态中进行更多日常工作了（via 飞书CLI）！今天把内容创作也从Obsidian尝试搬到了飞书。

> 来源: [Draco正在VibeCoding](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247495474&idx=1&sn=66c4be39c844517be3146336279ae805&chksm=eb812d31b3e32d189e8ad73d042284ee027a73b339dd07cd8589fc1eb2157af5a55ce26d38e7&mpshare=1&scene=1&srcid=0410MGeDV787n73BZaxxyk3H&sharer_shareinfo=7b342d8f576aab8f536830de683152b8&sharer_shareinfo_first=7b342d8f576aab8f536830de683152b8) | 2026-04-13

## 摘要

但是，之前本地是有从写作到发布公众号的全套自动化/半自动化工作流的，而把写作搬到了飞书上，首先需要封装一个直接将飞书文档中的内容进行渲染并推送到微信公众号草稿箱的skill。
今天全程使用Hermes Agent完成了这个skill的创建，并且开源了：
**项目地址**：https://github.com/dracohu2025-cloud/draco-skills-collection/tree/main/feishu-doc-to-wechat-draft
以下是对这个skill的介绍~ 欢迎试用并给出反馈；如果用的还不错，请动动手指在Github上给我个star吧~
如果你平时用飞书写内容，然后复制粘贴到公众号后台，一定会遇到这些头疼的问题：
•飞书里的图片要一张张下载再上传
•表格复制过去格式全乱
•代码块没有高亮，显示成纯文本
•排版和预览时看到的效果不一致
这篇文章介绍一个开源工具，可以把飞书文档一键转成微信公众号草稿，图片自动上传，格式完整保留。
简单说，它解决三个核心问题：
**1. 图片自动处理**
飞书文档里的图片会自动下载，上传到微信素材库，替换成微信 CDN ...

## 相关实体

[[GitHub]], [[Markdown]], [[Python]], [[微信]], [[飞书]]

## 相关概念

[[Vibe-Coding]], [[内容创作]]
