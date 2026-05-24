# oh-my-pi — 内置 IDE 能力的终端 AI 编程助手

> GitHub: https://github.com/can1357/oh-my-pi
> Stars: ~6k (2026-05) | 协议: MIT | 语言: TypeScript + Rust (~27k行)
> 技术栈: LSP、DAP调试器、Hashline编辑、双内核执行

## 一句话简介

**终端里的 AI 编程助手，从 Pi 项目 fork 而来，32 个内置工具、40+ Provider、13 种 LSP 操作、27 种 DAP 操作。约 27k 行 Rust 原生模块把 ripgrep、glob、bash、AST 操作全部做进进程内，主打编辑精度和性能极致。**

## 核心特点

- **IDE 深度集成**: LSP 全功能支持（诊断、导航、重命名、代码动作），DAP 调试器驱动
- **双内核执行**: 持久 Python 和 Bun Worker，均可回调 Agent 工具
- **Hashline 编辑**: 内容哈希锚点定位代码，减少 61% Token 消耗
- **一级子代理**: task 工具可并行派发隔离 worktree 的 worker
- **时间旅行流规则**: 正则匹配中断流、注入规则、从同点重试

## 快速安装

```bash
# macOS/Linux
curl -fsSL https://omp.sh/install | sh

# Bun（推荐）
bun install -g @oh-my-pi/pi-coding-agent

# Windows PowerShell
irm https://omp.sh/install.ps1 | iex
```

## 架构

```
┌──────────────────────────────────────┐
│          oh-my-pi (omp)              │
├──────────┬──────────┬────────────────┤
│ 32 Tools │ 40+ LLM  │ Rust Native    │
│          │ Providers│ (~27k LOC)     │
├──────────┼──────────┼────────────────┤
│ LSP (13) │ DAP (27) │ Hashline Edit  │
├──────────┴──────────┴────────────────┤
│   Python Kernel  |  Bun Worker      │
└──────────────────────────────────────┘
```

## 适用场景

- 终端重度用户的专业 AI 编程
- 需要精确代码编辑（而非模糊建议）的场景
- 大型项目的调试和代码导航
- 多模型切换和成本优化

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
