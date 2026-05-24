---
type: entity
name: mcp-server-chart
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# mcp-server-chart

**类型:** 实体 - MCP Server / 数据可视化工具
**开发者:** 蚂蚁集团 AntV 团队
**提及文章数:** 1

## 简介

蚂蚁集团 AntV 团队开源的 MCP Server，让 AI Agent 能够一句话生成 15+ 种专业数据可视化图表。以图片链接形式返回结果，方便嵌入任何场景。

## 核心特性

### 支持图表类型

**基础图表（5种）**
- 折线图 (Line Chart)
- 柱状图 (Bar Chart)
- 饼图 (Pie Chart)
- 面积图 (Area Chart)
- 条形图 (Horizontal Bar)

**分析图表（5种）**
- 直方图 (Histogram)
- 散点图 (Scatter Plot)
- 矩阵树图 (Treemap)
- 词云图 (Word Cloud)
- 双轴图 (Dual Axis)

**高级图表（5种）**
- 雷达图 (Radar Chart)
- 思维导图 (Mind Map)
- 网络图 (Network Graph)
- 流程图 (Flowchart)
- 鱼骨图 (Fishbone Diagram)

### 技术规格

- **协议支持**: STDIO、SSE、streamable Http
- **Docker 镜像**: `acuvity/mcp-server-chart:0.4.0`
- **GitHub**: https://github.com/antvis/mcp-server-chart
- **Docker Hub**: https://hub.docker.com/r/acuvity/mcp-server-chart

## 使用方式

### Docker 部署

```bash
docker run -d --name mcp-server-chart -it -p 8000:8000 acuvity/mcp-server-chart:0.4.0
```

### MCP 配置

**Cherry Studio (streamable Http)**
```json
{
  "name": "mcp-server-chart",
  "type": "streamable Http",
  "url": "http://10.44.32.14:8000/mcp"
}
```

**Dify Agent 策略 (SSE)**
```json
{
  "servers": {
    "mcp-server-chart": {
      "url": "http://10.44.32.14:8000/sse"
    }
  }
}
```

**重要**: Dify 插件 Agent 策略不支持 streamable_http，必须使用 SSE 协议。

## 输出特点

- 图片链接形式返回
- 公网可访问（支付宝 CDN）
- 支持 Markdown 直接嵌入
- 示例链接格式：`https://mdn.alipayobjects.com/one_clip/afts/img/...`

## 应用场景

### 1. Cherry Studio 客户端

直接添加 MCP 服务器，一句话生成图表：
```
根据诗人的名气以诗人的名字生成一个词云图，至少50位中国古代诗人
```

### 2. Dify 工作流集成

结合数据库查询实现：
- 自然语言 → SQL → 数据 → 图表
- 需要 DeepSeek-V3 模型（其他模型会失败）
- 配合 ROOKIE_TEXT2DATA 插件

### 3. AntV 插件替代

Dify 插件市场提供 antv 插件：
- 相同功能，无需 MCP 配置
- 需修改环境变量 `MAX_TOOLS_NUM=20`
- 可自定义图表宽高

## 相关实体

- [[AntV]] - 开发团队
- [[Dify]] - 工作流平台
- [[DeepSeek-V3]] - 必需模型
- [[Cherry Studio]] - MCP 客户端

## 相关概念

- [[数据可视化]]
- [[MCP协议]]
- [[Dify工作流]]
- [[自然语言转SQL]]

## 相关文章

- [[dify打造数据可视化图表]]