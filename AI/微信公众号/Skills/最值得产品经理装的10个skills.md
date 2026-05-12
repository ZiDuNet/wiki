> 📎 来源: [橘宝AI](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247484303&idx=1&sn=fc352fe4728bc415dc843b41e0933570&chksm=974ffaa77db8cb4722b9bcfbfe3ff4ec8170eb59065cd1cc6dfd13ac5dcd88ce895e5a4a4072&mpshare=1&scene=1&srcid=0420NYYyefNJs8roCRizeOsx&sharer_shareinfo=d9c040ae71100b2fe410d01961509921&sharer_shareinfo_first=d9c040ae71100b2fe410d01961509921) | 时间: 2026-04-20 15:46

---

很多产品经理开始用Claude的时候，第一反应都是：写 PRD、改文案、帮我整理会议纪要。

用久了就会觉得，好像也就这样。

但真正把 Claude 用深的 PM，已经开始**把产品经理日常工作里那些高频、重复、耗脑力的环节，一个一个接进来，** 让Claude成为自己的全能助手。

同样的Agent使用效果的差距取决于有没有把对的能力装进来。

我不想泛泛地给大家说"Claude 可以帮 PM 做很多事"，而是想结合产品经理实际工作场景回答一个问题：

**如果你是产品经理，最值得优先装的 Skills 到底是哪些？**

我的筛选标准有三个：

- 是不是产品经理真实工作里会高频碰到的事
- 装进来之后有没有明显提升，而不只是"也能用"
- 不和别的 skill 大量重叠

按这个标准，我把推荐的 10 个sills分成了三个方向：产品设计、需求管理、产品创作与研究。文档类格式处理的 skill（Word、PDF、PPT）网上已经有很多介绍，这里只保留 pptx 一个，其他重点放在真正属于 PM 工作核心的部分。

---

## Part.01 frontend-design：你不需要会写代码，但你需要会验证想法

很多 PM 在跟设计师和研发沟通的时候，会遇到一个尴尬处境：

脑子里有想法，说出来对方理解不了；画出来的原型太粗糙，说明不了问题；等高保真设计稿出来，方向又跑偏了。

frontend-design 解决的，就是这个中间地带。

它能帮你快速产出一个**真实可点击的 HTML 原型**，是可以在浏览器里打开、能展示交互逻辑的页面。用来在评审会上走一遍流程，用来和研发对齐交互细节，用来跟设计师说"我要的大概是这个感觉"。

不需要会写代码，只需要描述清楚你想要什么，frontend-design 会帮你把它做出来。

页面： https://skills.sh/anthropics/skills/frontend-design

安装命令：

```
npx skills add anthropics/skills@frontend-design -g -y
```

---

## Part.02 ui-ux-pro-max：把竞品 UI 分析从"截图收藏"变成真正的洞察

大多数产品经理做竞品分析，做到最后就是一堆截图加几行描述，真正有用的判断很少。

不是因为没有认真看，而是**从"看到"到"理解设计决策"之间，有一道很难靠自己翻越的墙。**

ui-ux-pro-max 解决的正是这个问题。把竞品的截图上传给 Claude，配上这个 skill，它会帮你：

- 拆解界面背后的设计逻辑是什么
- 信息层级是怎么组织的，优先级是怎么判断的
- 交互模式背后可能的产品思路是什么
- 和你自己的产品相比，差距在哪里，机会在哪里

**它不只是帮你描述截图，而是帮你读懂截图背后的产品决策。**

这个 skill 在 skills.sh 排行榜上一直稳定在前 100，做竞品分析的产品经理装完感受会很直接。

页面： https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max

安装命令：

```
npx skills add nextlevelbuilder/ui-ux-pro-max-skill@ui-ux-pro-max -g -y
```

---

## Part.03 brainstorming：在需求确定之前，先把想法跑一遍

产品经理有一类工作经常被低估：**在"开始写需求"之前，把想法真正想清楚。**

你有一个模糊的方向，不确定从哪个角度切入；你要开一个需求启动会，但不知道应该先讨论什么；你对一个功能有想法，但不知道有没有更好的做法。

这时候 brainstorming 的价值就来了。

它不是让 Claude 帮你"生成一堆想法然后你来挑"，而是让它真正参与你的思考过程：提出反驳、指出盲点、从不同角色视角拆解问题、帮你找到你没想到的切入点。

**它解决的不是"没有想法"的问题，而是"想法还没想透"的问题。**

对于经常要主导产品讨论、做决策的 PM 来说，一个会真正参与思考的 brainstorming 伙伴，价值比很多工具都大。

页面： https://skills.sh/obra/superpowers/brainstorming

安装命令：

```
npx skills add obra/superpowers@brainstorming -g -y
```

---

## Part.04 prd：让 PRD 不再是从空白文档开始的噩梦

