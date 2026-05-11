---
tags: [OpenClaw, Agent, Claude, GitHub, 飞书, PPT, Dify, Harness]
source: "墨语心菲"
created: 2026-04-23
updated: 2026-05-10
category: OpenClaw
---

# 1. Python 3.10+

> 来源: [墨语心菲](https://mp.weixin.qq.com/s?__biz=MjM5MzUxMjk3Nw==&mid=2448491462&idx=1&sn=39f62d0f563f113b288aa455427c8156&chksm=b3240fcd0650f1f827cc67d1fcff139fb4921b7e3bcdad65d2fa857cfb20e18099ca7fef678f&mpshare=1&scene=1&srcid=0423VFeSb2aJJJc8k6KdhlDw&sharer_shareinfo=1d8a89189984419402a902123e8fd084&sharer_shareinfo_first=1d8a89189984419402a902123e8fd084) | 2026-04-23

## 摘要

**点击蓝字**
**关注我们**
**一**
**使用感受：当工具从"玩具"变成"管家"**
最近把主力环境从OpenClaw（俗称"龙虾"）迁移到Hermes Agent，用一个词形容感受：从驯兽变成了用管家。
用龙虾的时候，我总有一种在"驯服野生AI"的错觉。它很聪明，但太不稳定——配置好的股票定时任务隔天就失联，微信端的消息偶尔能收到、偶尔石沉大海，最头疼的是定时任务，有时正常，有时发不出来，你永远不知道下次是否能正常发出来。
切换到Hermes之后，这些异常基本都消失了。
稳定性方面，Hermes的会话持久化做得扎实。我配置的每日16:30自动拉取腾讯财经API、更新持仓数据的定时任务，跑了两周没有掉过一次链子。微信、飞书两个通道同时在线，我在任何一个端发指令都能无缝接续上下文。这种"随时在、随时应"的感觉，才是Agent应有的样子。
操作授权方面，Hermes的设计更贴近真实工作流。它有一个危险命令检测+用户确认的中间层，不是一刀切地拒绝所有终端操作，而是智能识别风险等级——比如我让它
python3 /root/.openclaw/workspace/tencent\_s...

## 相关实体

[[Anthropic]], [[Claude]], [[DeepSeek]], [[Dify]], [[GPT-4]], [[GitHub]], [[Harness]], [[Hermes]], [[OpenAI]], [[OpenClaw]], [[Python]], [[微信]], [[飞书]]

## 相关概念

[[AI-Agent]], [[Agent架构]], [[Multi-Agent]], [[多模态]], [[思维链]], [[自进化系统]], [[记忆系统]]
