---
tags: [Python, 爬虫, Web-Scraping, Playwright, Cloudflare, MCP, Agent, GitHub, 开源]
source: "GitHub"
created: 2026-05-22
updated: 2026-05-22
category: 开发工具
---

# Scrapling - 自适应 Web 爬虫框架

> 来源: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | BSD-3-Clause | v0.4.8

## 摘要

Scrapling 是一个自适应 Web 爬虫框架，从单个请求到大规模爬取全搞定。其解析器能学习网站变化并自动重新定位元素，内置反反爬能力可绕过 Cloudflare Turnstile，Spider 框架支持并发、多 Session、暂停/恢复、自动代理轮换。

作者: Karim Shoair，Python 3.10+，PyPI 安装: `pip install scrapling`

## 核心特性

### 三种抓取模式

1. **Fetcher** — 纯 HTTP 请求，模拟浏览器 TLS 指纹，支持 HTTP/3，速度最快
2. **DynamicFetcher** — Playwright 驱动完整浏览器，处理 JS 动态渲染页面
3. **StealthyFetcher** — 高级隐身模式，指纹伪装，绕 Cloudflare Turnstile/Interstitial

### 自适应解析（最大卖点）

- 网站改版后自动重新定位目标元素
- `auto_save=True` 保存元素特征，`adaptive=True` 自动找回
- 智能相似度算法匹配元素

### Spider 框架（类 Scrapy）

- 并发爬取、多 Session、暂停/恢复（checkpoint）
- 内置代理轮换、域名限速、robots.txt 遵守
- 流式输出 + JSON/JSONL 导出
- 多种 Session 类型混用：HTTP + 隐身浏览器

### 其他亮点

- MCP Server（配合 Claude/Cursor 等 AI 工具使用）
- CLI 命令行直接抓网页，不用写代码：`scrapling extract get 'https://example.com' output.md`
- 交互式 IPython Shell 调试
- 解析速度比 BeautifulSoup 快 700+ 倍，与 Parsel/Scrapy 持平
- CSS / XPath / BeautifulSoup 风格选择器全部支持
- Docker 镜像: `docker pull pyd4vinci/scrapling`

## 安装

```bash
# 基础（仅解析器）
pip install scrapling

# 全部功能
pip install "scrapling[all]"

# 浏览器依赖
scrapling install --force
```

## 代码示例

### HTTP 请求
```python
from scrapling.fetchers import Fetcher
page = Fetcher.get('https://example.com', stealthy_headers=True)
quotes = page.css('.quote .text::text').getall()
```

### 隐身模式绕 Cloudflare
```python
from scrapling.fetchers import StealthyFetcher
page = StealthyFetcher.fetch('https://protected-site.com', headless=True, solve_cloudflare=True)
data = page.css('#content').getall()
```

### Spider 爬虫
```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
    name = "demo"
    start_urls = ["https://example.com/"]

    async def parse(self, response: Response):
        for item in response.css('.product'):
            yield {"title": item.css('h2::text').get()}

MySpider().start()
```

### CLI 直接抓取
```bash
scrapling extract get 'https://example.com' content.md
scrapling extract stealthy-fetch 'https://protected.com' data.txt --solve-cloudflare
```

## 性能对比（5000 嵌套元素文本提取）

| 库 | 耗时 | 对比 |
|---|---|---|
| Scrapling | 2.02ms | 1.0x |
| Parsel/Scrapy | 2.04ms | 1.01x |
| Raw Lxml | 2.54ms | 1.257x |
| PyQuery | 24.17ms | ~12x |
| BS4+Lxml | 1584ms | ~784x |

## 相关实体

[[Python]], [[Playwright]], [[Cloudflare]], [[MCP]], [[Scrapy]], [[BeautifulSoup]], [[Agent]], [[GitHub]]

## 相关概念

- Web Scraping
- 反反爬虫
- 浏览器自动化
- 自适应解析
- AI Agent 数据采集
