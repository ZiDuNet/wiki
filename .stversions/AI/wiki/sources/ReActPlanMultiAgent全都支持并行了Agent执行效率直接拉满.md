---
tags: [Agent, RAG, Prompt, API]
source: "二哥狗腿子"
created: 2026-04-25
updated: 2026-05-10
category: Agent
---

# ReAct、Plan、Multi-Agent全都支持并行了，Agent执行效率直接拉满

> 来源: [二哥狗腿子](https://mp.weixin.qq.com/s?__biz=MzUxNzAzMTU4OQ==&mid=2247487441&idx=1&sn=00b0cea856f07f5af98dfb4db19002b4&chksm=f8f1d653f957d3bd3a85b9d599b7ef298caee81e29280c5a663a48cc1c6a5c86ca09969af3a2&mpshare=1&scene=1&srcid=0425xE1y6V13P7VufMgaUzuW&sharer_shareinfo=c74f31a37a9239ac755be0d6aef77530&sharer_shareinfo_first=c74f31a37a9239ac755be0d6aef77530) | 2026-04-25

## 摘要

PaiCLI 已经更新到第7期了，ReAct、Plan-and-Execute、Memory、RAG、Multi-Agent、HITL，该有的都有了。
但有一个问题一直没解决——串行。
我们让 PaiCLI 帮忙读三个文件，它会老老实实读完第一个，再读第二个，再读第三个。三个文件之间没有任何依赖关系，完全可以同时读，但 Agent 偏偏要排队。
Plan-and-Execute 模式下更明显。五个任务拆出来，前两个互相不依赖，第三个依赖前两个的结果。按道理前两个应该同时跑，但现在是第一个跑完才轮到第二个。
Multi-Agent 也一样，两个 Worker 都闲着，但编排器只分配给其中一个，另一个干等。
今天，我们就把 PaiCLI 从串行改造成并行。改完之后，三条执行路径——ReAct、Plan-and-Execute、Multi-Agent——全部支持并行执行，效率直接拉满。
PaiCLI 里有三个可以并行的场景。
第一个是工具调用的并行。大模型在一次响应里返回多个
，这几个工具之间没有依赖，可以同时执行。
比如 LLM 说“我要同时读 pom.xml 和 README.md”，返...

## 相关实体

[[ReAct]]

## 相关概念

[[AI-Agent]], [[MultiAgent]]
