---
title: drawio skill让AI画图
type: source-summary
tags: [drawio, skill, AI画图, 流程图, 架构图, MCP, trae]
sources: [装上drawio skill，让AI帮你画各种图（流程图、架构图等），AI画完你还能接着改.md]
created: 2026-05-22
updated: 2026-05-22
---

# drawio skill让AI画图

## 功能概述

安装 drawio skill 后，AI 可以帮你画各种图：流程图、架构图等。AI 画完后可以直接打开文件继续修改完善。

## 效果展示

AI 生成的图可能不够完美（取决于提示词），但比从空白页从零开始拖拽框线要好很多。还可以让 AI 改形状、颜色、线条等格式。

## 安装步骤

### 一、下载 drawio

drawio 是开源免费软件，官网下载安装：

```
https://www.drawio.com/
```

### 二、下载 drawio skill

GitHub 地址：

```
https://github.com/jgraph/drawio-mcp/blob/main/skill-cli/drawio/SKILL.md
```

### 三、修改 skill（重要）

官方 skill 存在问题，需修改才能使用：

#### 问题 1：命令名称错误

Windows 安装后是 `draw.io.exe`，skill 写的是 `drawio`，AI 会报错找不到命令。

**修改**：将命令改为 `draw.io.exe` 的绝对路径。

#### 问题 2：XML 参考文档在线链接

每次调用需联网读取 XML 文件，对无网用户不友好。

**修改**：下载 XML 放到本地 `drawio-cli` 目录，修改路径指向本地文件。

### 四、导入使用

1. 记事本打开 SKILL.md
2. 修改 CLI 路径为绝对路径
3. Export command 只保留一条
4. XML reference 换成本地路径
5. 重新打成 zip 压缩包导入 skill

## 技术细节

- 清理无关内容（Linux/macOS/WSL、环境变量说明）
- 只保留当前系统相关命令
- 减少干扰模型上下文

## 使用平台

示例使用 trae，其他支持 skill 的平台同理。

## 来源

- 公众号：GetLost FindMyself
- 原文：[装上drawio skill，让AI帮你画各种图](https://mp.weixin.qq.com/s?__biz=MzkyMTA1NTQxOA==&mid=2247484055)
- 相关概念：[[drawio]]、[[skill]]、[[MCP]]、[[AI画图]]