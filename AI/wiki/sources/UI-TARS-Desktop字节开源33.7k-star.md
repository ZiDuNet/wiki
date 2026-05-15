---
title: 字节开源 UI-TARS Desktop：AI真的会操作电脑
type: source-summary
tags: [UI-TARS, GUI-Agent, 字节跳动, 桌面自动化, 计算机操作]
sources: [../微信公众号/字节UI-TARS Desktop/字节开源33.7k！这个AI真的会操作电脑，字节UI-TARS Desktop实测，附详细安装教程.md]
created: 2026-05-16
updated: 2026-05-16
---

# UI-TARS Desktop 字节开源 GUI Agent

## 核心摘要

**UI-TARS Desktop** 是字节跳动开源的桌面级 GUI Agent（33.7k+ Star），让 AI 能看懂屏幕、理解界面语义、操作鼠标键盘。与传统 RPA（固定坐标点击）不同，它是**纯视觉驱动**——像人一样找"搜索框"、输入内容、点"搜索按钮"，不依赖固定坐标。

## 架构三组件

1. **Operator（操作员）** — 跟电脑硬件交互：截图（把屏幕传给 AI）和执行（操作鼠标键盘）。支持 nut-js 桌面自动化、WebOperator（浏览器）、MobileOperator（手机）

2. **UI-TARS Model（大脑）** — 字节自研多模态大模型，输入截图+任务描述+历史操作记录，输出下一步动作（"点击坐标(100,200)"或"输入文本'hello'"）。1.5 是基础版，1.6 是增强版

3. **GUI Agent（协调员）** — 串联 Operator 和 Model，管理完整任务循环：截图 → 传模型 → 获取动作 → 执行 → 判断是否完成

## 核心能力

- **鼠标**：单击、双击、右键、拖拽、悬停
- **键盘**：输入文本、快捷键（Ctrl+C/V）、组合键
- **滚动**：页面上下/横向滚动
- **等待与观察**：等页面加载、观察界面变化

## 两种使用模式

| 模式 | 说明 | 适用场景 |
|---|---|---|
| Local Operator | AI 控制本地电脑 | 自动化办公、批量文件处理、界面测试 |
| Remote Operator | AI 控制远程电脑/浏览器 | 服务器管理、云端自动化测试 |

> Remote Browser Operator 完全免费，点击就能用，无需配置。

## 四种安装方式

1. **CLI（最推荐）**：`npx @ui-tars/cli start` → 配置 API Key（需在火山引擎申请）→ 开始使用
2. **桌面应用**：GitHub Releases 下载 dmg/exe，双击安装
3. **源码安装**：克隆仓库 → bun install → 配置 .env → `bun run dev`
4. **SDK 集成**：npm install @ui-tars/sdk → 写代码嵌入自有应用

## 与同类项目对比

| 项目 | 特点 | 适用场景 |
|---|---|---|
| UI-TARS Desktop | 纯视觉驱动、开源、字节出品 | 通用 GUI 自动化 |
| Claude Computer Use | Claude 官方、云端运行 | 简单任务演示 |
| OpenAI Operator | 浏览器专用、云端运行 | 网页自动化 |
| RPA 工具 | 固定流程、企业级 | 大规模重复任务 |

**优势**：开源免费 + 本地运行 + 纯视觉理解

## 实际测试场景

- ✅ 自动化办公：10 个 PDF 表格提取汇总 Excel（基本成功，复杂格式需人工检查）
- ✅ 数据采集：爬取电商前 5 页商品名称价格（比写爬虫脚本快）
- ✅ 软件测试：登录功能异常测试（最满意，AI 自动判断输入内容）

## 安全提醒

- 在虚拟机或沙箱环境运行
- 不要给 AI 管理员权限
- 敏感操作前人工确认
- 使用本地模型避免数据上传云端

## 相关概念

- [[AI-Agent]] — 上位概念
- [[浏览器自动化]] — 浏览器场景
- [[RPA]] — 传统方案对比
