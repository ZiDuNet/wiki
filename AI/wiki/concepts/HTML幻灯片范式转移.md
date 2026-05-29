---
title: HTML幻灯片范式转移
type: concept
tags: [HTML Slides, 范式转移, PowerPoint, 演示文稿]
sources: [全网最全html-slides实战教学.md]
created: 2026-05-29
updated: 2026-05-29
---

# HTML幻灯片范式转移

## 定义

HTML Slides不是"另一种PPT"，而是演示文稿领域的**范式转移**（Paradigm Shift）。从传统的PowerPoint/WPS二进制格式转向基于Web标准的HTML/CSS/JS纯文本格式。

## 核心变革

### 1. 体积与分发革命
- **传统PPT**：50MB，需要专用软件（Office/WPS）
- **HTML Slides**：几百KB，浏览器即可播放
- 解决痛点：
  - 字体丢失
  - 排版错乱
  - 对方没装Office
  - 手机无法查看

### 2. 版本控制革命
- **传统PPT**：二进制文件，Git无能为力，"最终版_v3_真最终.pptx"常态
- **HTML Slides**：纯文本格式，Git完美支持
  - 每次修改清晰记录
  - Review、Revert、分支协作全部打通
  - 团队可像管代码一样管幻灯片

### 3. 表现力革命
传统办公套件无法企及的能力：
- 内嵌代码高亮（[[Shiki]]）
- 实时编辑预览
- 嵌入Vue/React组件
- Canvas动画
- ECharts数据图表
- 3D过渡效果

### 4. 开放性革命
- **传统PPT**：闭源格式，依赖厂商（Microsoft/WPS）
- **HTML Slides**：HTML/CSS/JS是Web标准，不依赖任何厂商
  - 即使工具停更，源文件依然可在任何浏览器打开
  - 完全自由，不被绑定

## 市场趋势

连WPS都在网页版上线了"HTML素材"功能，这股浪潮已经不是预测，而是**正在进行时**。

## 工具生态

主流HTML Slides工具：

| 工具 | 定位 | 技术栈 | 适用场景 |
|------|------|--------|---------|
| [[Slidev]] | 开发者首选 | Vue + Markdown | 技术分享、代码演示 |
| [[reveal.js]] | 功能天花板 | 纯HTML/CSS/JS | 极致视觉效果 |
| [[Marp]] | 极简派 | 纯Markdown | 快速文档型演示 |
| Byeslide | Agent-first | CSS变量 | AI深度整合 |
| OpenSlides | 本地工作台 | Reveal.js + AI | 频繁迭代原型 |

## 核心理念

HTML Slides的革命本质：**从"手工排版"变成"工程化创作"**

- Markdown = 可版本控制的代码
- [[AI Skill]] = 审美的持续资产
- 每一页 = 精确控制下的自由表达

## 实战案例

作者实测：
- 25页幻灯片，15KB大小
- 制作时间：5分钟
- 浏览器打开就能讲

## 相关概念

- [[Markdown驱动幻灯片]]
- [[演示文稿版本控制]]
- [[AI生成PPT]]

## 相关实体

- [[PPT]]
- [[Slidev]]
- [[Marp]]
- [[reveal.js]]
- [[Shiki]]
- [[GitHub]]

## 来源

- [[全网最全html-slides实战教学]]