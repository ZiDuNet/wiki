> 📎 来源: [EthanJoker](https://mp.weixin.qq.com/s?__biz=MzcwOTMwNjgxNA==&mid=2247483652&idx=1&sn=9ed174c0f51ad771cc3b313112659061&chksm=f46212b372372a2e1a126194f4d70f937332e055d1b88de463e58b0d982ef362bc11f2ac2ef9&mpshare=1&scene=1&srcid=0524d6ca5BDe1JZ2oLk7HtEG&sharer_shareinfo=20d2fbda886d17d349719914e1cf9971&sharer_shareinfo_first=20d2fbda886d17d349719914e1cf9971) | 时间: 2026-05-24 02:44

---

如果你也有这种经历，这篇文章就是写给你的：

- 收藏了很多资料，但用的时候找不到

- 同一个问题每周都在“重新搜、重新问、重新总结”

- AI 回答看着像对的，但你很难追溯“它到底依据了什么”

`llm-wiki` 这个项目，解决的就是这类“知识工程”问题。

不是做一次性问答，而是把知识做成可持续迭代的系统。

项目地址：https://github.com/Ethanjoker3615/llm-wiki-learn-from-karpathy

---

1. 先说结论：它不是临时 RAG，而是持续编译知识

一句话定义：

llm-wiki = 把原始资料持续 ingest 进 wiki，让后续 query 可复用、可追溯、可检查。

它和“每次临时扔文档给模型问一遍”的区别在于：

- 你不是每次从零开始

- 你有版本化和来源校验

- 你可以做健康检查和闭环修复

 2. 三层架构（读懂了就能上手）

 2.1 `raw/`：原始事实层

这层像“档案室”。

原始文章、对话、草稿先放这里，尽量不改动。

目标：保留事实源，不让“二次加工内容”覆盖原始信息。

 2.2 `wiki/`：结构化知识层

这层像“可维护知识图谱”。

包括 `sources`、`concepts`、`entities`、`outputs` 等。

目标：让 AI 产出的知识可链接、可复查、可复用。

 2.3 `schema/`：规则约束层

这层像“工程规范”。

约束命名、frontmatter、字段完整性、流程边界。

目标：降低野生内容污染，保证团队协作一致性。

---

 3. 三段工作流：ingest -> query -> lint

这是 llm-wiki 的日常主循环。

 3.1 ingest：把资料“入库成可用知识”

做的事包括：

- 把 raw 文档转成 source-summary

- 写清元数据：`raw\_file`、`raw\_sha256`、`last\_verified`

- 更新索引和日志

结果：资料不再只是“存着”，而是“可检索、可引用”。

 3.2 query：从知识库回答问题并沉淀产物

做的事包括：

- 基于现有 wiki 页面回答问题

- 把高价值回答回写到 `wiki/outputs/`

结果：问答不是一次性聊天，而是知识持续积累。

 3.3 lint：健康检查与问题暴露

做的事包括：

- 查断链、冲突结论、孤立页面

- 标记过期信息和缺失字段

结果：系统能定期发现“知识债务”。

---

 4. 结合 Harness Engineering：让系统“少犯重复错误”

很多人把知识库做成“内容堆积”。

Harness Engineering 给出的启发是：

把错误模式固化为规则，让系统自动防错。

在 llm-wiki 里对应三件事：

1. 前置约束：写入时就校验 frontmatter 和字段

2. 过程管控：query 输出后要求回写与交叉链接

3. 后置修复：lint 发现问题后更新规则，避免再犯

这套机制的核心，不是“内容更多”，而是“质量越来越稳”。

---

 5. 一个真实小场景（初学者可直接照做）

假设你要整理“ROS2 Pro 项目材料”，目标是：

- 本周内把 2 篇文章 + 1 份对话纳入知识库

- 生成 1 篇对外介绍 output

- 保证来源可追溯

你的步骤可以是：

1. 原文放 `raw/articles/...`

2. ingest 生成 `wiki/sources/...`

3. query 产出 `wiki/outputs/2026-xx-xx-ros2-pro-xxx.md`

4. 跑 lint，修复断链/缺字段

做完后，你不仅“写了一篇文”，而是“搭了可重复流程”。

---

 6. 为什么这套方式对求职有用

因为它对应的是企业里更在意的能力：

- 不是你会不会问 AI，而是你会不会管 AI 产出

- 不是你能不能写一篇总结，而是你能不能维护长期知识资产

- 不是你会不会工具，而是你有没有工程闭环意识

换句话说：

你展示的是“知识系统建设能力”，不是“聊天技巧”。

---

 7. 给新手的最小目录模板

```text

llm-wiki/

  raw/

    articles/

    notes/

  wiki/

    sources/

    outputs/

    index.md

    log.md

  schema/

  scripts/

    lint.py

```

有了这个骨架，就能先把“可维护”跑起来。

---

 8. 常见误区与修正

 误区 1：只存内容，不存来源

修正：每篇 source 强制写 `raw\_file + raw\_sha256 + last\_verified`。

 误区 2：只做 query，不做回写

修正：高价值答案必须回写 outputs，避免下次重复劳动。

 误区 3：只增量，不体检

修正：定期 lint，把断链和冲突当“待修 bug”处理。

---

 9. 一周落地路线（可执行）

 Day 1：搭骨架

- 建 `raw/wiki/schema/scripts` 目录

- 写最小 `index.md` 和 `log.md`

 Day 2-3：跑 ingest

- 选 3 篇高价值原文入库

- 统一补齐 source 元字段

 Day 4-5：跑 query + 回写

- 选 2 个真实问题

- 输出 2 篇 output 页面

 Day 6：跑 lint 并修复

- 修断链、补缺字段、统一命名

 Day 7：写 README Quick Start

- 用“新同学 10 分钟上手”标准写使用说明

---

10. 结语

把 AI 用成“搜索引擎替代品”很容易，

把 AI 用成“可维护知识系统”才有长期壁垒。

llm-wiki 的价值，不在于它回答了一次问题，

而在于它让你下一次、下下次，都不用再从零开始。

这就是知识工程的复利。
