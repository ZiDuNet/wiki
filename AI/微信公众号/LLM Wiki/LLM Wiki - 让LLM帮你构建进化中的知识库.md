> 📎 来源: [元曜科技](https://mp.weixin.qq.com/s?__biz=MzYzNTE1NDMwNQ==&mid=2247486000&idx=1&sn=d77b1734e18f9712f020e835a1fb51ec&chksm=f1ed38221e2fa1123634ae2d479f677895f19dbff953bcfeaf9ecded316ef5be6276b5e08aac&mpshare=1&scene=1&srcid=0528qiyxGYU6iqjQMV7BjQ91&sharer_shareinfo=15bd75dd5e6100586b2b7f0fd7e0f5f2&sharer_shareinfo_first=15bd75dd5e6100586b2b7f0fd7e0f5f2) | 时间: 2026-05-28 21:06

---

#

## 它解决什么问题？

传统 RAG

- ❌ 每次查询都从零检索
- ❌ 没有结构化知识积累
- ❌ 无法发现知识盲区

LLM Wiki

- ✅ 知识编译一次，持续进化
- ✅ 四信号知识图谱
- ✅ Louvain 社区检测

## 核心功能

- **四信号知识图谱**

  — 直接链接×3.0 · 来源重叠×4.0 · Adamic-Adar×1.5 · 类型亲和×1.0
- **Louvain 社区检测**

  — 自动发现知识簇，找到你没意识到的知识盲区
- **Chrome 网页剪藏**

  — 一键捕获，自动纳入知识库
- **Obsidian 兼容**

  — 三栏布局 · [[wikilink]] 语法
- **两步思维链摄入**

  — 先分析，再生成，质量更高
- **深度研究**

  — LLM 智能生成搜索主题，自动填补知识空白

## 技术架构

基于 Andrej Karpathy 的 LLM Wiki 方法论：

- 三层架构：原始资料 → Wiki → Schema
- 三个核心操作：Ingest、Query、Lint

Tauri v2React 19TypeScriptsigma.jsLanceDB

立即体验

github.com/nashsu/llm\_wiki

元曜科技 · 2026