这是一个在 skills.sh 排行榜上低调但非常实用的 skill。

写 PRD 是每个产品经理都绕不过去的工作，但大多数人的起点都一样：对着空白文档发呆，不知道从哪里开始，写出来的结构每次都不一样，和团队沟通的时候发现理解又跑偏了。

prd 这个 skill 做的，是把 PRD 写作的最佳实践内化进 Claude 的工作方式：

- 按标准结构组织内容（背景、目标、用户、功能、非功能需求、验收标准）
- 每个部分应该写什么、不应该写什么，有清晰的约束
- 可以从一句话描述开始，逐步展开成完整文档
- 输出的格式研发和测试能直接看懂

它不会帮你"想清楚要做什么"，但**一旦你想清楚了，它能让你快速、规范地把它写出来。**

页面： https://skills.sh/github/awesome-copilot/prd

安装命令：

```
npx skills add github/awesome-copilot@prd -g -y
```

---

## Part.05 用户故事生成器（deanpeters/Product-Manager-Skills）：把需求描述变成可以直接进迭代的 Story

这是一个"装了就会每天用"的 skill 集合。

产品经理写需求文档，最耗时间的不是想清楚要做什么，而是**把想清楚的东西翻译成研发和测试能准确理解的格式**。

用户故事怎么拆？验收标准怎么写？边界条件有没有遗漏？粒度是不是合适？

deanpeters 的 Product-Manager-Skills 里有专门针对用户故事写作的 skill，配合优先级分析使用，可以帮你：

- 按 As a / I want / So that 的格式生成标准用户故事
- 给每条 Story 写对应的 Acceptance Criteria（支持 Gherkin 格式）
- 识别明显的边界场景和异常情况
- 按 INVEST 原则检查拆分粒度是否合适

如果你用 Jira 或 Linear，还可以让它直接输出对应格式，复制进去就能用。

**它解决的不是"写不出来"的问题，而是"把脑子里的想法准确翻译成协作语言"的问题。**

页面： https://github.com/deanpeters/Product-Manager-Skills

安装命令：

```
npx skills add deanpeters/Product-Manager-Skills --skill user-story -g -y
```

---

## Part.06 需求优先级分析（deanpeters/Product-Manager-Skills）：让"拍脑袋排优先级"变成有框架的判断

每个产品经理都知道需求要排优先级，但大多数人的排法其实是：凭感觉，加上谁嗓门大谁排前面。

因为如果真的要**把 MoSCoW、RICE、Kano 这些理论框架真正用起来太麻烦了**——要收集数据、要填表格、要算分、要解释结论，一套下来挺费时间的。

同样来自 deanpeters 的 prioritization-advisor skill 把这件事的成本压低了。

你把需求池发给它，告诉它背景、目标用户、资源约束，它会先问你 3-5 个关键问题，再：

- 根据你的产品阶段推荐最合适的框架（RICE / ICE / Kano / MoSCoW）
- 用选定框架对每条需求打分或分类
- 给出一个综合判断和排序理由

更有价值的是，它会**把排序背后的逻辑解释清楚**。这样你在评审会上就不只是说"这个排在前面"，而是能说清楚为什么。

页面： https://github.com/deanpeters/Product-Manager-Skills

安装命令：

```
npx skills add deanpeters/Product-Manager-Skills --skill prioritization-advisor -g -y
```

---

## Part.07 copywriting：UX 文案不是最后一步，是产品体验的一部分

UX 文案是一个很容易被忽视、但一旦做差就会明显拉低产品体验的环节。

空状态怎么写才不冷漠？错误提示怎么写才不让人沮丧？Onboarding 引导文案怎么写才能把用户留下来？按钮文字怎么写才能让人知道点了会发生什么？

这些问题，很多 PM 的处理方式是：先写一个凑合的，等以后再优化。结果"以后"就从来没来。

copywriting 这个 skill 不只是"帮你写文案"，它内置了一套说服力框架和用户心理模型：

- 给同一个场景生成多个不同语气的版本（正式、亲切、简洁、直接）
- 检查文案里是否有过于技术性、用户看不懂的表达
- 确保整个产品的文案语气和品牌调性一致
- 快速响应迭代——改了功能逻辑，文案跟着同步更新

**它让"文案"这件事不再是靠等、靠催、靠运气，而是随时能做、随时能改。**

页面： https://skills.sh/coreyhaines31/marketingskills/copywriting

安装命令：

```
npx skills add coreyhaines31/marketingskills@copywriting -g -y
```

---

## Part.08 xlsx — 需求池与数据管理：别再用表格手工维护需求了

产品经理最累的维护工作之一，就是需求池。

每周加新需求、更新状态、调整优先级、补充工作量评估、筛选本迭代要做的——这些事做起来不难，但每次都要花大量时间。

Claude 配合 xlsx skill，可以帮你：

