# Understand-Anything — 把代码库变成可交互知识图谱

> GitHub: https://github.com/Lum1104/Understand-Anything
> Stars: ~20k (2026-05) | 协议: MIT | 语言: TypeScript
> 技术栈: 多代理管道、知识图谱、AST分析、交互式Dashboard

## 一句话简介

**通过多代理管道分析项目、提取文件/函数/类/依赖、构建知识图谱，并提供交互式 Dashboard 探索。让陌生代码库一眼看透，还支持业务逻辑域视图和知识库分析。**

## 核心特点

- **结构化知识图谱**: 文件、函数、类、依赖为节点，可视化代码库全貌
- **业务逻辑域视图**: domains、flows、steps 三层业务流程建模
- **Guided Tours**: 自动生成架构导览，快速了解项目结构
- **模糊/语义搜索**: 在代码库中进行智能搜索和问答
- **多平台兼容**: 支持 Claude Code、Cursor、Codex、Copilot、Gemini CLI 等 15+ 平台

## 快速安装

```bash
# Claude Code
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything

# 通用安装
curl -fsSL install.sh | bash
```

## 核心命令

| 命令 | 说明 |
|------|------|
| `/understand` | 分析代码库，构建知识图谱 |
| `/understand-dashboard` | 打开交互式可视化面板 |
| `/understand-chat` | 基于图谱的问答 |
| `/understand-diff` | 变更影响分析 |
| `/understand-domain` | 业务流程视图 |
| `/understand-knowledge` | Wiki/知识库分析 |

## 适用场景

- 新入职快速了解陌生代码库
- 开源项目贡献前的架构理解
- 大型项目重构前的依赖分析
- 代码审查时的变更影响评估

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
