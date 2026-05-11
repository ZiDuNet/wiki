---
tags: [Obsidian, Agent, Claude, GitHub, API, Python, Skill]
source: "CostaLong"
created: 2026-04-21
updated: 2026-05-10
category: Obsidian
---

# macOS (Homebrew)brew install hermes-agent# 或通过 npm 安装npm install -g hermes-agent# 验证安装hermes --version

> 来源: [CostaLong](https://mp.weixin.qq.com/s?__biz=MzA5NzgzNjE1Ng==&mid=2247485768&idx=1&sn=90d4c08b0aec92f848bb957b2f0e6d25&chksm=9136d9fa1b5ee2c4b8aabb576246e4e0d549b12349dfef112157fd39d73c1908615e9b35bda9&mpshare=1&scene=1&srcid=0421IzNOFFngucumYPrI5OIr&sharer_shareinfo=b3b007d806f3f7833ae748dc882c9863&sharer_shareinfo_first=b3b007d806f3f7833ae748dc882c9863) | 2026-04-21

## 摘要

封面图
**📄 核心要点**
- Hermes：统一的 CLI 输入层，支持多源内容快速录入
- AutoCLI：规则引擎驱动，自动完成分类、标签、入库操作
- Obsidian：结构化知识库，双向链接构建知识网络
- 三者联动：内容进 → 自动处理 → 知识库沉淀 → 微信汇报推送
技术文章、命令行输出、项目笔记散落各处，找起来费时费力。整理好后还得手动复制到微信、笔记软件——这套系统的目标就是：**内容进来，自动处理好，人只需要做决策**。
Hermes+AutoCLI+Obsidian 系统架构图
我自己在搭建这套系统的时候，最花时间的就是弄清楚这三层之间的边界——不是说它们有多复杂，而是要确保每一层只做一件事。
验证三层联通是否正常，用一行命令就够了——执行输入命令，然后检查知识库目录是否有新文件出现。
如果需要扩展第四层（微信推送），在自动化引擎中添加新规则并重启服务即可，不需要修改现有任何配置。
Hermes 是整个系统的入口，负责统一处理各类内容输入。
我一开始没用 Hermes，试过直接写 shell 脚本做同样的事——大概 80 行代码，抓取、解析、写入全塞在一个脚本...

## 相关实体

[[Anthropic]], [[B站]], [[Claude]], [[Docker]], [[GitHub]], [[Hermes]], [[Notion]], [[Obsidian]], [[Python]], [[微信]]

## 相关概念