- 根据你描述的需求自动生成结构化的需求条目
- 按你的字段规范（状态、优先级、迭代、负责人）填充表格
- 对现有需求池做批量更新和整理
- 生成本迭代的交付清单或排期表

如果你的需求池已经积累了大量数据，还可以让 Claude 帮你做分析——**哪个模块的需求最多、哪些需求长期没有推进、历史需求完成率是多少。**

不是把 Excel 换成别的工具，而是让你手里的表格真正开始产生价值。

页面： https://skills.sh/anthropics/skills/xlsx

安装命令：

```
npx skills add anthropics/skills@xlsx -g -y
```

---

## Part.09 summarize：信息这么多，先学会压缩

产品经理每天要消化的信息量太大了：

竞品的更新日志、行业分析报告、用研访谈录音转文字、技术方案文档、上下游团队的沟通记录……很多时候你并不是不想读，而是真的没时间读完。

summarize 做的事很直接：**帮你把一大段信息压缩成你真正需要的部分。**

不是简单地截取前几段，而是理解内容之后，按你关心的角度提炼——关键结论是什么、有哪些需要注意的风险、对你的产品决策有什么参考价值。

对产品经理来说，这个 skill 的价值是：**让你在信息过载的环境里，保持判断的质量。**

它最适合处理的内容：长网页、竞品文档、播客/会议录音转录、多篇资料汇总、用研访谈记录。

页面： https://skills.sh/steipete/clawdis/summarize

安装命令：

```
npx skills add steipete/clawdis@summarize -g -y
```

---

## Part.10 skill-creator：把你自己的工作方式沉淀下来

最后这一个，是所有重度用户最终都会走到的地方。

前面九个都是"用别人沉淀好的能力"，而 skill-creator 是"把你自己的工作方式沉淀成能力"。

每个产品经理都有自己习惯的一套做法：PRD 有自己偏好的结构、需求评审有固定的检查框架、竞品分析有自己的维度模板、版本复盘有自己的问题清单。

这些东西放在脑子里，每次都要重新调用；如果能固化成 skill，Claude 每次帮你做这类工作的时候，就不需要你再反复解释"我要的格式是这样的"。

**你积累得越多，它对你的工作理解就越深，产出就越稳定。**

这不只是一个效率工具，而是把你的经验真正变成资产的开始。

页面： https://skills.sh/anthropics/skills/skill-creator

安装命令：

```
npx skills add anthropics/skills@skill-creator -g -y
```

---

## 最后：别先追求"装很多"，先追求"装进去之后真的在用"

skill 不是收藏夹，不是装了就算数的。

真正有价值的 skill，是你装进去之后，会在很多不同的任务里反复调用。如果装完之后两周都没有再打开，那它对你来说就没有价值——不管有多少人推荐。

所以按优先级，我建议这样来：

**第一梯队，先装这三个：**

**prd + 用户故事（deanpeters） + summarize**

这三个覆盖了产品经理日常工作里最高频的脑力消耗：写需求、拆 Story、消化信息。装完之后，你会立刻感受到变化。

**第二梯队，根据你的岗位特点补充：**

偏前期调研和设计的，加 **brainstorming + ui-ux-pro-max + frontend-design**；

偏产品执行和交付的，加 **需求优先级分析 + copywriting + xlsx**；

想把 Claude 用深、用长期的，加 **skill-creator**。

---

产品经理的工作，核心是判断和沟通。Claude 解决不了判断本身，但它可以**大幅降低判断前的信息处理成本，和判断后的表达传递成本。**

这就是 skills 的价值所在。

如果觉得这篇内容有帮助，欢迎点赞、在看、转发支持。也欢迎在评论区告诉我：你在用 Claude 做产品工作的时候，觉得最有价值的场景是什么？

往期推荐

- [小白如何用AI做产品并发布上线](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247484184&idx=1&sn=509d54f949c8a895e12ba295ed446426&scene=21#wechat_redirect)
- [3个免费使用Nano Banana Pro的平台，赶紧去薅](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247484004&idx=1&sn=80b406da8c34eae390cacdcfa7c01449&scene=21#wechat_redirect)
- [拜拜了Get笔记、ima知识库，用了NotebookLM才知道AI知识管理工具有多香](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247483903&idx=1&sn=7a005fce31fef6e65a114dc5b06adf46&scene=21#wechat_redirect)
- [Lovart地表最好用的AI出图工具](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247483860&idx=1&sn=665ac7862d7ec393aca810112b82d86d&scene=21#wechat_redirect)
- [如何让AI听懂你的需求，做出你想要的产品](https://mp.weixin.qq.com/s?__biz=MzE5ODkwNjExNQ==&mid=2247484166&idx=1&sn=7510f0fb9bbd7e01303b545b1f64a9e0&scene=21#wechat_redirect)
