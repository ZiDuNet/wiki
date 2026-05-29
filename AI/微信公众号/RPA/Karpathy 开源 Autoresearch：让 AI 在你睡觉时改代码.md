> 📎 来源: [硅基苔藓](https://mp.weixin.qq.com/s?__biz=MzIxMDYwODQ4Nw==&mid=2247484198&idx=1&sn=2b95592f176df04b4fd99062bdece32b&chksm=96d040b02a26b238cc276c7556b04d46d7179e72a04bb3570210a76c3939933a409775b3816b&mpshare=1&scene=1&srcid=0528bpT7pao3879N5VevX5zf&sharer_shareinfo=828e222c0fb26946560027d0beb175ac&sharer_shareinfo_first=828e222c0fb26946560027d0beb175ac) | 时间: 2026-05-28 20:36

---

我梦见自己变成了一个科研外包商。客户说："帮我试试能不能把项目的响应降一点，不用太复杂，你随便折腾。" 我想了想，回了一句："行，我把代码交给 AI，你明天早上来看结果。"

这已经不是梦， 2026年3月 Karpathy 真的把这件事做成了一个开源项目，而且一夜之间就飙到了 77,000 星。

项目名叫 autoresearch，直译就是"自动驾驶科研"。它的核心想法极其简单：你写一份 Markdown 文件告诉 AI "往哪个方向探索"，然后 AI 自己改代码、自己跑实验、自己判断结果好不好。你睡一觉，醒来看到的不是一成不变的代码，而是一百多次实验的结果和一段自动优化的模型。

Karpathy 在 README 里写了一段很妙的开场白："有一天，前沿 AI 研究是由肉电脑在吃饭、睡觉、开会的间隙做的。那个时代已经过去了。科研现在是自主 AI 集群的天职。"他说现在已经是第 10,205 代代码了——当然这可能是开玩笑，但这个笑话本身就很能说明问题：当 AI 开始迭代自己的代码时，人类的阅读能力很快就会跟不上。

一、科研的瓶颈：人太慢，GPU 太贵

先说一个真实的场景。你在实验室有一张 H100，每次跑一个训练实验需要 5 分钟。你一天能工作 8 小时，扣掉写代码、看论文、回邮件的时间，你大概能跑 50 个实验。但问题是，这些实验之间不是并行的——你得等一个跑完，看了结果，再决定下一个怎么改。

更致命的是，人在深夜和周末的效率几乎为零。但 GPU 不在乎你睡不睡觉。一张 H100 每小时租金约 8-12 美元，如果它在你睡觉的时候空转，这相当于你每周浪费了 600-800 美元。

传统的 HPO（超参搜索）工具如 Optuna、Ray Tune 能自动化搜索，但它们只能在一个预设的搜索空间里打转。它们不会"灵光一现"突然把 ReLU 换成 ReLU²，也不会"直觉上觉得"某个层去掉会更好。这些创造性的跳跃，目前只有人——或者更准确地说，只有能理解代码语义的 LLM——能做到。

autoresearch 要解决的根本问题不是"自动化超参搜索"，而是"把实验设计的创造力交给 AI"。这听起来很科幻，但它的实现方式出人意料地朴素。

二、架构：三个文件，一个实验循环

autoresearch 整个仓库只有三个核心文件，这种极简主义本身就值得研究：

```
prepare.py
```

——固定不变。包含数据预处理、BPE tokenizer 训练、数据加载器和评估函数。这是"实验的不变部分"，定义了公平比较的基准。

```
train.py
```

——唯一被 AI 编辑的文件。包含完整的 GPT 模型定义、Muon+AdamW 混合优化器、训练循环。从架构到超参数，一切皆可改。

```
program.md
```

——你（人类）写的 Markdown 指令文件。它本质上是一个极简的 "skill"，告诉 AI 实验的边界、目标、和实验循环的规则。这个文件是你对 AI 的唯一控制接口。

这个设计的精妙之处在于它的约束-自由对称性。实验循环非常直接：

1. AI 读取 

```
program.md
```

，决定这次要尝试什么改进

2. AI 编辑 

```
train.py
```

，git commit

3. 运行训练，固定 5 分钟 时间预算

4. 读结果：

```
val_bpb
```

（验证集 bits per byte），越低越好

5. 如果改进，保留；如果变差，git reset 回退；如果崩溃，记录后跳过

6. 回到步骤 1，永不暂停

整个循环大约 6-7 分钟一轮（含启动开销），也就是说一个晚上能跑约 100 个实验。Karpathy 的设计哲学是：每个实验的时间预算固定，这样不同架构、不同 batch size 的实验之间可以直接比较。你改了多少参数不重要，重要的是 val\_bpb 降了多少。

三、技术细节：这个训练脚本里藏了什么

我花了大量时间读 

```
train.py
```

 的源代码。表面上它只是一个"单文件 GPT 训练脚本"，但里面藏了很多近期 SOTA 训练技术的浓缩版。这不是一个 toy model——这是一个认真的、生产级的训练实现。

让我逐层拆解：

1）

```
Value Embedding
```

：模型用了 ResFormer 架构的变体，包含 Value Embedding（VE）机制。每隔一层，注意力头会从词表嵌入中额外提取一个 value embedding，通过输入相关的门控混合到 value 中。这不是随便加的——这是对 ResFormer 论文的工程化实现。

2）

```
Muon+AdamW 混合优化器
```

：Muon 是 Karpathy 自研的优化器，专门用于 2D 矩阵参数。它结合了 Nesterov 动量、Polar Express 正交化（类似自然梯度）、和 NorMuon 方差缩减。对于嵌入和标量参数，则用 AdamW。这种混合策略让同一个模型里不同类型的参数可以用最适合它们的优化方式。

3）

```
Flash Attention 3
```

：用了 Flash Attention 3，根据 GPU 型号自动切换后端（H100 用 varunneal 的版本，其他用 kernels-community 的）。

4）

```
Sliding Window Attention
```

：SSSL 模式，即浅层用短窗口注意力（half context），深层用长窗口。最后一层强制长窗口。这种交替模式在同样的参数规模下实现了更好的上下文建模。

5）

```
可学习残差缩放
```

：每层有两个可训练标量 

```
resid_lambda
```

 和 

```
x0_lambda
```

，实现类似 mixtral 的动态路由效果：残差连接和初始输入的混合比例可学习。

6）

```
Softcapping
```

：对 logit 做 

```
tanh
```

 限制，防止训练早期的数值爆炸。

把这些技术放在一起，加上 ReLU² 的激活函数（ReLU 平方）、Muon 专属 的正则化（cautious weight decay，只在梯度和参数同号时施加 decay），你得到的是一个在 约 50M 参数规模下、单 H100 上 5 分钟 训练 500M tokens 就能达到 约 0.998 val\_bpb 的模型。这个数字已经逼近了许多学术论文中同规模模型的结果。

四、实际体验：当 AI 开始做科研

```
program.md
```

 里有一段我特别喜欢的规则："NEVER STOP"——意思是，实验一旦开始，不要停下来问人类"要不要继续"。人类可能在睡觉，可能离开了电脑，AI 应该持续工作直到被手动停止。

这个设计决定了整个项目的基因。它不是"半自动"的——它是一个真正的无人值守系统。你早上看到的不是 AI 等你确认的中间结果，而是它自己判断、自己保留或丢弃、自己推进了上百个实验的最终状态。

community forks 已经非常活跃。Mac 用户有 autoresearch-macos 和 autoresearch-mlx 分支，Windows 用户有 autoresearch-win-rtx。AMD 用户有 ROCm fork。社区甚至有人在尝试让它在 MacBook 上跑——虽然 Karpathy 本人在 README 里建议小计算平台用户使用特定的 fork 和调优参数。

我注意到一个有趣的现象：autoresearch 的 PR 数量已经超过了很多传统开源项目的 issue 数量。notable forks 的活跃 forks 超过 20+ 个，每个 fork 都在尝试不同的架构改进。这本身就像一个分布式的研究组织——没有中央协调，但每个 fork 都在向同一个目标（降低 val\_bpb）努力。

五、同类方案对比

autoresearch 不是第一个做 AI 自动实验的项目，但它在设计哲学上和其他方案有明显区别。

对比 

```
GPT-Researcher
```

（Assaf Elovic, 26,760 星）：GPT-Researcher 是一个面向"调研"的 agent，它能搜索网页、阅读论文、生成报告。但它不碰代码。autoresearch 则完全相反——它不写报告，它直接改训练代码。

对比 

```
Deer-Flow
```

（Bytedance, 64,115 星）：Deer-Flow 是一个长程超级 agent 框架，能同时做研究、编码、创作。功能更全面，但也更重。autoresearch 只有一个文件和 5 分钟时间预算，刻意限制了范围以追求效率。

对比 

```
nanochat
```

（Karpathy 自己的项目, 52,629 星）：nanochat 是 autoresearch 的父项目，提供了完整的 GPT 训练代码。autoresearch 是从 nanochat cherry-pick 出来的简化版，砍掉了分布式训练、复杂配置等一切可能让 AI agent 困惑的东西。

对比 Optuna/Ray Tune 等传统 HPO：它们在一个预设的网格里搜索。autoresearch 的 AI 可以做任何它觉得合理的修改——改变激活函数、去掉层、改优化器、甚至完全重写注意力机制。这种"结构级搜索"是传统 HPO 做不到的。

六、设计洞察：为什么它值得关注

我认为 autoresearch 最重要的贡献不是技术层面的，而是方法论层面的。它提出了一种新的科研范式："AI as experimental loop, human as research direction"。

传统的科研流程是：人想出一个想法 -> 写代码实现 -> 跑实验 -> 看结果 -> 想下一个想法。这个循环的瓶颈是人的创意速度和注意力。autoresearch 把"写代码实现 -> 跑实验 -> 看结果"这三步压缩成了一个自动化的 6 分钟循环。人只需要做最上游的工作：定义实验方向和约束。

这有点像从"手动编译"到"实时预览"的跨越。以前你改一行 CSS，要重新编译、刷新浏览器、看效果。现在你在编辑器里改，右侧实时预览。autoresearch 把这种"即时反馈"的体验带进了 ML 研究。

另一个关键洞察是 小即是快。项目只有 3 个核心文件，AI 可以一次性把所有代码加载进上下文。如果项目有几十个文件，AI 的每次修改都会变得低效和容易出错。Karpathy 通过刻意限制代码规模，换取了 AI 的修改质量。

第三个洞察是 Markdown as programming。用 Markdown 文件给 AI agent 下指令，而不是写复杂的 Python 配置。这降低了人类用户的门槛——你不需要学一个新框架，你只需要写一个 .md 文件。

七、局限与未来

autoresearch 不是银弹，它有明显的局限：

1. 硬件依赖：它目前只支持单 NVIDIA GPU。这意味着消费级用户、Mac 用户、AMD 用户都需要依赖社区 fork。Karpathy 本人说他不打算维护多平台支持，因为"这会让代码膨胀"。

2. 任务锁定：训练任务被锁定为语言模型预训练（val\_bpb 指标）。如果你想用它做其他任务（比如目标检测、强化学习），你需要从头写一套 prepare.py 和评估函数。

3. 创意天花板：AI 的实验创意质量取决于基座模型的能力。用 Claude Sonnet 和用 Claude Opus 得到的实验质量可能不同。而且 AI 有时会陷入"局部最优"的创意模式，反复尝试相似的微调而不是大胆的结构改变。

4. 分析缺口：虽然 AI 能自动化实验，但它不写论文、不做 ablation study、不写 analysis。这些工作最终还是需要人来完成。autoresearch 加速了"试错"环节，但没有替代"理解"环节。

但这些问题可能正在被解决。autoresearch 社区已经出现了 

```
AutoResearchClaw
```

 这样的 fork——它不仅自动跑实验，还自动生成分析报告。而 Karpathy 在最近的 tweet 中提到，他正在思考如何让多个 autoresearch 实例协同工作，形成一个真正的"分布式研究集群"。

更深远地看，autoresearch 揭示了一个趋势：科研的边界正在从"实现能力"向"方向判断"转移。当 AI 能自动实验时，研究的核心竞争力从"你会不会调参"变成了"你知不知道该往哪个方向调"。这意味着研究人员的核心技能将从工程实现转向问题定义和方向判断。

也许有一天，我们真的会像 Karpathy 开玩笑说的那样——面对第 10,205 代的自修改代码，完全看不懂，但知道它比第 1 代好多了。

---

信息来源

[1] karpathy/autoresearch · AI agents running research on single-GPU nanochat training automatically · 77,471 stars

[2] karpathy/nanochat · The best ChatGPT that $100 can buy · 52,629 stars

[3] miolini/autoresearch-macos · MacOS port of autoresearch · notable fork

[4] aiming-lab/AutoResearchClaw · Fully autonomous & self-evolving research from idea to paper · 11,774 stars

[5] assafelovic/gpt-researcher · Autonomous agent that conducts deep research · 26,760 stars

[6] bytedance/deer-flow · Open-source long-horizon SuperAgent harness · 64,115 stars

[7] browser-use/browser-harness · Self-healing harness that enables LLMs to complete any task · 7,813 stars

[8] Karpathy on X · autoresearch project announcement and context
