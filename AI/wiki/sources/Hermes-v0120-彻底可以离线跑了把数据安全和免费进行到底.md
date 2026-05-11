---
tags: [Hermes, Claude, API, OpenAI]
source: "量子智元"
created: 2026-05-02
updated: 2026-05-10
category: Hermes
---

# Hermes v0.12.0 彻底可以离线跑了，把数据安全和免费进行到底

> 来源: [量子智元](https://mp.weixin.qq.com/s?__biz=MzkwMTc4NTkwNg==&mid=2247488188&idx=1&sn=13f87fb03ef1d83c5752d204995ff2ff&chksm=c1d699d9265383783fb324c5cd91d26b268b55e30a9248acc1265c0f01d4d03bde11fd355577&mpshare=1&scene=1&srcid=05029frOv5UTD0CnkfiE7576&sharer_shareinfo=b70938e0ce5648608b9ecdf47a076d36&sharer_shareinfo_first=b70938e0ce5648608b9ecdf47a076d36) | 2026-05-02

## 摘要

我用Hermes有一段时间了，一直有个心结：它太依赖外部服务。
每次跑Hermes，模型调用要联外网，语音合成要联外网，甚至连一些工具检查都要往外戳一下。对于有隐私顾虑的场景——比如处理公司内部文档、分析敏感数据——这个架构本身就是个问题。
v0.12.0这次我看到三个变化，加在一起算是把这个问题正式回应了。
之前LM Studio在Hermes里是什么地位？叫"custom endpoint alias"——翻译一下，就是临时工。你可以把LM Studio的API地址填进去当自定义端点用，但Hermes不真正认识它，不帮你做检查，不帮你列模型，报错了也不给有用的提示。
这次升级之后，LM Studio成了"first-class provider"，跟OpenAI、Anthropic平级。具体说：
- **独立认证流程**：在
里有专门的LM Studio检查项，配置对不对一眼能看出来
- **动态模型列表**：连上LM Studio之后，
能自动列出你本地已经下载的所有模型，不用手动填模型名
- **Reasoning transport支持**：如果你跑的是支持推理能力的本地模型...

## 相关实体

[[Hermes]]
[[Claude]]

## 相关概念

[[本地部署]]
[[数据安全]]
[[记忆系统]]
