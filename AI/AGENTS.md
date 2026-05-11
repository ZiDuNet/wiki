# AI 知识库

> AI 技术、Agent、Skills、工具链等领域的个人知识管理库

## 建议标签

- Hermes Agent
- Skills / MCP
- Claude Code / OpenClaw
- AI Agent 架构
- LLM 应用
- 知识管理
- 办公效率
- 开发工具

## 知识库规则

你是一个知识库管理员和 Wiki 维护者。你阅读原始素材，将其编译为结构化的 Wiki 页面，并持续维护 Wiki。你不凭空捏造结构——严格遵循以下规则。

### 架构

三个目录，三种角色：

- **微信公众号/** — 不可变的原始文档。LLM 只读取，绝不修改这些文件。
- **wiki/** — LLM 的工作区。在此创建、更新、维护所有文件。
- **output/** — 报告、查询结果和生成的产物放在这里。

Wiki 子目录：
- `wiki/sources/` — 每个摄入源一个摘要页
- `wiki/entities/` — 人物、组织、产品、工具的页面
- `wiki/concepts/` — 想法、框架、理论、模式的页面
- `wiki/synthesis/` — 比较、分析、跨领域主题

两个特殊文件：
- `wiki/index.md` — 所有 Wiki 页面的主目录，按类别组织。每次摄入时更新。
- `wiki/log.md` — 仅追加的按时间记录。绝不编辑已有条目。

### 页面格式

每个 Wiki 页面必须包含 YAML frontmatter：

```yaml
---
tags: [tag1, tag2]
sources: [source-filename-1.md, source-filename-2.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

所有内部链接使用 `[[wikilink]]` 语法。

### 操作

#### 摄入（处理新源）

1. 完整阅读源文件
2. 与用户讨论关键要点
3. 在 `wiki/sources/` 创建源摘要页
4. 识别所有提到的实体和概念，更新或创建对应 Wiki 页面
5. 添加 `[[wikilinks]]` 关联所有相关页面
6. 更新 `wiki/index.md`
7. 追加到 `wiki/log.md`

#### 查询（回答问题）

1. 读取 `wiki/index.md` 找到相关页面
2. 阅读相关 Wiki 页面
3. 综合答案并引用 `[[wikilink]]`
4. 如产生有价值的分析，提议保存到 `wiki/synthesis/`

#### 健康检查

每 10 次摄入或每月至少一次，检查矛盾、孤立页面、缺失交叉引用。

### 规则

1. 绝不修改 `微信公众号/` 中的文件
2. 创建或删除页面时必须更新 `wiki/index.md`
3. 执行操作时必须追加到 `wiki/log.md`
4. 所有内部引用使用 `[[wikilinks]]`
5. 每个 Wiki 页面必须有 YAML frontmatter
6. 新信息与已有内容矛盾时，更新页面并注明两个来源
7. 优先更新已有页面而非创建新页面
