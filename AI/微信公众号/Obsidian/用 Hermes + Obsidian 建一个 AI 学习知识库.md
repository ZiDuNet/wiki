> 📎 来源: [亲爱的缪斯](https://mp.weixin.qq.com/s?__biz=Mzk4ODIzNzc4OQ==&mid=2247484731&idx=1&sn=cf7dfd9ec049ac29d481c343b17d025d&chksm=c40ed7f82150186aebfb2c1e8b6b051c1c1a0e5d214c3e7676daea410350d4fc3ceb13420745&mpshare=1&scene=1&srcid=0430dtz2tLgoQxce3LFwahpi&sharer_shareinfo=d2b5a0b6e717d3bac3cd99c9c946be2f&sharer_shareinfo_first=d2b5a0b6e717d3bac3cd99c9c946be2f) | 时间: 2026-04-30 19:40

---

今天教大家如何在自己的本地电脑构建一个 Karpathy LLM Wiki。

先来了解一下什么是 LLM Wiki。

平时我们用 ChatGPT 或者 NotebookLM 查资料，每次问问题它都要重新从文档里找，找完回答，下次再问还是从头来，什么都没积累下来。

LLM Wiki 反过来：你把资料丢进去，LLM 先把它消化成结构化的页面，概念和概念之间互相链接，之后你问任何问题，它在这张已经整理好的网上找答案，不用每次重新发现。

Hermes Agent 把这个做成了内置 Skill，配合 Obsidian 用体验很好。下面说怎么搭。

**第一步：初始化知识库**

打开 Hermes，说：

> 帮我初始化一个 AI 学习的 LLM Wiki

它会在 

```
~/wiki
```

下建好这个目录：

```
~/wiki/├── SCHEMA.md        ← 知识库的规则文件，Hermes 根据你的主题自动生成├── index.md         ← 所有页面的目录├── log.md           ← 操作日志├── raw/             ← 原始资料放这里，只读不改│   ├── articles/│   ├── papers/│   └── assets/├── entities/        ← 模型、机构、人物的页面├── concepts/        ← 技术概念的页面├── comparisons/     ← 对比分析└── queries/         ← 有价值的查询结果
```

**第二步：用 Obsidian 打开同一个文件夹**

Obsidian → Open folder as vault → 选 

```
~/wiki
```

三个设置：

- 附件目录改成 

  ```
  raw/assets
  ```
- Wikilinks 确认是开的（默认就开着）
- 装一个 Dataview 插件（社区插件里搜索安装）

Wiki 路径默认是 

```
~/wiki
```

，不用配置直接能用。想换路径的话，在 

```
~/.hermes/.env
```

加一行：

```
WIKI_PATH=/你想要的路径
```

Obsidian 的 vault 指向同一个文件夹就行，两边共享同一堆 Markdown 文件，没有同步问题。

**第三步：开始喂资料**

看到文章或论文，直接扔给 Hermes：

> 帮我 ingest 这篇：https://arxiv.org/abs/xxxx

它会自动读完、提取关键信息、建页面、把相关概念用 

```
[[wikilinks]]
```

连起来，最后告诉你新建或更新了哪些文件。去 Obsidian 刷新就能看到变化。

## 日常三个操作

**查东西**

> 我库里关于 RAG 有什么？帮我整理一下

Hermes 在你已经整理好的知识里找答案，不是重新搜网。库里喂的东西越多，回答越有深度。

**整理 Wiki**

> 帮我 lint 一下 Wiki

Hermes 会找出孤立页面、断掉的链接、互相矛盾的地方，列个报告给你。

**在 Obsidian 里浏览**

打开 Graph View，能看到所有概念之间的连线。喂的东西越多，图越密，整个知识网络越清晰。

也可以用 Dataview 查询，比如列出所有跟训练相关的概念页面：

```
TABLE created, tags FROM "concepts"WHERE contains(tags, "training")SORT created DESC
```

---

✨ 有任何问题欢迎随时联系缪斯

![](assets/img_32f30138a11e.png)
