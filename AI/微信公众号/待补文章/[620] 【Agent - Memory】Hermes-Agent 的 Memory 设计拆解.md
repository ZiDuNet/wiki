# 【Agent - Memory】Hermes-Agent 的 Memory 设计拆解

> **状态**: 待补全文（原文链接无法抓取正文）
> **来源**: 微信公众号 | 时间: 2026-05-11 22:15

## 简介

TL;DR Hermes 的记忆系统不是"一个记忆库"，而是把不同稳定性、不同粒度、不同调用成本的信息放到不同层里。

## 原文链接

[【Agent - Memory】Hermes-Agent 的 Memory 设计拆解](https://mp.weixin.qq.com/s?__biz=Mzk2NDU1NDcyMA==&mid=2247484287&idx=1&sn=f0fc8de3bfa818df8aa61d7325fd957c&chksm=c5ec465aca9744b5d99e7bdc0fbb5e7a2bd637caf3a704b9ec5565ab71b896d0f470c953dc14&mpshare=1&scene=1&srcid=0511qFePfrGFGyUSxLxbViUP&sharer_shareinfo=594251bb4a759b144df2106565f9c693&sharer_shareinfo_first=594251bb4a759b144df2106565f9c693)
