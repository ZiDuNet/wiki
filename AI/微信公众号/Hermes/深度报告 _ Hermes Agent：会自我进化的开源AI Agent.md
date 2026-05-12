> 📎 来源: [小朱的学堂](https://mp.weixin.qq.com/s?__biz=MzIxNTU2NjQzNQ==&mid=2247484267&idx=1&sn=49f54d631cc56edf5b069d744bf1610f&chksm=96fd0248faf6eba94232098123e1ed9f19a6a2d9815acef294c50b5dcf97f35ffea7bf974d30&mpshare=1&scene=1&srcid=0421wgSWDLyMtiX0fkZ3aqFf&sharer_shareinfo=3cc2e6bfb11be19849cf767f95369302&sharer_shareinfo_first=3cc2e6bfb11be19849cf767f95369302) | 时间: 2026-04-21 20:32

---

# Hermes Agent 横纵分析报告

> 研究时间：2026年4月18日 | 所属领域：AI Agent / 自主智能体 | 研究对象类型：开源产品

## 一句话定义

Hermes Agent 是由美国开源AI实验室 Nous Research 于 2026 年 2 月发布的开源自主 AI 智能体框架，核心定位为"会与你共同成长的智能代理"（An Agent That Grows With You），其最大创新在于内置唯一的学习闭环——能够从每次任务执行中自动创建和迭代技能，运行时间越长能力越强，采用 MIT 协议完全开源。

---

## 二、纵向分析：从诞生到当下

### 起源：开源AI运动中的一支异类

要理解 Hermes Agent，必须先理解它的缔造者 Nous Research。

Nous Research 成立于 2023 年，诞生于 Discord 社区中 AI 爱好者的一次草根协作——一群人不满意大厂闭源模型的"内容审查"和"使用限制"，决定自己动手训练完全开放、不设藩篱的语言模型。创始人团队规模约 20 人，核心成员包括 CEO Jeffrey Quesnelle、共同创始人 Karan Malhotra，以及在开源社区极具影响力的 Teknium——他是 OpenHermes 数据集的创建者，该数据集是开源LLM微调领域最流行的训练数据之一，在 HuggingFace 上的下载量以百万计。顾问名单里甚至出现了 Diederik Kingma，Adam 优化器的共同发明人。

这个配置在开源AI圈子里是罕见的豪华阵容。开源圈不缺理想主义者，但缺能把理想落地的工程能力。Nous Research 的不同之处在于：它不仅发表论文、开放权重，还真的把产品做到了可用级别。这为 Hermes Agent 的诞生埋下了技术积累的种子。

### Hermes 系列模型的铺垫

在 Hermes Agent 之前，Nous Research 的成名作是 Hermes 系列大型语言模型。这个系列在开源社区以"非拒绝率"著称——与 ChatGPT 的安全审查机制不同，Hermes 模型几乎不拒绝任何请求，非拒绝率达到 60%，而 ChatGPT 只有约 5%。这一设计哲学深刻影响了 Hermes Agent 的产品路线：不设限、做真正的工具，而非带护栏的消费产品。

2024 年，Nous Research 完成种子轮融资 2000 万美元。2025 年 4 月，获得 Paradigm 领投的 5000 万美元 A 轮融资，估值达到 10 亿美元，跻身独角兽行列。值得注意的是，Paradigm 是加密领域的顶级投资机构，这暗示了 Nous Research 的另一个野心方向：去中心化AI训练。团队正在 Solana 区块链上构建 Psyche 网络，试图用分布式计算解决模型训练的数据协调问题。这一背景解释了一个看似矛盾的现象：一家融资过亿美元的 AI 公司，为什么会把产品做成完全免费的开源项目——他们在赌的是生态，而非软件本身。

### Hermes 4：技术上的承前启后

2025 年 8 月 29 日，Nous Research 发布 Hermes 4 系列混合推理大模型，成为公司历史上最重要的技术里程碑。最大版本拥有 4050 亿参数，在 MATH-500 数学基准测试中获得 96.3% 的成绩，AIME'24 数学竞赛得分 81.9%，在数学能力上与 ChatGPT 持平甚至更优。

Hermes 4 的核心创新是混合推理模式——用户可以在"快速响应"和"逐步深入思考"之间自由切换。启用后，模型会在特殊标签内生成思考过程，再给出最终答案。这与 OpenAI o1 的推理模式类似，但 Hermes 4 的思考过程对用户完全透明。

在训练方法上，Hermes 4 引入了 DataForge（将简单预训练数据转换为复杂指令遵循实例的数据合成系统）和 Atropos（内置数百个专门训练环境的开源强化学习框架）。这套技术组合让 Hermes 4 实现了几乎无内容限制的响应能力。

2025 年 12 月，团队又发布了基于 Qwen 3 14B 架构的 Hermes 4 14B 版本，进一步扩大了模型的适用范围。

正是 Hermes 4 的技术积累，让 Hermes Agent 在 2026 年 2 月的发布具备了足够的技术底气。

### Hermes Agent 的诞生：从内部工具到开源爆款

2026 年 2 月底，Nous Research 悄悄在 GitHub 上开源了 Hermes Agent。最初它只是一个内部项目，官方没有大张旗鼓地宣传。但就是这样一颗"小石子"，激起了 AI Agent 赛道的巨大涟漪。

发布的头两周，项目默默积累关注。然后，GitHub Trending 效应开始发作——这个开源项目开始被社区自发地推荐、讨论、fork。开发者们发现，Hermes Agent 与当时最火的 OpenClaw（俗称"龙虾"）相比，有一个根本性的差异化卖点：内置学习闭环。大多数 AI Agent 是无状态的——每次对话都是独立的，关闭终端就失去所有记忆，下次重启如同与一个陌生人对话。Hermes Agent 彻底改变了这一点。

它的记忆系统分三层：工作记忆（当前会话）、情境记忆（近期会话的 FTS5 全文检索）和长期记忆（跨会话积累的技能和偏好）。配合自动技能创建机制，Agent 不仅记住你告诉了它什么，还能从这些记忆中提炼出可复用的"技能"（Skills），下次遇到类似任务自动调用。

2026 年 4 月 3 日，v0.7.0 发布，引入可插拔记忆提供者、Camofox 浏览器、Inline Diff 等功能。此后每周一个大版本：v0.8.0（后台任务自动通知、/model 动态切换、Gemini 原生支持）、v0.9.0（本地 Web Dashboard、微信/企业微信接入、iMessage、Termux/Android）、v0.10.0（Nous Tool Gateway，直连网页搜索、图像生成、TTS 与浏览器自动化）。从 4 月 3 日到 4 月 16 日，不到两周内连发 4 个版本，这种迭代速度在整个开源 Agent 领域极为罕见。

GitHub Star 从零到 40,000 用了不到两个月，到 80,000 只用了约两周，目前已达 88,000+，Fork 超过 5,200。同期 OpenClaw 用了一年时间才达到 300,000 Star 的体量。Hermes Agent 的增速，在开源 Agent 赛道里是前所未见的。

### 争议：抄袭风波

2026 年 4 月 15 日，中国 AI 团队 EvoMap 公开指控 Hermes Agent 系统性复刻其开源项目 Evolver，震动 AI 圈。

EvoMap 提出的核心证据令人无法忽视：Hermes Agent 的自进化引擎与 Evolver 的核心架构高度吻合——10 步主循环步骤一一对应，12 组术语被系统性替换（这是开源社区所说的"AI洗代码"操作：吃透原项目的逻辑架构，用不同变量名和术语重新表述，吐出所谓"原创"代码），7 份公开材料中对最相似的 Evolver 只字未提，却引用了 Stanford/Berkeley 的 GEPA/DSPy 等远得多的学术来源。

时间线是争议的核心：Evolver 于 2026 年 2 月 1 日公开核心概念，2 月 25 日正式开源；而 Hermes Agent 的自进化模块仓库创建于 3 月 9 日——晚于 Evolver 公开超过 36 天。Nous Research 联合创始人 Teknium 在社交平台回应称"从未听说过该项目"，并要求对方"删除账号"，但对核心指控（10 步循环、术语替换）始终未正面回应。随后 Nous Research 的官方账号删除了回应帖子、拉黑对方、全线沉默。

这一争议揭示了 AI 开源领域的一个深层矛盾：当架构级别的"借鉴"变得如此容易区分，传统开源协议的约束力正在受到前所未有的挑战。Evolver 团队最终将核心模块改为混淆发布，协议从 MIT 变更为 GPL-3.0，试图通过更严格的许可证阻止进一步复制。

### 阶段划分

回顾 Hermes Agent 的发展，可以划分为三个阶段：

**第一阶段：草根积累（2023-2024年）**。Nous Research 从 Discord 社区起步，靠 Hermes 系列模型在开源圈积累声誉。团队小而精，定位清晰——做"不受限制"的AI模型。这个阶段的核心矛盾是：如何在没有大厂资源的情况下，训练出足够好的模型？答案是合成数据（超过90%的训练数据为合成数据）和社区协作。

**第二阶段：资本加速（2025年）**。Paradigm 的 5000 万美元注入让 Nous Research 有了更充裕的弹药。团队开始两条腿走路：一边继续模型训练（Hermes 4 发布），一边布局去中心化训练网络（Psyche）。这个阶段的核心矛盾是：开源免费的模型如何创造商业回报？答案是生态锁定——先把开发者圈住，再通过基础设施服务变现。

**第三阶段：Agent 爆发（2026年至今）**。Hermes Agent 的爆火让 Nous Research 从"模型公司"转型为"平台公司"。核心矛盾变成了：快速增长的用户规模与不成熟的架构之间的张力——6 周内 4 个大版本，高速迭代带来了 Reddit 用户的集体吐槽："3个版本根本无法工作，版本太少无法验证稳定性"。与此同时，抄袭争议给这个故事蒙上了一层阴影。

---

## 三、横向分析：竞争图谱

### 赛道定位

Hermes Agent 处于"个人AI助手"赛道，这个赛道里同时有专注浏览器自动化的 Browser-Use、专注多渠道接入的 OpenClaw、专注代码开发的 Claude Code，以及通用型的 Manus、AutoGPT 等。从功能光谱上看，Hermes Agent 的独特位置在于：它是唯一一个将"自进化"作为核心卖点而非附加功能的开源 Agent。

### 竞品对比

**OpenClaw**（最强竞品）

OpenClaw 是这个赛道的领跑者，GitHub Star 突破 319,000，甚至超越了 React 成为 GitHub 最火开源项目。它的核心哲学是"接入一切"——支持 50+ 消息平台、13,000+ 社区技能、成熟的多 Agent 路由架构。在 OpenClaw 的生态里，你可以用 Telegram 发起任务、在 Discord 里继续、最后通过 Slack 接收结果——它是真正的"AI 操作系统"。

Hermes Agent 与 OpenClaw 的竞争，本质上是两种哲学路线的竞争：OpenClaw 是"控制"——用户定义规则、配置技能、编排流程；Hermes 是"进化"——让 Agent 自己从经验中学习。Reddit 社区的真实反馈印证了这种分化：需要多渠道集成的用户坚定地留在 OpenClaw，需要处理重复性任务的用户则快速转向 Hermes。

有趣的是，资深用户正在探索"OpenClaw + Hermes"的混合架构：OpenClaw 负责规划和分解复杂任务，Hermes 负责执行快速、可重复的任务循环。两者不是非此即彼的关系，而是互补的。

**Browser-Use**（浏览器自动化专家）

Browser-Use 是当前 GitHub 上最活跃的浏览器自动化开源项目，81,600+ Star，在 WebVoyager 基准测试中获得 89.1% 的准确率，优于 OpenAI 的 Operator（87%）和 Google 的 Project Mariner（83.5%）。它的技术路线是"浏览器优先"——通过 DOM 感知和视觉补偿，让 AI 模型精确地"看见"并操作网页元素。

Hermes Agent 内置了对 Browser-Use 的支持（通过 Browser Use 云模式），这意味着两者更多是合作关系而非竞争关系——Browser-Use 提供底层浏览器能力，Hermes 提供上层的记忆和学习能力。

**AutoGPT**（先驱老兵）

AutoGPT 是这个赛道的"鼻祖"，2023 年就以"自主执行多步骤任务"的概念引爆了 AI Agent 浪潮，GitHub Star 达 167,000+。但 AutoGPT 近年来显得有些疲惫——架构偏重、插件系统复杂、记忆机制原始。在 2025 年的 Agent 赛道洗牌中，AutoGPT 的市场份额正在被 OpenClaw 和 Hermes Agent 蚕食。

**Manus**（闭源对手）

Manus 是通用型 AI Agent 的代表，2025 年被 Meta 以 20 亿美元收购。它走的是闭源+订阅路线（$39/月起），定位是"不想折腾技术的普通用户"。与 Hermes Agent 的开源自托管路线形成鲜明对比：Manus 的优势是开箱即用，Hermes 的优势是完全掌控和数据隐私。

### 技术架构差异

从架构哲学看，各竞品的技术路线可以这样概括：

OpenClaw 是"多 Agent 网关"——通过路由层连接不同的渠道、技能和 Agent 实例，每个 Agent 可以有独立的人格和专长。Browser-Use 是"浏览器优先"——Playwright 驱动 + 视觉补偿，AI 模型是视觉地"看"网页而非解析 DOM。Skyvern 是"视觉驱动"——更进一步，把计算机视觉引入浏览器自动化，LLM+CV 双感知。Hermes Agent 是"自进化闭环"——任务执行→记忆提取→技能生成→持续优化，核心是让 Agent 自己改进自己。

### 用户口碑

Reddit r/openclaw 社区（103,000 成员）对两个产品的评价颇具参考价值：

OpenClaw 被最多提及的投诉是"每个新版本带来的 bug 比解决的问题还多"（305 赞），以及"内存不可靠，Agent 会遗忘指令"（多位用户反馈）。正面评价是"生态真的大，技能真的多"。

Hermes Agent 被最多点赞的吐槽是"它永远觉得自己干得漂亮——任务全搅乱了自己还以为超神了"（107 赞），以及"自我学习会覆盖我手动修改的技能配置"。正面评价是"安装比 OpenClaw 简单很多，默认配置更合理"。

两种投诉指向了同一个深层问题：Agent 的自我评估能力还非常原始——它既无法准确判断自己是否做对了，也无法处理"人类偏好"与"自我学习"之间的冲突。这是整个 Agent 赛道的技术瓶颈，Hermes Agent 并不例外。

### 市场份额与生态位

从 GitHub Star 的维度看，当前赛道格局是：OpenClaw 319K（绝对领先）、AutoGPT 167K（先发优势）、Browser-Use 81.6K（垂直专家）、Hermes Agent 88K（快速追赶）、Skyvern 17.6K（稳步增长）。Hermes Agent 用不到三个月的时间超越了 Browser-Use 的积累速度，但距离 OpenClaw 的体量还有相当距离。

---

## 四、横纵交汇洞察

### 历史如何塑造了当下的竞争位置

纵向回溯 Hermes Agent 的发展路径，有一个关键决策奠定了今天的一切：2023 年，Nous Research 选择了一条与主流开源社区相反的路线——不做"安全的"微调模型，而是做"无限制的"完全开放模型。Hermes 系列的非拒绝率达到 60%，这一数字在开源圈子里既是标签也是护城河：吸引来的是最认同"AI 应当无限制"的用户群体，这批用户恰好也是最愿意折腾自托管 AI Agent 的极客群体。

这解释了为什么 Hermes Agent 的种子用户增长如此迅猛：它不是从零开始教育市场，而是直接对接了一个已经存在、认同其价值观的社区。没有 Hermes 4 模型积累的技术信任，没有开源圈子里" Nous = 做不受限制 AI"的品牌认知，Hermes Agent 不可能在没有任何推广预算的情况下自然增长到 88K Star。

### 竞品的纵向对比

把主要竞品也放入时间线看，OpenClaw 和 Hermes Agent 实际上是"同源异流"——两者都在 2023-2024 年间萌芽，都受益于开源 AI 运动的大潮，但走向了完全不同的方向。OpenClaw 的创始团队 Peter Steinberger 是 iOS 开发的老兵，他做 OpenClaw 的出发点是"做一个能在任何平台上运行的个人 AI 助手"，核心矛盾是生态丰富度与稳定性的平衡。Hermes 的创始团队是 LLM 研究者，做 Hermes Agent 的出发点是"验证自进化 Agent 的可行性"，核心矛盾是学习能力与可靠性之间的张力。

这两个方向都没有错，但它们面对的是不同类型的用户。OpenClaw 的理想用户是"愿意花时间配置、追求功能丰富"的开发者；Hermes 的理想用户是"希望 Agent 越用越聪明、愿意交出部分控制权"的长期用户。

### 优势的历史根源

Hermes Agent 的每个核心优势，都能追溯到明确的决策节点：自进化能力来源于 Hermes 4 模型在强化学习训练（Atropos 框架）中的技术积累；多平台消息集成来源于 Nous Research 多年来维护多渠道接入基础设施的工程经验；极低运行成本（$5 VPS 可运行）来源于团队对去中心化推理的持续投入（DisTrO 技术大幅减少了分布式训练的数据传输量，这一技术也被应用于推理优化）。

### 劣势的历史根源

同样，每个劣势也能追溯到早期决策：自我学习覆盖用户偏好这个 bug，根源在于"让 Agent 自主决策"的哲学过于激进——团队在早期设计中没有给用户足够的"学习开关"控制权。版本稳定性差，根源在于 Paradigm 融资后的增长压力——团队在商业化压力下选择了"快速迭代抢占市场"的策略，这牺牲了质量。抄袭争议，根源在于"开源社区借鉴边界模糊"的行业痼疾——这不仅是 Hermes 的问题，而是整个开源 AI 领域面临的共同挑战。

### 未来推演

**最可能的剧本：生态互补**。Hermes Agent 与 OpenClaw 在未来 12 个月内形成事实上的"标准分工"——OpenClaw 负责多渠道接入和复杂编排，Hermes 负责单点执行和长期记忆优化。两者都活下来，但都不消灭对方。Nous Research 靠 Hermes Agent 的云端服务（Psyche 网络、Nous Portal）实现商业化，不靠软件本身赚钱。

**最危险的剧本：信任危机加深**。抄袭争议持续发酵，核心开发者社区开始分化——一部分人因为"架构复制"的指控转向其他项目，另一部分人因为认同 Nous Research 的品牌继续使用。Hermes Agent 的增长停滞，用户规模稳定在 OpenClaw 的 20-30%，成为一个"有争议的利基选择"。

**最乐观的剧本：重新定义赛道**。自进化能力在实践中被验证有效（不是因为自我宣称，而是因为真实用户的任务完成率显著提升），吸引更多开发者基于 Hermes 的架构构建应用。Nous Research 成功通过 Psyche 网络将分布式推理商业化，Hermes Agent 成为去中心化 AI 生态的流量入口。

---

## 五、信息来源

1. Hermes Agent 官方网站[1]
2. Hermes Agent GitHub 仓库[2]
3. Nous Research 官方网站[3]
4. Hermes Agent 中文社区[4]
5. Hermes Agent 版本发布历史[5]
6. 36氪 - Hermes Agent 抄袭争议报道[6]
7. 虎嗅网 - Hermes Agent 争议报道[7]
8. 搜狐 - Nous Research Hermes 4 模型发布报道[8]
9. 区块文摘 - Nous Research 融资分析[9]
10. Reddit r/openclaw 社区讨论[10]
11. AI Browser Agent Leaderboard[11]
12. Hermes Agent 完全指南 - Ofox[12]
13. Hermes Agent vs OpenClaw 深度对比[13]
14. Browser Use 官网[14]
15. OpenClaw GitHub[15]

---

*横纵分析法由数字生命卡兹克（Khazix）提出，融合了索绪尔的历时-共时分析、社会科学的纵向-横截面研究设计、商学院案例研究法与竞争战略分析的核心思想。*

### 引用链接

[1]Hermes Agent 官方网站: *https://hermes-agent.nousresearch.com/*

[2]Hermes Agent GitHub 仓库: *https://github.com/NousResearch/hermes-agent*

[3]Nous Research 官方网站: *https://nousresearch.com/*

[4]Hermes Agent 中文社区: *https://hermesagent.org.cn/*

[5]Hermes Agent 版本发布历史: *https://hermesagent.org.cn/releases*

[6]36氪 - Hermes Agent 抄袭争议报道: *https://www.36kr.com/p/3767967755371011*

[7]虎嗅网 - Hermes Agent 争议报道: *https://m.huxiu.com/article/4851163.html*

[8]搜狐 - Nous Research Hermes 4 模型发布报道: *https://www.sohu.com/a/929801069\_122396381*

[9]区块文摘 - Nous Research 融资分析: *https://blocksummary.com/nous-research-%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90*

[10]Reddit r/openclaw 社区讨论: *https://kilo.ai/articles/openclaw-vs-hermes-what-reddit-says*

[11]AI Browser Agent Leaderboard: *https://leaderboard.steel.dev/*

[12]Hermes Agent 完全指南 - Ofox: *https://ofox.ai/zh/blog/hermes-agent-self-improving-ai-complete-guide-2026/*

[13]Hermes Agent vs OpenClaw 深度对比: *https://blog.moewah.com/posts/hermes-agent-vs-openclaw-comparison/*

[14]Browser Use 官网: *https://browser-use.com/*

[15]OpenClaw GitHub: *https://github.com/openclaw/openclaw*
