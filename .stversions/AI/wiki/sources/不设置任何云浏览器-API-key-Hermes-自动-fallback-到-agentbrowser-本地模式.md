---
tags: [Hermes, Agent, MCP, GitHub, API, Skill]
source: "AI炼金社"
created: 2026-04-20
updated: 2026-05-10
category: Hermes
---

# 不设置任何云浏览器 API key# Hermes 自动 fallback 到 agent-browser 本地模式

> 来源: [AI炼金社](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA==&mid=2247484499&idx=1&sn=b92afc2206ed1be2e5ef25d08cf24f51&chksm=9711702a20ef1fd902b83f2f0ac01ec40ac94a57afa3d33126ad1d19c4c592e326cc5cd99dce&mpshare=1&scene=1&srcid=0420ckMliHMXCdoHuSDmftNE&sharer_shareinfo=8fb0fe9da68a89f351d63fe7af926ddf&sharer_shareinfo_first=8fb0fe9da68a89f351d63fe7af926ddf) | 2026-04-20

## 摘要

自动签到脚本跑不起来，因为浏览器要花钱？
Browserbase $0.05/分钟，Browser Use $0.02/请求。一个月自动签到 30 个站点，云浏览器成本几百块。更坑的是，每次截图、每次点击都要消耗 Token——8000 字 accessibility tree 直接塞进 context，跑几个任务 context 就爆了。
有没有免费方案？
有。**Hermes Agent + playwright-cli，Linux 服务器无头运行，零云浏览器成本，Token 消耗降低 93%。**
Playwright 官方 2026 年推出
，不是给人用的，是给 AI Agent 用的。
核心设计理念：**token-efficient**。
传统 Playwright MCP 把整个 accessibility tree 塞进 context，一个页面 8000+ 字。playwright-cli 只输出 element refs（
,
,
），Agent 用 ref 就能操作，不需要理解整个 DOM。
| 方案 | Token 消耗 | 成本 |
| --- | --- |...

## 相关实体

[[GitHub]], [[Hermes]], [[MCP]], [[Nodejs]], [[Vercel]]

## 相关概念

[[AI-Agent]], [[浏览器自动化]]
