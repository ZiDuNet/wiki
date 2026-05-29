---
type: entity
name: CNIPA
created: 2026-05-29
updated: 2026-05-29
mentions: 1
---

# CNIPA

**类型:** 实体
**全称:** 中国国家知识产权局（China National Intellectual Property Administration）

## 简介

中国国家知识产权局专利公布公告站，专利查新的主要数据源。

## 功能

- 专利公布公告查询
- 专利检索与分析
- 专利申请状态跟踪
- 专利文献下载

## 在专利查新中的应用

[[patent-disclosure-skill]] 优先爬取 CNIPA 专利公布公告站：

1. 精准获取对比专利文献
2. 判断专利申请新颖性和创造性
3. 检索结果自动写入交底书第一章
4. 如站点异常或无结果，自动降级到网络搜索

## 技术集成

- 专属爬虫工具 `cnipa_epub_search.py`
- 依赖 Playwright（可选依赖）
- 降级机制保证查新不中断

## 相关概念

- [[专利查新]]
- [[技术交底书自动化]]

## 相关实体

- [[patent-disclosure-skill]]

## 来源文章

- [[ai帮我写专利交底书这个716星技能做到了]]