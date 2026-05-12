---
tags: [synthesis, obsidian, 知识管理, ai, claudian, llm-wiki]
sources:
  - Obsidian本地知识库文档多而杂，难维护，不够智能？通过AI大神Karpathy这套方法
  - 超详细版：Obsidian + Claude Code 搭建个人知识库实践指南
  - 个人知识库还得是Obsidian + AI Agent
  - AI时代怎么打造个人专属的知识库？Obsidian完美契合
  - Hermes Agent(爱马仕) × Obsidian × LLMWiki：打造你的个人AI知识中枢
  - Obsidian Cli 基础使用教程 AI化知识管理全过程
  - Obsidian内容创作系统：如何让你的文章没有AI味
  - 把AI接入Obsidian：一篇真正能跑通的完整配置指南
  - 日记 3.0：我用 Hermes+Obsidian，把流水账日记变成洞察与成长的飞轮
  - 微信一键同步Obsidian
  - 我为什么要升级知识管理到obsidian
  - 下篇：Obsidian 个人知识库搭建实录
  - 一句话生成PPT丨Obsidian + Claude Code 实践手记 · 04
  - 用 Hermes + Obsidian 建一个 AI 学习知识库
created: 2026-05-10
updated: 2026-05-10
---

# Obsidian-AI 工作流

## 概述

Obsidian 是一个基于本地 Markdown 文件的知识管理平台，凭借双链笔记和知识图谱，成为 AI 时代最佳的个人知识库基础设施。本文综合 18 篇源文章，从基础搭建到 AI 深度集成，构建完整的 Obsidian + AI 工作流体系。

## 一、为什么是 Obsidian

### 1.1 核心优势

| 特性 | 说明 |
|------|------|
| **本地存储** | 数据完全在你的硬盘上，零泄露风险 |
| **Markdown 格式** | AI 最擅长读写的格式，可被 AI 无缝接管 |
| **双向链接** | 模仿大脑神经元连接，知识不是孤岛 |
| **知识图谱** | 可视化知识网络，发现隐藏关联 |
| **开放社区** | 巨多插件，可自定义扩展 |

### 1.2 与其他笔记软件的区别

| 工具 | 数据归属 | AI 兼容性 | 双链支持 | 本地存储 |
|------|---------|----------|---------|---------|
| Obsidian | 你自己 | 原生 Markdown | 是 | 是 |
| Notion | 平台 | 有限 API | 有限 | 否 |
| 飞书 | 平台 | 有限 | 否 | 否 |
| 印象笔记 | 平台 | 有限 | 否 | 否 |

### 1.3 适合人群

- 跟 AI 聊得多的人：保存所有对话记录
- 试过各种笔记软件都放弃的人：让 AI 管理知识库
- 想做内容输出的人：从灵感到成品全流程
- 数据控：收藏内容让 AI 分析

## 二、LLM Wiki 方法论（Karpathy 方法论）

### 2.1 三层架构

AI 大神 Karpathy 提出了一套构建本地 llm.wiki 知识库的方法论，核心是三层架构：

```
知识库根目录/
├── sources/          # 第一层：Raw sources（原始资料层）
│   └── 文章、图片、数据文件（只读，不修改）
├── wiki/             # 第二层：Wiki（结构化知识层）
│   ├── entities/     # 实体页
│   ├── concepts/     # 概念页
│   ├── synthesis/    # 综合分析页
│   ├── index.md      # 全局索引
│   └── log.md        # 操作日志
└── CLAUDE.md         # 第三层：Schema（规则层）
```

**第一层：Raw sources（原始资料层）**
- 存放原始文档
- 严格要求：不修改，只读取
- 使用者只管收集原始物料

**第二层：Wiki（结构化知识层）**
- LLM 生成的摘要、对比分析、总览综述
- 由大模型独立负责创建、更新、维护
- 人工不进行任何更新操作，只做阅读

**第三层：Schema（规则层）**
- 配置文件如 CLAUDE.md / AGENTS.md
- 限定大模型使用知识库的规则
- 描述知识库结构、使用惯例和流程

### 2.2 关键文件

