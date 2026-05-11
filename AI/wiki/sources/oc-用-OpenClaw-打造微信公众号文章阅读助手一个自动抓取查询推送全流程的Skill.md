---
tags: [Agent, GitHub, OpenClaw, Skill, 公众号, 微信, 自动化, 部署]
sources: ['微信公众号/OpenClaw/用 OpenClaw 打造微信公众号文章阅读助手：一个自动抓取、查询、推送全流程的Skill.md']
created: 2026-05-10
updated: 2026-05-10
---

# 用 OpenClaw 打造微信公众号文章阅读助手：一个自动抓取、查询、推送全流程的Skill

**Source:** OpenClaw 公众号文章
**Category:** OpenClaw
**Date ingested:** 2026-05-10
**Type:** article

## Summary

> 📎 来源: REITs研习笔记 | 时间: 2026-04-20 19:11 你有没有这样的困扰：每天要翻十几个公众号才能看完行业动态；想找一篇几天前读过的文章却怎么也翻不到；或者想针对某篇推文做深度分析，却只能手动复制粘贴…… 现在，我开发了一个 Skill（可直接应用于 OpenClaw）—— **wechat-query-skill**，它把微信公众号的订阅、新文章内容缓存、查询、推送、巡检串成了一条自动化流水线。

## Key Claims

- 你拥有一个微信公众号（订阅号、服务号均可）
- 首次使用或登录失效时，需要**公众号管理员微信**扫码登录（登录有效期为4天，可随时重新登录续期）
- 支持 Linux / macOS / Windows
- 后台自动轮询已订阅的公众号并把文章缓存到本地数据库
- 之后查询、分析、推送都优先基于缓存库进行

## Entities Mentioned

- [[GitHub]]
- [[OpenClaw]]
- [[飞书]]

## Concepts Covered

- [[Cron定时任务]]
- [[Skill开发]]
- [[本地部署]]

## Related Sources

- [[OpenClaw文章索引]]
