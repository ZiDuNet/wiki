---
title: 不到 1000 行代码：Markdown 浏览器渲染插件
type: source-summary
tags: [Markdown, Chrome Extension, 浏览器, 主题, Wiki-link]
sources: [不到 1000 行代码，让本地 .md 文件在浏览器里拥有在线一样的阅读体验.md]
created: 2026-05-22
updated: 2026-05-22
---

# 不到 1000 行代码：Markdown 浏览器渲染插件

> 📎 来源: [武始舞终悟无极](https://mp.weixin.qq.com/s?__biz=MjM5NzEwNjkzMg==&mid=2448260614&idx=1&sn=02f4e3722288e8b9afe7611a14aadad7) | 时间: 2026-05-22

## 核心定位

一个晚上造的 Chrome 扩展——**打开即用，零配置**。让本地 `.md` 文件在浏览器里拥有在线一样的阅读体验。

> 最好的工具，是让你忘记它存在的工具。

---

## 解决的问题

**痛点：**

- Chrome 默认把 `.md` 文件当纯文本处理（满屏 `#` 号和 `**` 加粗标记）
- 想分享给同事预览，对方说「打不开，全是乱码」
- 装插件要么要注册账号，要么配置复杂到劝退

---

## 功能特性

任意本地 `.md` 文件拖进浏览器，看到的是：

- ✅ **渲染后的排版**（标题层级、表格、代码高亮、引用块）
- ✅ **三档主题切换**（🌙 暗夜 / ☀️ 白昼 / 📜 羊皮卷），刷新不丢失
- ✅ **左侧常驻文件目录**（📂 按钮切换）
- ✅ **顶部面包屑导航**
- ✅ **浮动目录**
- ✅ **Wiki 风格内链**（`[[概念页]]`）自动跳转

---

## 架构设计

| 文件 | 职责 |
|------|------|
| `manifest.json` | Chrome 扩展声明，MV3 协议 |
| `content.js` | 页面注入、渲染、主题、交互 |
| `background.js` | Service worker，处理 file:// 目录请求和跨页导航 |
| `404.html` + `404.js` | 兜底 404 页面 |

**核心依赖：** `lib/marked.min.js` — GitHub 同款 GFM 解析器，单文件零依赖。

---

## 工作流程时序

```
用户 → 拖入 .md 文件 → content.js 拦截 Chrome 原生渲染
    ↓ content.js → background.js 请求读取文件内容
    ↓ background.js 代理 fetch file:// 资源
    ↓ background.js → content.js 返回文件文本
    ↓ content.js → marked.js 调用 parse() 解析
    ↓ marked.js → content.js 返回 HTML
    ↓ content.js → 注入完整页面 DOM
    ↓ 用户 → 渲染完成，主题/目录/导航就绪
```

---

## 技术亮点

### 1. 主题系统靠 CSS 变量

只声明一套变量，三个主题各定义一次值：

```css
/* 默认主题 + 暗夜主题共用一套变量 */
:root, [data-theme="night"] {
  --bg: #121220;      /* 深邃夜空蓝 */
  --text: #e0dcc8;    /* 暖米白 */
  --gold: #d4b356;    /* 复古金 */
  --accent: #8fa0d4;  /* 紫罗兰 */
}

/* 白昼主题覆盖变量值 */
[data-theme="day"] {
  --bg: #f5f3ed;      /* 羊皮纸白 */
  --text: #2a2a34;    /* 深灰黑 */
  --gold: #a8841e;    /* 琥珀金 */
  --accent: #4a6098;  /* 深海蓝 */
}
```

切换主题只改一行 `document.documentElement.dataset.theme`，所有元素自动跟随。

主题记忆走 `localStorage`，打开新页不丢失。

### 2. Content script 注入整页 DOM

把整个页面换成自己的 HTML：

```javascript
// 拦截 Chrome 原生文件渲染，用自己的 bodyHTML 替换
document.body.innerHTML = bodyHTML;
```

`bodyHTML` 是完整页面模板字符串，包含顶栏、侧边栏、内容区、目录浮层、404 页。

---

## 设计哲学

> 限制不是障碍，是创造力的催化剂。

---

## 相关实体与概念

- [[Markdown]] — 核心格式
- [[Chrome Extension]] — MV3 扩展
- [[GFM]] — GitHub Flavored Markdown
- [[Wiki-link]] — `[[概念页]]` 内链语法
- [[Obsidian]] — Markdown 编辑器
- [[VS Code]] — Markdown 编辑器

---

## 适用场景

- Obsidian / VS Code 写好的 Markdown 笔记，想在浏览器里预览
- 分享给同事预览 Markdown 文件
- Wiki 风格知识库的本地阅读