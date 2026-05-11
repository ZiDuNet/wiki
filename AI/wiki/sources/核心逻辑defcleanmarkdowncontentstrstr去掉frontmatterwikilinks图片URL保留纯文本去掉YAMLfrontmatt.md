---
tags: [Hermes, Agent, Obsidian, RAG, API, OpenClaw]
source: "飞哥的技术与烟火"
created: 2026-04-29
updated: 2026-05-10
category: Hermes
---

# 核心逻辑def cleanmarkdown(content: str) -> str:    """去掉 frontmatter、wikilinks、图片、URL，保留纯文本"""    # 去掉 YAML frontmatter    if content.startswith("---"):        end = content.find("---", 3)        if end > 0:            content = content[end+3:]    # 去掉 [[wikilinks]] 但保留文字    content = re.sub(r'\[\[([^\]|]+?)\]\]', r'\1', content)    # 清理空格    return content.strip()

> 来源: [飞哥的技术与烟火](https://mp.weixin.qq.com/s?__biz=MzAxNjU3NTY0MA==&mid=2454267749&idx=1&sn=79d74a479ef0eb2cdee22555b95647f6&chksm=8df19e4cba940206aecd61f0bd500e102eca1106b7df6d338837e481cb6b76b061928230ce4b&mpshare=1&scene=1&srcid=04298G3Xmzv826pW5FIs80e1&sharer_shareinfo=a7ad769c3c27b332602047dae4034e64&sharer_shareinfo_first=a7ad769c3c27b332602047dae4034e64) | 2026-04-29

## 摘要

👇关注我，后续继续分享更多的 AI Agent、技术开发相关的文章.
有几天没有写了🥲，争取保持每周1-2篇记录📝，经过多年的积累其实已经有很多总结的md笔记🥲，之前Emacs  org-mdoe也有部分笔记记录，切换到hermes agent智能体后就一直想能否能让大模型回答问题先检索以前记录的笔记内容这样会回答的更精确点，这段时间也折腾尝试过很多方法，也就以下的方案稳步运行到现在。
我试过以下几种「知识管理」方案，全都拉垮了：
| 方案 | 问题 |
| --- | --- |
| **文件夹分类** | 一个笔记可能同时属于「心理学」「决策」「投资」，放哪都不对 |
| **标签系统** | 标签越加越多，最后忘了自己打了什么标签 |
| **全文搜索** | 搜「杠铃策略」找不到我写过「塔勒布 杠铃」的那篇笔记 |
| **纯人工记忆** | 我已经不是 20 岁了，记不住 |
**核心痛点不是「找不到文件」，而是「想不起当时是怎么想的」。**
Hermes RAG 的目标是：**你写过的所有东西，都能用自然语言「问」出来**。
架构图：
**关键技术决策：**
1. 1. *...

## 相关实体

[[Gemini]], [[Hermes]], [[Markdown]], [[Obsidian]], [[OpenClaw]], [[Qwen]]

## 相关概念

[[AI-Agent]], [[嵌入向量]], [[知识管理]]
