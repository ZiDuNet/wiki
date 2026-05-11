---
tags: [Hermes, Agent, GitHub, 飞书, Prompt, API, Python, OpenAI]
source: "i龙虾"
created: 2026-04-28
updated: 2026-05-10
category: Hermes
---

# 给 Hermes 装个好看的壳：Open WebUI 接入完整指南

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484477&idx=1&sn=e6fa49dd8a9f3dbc93812b7b09c2b977&chksm=ea9f16b3e92f45cf4dcb3455db6e8c6f0a7bda7cbb87281793a4338b384afc3f0b1d109fdbb4&mpshare=1&scene=1&srcid=0428FJFM0pxxJ4opy0UzCile&sharer_shareinfo=e51e8cb8489d03466901985958960b60&sharer_shareinfo_first=e51e8cb8489d03466901985958960b60) | 2026-04-28

## 摘要

昨天看到一个视频，以 Open WebUI的界面使用Hermes ，看起来效果还不错，然后我就去折腾了一下 Open WebUI。
**接入之后，Hermes 直接变成了一个本地版 ChatGPT**。界面干净，对话记录自动存，代码能直接预览，文件拖上去就能用。而且是开源项目，可以免费部署。
Open WebUI 本质上是个前端壳，它本来是用来连 Ollama 的，但因为走的是 OpenAI 兼容协议，所以只要后端能吐
格式的接口，它都能连。
Hermes 从 v0.4.0 起就内置了 API 服务器，完整兼容这个格式。所以整个流程就是：
1. 在 Hermes 的
里开启 API 服务器
2. 用
把它跑起来
3. Docker 启动 Open WebUI，把接口地址指向 Hermes
4. 打开浏览器，开聊
编辑
，加上这两行：
就是个访问令牌，Open WebUI 连接时要带上它。随便写，比如
，记住就行。
然后启动网关：
看到这行就说明 API 服务器起来了：
默认端口是 **8642**，只监听本机（
），不对外暴露。这个设计很合理，本地用完全够。
想验证一下有没有跑起来，可...

## 相关实体

[[ChatGPT]], [[Docker]], [[GitHub]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[Python]], [[飞书]]

## 相关概念

[[记忆系统]]
