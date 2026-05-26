---
type: entity
name: Understand-Anything
tags: [代码分析, 知识图谱, GitHub-Trending, 开源, Tree-sitter]
sources: [今天 GitHub 上涨疯了的这个开源项目，程序员都在收藏.md]
created: 2026-05-26
updated: 2026-05-26
mentions: 1
---

# Understand-Anything

**类型:** 实体 / 开源项目
**提及文章数:** 1

## 简介

Understand-Anything 是一款将代码库变成可交互知识图谱的工具，2026年5月26日登顶 GitHub Trending 第一名，单日新增 5,604 Stars，总 Star 数破 31,000。它用 Tree-sitter 做静态解析 + LLM 语义理解，生成可点击、可搜索、可问答的代码知识图谱，支持 Claude Code、Cursor、Codex、Gemini CLI 等 15+ 主流 AI 编程工具。

## 核心数据

| 指标 | 数值 |
|---|---|
| GitHub Stars | 31,000+ |
| 单日新增 Stars | 5,604 |
| 扫描 Agent 数量 | 5个 |
| GitHub Trending 排名 | 第一名 |

## 核心功能

| 命令 | 功能 |
|---|---|
| `/understand` | 启动 5 个 Agent 并行扫描项目（文件结构、函数关系、架构层次、导览路径） |
| `/understand-dashboard` | 打开交互式图谱界面（节点=文件/模块，边=依赖关系，颜色=架构层） |
| `/understand-diff` | 分析改动影响范围 |
| `/understand-chat "问题"` | 直接问答代码逻辑 |

## 技术特点

1. **不是纯 LLM 分析**：先用 [[Tree-sitter]] 做静态解析提取代码结构，再交给 LLM 生成语义理解
2. **图谱可提交到 Git**：生成 JSON 文件，团队共享，新人入职直接打开图谱看
3. **多工具兼容**：一条安装命令适配 15+ AI 编程工具
4. **架构层自动识别**：API / Service / Data / UI 层颜色区分

## 安装方法

**Claude Code 用户：**
```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

**macOS / Linux：**
```bash
curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | bash
```

**Windows：**
```powershell
iwr -useb https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.ps1 | iex
```

**在线 Demo：** understand-anything.com/demo

## 适用场景

- 接手陌生大型项目的开发者
- 做代码 Review 的 Tech Lead
- 需要快速了解某个开源库内部逻辑的人

## 相关概念

- [[代码知识图谱]] — 将代码库变成可交互、可搜索、可问答的结构化图谱
- [[tree-sitter]] — 增量 AST 解析器，用于静态解析代码结构
- [[知识图谱可视化]] — Dashboard 界面，节点/边/颜色三层信息

## 相关实体

- [[Tree-sitter]] — 静态解析引擎
- [[Claude Code]] — 支持的 AI 编程工具
- [[Cursor]] — 支持的 AI 编程工具
- [[Codex]] — 支持的 AI 编程工具

## 官网

- 仓库：https://github.com/Lum1104/Understand-Anything
- Demo：https://understand-anything.com/demo