**index.md** -- 全局索引
- 每篇文档的页面地址、类型和摘要
- AI 回答时通过 index.md 快速索引
- 中等规模（约 100 个来源）效果出奇地好
- 避免了基于嵌入的 RAG 架构的复杂性

**log.md** -- 操作日志
- 按时间顺序记录所有操作
- 帮助 LLM 了解最近的工作内容

### 2.3 核心理念

让大模型从"临时回答工具"变成"长期知识维护者"，使个人知识管理实现复利增长。知识库不再是静态的仓库，而是一个能够通过持续链接**自我进化**的有机体。

## 三、Obsidian + Claude Code 搭建指南

### 3.1 环境搭建

**第一步：安装 Obsidian**
1. 下载安装 Obsidian
2. 创建知识库（Vault），存放位置选非系统盘
3. 开启核心插件：反向链接、关系图谱、标签列表

**第二步：安装 Claude Code**
```bash
pip install anthropic-cli
```

### 3.2 推荐目录结构

```
知识库/
├── 00_Inbox/         # 收集箱：未经处理的临时信息
├── 01_Daily/         # 每日笔记：日记、日复盘
├── 02_Reading/       # 阅读笔记：文章精华摘录
├── 03_Knowledge/     # 主题知识：按领域分类
├── 04_Projects/      # 项目资料
├── 05_Templates/     # 模板库
├── 06_Assets/        # 资源库
└── CLAUDE.md         # 核心规则
```

### 3.3 CLAUDE.md 配置

CLAUDE.md 是 AI 知识管理员的角色定义与规则：

```yaml
# AI 知识管理员规则
角色：你是这个知识库的管理员
规则：
  - 使用中文输出
  - 输出 Markdown 文件
  - 不随意修改原始资料
  - 新建内容写入指定目录
```

## 四、AI 插件与工具集成

### 4.1 Claudian（Obsidian AI 插件）

Claudian 是 Obsidian 中直接与 Claude 交互的插件：
- 在 Obsidian 聊天框中打开 Claude Code
- 支持加载 CLAUDE.md 规则
- 通过 `/wiki` 命令执行知识库操作

**注意事项**：CLAUDE.md 在 Claude Code CLI 中直接生效，但在 Claudian 中需要手动通过 `/wiki` 命令加载。

### 4.2 Hermes Agent + Obsidian

Hermes Agent 与 Obsidian 的深度集成：
- 微信文章一键同步到 Obsidian
- 自动入库、自动整理、自动汇报
- 通过飞书 CLI 实现跨平台协作

### 4.3 Obsidian CLI

命令行方式操作 Obsidian，实现 AI 化知识管理全过程：
- 自动创建笔记
- 批量处理文件
- 脚本化工作流

## 五、知识管理工作流

### 5.1 信息收集流

```
信息源（微信/网页/PDF）-> 00_Inbox -> AI 自动分类 -> 03_Knowledge
```

### 5.2 内容创作流

```
灵感/素材 -> AI 分析整理 -> 初稿 -> AI 润色 -> 发布
```

Obsidian 内容创作系统的核心原则：**让文章没有 AI 味**。通过结构化提示词和个人风格模板，保持写作的原创性。

### 5.3 日记系统

日记 3.0：基于 Karpathy 日记法演进：
- 流水账日记 -> AI 提取洞察 -> 周期性总结
- 把日记变成洞察与成长的飞轮

### 5.4 知识库巡检

定期对知识库进行健康检查：
- 检查孤立笔记（没有双向链接）
- 发现潜在关联（未链接但相关的笔记）
- 更新过时内容

## 六、文档格式转换

### 6.1 批量转 Markdown

支持将以下格式批量转为 Markdown：
- PDF 文档
- DOCX 文件
- XLSX 表格

### 6.2 微信同步

微信一键同步 Obsidian：
- 链接文章自动保存
- 随笔轻松储存
- 支持标签分类

## 相关页面

- [[Claude-Code深度指南]] -- Claude Code 与 Obsidian 的结合使用
- [[Obsidian]] -- Obsidian 实体页
- [[知识库构建]] -- 知识库构建方法论
- [[LLM-Wiki]] -- LLM Wiki 方法论
- [[Karpathy]] -- Karpathy 方法论来源
- [[Hermes-Agent]] -- Hermes Agent 与 Obsidian 集成
