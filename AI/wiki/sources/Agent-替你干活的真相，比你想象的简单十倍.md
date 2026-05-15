---
tags: [Agent, Claude]
source: "程序员红哥"
created: 2026-05-15
updated: 2026-05-15
category: Agent
---

# Agent 替你干活的真相，比你想象的简单十倍

> 来源: [程序员红哥](https://mp.weixin.qq.com/s?__biz=MzkwMDcyMDI5Mg==&mid=2247483937&idx=1&sn=cf1f8fce6613ab32c3e0b954f941ba56&chksm=c1960825ba945c1f7615b252f695214a9f4c9a0585d49f01909129e9bae49476e9fdbc95f78a&mpshare=1&scene=1&srcid=0515YCyggqimpn20hDyjUv3x&sharer_shareinfo=ba8534a71af75809c49f329125dd87cd&sharer_shareinfo_first=ba8534a71af75809c49f329125dd87cd) | 2026-05-15

## 摘要

---
你用 Claude Code 写项目，它自动读文件、改代码、跑测试，看起来像个真正的程序员在干活。你用 Manus 做调研，它自己搜索、整理、出报告，全程没问你一句。
你会觉得——这 AI 真厉害，什么都会干。
**真相是：大模型连一行代码都没执行过。**
它既不会上网，也不会写文件，更不会调 API。[它只会一件事：根据你给它的信息，预测下一个 token，然后输出一段文字。](https://mp.weixin.qq.com/s?__biz=MzkwMDcyMDI5Mg==&mid=2247483902&idx=1&sn=c4ff07feac954fc24cd2e58b530b70ac&scene=21#wechat_redirect)
那它怎么做到的"自己动手"？
答案比你想的简单得多——每次它想干点什么，它就输出一段 JSON，说"我想调这个工具，参数是这些"。真正去执行的...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Dify]], [[GitHub]], [[MCP]], [[OpenAI]], [[Python]]

## 相关概念


