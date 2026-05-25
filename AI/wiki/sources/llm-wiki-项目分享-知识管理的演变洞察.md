---
tags: [LLM-Wiki, 知识管理, 方法论, Karpathy]
sources: [LLM Wiki/LLM Wiki 项目分享：知识管理的演变洞察.md]
created: 2026-05-25
updated: 2026-05-25
---

# LLM Wiki 项目分享：知识管理的演变洞察

**来源：** LLM Wiki/LLM Wiki 项目分享：知识管理的演变洞察.md
**摄入日期：** 2026-05-25
**类型：** 文章

## 摘要

本文系统介绍基于大语言模型构建个人知识库的方法论与工具集合（LLM Wiki），核心理念源自 Andrej Karpathy 提出的 LLM Wiki Pattern。传统 RAG 系统是「查询时检索」，每次提问模型都像第一次接触材料；LLM Wiki 则是「知识编译器」，知识被编译一次并持续更新，让答案可以回写成页面而非消失在聊天记录里。

## 核心观点

- **知识复利**：知识随资料增加而复合增长，交叉引用已建好，矛盾已标注
- **答案沉淀**：让答案可回写成页面而非消失在聊天记录中
- **三层架构**：Raw Sources（不可变）→ Wiki（LLM工作区）→ Schema/Config（行为规范）
- **人类-LLM 分工**：人类负责选题、提问、审查、指引方向；LLM 承担摘要、交叉引用、归档、维护
- **摄取（Ingest）**：读取源文件→提取关键实体/概念/论点→关联发现→生成 Wiki 文件→更新 index/log
- **查询（Query）**：分词搜索→向量语义搜索→知识图谱扩展→上下文组装
- **Lint（检查）**：定期健康检查矛盾内容、过时断言、孤立页面、缺失交叉引用
- **index.md**：内容目录，按类别组织，每摄取时更新
- **log.md**：追加式操作日志

## 涉及实体

- [[LLM Wiki]] — 方法论起源，Karpathy 提出的知识库模式
- [[nashsu/llm_wiki]] — 桌面应用，Tauri + React，sigma.js 知识图谱可视化
- [[nvk/llm-wiki]] — Agent 插件，支持 5-10 个并行智能体研究

## 涉及概念

- [[知识复利]] — 知识随资料增加而复合增长
- [[RAG]] — 对比传统查询时检索，LLM Wiki 是编译时索引
- [[知识图谱]] — 四信号相关性模型（直接链接×3.0、来源重叠×4.0、Adamic-Adar×1.5、类型亲和度×1.0）
- [[摄取流程]] — Ingest 的完整工作流

## 相似项目对比

| 特性 | nashsu/llm_wiki | nvk/llm-wiki |
| --- | --- | --- |
| 形态 | 桌面应用 | Agent 插件 |
| 技术栈 | Tauri + React | 纯 Agent 指令集 |
| 知识图谱 | sigma.js 可视化 + Louvain | 概念层支持 |
| 并行研究 | 基础 | 5-10 个并行智能体 |

## 相关链接

- Karpathy 原型：https://gist.github.com/Wanglaisi/c0224af24c22fbb769a6a20ee089d607
- nashsu/llm_wiki：https://github.com/nashsu/llm_wiki
- nvk/llm-wiki：https://github.com/nvk/llm-wiki