---
title: Slidev
type: entity
tags: [HTML Slides, 工具, Vue, Markdown, 演示文稿]
sources: [全网最全html-slides实战教学.md]
created: 2026-05-29
updated: 2026-05-29
---

# Slidev

## 简介

Slidev是HTML Slides工具生态中的**开发者首选**，Markdown驱动的现代幻灯片制作工具，基于Vue技术栈，由Anthony Fu（Vue团队成员）开发。

## 核心特性

### 1. Markdown驱动
- 使用Markdown语法编写幻灯片内容
- 分隔符`---`分隔页面
- 支持Frontmatter配置每页样式

### 2. Vue技术栈
- 内置Vue 3支持
- 可在幻灯片中嵌入Vue组件
- 响应式数据绑定
- 组件复用

### 3. 代码高亮（Shiki）
- 内置[[Shiki]]代码高亮
- 支持多种编程语言
- 高精度语法高亮
- 行号、行高亮功能

### 4. 开发者友好功能
- **热更新**：实时预览修改
- **演讲者模式**：备注+下一页预览
- **绘图批注**：现场标注
- **导出功能**：PDF/PPTX/PNG

## 快速开始

```bash
npm init slidev@latest
```

输入命令即可启动项目，无需复杂配置。

## 适用场景

- **前端/全栈开发者**：技术分享、代码演示
- **需要大量代码演示的场景**：API工作坊、编程教学
- **团队协作**：Git版本控制+纯文本格式

## 优势

1. **版本答案**：做技术分享，Slidev是当前最佳选择
2. **代码高亮惊艳**：Shiki提供专业级代码展示
3. **生态完善**：Vue生态支持，组件丰富
4. **导出灵活**：PDF/PPTX多格式输出

## GitHub生态

### Slidev官方Skill
```bash
npx skills add slidevjs/slidev
```

官方团队维护，覆盖：
- Markdown语法
- 动画配置
- 代码高亮
- 图表嵌入
- 导出功能

### dev-slides
```bash
npx skills add https://github.com/claude-office-skills/skills --skill dev-slides
```

针对API工作坊、编程教学场景，包含可运行示例代码。

### slidev-syntax-guide
语法速查，通过LobeHub平台加载。

## 技术架构

- **前端框架**：Vue 3
- **构建工具**：Vite
- **代码高亮**：Shiki
- **Markdown解析**：Markdown-it
- **样式系统**：UnoCSS/WindiCSS

## 项目信息

- **GitHub**：slidevjs/slidev
- **开发者**：Anthony Fu
- **开源协议**：MIT
- **官网**：https://sli.dev/

## 相关工具对比

| 维度 | Slidev | [[reveal.js]] | [[Marp]] |
|------|--------|---------------|----------|
| 技术栈 | Vue + Markdown | 纯HTML/CSS/JS | 纯Markdown |
| 代码高亮 | Shiki（惊艳） | Prism/Highlight.js | 基础 |
| 学习成本 | 低（Markdown） | 中（需HTML/CSS） | 极低 |
| 表现力 | 高 | 极高 | 中 |
| 适用人群 | 开发者 | 设计师/创作者 | 极简主义者 |

## 相关概念

- [[HTML幻灯片范式转移]]
- [[Markdown驱动幻灯片]]
- [[演示文稿版本控制]]

## 相关实体

- [[Shiki]]
- [[Vue]]
- [[GitHub]]
- [[reveal.js]]
- [[Marp]]
- [[PPT]]

## 来源

- [[全网最全html-slides实战教学]]