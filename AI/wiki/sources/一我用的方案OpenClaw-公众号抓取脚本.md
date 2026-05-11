---
tags: [OpenClaw, Obsidian, 飞书, RAG, Python]
source: "智码探路"
created: 2026-04-21
updated: 2026-05-10
category: OpenClaw
---

# 一、我用的方案：OpenClaw + 公众号抓取脚本

> 来源: [智码探路](https://mp.weixin.qq.com/s?__biz=MzU2NDIyOTUxMw==&mid=2247483657&idx=1&sn=8b2309f257fc798da3019b9a8d77b471&chksm=fd6e85fb7090a749960fd0f93b6da488f172d546de266c1e83e99c4c95627ed2ccdbed77b1af&mpshare=1&scene=1&srcid=04215UBJrD5dDc2GvKjtd599&sharer_shareinfo=9daf2f7fb5dbe0b0dc77c50fe3c1996f&sharer_shareinfo_first=9daf2f7fb5dbe0b0dc77c50fe3c1996f) | 2026-04-21

## 摘要

你是不是也有这样的经历：
刷到一篇好文章，随手收藏，想着「有空再看」。结果收藏夹越堆越多，真要用的时候却找不到；或者文章被删了、链接失效了，想回头翻都翻不出来。
更麻烦的是，当你在做某个主题的调研——比如「AI 组织转型」「人机协同」——需要系统性地整理一批公众号内容时，只能一个个打开、复制、粘贴，再手动建文件夹、起名字，费时费力。
有没有办法，让公众号文章自动下载、自动分类，还能生成本地知识库索引？
有。我基于 OpenClaw 搭了一套工具，实现了这件事。
具体做法是：
写一个 Python 脚本
：用 Playwright 打开公众号链接，抓取正文和图片，保存为 HTML + TXT
用 jieba 做关键词分类
：根据预设的类别（战略与框架、实践与案例、工具与方法、组织与文化等），自动把文章归到对应目录
生成知识库索引
：自动生成 README.md，包含分类、标题、摘要、关键词，方便检索
在 OpenClaw 的 TOOLS.md 里声明这个工具
：AI 助手在对话中收到公众号链接时，可以主动调用脚本，帮你下载并整理
这样一来，你只需要：
在飞书或 Web 里对 AI 说：「...

## 相关实体

[[Notion]], [[Obsidian]], [[OpenClaw]], [[Python]], [[飞书]]

## 相关概念


