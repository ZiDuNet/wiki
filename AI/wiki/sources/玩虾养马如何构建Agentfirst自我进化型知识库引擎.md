---
tags: [Agent, Claude, MCP, GitHub, Obsidian, PPT, RAG, Harness]
source: "豪哥搞懂了"
created: 2026-04-20
updated: 2026-05-10
category: Agent
---

# 【玩虾养马】如何构建Agent-first自我进化型知识库引擎

> 来源: [豪哥搞懂了](https://mp.weixin.qq.com/s?__biz=MzAwNDU0MTkxMw==&mid=2247484258&idx=1&sn=f203f48d0977bbf15be8c8baa12a7722&chksm=9a179c224d27230fd5f18815460b93a9e9032ab4ca95fbeffebe9f141b9ab4c2dd6368d62372&mpshare=1&scene=1&srcid=0420uXtsKs3VLA7kcWgg9ew6&sharer_shareinfo=100c49865fa16e0731a1b61dff8e86a7&sharer_shareinfo_first=100c49865fa16e0731a1b61dff8e86a7) | 2026-04-20

## 摘要

产品文档散落在 SharePoint、本地硬盘、各种即时通讯频道里。方案很标准——RAG。上传文件，切片，向量化，检索拼接，LLM 生成回答。
跑了一段时间后，你就会发现：
这不是个段子，而是 RAG 在知识管理场景中的结构性问题。
先说清楚：**RAG 在特定场景下非常有效**——知识问答、单文档检索、FAQ 响应，这些都是 RAG 的舒适区。
但在知识管理这个场景下，会反复撞到四面墙：
**跨文档综合做不到**
产品定价在 PPT 里，技术参数在 PDF 里，案例描述在 Word 里。RAG 检索到的是片段，不是经过整合的知识。
**矛盾检测是盲区**
三个月前的报价单和上周的价格表同时存在，RAG 不知道哪个该信——它甚至不知道它们矛盾。
**答案不可溯源**
出了问题回头查，根本说不清 AI 的回答基于哪份文件的哪个版本。
**维护成本随规模飙升**
源文件一变就要重建索引，向量数据库是个黑盒，没人敢碰。
这不是某个产品的问题，是"查询时临时拼接"这条路线在复杂知识场景下的局限。
我后来在 Compounding Wiki 方向的前沿研究中读到一段话：
这句话让我的思路转了过来...

## 相关实体

[[Claude-Code]], [[Claude]], [[Harness]], [[Hermes]], [[MCP]], [[Markdown]], [[Notion]], [[Obsidian]], [[OpenClaw]]

## 相关概念

[[嵌入向量]], [[知识图谱]], [[知识管理]]
