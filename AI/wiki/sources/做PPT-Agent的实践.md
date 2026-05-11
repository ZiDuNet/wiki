---
tags: [Agent, GitHub, PPT, Prompt, API, Python, OpenAI]
source: "阿布布爱读书"
created: 2026-04-29
updated: 2026-05-10
category: Agent
---

# 做PPT Agent的实践

> 来源: [阿布布爱读书](https://mp.weixin.qq.com/s?__biz=MjM5MzQ5ODExNw==&mid=2247483984&idx=1&sn=794fbf712c18612d9c0fb150a7662538&chksm=a7ae7f87e907813b0574fbe6e436e362c8a4a5298e6b5c1267d908273efc635680dbc1bf4e97&mpshare=1&scene=1&srcid=0429Bqg83uoUEqe2ZKk2z5U3&sharer_shareinfo=76d1854d42eb88347441f3acca61cc93&sharer_shareinfo_first=76d1854d42eb88347441f3acca61cc93) | 2026-04-29

## 摘要

DEEP DIVE / 工程实践
从一份业务报告到一份咨询级 PPT，中间需要多少步？答案是：**6 个 Agent、2 个检查点、和一个"不丢信息"的要求**。
◆ ◆ ◆
我总结了市面上的 AI 做 PPT，大致分两种路子：
**第一种，模板填空型。**
选个模板，把内容往里塞。问题在于，它不理解你的内容在说什么——只是把段落贴到固定位置，出来的是排版文件，不是演示文稿。
**第二种，一键生成型。**
把文档丢给 LLM，让它一口气把整个 PPT 写出来。看似省事，但你完全不知道它在中间丢了什么。试过的人都知道，生成的 PPT 往往"泛泛而谈"——原文里那些具体的数据、结论、专有名词，不知道去哪了。
两者的共同问题：**你没法干预。**生出来什么样就是什么样，不满意只能从头再来。
我的想法很简单——能不能做一个这样的工具：
**① 不丢信息**原文的核心数据和结论，PPT 里必须有
**② 每步可控**大纲让我看、内容让我改，不满意就退回去重来
**③ 图表真实**数据来自原文表格，不是 LLM 编的
**④ 输出专业**生成的是原生 PPTX，图表是矢量对象，打开就能改
我把生成...

## 相关实体

[[DeepSeek]], [[GitHub]], [[OpenAI]], [[Python]], [[Qwen]], [[React]]

## 相关概念


