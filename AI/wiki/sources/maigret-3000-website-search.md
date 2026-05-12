---
title: "GitHub 2.4万Star的Maigret：一个用户名搜遍3000+网站"
type: source-summary
created: 2026-05-11
updated: 2026-05-11
sources: [GitHub 上狂揽 2.4 万 Star！输入一个用户名，就能查遍 3000+ 网站。.md]
tags: [GitHub开源项目, 开源情报, OSINT, Python工具]
---

## Summary

Maigret 是一个开源用户名搜索工具（GitHub 2.4万Star），输入一个用户名即可在全球3000+网站搜索该用户的注册痕迹，生成完整数字画像报告。支持递归搜索（发现新线索自动继续挖掘）、AI分析模式（LLM智能梳理关联信息）、多格式输出（HTML/PDF/XMind/JSON/CSV/D3图谱）。已被多个专业OSINT平台商业化采用。

## Key Claims

1. Maigret 默认扫描全球访问量前500站点，-a 参数全量扫描3000+站点
2. 递归搜索：当在一个站点发现新关联ID或用户名，自动拿新线索继续搜索，形成账号关系网
3. 2026年4月新增AI分析模式，由LLM对原始搜索结果进行智能分析
4. 支持按标签筛选站点（如只搜某国家或某类型平台）
5. 站点数据库每24小时自动从GitHub拉取更新
6. 自带Web界面（Docker一键启动）和Telegram机器人

## Entities Mentioned

- [[GitHub开源项目]] — Maigret 项目托管
- [[Maigret]] — 工具本身

## Concepts

- [[开源情报(OSINT)]] — Maigret 属于公开来源情报工具

## Notable Quotes

> "SEO 是让百度收录你，GEO 是让 ChatGPT 在回答用户问题时报出你的名字。"（来自文中相关背景）

## Limitations

- 仅供教育与合法用途，需遵守当地法律法规
- 对隐私和个人信息保护存在争议
