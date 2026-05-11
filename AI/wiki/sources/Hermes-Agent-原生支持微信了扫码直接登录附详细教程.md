---
tags: [Hermes, Agent, GitHub, API, Python, Skill, OpenClaw]
source: "守护的AI笔记"
created: 2026-04-24
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 原生支持微信了，扫码直接登录（附详细教程）

> 来源: [守护的AI笔记](https://mp.weixin.qq.com/s?__biz=MzYyNDE5NTM4Ng==&mid=2247484524&idx=1&sn=85a49f2ea45e68e1ec9c1d9880c750e4&chksm=f18b78172b66aad6ae559ea3a2bb32260f73864f02ec442c8bed8a501293adc9b4e30cfaa160&mpshare=1&scene=1&srcid=0424PoBTxfYH1zzByYbXflrz&sharer_shareinfo=21d85be8159d6b2d0b0dd50a406e4384&sharer_shareinfo_first=21d85be8159d6b2d0b0dd50a406e4384) | 2026-04-24

## 摘要

Hermes Agent 最近更新了微信原生支持，用的还是腾讯官方的 iLink Bot API，不是那种容易被封的第三方协议。
加上它本身有内置学习循环机制，越用越聪明，值得试一下。
而且直接在微信里面完成闭环，直接让 AI 处理，方便多了。
这篇文章给你完整的安装和微信连接教程，从零基础到能用，大约 5 分钟。
安装非常简单，一条命令搞定。（mac 和 linux 可以直接安装，windows 不支持，需要用 WSL2。如果你之前没装过 WSL2，先去微软商店装一个 Ubuntu，再在 WSL2 里跑上面的命令。）
这里使用服务器给大家演示一下，直接执行命令，然后等待即可。
安装完成后会自动检测系统环境，如果之前用过 OpenClaw，它会提示你是否迁移配置：
选择迁移的话，SOUL.md、用户设定、消息配置、大模型供应商信息、已安装的 Skills 都会自动导入。省了不少事。
如果之前没有 OpenClaw 配置，安装脚本会引导你一步步设置模型供应商、Agent 配置、消息平台等。
配置完成后，重新刷新资源（不刷新的话，会找不到 hermes 命令），然后启动对话。
**1. 配...

## 相关实体

[[GitHub]], [[Hermes]], [[OpenClaw]], [[Python]], [[微信]]

## 相关概念


