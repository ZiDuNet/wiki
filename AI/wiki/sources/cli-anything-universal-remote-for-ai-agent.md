---
title: CLI-Anything：AI Agent 的万能遥控器
type: source-summary
tags: [CLI-Anything, Agent, CLI, HKUDS, 自动化, Skill]
sources: [AI Agent 的万能遥控器：CLI-Anything 让所有软件都能被智能体直接调用.md]
created: 2026-05-22
updated: 2026-05-22
---

# CLI-Anything：AI Agent 的万能遥控器

> 📎 来源: [时之AI测评](https://mp.weixin.qq.com/s?__biz=MzIyMjg2MTM0OQ==&mid=2247485444&idx=1&sn=0f7644b89650e2b55af392b95a52b122) | 时间: 2026-05-22

## 核心定位

HKUDS 团队开源的 **CLI-Anything**：一行命令把任意软件变成 AI Agent 可操作的 CLI 工具。

> 今天的软件为人服务，明天的用户将是 Agent，CLI-Anything 就是两者之间的桥梁。

---

## 问题背景

**AI Agent 的困境：** 能写代码、查资料、调用 API，但遇到图形用户界面（GUI）就抓瞎。

绝大多数专业软件（CAD、3D建模、视频编辑、笔记管理）都长着一张「给人类看」的图形脸，没有 CLI 接口，Agent 无能为力。

---

## 解决方案

**CLI-Anything 的思路：** 自动为任何软件生成 CLI 封装——不改造软件本身，而是在外面包一层命令行壳。

---

## 工作流程（以 Claude Code 为例）

```
/cli-anything ./gimp
```

**七步管道：**

1. **分析** — 扫描软件源代码或 API，把 GUI 操作映射成可调用功能
2. **设计** — 规划命令组、状态模型、输出格式
3. **实现** — 用 Python Click 库生成 CLI 代码，自带 REPL 交互、JSON 输出、撤销/重做
4. **计划测试** — 创建单元测试和端到端测试方案
5. **写测试** — 自动实现完整测试套件
6. **文档** — 更新测试结果
7. **发布** — 生成 setup.py，安装到 PATH

**迭代命令：**
```
/cli-anything:refine
```
增量更新，不破坏已有内容。

---

## CLI-Hub：集中式仓库

```
pip install cli-anything-hub
```

**已有 CLI 封装示例：**

| CLI | 用途 |
|-----|------|
| Blender CLI | 3D建模与渲染自动化 |
| GIMP CLI | 图像处理 |
| FreeCAD CLI | 工业设计（258条命令、17个命令组） |
| Zotero CLI | 文献管理 |
| Obsidian CLI | 知识库操作 |
| Kdenlive CLI | 视频编辑 |
| Safari CLI | 浏览器自动化（基于 MCP） |
| Godot CLI | 游戏引擎控制 |
| MuseScore CLI | 乐谱编辑 |

**每个 CLI 都附带 SKILL.md 文件** — AI 可发现的技能定义，让 Agent 能直接「读懂」这个 CLI 能干什么。

---

## 为什么非要用 CLI？

**CLI 的优势：**

| 特性 | 说明 |
|------|------|
| 结构化 | 方便 LLM 处理 |
| 轻量级 | 无图形依赖 |
| 自描述 | `--help` 就是天然文档 |
| 确定输出 | 输出 JSON，Agent 不需要猜 |

> Claude Code 每天通过 CLI 运行成千上万的真实工作流，证明这条路行得通。

---

## 适用人群

1. **AI Agent 重度用户** — 让 Agent 替你完成重复软件操作（批量渲染、自动排版、定时数据导出）
2. **软件插件开发者** — 为你的应用贡献 CLI 封装，提交 PR 后出现在 CLI-Hub
3. **好奇心用户** — 下载现成 CLI 玩一玩，看「AI 能不能打开 Photoshop」

**前提条件：**
- 目标软件已安装
- 有一个支持 CLI-Anything 的 AI 代理（Claude Code、Pi、OpenClaw 等）

---

## 项目信息

- **GitHub:** https://github.com/HKUDS/CLI-Anything
- **团队:** HKUDS（香港大学数据科学实验室）
- **特点:** 2280+ 个测试 100% 通过

---

## 相关实体与概念

- [[CLI-Anything]] — 本项目
- [[HKUDS]] — 开发团队
- [[Claude Code]] — 支持的 AI 代理之一
- [[OpenClaw]] — 支持的 AI 代理之一
- [[Pi]] — 支持的 AI 代理之一
- [[CLI]] — 命令行接口
- [[Skill]] — SKILL.md 文件，AI 可发现的技能定义
- [[Agent]] — AI 智能体
- [[MCP]] — Safari CLI 基于 MCP 协议

---

## 关键洞察

> AI Agent 正在从「只会聊天」进化成「能干实事」。CLI-Anything 的野心是把所有专业软件都变成 Agent 的原生工具。

**趋势判断：** 说不定过不了多久，你只需要对手机说一句：「帮我用 Blender 做一个凳子模型，导出 STL」，后台的 Agent 就调用 CLI-Anything 帮你完成了。