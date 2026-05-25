# 初始化知识库

搭建知识库目录结构，生成配置文件。

## 参数收集

一次性确认以下信息（不需要逐个问，能推断的就直接用）：

1. **知识库名称** — 默认 `second-brain`
2. **路径** — 默认 `~/Documents/`，接受绝对路径
3. **主题** — 用一句话描述知识库关注什么，用于生成标签和描述
4. **raw 目录** — 如果用户有已有文件夹要作为 raw（如 `政策库/`），记下名字；否则用默认 `raw/`

## 执行步骤

### 1. 创建目录

```bash
# 默认（创建 raw/）
bash <skill-directory>/scripts/onboarding.sh <vault-path>

# 自定义 raw（用已有文件夹，不创建 raw/）
bash <skill-directory>/scripts/onboarding.sh <vault-path> <existing-folder-name>
```

### 2. 生成配置文件

**Agent 检测：**
- 检测到 Claude Code → 读 `references/agent-configs/claude-code.md` 生成 `CLAUDE.md`
- 检测到 Codex → 读 `references/agent-configs/codex.md` 生成 `AGENTS.md`
- 检测到 Cursor → 读 `references/agent-configs/cursor.md` 生成 `.cursor/rules/second-brain.mdc`
- 检测到 Gemini CLI → 读 `references/agent-configs/gemini.md` 生成 `GEMINI.md`
- **检测不到 → 生成通用 `SCHEMA.md`**

模板替换：
- `{{VAULT_NAME}}` → 知识库名称
- `{{DOMAIN_DESCRIPTION}}` → 主题描述
- `{{DOMAIN_TAGS}}` → 生成 5-8 个领域标签
- `{{WIKI_SCHEMA}}` → 读 `references/wiki-schema.md`，插入 `## Architecture` 之后的所有内容

**自定义 raw 目录时**：将配置文件中所有 `raw/` 替换为实际目录名。

### 3. 更新日志

追加到 `wiki/log.md`：

```
## [YYYY-MM-DD] setup | 知识库初始化
创建知识库"{{VAULT_NAME}}"，主题：{{DOMAIN_DESCRIPTION}}。
配置文件：{{生成的文件}}。Raw 目录：{{raw目录名}}。
```

### 4. 可选工具安装

询问用户是否安装：
- **summarize** — `npm i -g @steipete/summarize`
- **qmd** — `npm i -g @tobilu/qmd`
- **agent-browser** — `npm i -g agent-browser && agent-browser install`

### 5. 展示结果

告诉用户：
- 创建了什么（目录树 + 配置文件）
- 下一步：安装 Obsidian Web Clipper 浏览器扩展，剪藏文章到 raw 目录，然后用 `/second-brain` 摄入
