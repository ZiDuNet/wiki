> 📎 来源: [繁星AI随笔](https://mp.weixin.qq.com/s?__biz=MzY5OTE1NzUzNw==&mid=2247484779&idx=1&sn=4c4fb9f451e23ea6ccc95dacb79d4779&chksm=f542a31c422689a331d445c7d4a10d9413d74b7a0fac0d9583c90fb27fca0041124c9e5df5b8&mpshare=1&scene=1&srcid=0517Kdqfmr87i1ZHN5DIufCJ&sharer_shareinfo=65ccabfdbf1131613d1d7862a0a0fbd1&sharer_shareinfo_first=65ccabfdbf1131613d1d7862a0a0fbd1) | 时间: 2026-05-17 23:50

---

大家好，这里是繁星。

市面上提示词合集很多，但仔细翻看就会发现一个尴尬的现实：

大多数要么是全英文的，对中文场景水土不服。

要么就是千篇一律的“扮演一个xxx，帮我做某件事”这类入门级模板。

真正具备工程质量的中文提示词合集，真的稀有。

直到在 GitHub 上发现了开源的项目：Yao Open Prompts。

![](assets/img_df0b4338c9aa.png)

一、项目介绍

Yao Open Prompts 是一个面向真实工作、学习、内容、营销和生活场景的中文 AI 提示词库。

作者：姚金刚老师。

目前共 116 个提示词文件，按场景分了 9 大类：

![](assets/img_8ec5b59a5cbe.png)

二、核心亮点

1、智能元提示词生成系统：

这个项目最大的亮点，不是简单的 116 个模板，而是这一套智能元提示词生成系统。

该系统基于经典的 RTF 框架（Role-Task-Format，角色-任务-格式），将提示词生产的全流程标准化：

需求分析 → 角色工程 → 任务架构 → 格式规范 → 质量评估。

![](assets/img_30786716f52d.png)

这套流程把原本依赖灵感和运气的提示词编写，变成了可复制、可批量的工程化流水线。

简单来说：

我们不仅能使用现成的 116 个提示词，还能用这套元系统快速生成更多符合自己业务场景的高质量提示词。

2、提示词文件规范：

每个提示词文件包含统一 frontmatter：

```
title: 提示词标题
```

PS：

正文只保留三部分：标题、简介、Prompt。

需要展示案例、评测截图、教程链接或长说明时：

优先放到 references/ 或后续的案例目录。

不和可复制提示词正文混在一起。

三、快速入门

项目地址：

https://github.com/yaojingang/yao-open-prompts。

直接阅读 README。

或者

将项目克隆到本地：

```
git clone https://github.com/yaojingang/yao-open-prompts.git
```

四、结语

Yao Open Prompts 真正价值在于：

它把零散的、过于简单的提示词经验，升级成了可管理、可扩展、可评估的工程结构。

无论是普通用户、内容创作者，还是 AI 产品经理或营销人员，都能从中获得两种能力：

1、直接解决当下问题的现成提示词。

2、持续生产新提示词的能力。

不妨现在就去看看，也许你一直想要的提示词就在里面。

项目地址：

https://github.com/yaojingang/yao-open-prompts。

**以上就是今天的分享，希望对各位伙伴有所帮助，如果觉得内容不错，希望你能点个赞，给予鼓励。**
