---
name: AI知识库
domain: AI技术、Agent、LLM应用、工具链
created: 2025-01-01
updated: 2025-05-11
---

# AI 知识库 — 操作契约

> 所有 AI Agent 的唯一操作依据。以此为准，不凭空捏造。

---

## 核心原则

1. **raw/ 是只读证据层** — 微信公众号文章原文（`/微信公众号/` 文件夹），LLM 只读取，绝不修改
2. **wiki/ 是 LLM 工作区** — 在此创建、更新、维护所有派生知识
3. **SCHEMA.md 是单一操作契约** — 所有行为规则集中于此，不在 pointer 文件中重复规则
4. **所有内部链接使用 `[[wikilink]]` 语法**

---

## 目录结构

```
{wiki-root}/              ← AI知识库根目录
├── SCHEMA.md             ← 本文件，唯一操作契约
├── CLAUDE.md             ← Thin pointer → SCHEMA.md
├── AGENTS.md             ← Thin pointer → SCHEMA.md
├── EXTEND.md             ← 用户偏好（BM25、语言、风格）
├── CLAUDE.md             ← Thin pointer → SCHEMA.md
├── raw/                  ← 只读证据层（映射到 ../微信公众号/）
│   └── .gitkeep
├── wiki/
│   ├── index.md         ← 知识库导航入口
│   ├── concept-table.md ← 概念关系表（持续维护）
│   ├── overview.md      ← 知识库总览
│   ├── log.md           ← 变更日志（仅追加）
│   ├── sources/         ← 源摘要页（每个摄入源一个）
│   ├── entities/        ← 实体页（人物/组织/产品/工具）
│   ├── concepts/        ← 概念页（框架/理论/模式）
│   └── synthesis/       ← 综合页（跨源整合的高价值分析）
├── scripts/
│   └── wiki_fts.py      ← BM25 全文搜索脚本
└── indexes/             ← 搜索索引
```

---

## 页面格式

每个 Wiki 页面**必须**包含 YAML frontmatter：

```yaml
---
title: 页面标题
type: source-summary | entity | concept | synthesis | comparison
tags: [tag1, tag2]
sources: [source-filename-1.md, source-filename-2.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## 页面类型（AI 领域专用）

| 类型 | 用途 | 存放位置 |
|---|---|---|
| `source-summary` | 微信公众号文章的 LLM 摘要 | `wiki/sources/` |
| `entity` | 人物/组织/产品/工具（如：Claude、OpenAI、Codex） | `wiki/entities/` |
| `concept` | 框架/理论/模式（如：RAG、Agent、Prompt Engineering） | `wiki/concepts/` |
| `synthesis` | 跨源整合分析 | `wiki/synthesis/` |
| `comparison` | 工具/方案对比 | `wiki/synthesis/` |

---

## 操作规程

### 摄入（Ingest）— 处理新文章

1. 读取 `../微信公众号/` 中新增的微信公众号文章
2. 生成 `wiki/sources/{slug}.md` 源摘要页
3. 识别文章中的实体和概念，更新或创建 `wiki/entities/` 和 `wiki/concepts/` 页面
4. 添加 `[[wikilinks]]` 关联相关页面
5. 更新 `wiki/index.md`（新页面加入目录）
6. 追加到 `wiki/log.md`
7. 若 BM25 已启用，执行 `python3 scripts/wiki_fts.py build`

### 查询（Query）— 回答问题

1. 读取 `wiki/index.md` 定位相关页面
2. 阅读相关 Wiki 页面
3. 综合答案，引用 `[[wikilink]]`
4. 若产生有价值的分析，提议保存到 `wiki/synthesis/`

### 健康检查（Lint）— 维护质量

每 10 次摄入或每月至少一次，执行：

1. 扫描断裂 wikilink
2. 检查孤立页面（无入链）
3. 检查矛盾内容
4. 检查 `concept-table.md` 与实际页面一致性
5. 修复问题或报告给用户

---

## Obsidian 设置

- 附件文件夹路径：`raw/assets/`（如有图片）
- 推荐插件：Dataview（数据查询）、Marp（幻灯片）
- 使用图谱视图检查知识库结构
- 绑定快捷键下载 Web Clipper 内容到 `raw/`

---

## 硬规则

1. **绝不修改 `raw/` 中的文件**
2. 创建或删除页面时必须更新 `wiki/index.md`
3. 执行操作时必须追加到 `wiki/log.md`
4. 所有内部引用使用 `[[wikilinks]]`
5. 每个 Wiki 页面必须有 YAML frontmatter
6. 新信息与已有内容矛盾时，更新页面并注明两个来源
7. 优先更新已有页面而非创建新页面
8. `concept-table.md` 是概念关系表，每次摄入后维护
