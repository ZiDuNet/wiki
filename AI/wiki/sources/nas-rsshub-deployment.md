---
title: "NAS部署RSSHub，全网平台信息一把抓！"
type: source-summary
created: 2026-05-22
updated: 2026-05-22
sources: [NAS部署RSSHub，全网平台信息一把抓！.md]
tags: [RSSHub, NAS, RSS, 信息聚合, Docker]
---

## Summary

这篇文章介绍了如何在 NAS 上部署 RSSHub 这一开源项目，实现全网平台信息的统一订阅和管理。RSSHub 可以将不支持 RSS 的平台转换为 RSS 订阅源，支持 400+ 网站，包括微博、小红书、B站、知乎、Twitter 等主流平台。

文章提供了完整的 docker-compose 部署方案，包括 RSSHub 主服务、Redis 缓存服务和 browserless 无头浏览器服务。详细介绍了各平台的路由支持情况和使用示例，特别是国内平台的订阅方法，以及需要 Cookie 配置的特殊路由（微博、小红书）。还推荐了配套的 RSS 阅读器和浏览器插件。

## Key Claims

1. RSSHub 支持 400+ 网站，一个服务全网通用
2. 微博路由需要 Cookie 才能稳定抓取，否则部分博主可能无法订阅
3. 小红书路由请求量排名第一，可见大家对小红书订阅的需求有多强烈
4. B站是 RSSHub 最热门的平台之一，请求量排第四，支持47条路由
5. 部署包含三个服务：RSSHub 主服务、Redis 缓存、browserless 无头浏览器

## Entities Mentioned

- [[RSSHub]]
- [[Docker]]
- [[Redis]]
- [[browserless]]
- [[B站]]
- [[微博]]
- [[小红书]]

## Concepts

- [[RSS订阅]]
- [[信息聚合]]
- [[Docker部署]]
- [[无头浏览器]]
- [[NAS自建服务]]

## Notable Quotes

> "不知道大家有没有这种情况——刷微博、刷小红书、看B站，想要的内容散落在各个平台，每天打开一堆APP来回切换，时间全碎片化了。"

> "RSS阅读器会定期访问这个地址，自动抓取最新内容推送到你面前——再也不用打开微博、B站刷来刷去了，在一个地方看完所有更新。"

## Limitations / Bias

文章由"前端仔"撰写，偏向技术教程风格，对新手友好但深度有限。部分平台路由需要 Cookie 配置，存在一定的技术门槛和隐私风险考量。