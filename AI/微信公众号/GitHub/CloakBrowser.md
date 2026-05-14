---
title: CloakBrowser - 隐形 Chromium 浏览器
source: https://github.com/CloakHQ/CloakBrowser
author: CloakHQ
date: 2026-05-14
tags:
  - GitHub
  - 浏览器
  - 自动化
  - 反检测
  - Chromium
  - 爬虫
  - Playwright
---

# CloakBrowser - 隐形 Chromium 浏览器

## 项目简介

CloakBrowser 是一个隐形 Chromium 浏览器（Stealth Chromium Browser），通过在 **C++ 源码级别修改浏览器指纹**，实现对反机器人检测系统（Anti-Bot Systems）的绕过。它作为 Playwright 和 Puppeteer 自动化框架的直接替代品，无需修改代码即可实现隐形浏览。

**核心理念**：真正的 Chromium 二进制文件，指纹在 C++ 源码级别修改。

## 项目信息

| 属性 | 信息 |
|------|------|
| GitHub | https://github.com/CloakHQ/CloakBrowser |
| 官方网站 | https://cloakbrowser.dev |
| 当前版本 | v0.3.26 (Chromium 146.0.7680.177.4) |
| 许可证 | MIT（封装代码），自定义（二进制文件免费使用，禁止再分发） |
| Stars | 5,256+ |

## 核心架构

```
用户代码 (Playwright/Puppeteer API)
        ↓
CloakBrowser 封装层 (Python/JavaScript)
        ↓
定制 Chromium 二进制文件 (57 个C++ 补丁)
        ↓
目标网站 (反机器人系统看到的是正常浏览器)
```

### 技术栈

| 组件 | 技术 |
|------|------|
| 浏览器引擎 | Chromium 146（定制编译） |
| Python 封装 | Playwright 兼容 API |
| JavaScript 封装 | TypeScript，完整类型定义，支持 Playwright |

## 功能特性

### 🛡️ 源码级指纹补丁

- **57 个 C++ 补丁**：在 Chromium 源码级别修改浏览器指纹
- **通过所有机器人检测测试**：30/30 测试全部通过
- **无需额外配置**：开箱即用的隐形浏览器

### 🔄 框架兼容性

- **Playwright 直接替代**：无需修改代码，直接替换
- **Puppeteer 支持**：同样支持无缝替换
- **CDP（Chrome DevTools Protocol）**：完整支持开发者工具协议

### 🔒 隐私与安全

- 专注于用户隐私保护
- 阻止追踪器
- 提供匿名性和安全性保障

## 指纹补丁原理

CloakBrowser 的核心创新在于**源码级指纹修改**：

1. **修改 Chromium 源码**：直接在 C++ 层面修改浏览器引擎
2. **消除自动化痕迹**：移除 WebDriver、navigator.webdriver 等自动化标识
3. **模拟真实浏览器行为**：确保所有指纹特征与真实浏览器一致
4. **57 个定向补丁**：针对各种反检测技术进行源码级别修复

相比传统的 JavaScript 注入方式（如 puppeteer-extra-plugin-stealth），源码级修改更加彻底、更难被检测。

## 安装方式

### Python 安装

```bash
pip install cloakbrowser
```

### JavaScript/TypeScript 安装

```bash
npm install cloakbrowser
```

### 下载二进制文件

访问 GitHub Release 页面下载预编译的定制 Chromium 二进制文件。

## 使用方法

### Python 示例

```python
from cloakbrowser import Browser

# 与 Playwright API 完全兼容
browser = Browser()
page = browser.new_page()
page.goto('https://example.com')
print(page.content())
browser.close()
```

### JavaScript 示例

```typescript
import { Browser } from 'cloakbrowser';

const browser = await Browser.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
console.log(await page.content());
await browser.close();
```

## 与 Playwright 对比

| 特性 | Playwright | CloakBrowser |
|------|------------|--------------|
| 浏览器引擎 | 标准 Chromium | 定制编译 Chromium |
| 反检测能力 | 需要 stealth 插件 | 源码级别修复 |
| 指纹修改 | JavaScript 注入 | C++ 源码修改 |
| 检测测试通过率 | 部分通过 | 30/30 全通过 |
| 代码兼容性 | - | 100% 兼容 Playwright |
| 额外配置 | 需要 stealth 插件配置 | 无需额外配置 |

## 应用场景

1. **Web 爬虫**：绕过反爬虫检测
2. **自动化测试**：模拟真实用户行为
3. **数据采集**：避免被封禁
4. **隐私浏览**：保护用户匿名性
5. **RPA 自动化**：机器人流程自动化

## 相关项目

- **CloakBrowser-Manager**：基于 Web 的浏览器配置文件管理器，创建、启动和管理隔离的浏览器实例

## GitHub 链接

- **项目主页**：https://github.com/CloakHQ/CloakBrowser
- **官方网站**：https://cloakbrowser.dev

---

> 📝 **说明**：CloakBrowser 通过源码级别的指纹修改，提供了比传统 stealth 插件更彻底的反检测方案。对于需要高度隐蔽性的自动化任务，是一个值得考虑的选择。