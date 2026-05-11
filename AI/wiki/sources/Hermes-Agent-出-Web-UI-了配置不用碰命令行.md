---
tags: [Hermes, Agent, API, Skill]
source: "守护的AI笔记"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# Hermes Agent 出 Web UI 了，配置不用碰命令行

> 来源: [守护的AI笔记](https://mp.weixin.qq.com/s?__biz=MzYyNDE5NTM4Ng==&mid=2247484544&idx=1&sn=73cde356a39db9c7a4e5e30c654bd819&chksm=f1ab84b8dd3568ef7ef46428b4d119ca1945f8475efa9a55a1136c3166f60a14f227208cf394&mpshare=1&scene=1&srcid=0422m2rtlNMqWeZPC2LfC9H7&sharer_shareinfo=db72d7ec1ca8127d90b7b33240fbd283&sharer_shareinfo_first=db72d7ec1ca8127d90b7b33240fbd283) | 2026-04-22

## 摘要

有个场景可能你很熟悉：
好不容易把 Hermes Agent 装好了，要改个模型配置，打开终端，找到
，改了几行，重启，报错了。
看半天发现是 YAML 缩进写错了。
配个 API key，不知道改哪个 .env 文件，改完不生效，干脆重装。
现在这些不用碰命令行了。
Hermes 官方刚刚上线了 Web UI，所有配置在浏览器里点几下就搞定。
两步：
update 先把版本更新到最新，dashboard 把 Web UI 跑起来。
默认地址
，浏览器打开就行。
如果已经是最新版本了，那么直接执行下面的命令就好啦
如果你是服务器的话，需要使用 ssh 搭个隧道，这样你才能在本地打开页面。和小龙虾是类似。
我使用的是 finalshell，在设置-隧道里面里面添加即可。
Hermes Web UI 的定位是管理工具，它没有聊天界面，不知道后面会不会支持。
打开界面后，你会看到这些内容（右上角可以切换中文面板）：
**·状态Status**
相当于系统的健康检查面板。hermes 版本号、Gateway 进程 ID、当前有多少活跃会话，一目了然。
消息平台的连接状态和心跳时间也在下面排着。...

## 相关实体

[[Hermes]], [[OpenClaw]], [[微信]]

## 相关概念


