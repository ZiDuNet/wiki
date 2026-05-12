> 📎 来源: [小虾的 AI 笔记](https://mp.weixin.qq.com/s?__biz=MzcwOTIxOTY4Mw==&mid=2247484030&idx=1&sn=154f3f63e796226215528f8c83bb62bf&chksm=f4a2387e0dc2b751fd10250f4d40e7682b39f34df18acb8979284f1dd097918b02cb4bd42c86&mpshare=1&scene=1&srcid=0513MMTozUivmrAzeyC5nTQa&sharer_shareinfo=72f9794dfb9af75bae0cfd20635cc853&sharer_shareinfo_first=72f9794dfb9af75bae0cfd20635cc853) | 时间: 2026-05-13 01:57

---

**核心观点：**Skill 是高度私人化、定制化的东西。拿来主义找来的 skill，放到自己的场景里十有八九水土不服。自己做自己需要的 skill，才是最好的。

用过他山之石的开发者都会有这个感受：GitHub 上 Star 10k 的自动化模板，拿过来跑不通；ClawHub 评分最高的 skill，用了两天就扔了。

问题不在于这些 skill 不好，而在于**你的上下文和开发者的上下文不一样**：

• 你的视频在 B 站，开发者的数据源是 YouTube RSS

• 你的笔记要存飞书，开发者的输出是本地 Markdown

• 你的 cron 跑在 macOS，开发者的环境是 Linux server

Agent skill 不是 App Store 里一键安装的应用——它是**为你的工作流量身定制的工具**。最了解你的场景的人，只有你自己。

所以更好的方式是：自己动手，用三步链路，把你的需求变成 skill。

三步链路：做 skill 的流水线

我把“做 skill”这件事拆成了三个标准步骤，每一步对应一个专业 skill，三者串联起来，就是从想法到可运行 skill 的完整流水线。

第一步：workflow-analyzer（场景分析）

**职责：**判断一个想法值不值得做 skill，以及怎么做。

1. 可行性判断 —— 技术上能不能实现？Agent 能做到什么边界？

2. Skill 化评估 —— 场景频率高不高？做完能省多少时间？值不值得投入？

> workflow-analyzer 会把一个模糊需求拆成具体步骤，逐一判断哪些能自动化、哪些有坑、哪些根本做不了，最后给出一个结论 + SKILL.md 草案。

Skill仓库：

https://clawhub.ai/skills/openclaw-workflow-analyzer

第二步：l4-skill-forge（Skill 设计）

**职责：**基于草案，把 skill 做成一个完整的、可交付的、生产级质量的包。

这是三步链路中专业门槛最高的一步。它不只是写个能跑的脚本，而是要求 skill 真正具备可维护性、可验证性、可演进性。

• 定义产物边界：SKILL.md、references、templates、evals 要齐

• 安全门控：高风险操作必须有显式确认点

• 失败处理路径：网络失败、空数据、权限不足都要考虑

• 评估用例：交付时就告诉使用者“怎样才算跑通”

Skill仓库：

https://clawhub.ai/skills/l4-skill-forge

第三步：superpowers（代码实现）

**职责：**TDD 驱动，把 skill 的代码写出来。

• 简单 skill 可以跳过它，l4-skill-forge 直接产出可运行代码

• 复杂 skill 则需要它来写多模块并行、TDD 测试

Skill仓库：

https://clawhub.ai/skills/superpowers

三步如何串联

> 你的需求
> ↓
> [第一步] workflow-analyzer → 判断能不能做 + 输出草案
> ↓
> [第二步] l4-skill-forge → 基于草案构建完整 skill 包
> ↓（按需）
> [第三步] superpowers → TDD 写代码
> ↓
> 可运行的 skill

三步链路的关键约束：**不给多选项，让用户决定下一步。** 不想做了就停，想继续就往下走。

实战案例：B站视频笔记 skill

这次用三步链路做了一个 B站视频笔记 skill：**video-note-maker**。

看学习类 B站视频，想把内容整理成结构化笔记。以前做法：边看边截图，手动敲重点，一期视频整理下来半小时没了。

目标：输入一个 B站视频链接，输出结构化笔记（概览 + 关键观点 + 金句 + 行动建议）

• 第一步判断这件事值得做：频率高、耗时高、自动化收益大

• 第二步设计完整 skill 包：字幕获取 → Whisper ASR → AI 分析 → Markdown 生成

• 第三步把 Whisper、下载、分析模块逐个写出来

![](assets/img_0c89e928a281.jpg)

![](assets/img_3eee9688b56d.jpg)

总结

Skill 是生产资料，不是通用商品。别人的 skill 再好，放到你的上下文里总是差那么一点。

• workflow-analyzer 帮你判断值不值得做

• l4-skill-forge 帮你把想法变成可交付的 skill 包

• superpowers 帮你把代码真正写出来

三个 skill 各司其职，串联起来就是一条 skill 生产流水线。

下一步你有什么想自动化的？试试用三步链路把它做成 skill。

本篇使用工具：OpenClaw + Hermes Agent + 三步链路 skill 流水线
