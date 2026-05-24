---
type: entity
name: AntV
created: 2026-05-24
updated: 2026-05-24
mentions: 1
---

# AntV

**类型:** 实体 - 组织/数据可视化团队
**所属:** 蚂蚁集团 (Ant Group)
**提及文章数:** 1

## 简介

蚂蚁集团数据可视化团队，专注于企业级数据可视化解决方案。开源了 mcp-server-chart MCP Server 和 Dify 插件市场的可视化工具。

## 核心贡献

### mcp-server-chart

开源 MCP Server，支持 15+ 种图表类型的自然语言生成：

- GitHub: https://github.com/antvis/mcp-server-chart
- Docker Hub: https://hub.docker.com/r/acuvity/mcp-server-chart
- 特点：图片链接返回，三协议支持（STDIO/SSE/streamable Http）

### Dify 插件市场 AntV 插件

提供 15 种可视化工具的 Dify 插件：
- 与 mcp-server-chart 功能相同
- 直接 Agent 调用，无需 MCP 配置
- 可自定义图表宽高参数

## 技术特点

### 图表类型覆盖

| 类别 | 图表类型 |
|---|---|
| 基础图表 | 折线图、柱状图、饼图、面积图、条形图 |
| 分析图表 | 直方图、散点图、矩阵树图、词云图、双轴图 |
| 高级图表 | 雷达图、思维导图、网络图、流程图、鱼骨图 |

### 输出格式

所有图表通过支付宝 CDN 返回图片链接：
- 公网可访问
- 支持 Markdown 嵌入
- 链接格式：`https://mdn.alipayobjects.com/one_clip/afts/img/...`

## 开源项目

AntV 团队维护的数据可视化开源项目矩阵：
- G2 - 可视化语法
- G6 - 图可视化引擎
- F2 - 移动端可视化
- X6 - 图编辑引擎
- L7 - 地理空间可视化
- AVA - 可视分析框架

## 相关实体

- [[mcp-server-chart]] - 开源 MCP Server
- [[蚂蚁集团]] - 母公司
- [[Dify]] - 插件平台

## 相关概念

- [[数据可视化]]
- [[MCP协议]]
- [[图表生成]]
- [[自然语言转图表]]

## 相关文章

- [[dify打造数据可视化图表]]