---
title: Dify打造数据可视化图表
type: source-summary
tags: [Dify, 数据可视化, MCP, mcp-server-chart, AntV, DeepSeek-V3]
sources: [dify打造数据可视化图表.md]
created: 2026-05-24
updated: 2026-05-24
---

# Dify打造数据可视化图表

> 来源：白聊科技 | 时间：2026-05-24

## 核心内容

本文介绍如何使用蚂蚁集团 AntV 团队开源的 [[mcp-server-chart]] MCP Server，结合 [[Dify]] 工作流实现自然语言驱动的数据可视化。

## 关键实体

### [[mcp-server-chart]]

蚂蚁集团 AntV 团队开源的 MCP Server，支持 15+ 种可视化图表类型：

- 基础图表：折线图、柱状图、饼图、面积图、条形图
- 分析图表：直方图、散点图、矩阵树图、词云图、双轴图
- 高级图表：雷达图、思维导图、网络图、流程图、鱼骨图

**特点**：
- 以图片链接形式返回结果
- 支持 STDIO、SSE、streamable Http 三种调用方式
- Docker 镜像：`acuvity/mcp-server-chart:0.4.0`

### [[AntV]]

蚂蚁集团数据可视化团队，专注于企业级可视化解决方案。提供 mcp-server-chart 和 Dify 插件市场中的可视化工具。

### [[DeepSeek-V3]]

**关键发现**：Dify 工作流中必须使用 DeepSeek-V3 模型才能成功生成图表。其他模型会导致图表生成失败。

## 技术方案

### 方案一：Cherry Studio + MCP

```bash
docker run -d --name mcp-server-chart -it -p 8000:8000 acuvity/mcp-server-chart:0.4.0
```

配置 MCP 服务器（streamable Http 模式）：
- 名称：mcp-server-chart
- 地址：http://IP:8000/mcp

### 方案二：Dify 工作流 + MCP

完整工作流节点：

1. **开始节点** - 接收用户问题
2. **需求提炼** - 判断是否需要图表，提取 SQL 查询需求（使用 DeepSeek-V3）
3. **参数提取器** - 提取 sql_requirement、need_chart、chart_type
4. **自然语言转SQL** - 使用 ROOKIE_TEXT2DATA 插件
5. **执行SQL** - 连接数据库执行查询
6. **条件分支** - 根据 need_chart 决定路径
7. **图文总结** - Agent 策略（ReAct + MCP Tools，SSE 模式）
8. **文字总结** - 简洁自然语言分析
9. **回复节点** - 输出结果

**重要提示**：
- MCP 服务器配置必须使用 **SSE 模式**，不能用 streamable_http
- 原因：Dify 插件 Agent 策略暂不支持 streamable_http 协议生成图表
- Cherry Studio 客户端支持 streamable_http，但 Dify 插件不支持

### 方案三：AntV 插件

Dify 插件市场搜索 "antv" 安装蚂蚁集团可视化插件：

- 同样支持 15 种图表工具
- Agent 策略直接调用
- 可自定义图表宽高参数
- 需修改环境变量 `MAX_TOOLS_NUM=20` 才能添加全部工具

## 示例场景

### 票房数据库可视化

示例数据表 `boxoffice`：
- 字段：id, years, movie_name, score, director, box_office
- 测试查询：
  - "各导演的票房占比" → 饼图
  - "历年票房变化" → 折线图

### 词云图生成

输入：
```
根据诗人的名气以诗人的名字生成一个词云图，至少50位中国古代诗人
```

输出：图片链接 + Markdown 展示

## 与传统方案对比

| 方案 | 复杂度 | 优点 | 缺点 |
|---|---|---|---|
| 传统：数据库 + ECharts 插件 | 高 | 自定义程度高 | 需要 Python 转换数据格式，易出错 |
| MCP + mcp-server-chart | 低 | 一句话生成，无需代码 | 图表类型受限，依赖特定模型 |

## 关键概念

- [[数据可视化]] - 通过图表直观呈现数据洞察
- [[MCP协议]] - Model Context Protocol，AI Agent 工具调用标准
- [[Dify工作流]] - 可视化工作流编排平台
- [[自然语言转SQL]] - ROOKIE_TEXT2DATA 插件核心能力

## 部署要点

1. Docker 部署 mcp-server-chart（端口 8000）
2. MySQL 数据库准备示例数据
3. Dify 安装 ROOKIE_TEXT2DATA 插件
4. 工作流配置使用 DeepSeek-V3 模型
5. MCP 配置选择 SSE 协议模式

## 输出格式

所有图表以图片链接形式返回，可直接嵌入文档：

```
https://mdn.alipayobjects.com/one_clip/afts/img/...
```

链接公网可访问，支持 Markdown 直接展示。