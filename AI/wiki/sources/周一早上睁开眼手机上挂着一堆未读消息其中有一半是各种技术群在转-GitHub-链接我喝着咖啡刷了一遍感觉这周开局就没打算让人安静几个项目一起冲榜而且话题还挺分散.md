---
tags: [GitHub, Agent, Claude, RAG, Prompt, API, Skill]
source: "AI程序员的牛马生活"
created: 2026-04-27
updated: 2026-05-10
category: GitHub
---

# 周一早上睁开眼，手机上挂着一堆未读消息，其中有一半是各种技术群在转 GitHub 链接。我喝着咖啡刷了一遍，感觉这周开局就没打算让人安静——几个项目一起冲榜，而且话题还挺分散，从 Agent 技能到 TypeScript 换底层，全都在同一天挤进了视野。

> 来源: [AI程序员的牛马生活](https://mp.weixin.qq.com/s?__biz=MzU3MjQzMzk5MA==&mid=2247483693&idx=1&sn=497dd4e77db5fa76bb568a38a727cedc&chksm=fd22d1ef16bd5d6180fdb1a84063c3d5de91c7c33b6a7b76d6c7df882e877da2a4fa423fe4a0&mpshare=1&scene=1&srcid=0427gWoaMJnjpp6gzcV7dTvQ&sharer_shareinfo=b5c6c79b1c3f3e9090ded1565600e480&sharer_shareinfo_first=b5c6c79b1c3f3e9090ded1565600e480) | 2026-04-27

## 摘要

下面是今天值得看一眼的东西，不废话，直接进正题。
这个项目一上来就吸引了我的注意——作者 Matt Pocock 是 TypeScript 社区的老熟脸，他直接把自己平时用的 Agent 技能集合开了一个公开仓库。
简单说：这是一堆 shell 脚本和 prompt 文件，专门用来告诉 AI 编码助手"你在我这个项目里该怎么工作"。比如代码审查的规则怎么定、提交信息要用什么格式、跑测试之前要检查哪些东西。不是什么黑科技，但实用程度很高。
我自己也在折腾类似的东西，每次换项目都得重新给 AI 讲规矩，这种"可复用的技能包"思路确实省事。Star 数已经破 23K，说明不止我一个人有这个痛点。
微软在悄悄干一件大事：用 Go 重写 TypeScript 编译器。
这个项目现在还是"暂存仓库"状态，25K 星已经说明社区热度不低。逻辑很直接——现有的 TypeScript 编译器是 JS 写的，跑在 Node.js 上，性能有天花板；换成 Go 之后，编译速度理论上有大幅提升空间。
对我们日常开发影响几何？短期内基本感受不到，长期来看如果大型项目的
时间从 30 秒变成 3 秒，那体感确实完...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]], [[Hermes]], [[LangChain]], [[Node.js]], [[VS-Code]]

## 相关概念

[[AI-Agent]], [[代码审查]], [[知识图谱]], [[自进化系统]]
