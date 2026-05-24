# codegraph — 给 AI 提前做好功课的代码知识图谱

> GitHub: https://github.com/colbymchenry/codegraph
> Stars: ~18k (2026-05) | 协议: MIT | 语言: TypeScript
> 技术栈: tree-sitter、SQLite、MCP Server、FTS5

## 一句话简介

**提前把整个代码库索引成语义代码知识图谱（MCP Server），AI 一上来就对你的项目了如指掌。在 7 个真实代码库基准测试中，平均节省 35% 成本、59% Token、49% 时间、70% 工具调用。**

## 核心特点

- **智能上下文构建**: 一次工具调用返回入口点、相关符号和代码片段，无需昂贵探索
- **FTS5 全文搜索**: 即时符号名搜索，跨整个代码库
- **影响分析**: 追踪调用者、被调用者及完整影响半径
- **自动同步**: 文件监视器使用原生 OS 事件，带防抖自动同步
- **框架感知路由**: 识别 13 种 Web 框架的路由文件，链接 URL 模式到处理器

## 快速安装

```bash
# 交互式安装
npx @colbymchenry/codegraph
codegraph init -i

# 全局安装
npm install -g @colbymchenry/codegraph
```

## 支持范围

- **Agent**: Claude Code、Cursor、Codex CLI、OpenCode
- **语言**: 19+ 种（TypeScript、Python、Go、Rust、Java、C#、PHP、Ruby 等）
- **工作原理**: tree-sitter 解析→AST 提取符号→SQLite 存储→MCP 工具查询

## 基准测试

| 指标 | 平均节省 |
|------|----------|
| 成本 | 35% |
| Token | 59% |
| 时间 | 49% |
| 工具调用 | 70% |

## 适用场景

- 大型代码库的 AI 辅助开发（效果最显著）
- 频繁让 AI 改代码但每次都要重新理解项目的场景
- 代码审查和重构决策
- 多人协作项目的 AI 编程助手

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
