---
name: second-brain
description: >
  LLM Wiki 个人知识库系统。基于 Karpathy 的 LLM Wiki 模式，LLM 持续构建和维护结构化 wiki。
  支持四种模式：初始化（init）、摄入（ingest）、检索（query）、健康检查（lint）。
  当用户说"初始化知识库"、"创建知识库"、"onboard"时触发 init；
  当用户说"摄入"、"处理源文件"、"ingest"、"导入"时触发 ingest；
  当用户说"检索"、"查询"、"搜索知识库"、"query"时触发 query；
  当用户说"检查"、"lint"、"健康检查"、"audit"时触发 lint。
allowed-tools: Bash Read Write Edit Glob Grep
---

# Second Brain — LLM Wiki 个人知识库

LLM 不是在查询时从原始文档重新检索，而是**持续构建和维护一个持久化 wiki**——一个结构化、相互链接的 markdown 文件集合。每次新增源文件，LLM 读取、提取关键信息、整合进现有 wiki——更新实体页、修订主题摘要、标注矛盾。知识被编译一次，然后**持续保持更新**。

核心区别：**wiki 是持续复利的持久产物。** 交叉引用已经建好，矛盾已经标注，综合已经反映你读过的所有内容。每加一个源文件、每问一个问题，wiki 都在变得更丰富。

## 模式判断

根据用户意图自动选择模式：

| 用户意图 | 模式 | 指令文件 |
|---|---|---|
| "初始化知识库"、"创建知识库"、"onboard"、"搭建" | **init** | `<skill-directory>/references/init.md` |
| "摄入"、"处理源文件"、"ingest"、"导入"、"处理一下" | **ingest** | `<skill-directory>/references/ingest.md` |
| "检索"、"查询"、"搜索知识库"、"query"、"问一下" | **query** | `<skill-directory>/references/query.md` |
| "检查"、"lint"、"健康检查"、"audit"、"找问题" | **lint** | `<skill-directory>/references/lint.md` |

确定模式后，读取对应的指令文件并执行。

## 三层架构

```
知识库根目录/
├── raw/              ← 不可变源文件（或用户自定义目录名）
├── wiki/             ← LLM 工作区
│   ├── sources/      ← 源文件摘要
│   ├── entities/     ← 实体页（人物、组织、产品、工具）
│   ├── concepts/     ← 概念页（想法、框架、理论、模式）
│   ├── synthesis/    ← 综合分析（对比、分析、跨主题）
│   ├── index.md      ← 总目录（每次 ingest 更新）
│   └── log.md        ← 操作日志（只追加，不修改）
├── output/           ← 导出产物
└── SCHEMA.md         ← 知识库规则（可选，agent 通用）
```

**raw 目录可以自定义**。用户可以用已有文件夹（如 `政策库/`）作为 raw，不需要改名为 `raw/`，也不需要创建 `raw/` 子目录。

## 通用规则

1. **raw 文件不可变**——只读，永远不修改
2. **wiki 是 LLM 的工作区**——创建、更新、维护所有文件
3. **每次操作都要更新 index.md 和 log.md**
4. **所有内部引用使用 `[[wikilink]]`**——不用原始文件路径
5. **每个 wiki 页面必须有 YAML frontmatter**：

```yaml
---
tags: [tag1, tag2]
sources: [source-file.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

6. **好的回答要存回 wiki**——对比、分析、新发现，这些有价值的结果不应消失在对话历史中
7. **页面命名**：文件名用 `kebab-case.md`，页面标题用 Title Case，wikilink 用页面标题

## 角色分工

- **人类**：选题、提问、审查、指引方向
- **LLM**：摘要、交叉引用、归档、维护——所有苦力活
- **Obsidian 是 IDE，LLM 是程序员，wiki 是代码库**

## BM25 全文检索

知识库超过 ~100 页后，使用 BM25（SQLite FTS5）进行高效检索。

**脚本位置**：`<skill-directory>/scripts/wiki_fts.py`

部署时将脚本复制到 `<wiki-root>/scripts/` 下：

```bash
cp <skill-directory>/scripts/wiki_fts.py <wiki-root>/scripts/
cd <wiki-root>
python3 scripts/wiki_fts.py stats      # 查看索引状态
python3 scripts/wiki_fts.py build      # 构建/重建索引（索引存放在 <wiki-root>/indexes/fts.sqlite）
python3 scripts/wiki_fts.py search "关键词" --limit 5  # 搜索
```

- `<wiki-root>` 即知识库目录下的 `wiki/` 文件夹
- 索引数据库自动存放在 `<wiki-root>/indexes/fts.sqlite`
- 可配合 cron 定时任务定期重建索引

## 参考文件

- `<skill-directory>/references/wiki-schema.md` — wiki 规范（所有配置的单一事实来源）
- `<skill-directory>/references/tooling.md` — CLI 工具详情（含 qmd 搜索引擎）
- `<skill-directory>/references/agent-configs/` — agent 专属配置模板
- `<skill-directory>/references/bootstrap.md` — 知识库初始化引导（从 karpathy-llm-wiki 迁移）
- `<skill-directory>/references/bm25.md` — BM25 全文检索详细工作流（从 karpathy-llm-wiki 迁移）
- `<skill-directory>/scripts/onboarding.sh` — 初始化脚本
- `<skill-directory>/scripts/wiki_fts.py` — BM25 索引构建/搜索/统计脚本（SQLite FTS5）
