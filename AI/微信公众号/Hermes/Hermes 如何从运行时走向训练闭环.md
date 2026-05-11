> 📎 来源: [AI步步通](https://mp.weixin.qq.com/s?__biz=MzY4NTE4OTYzNg==&mid=2247483879&idx=1&sn=e5476ed648410e6fee4ae41e1e24667f&chksm=f27ffd56e8733bf6c4f19a72825e5df8ca9638acdf0fa47f24af0251906373283f4306525089&mpshare=1&scene=1&srcid=0430gc9rk9OLDvOm87Si5kyo&sharer_shareinfo=fe47854624a882a10a8856cd49f6c6ba&sharer_shareinfo_first=fe47854624a882a10a8856cd49f6c6ba) | 时间: 2026-04-30 14:24

---

Agent 系统完成任务之后，执行过程本身也值得被保存下来。Hermes 的一个重要设计是把这些过程结构化：哪些工具被调用、上下文如何变化、结果是否完成、奖励如何计算，都可以继续进入评估、微调和强化学习链路。

这条链路的入口可以来自人工对话，也可以来自定时任务和批量环境。Cron 让任务可以按时间自动触发，并在独立 session 里运行；Trajectory 把多轮对话和工具结果保存成可训练的 ShareGPT JSONL；Environment 把任务、工具、沙盒和评分函数封装起来；RL 工具再把这些 scored trajectories 接到 Atropos 和 Tinker。

这样看 Hermes，它的运行时能力正在延伸成一条数据生成链路。Agent 执行过程可以被复盘、评分和批量生产，最终成为下一轮模型改进的输入。

Hermes 的训练闭环可以拆成四层：Cron 负责主动触发任务，Trajectory 负责保存过程，Environment 负责给任务定义评分标准，Atropos/Tinker 负责把 scored rollouts 送进 SFT 或 RL 训练。

Hermes 运行时到训练闭环任务触发、工具执行、轨迹保存、环境评分、训练反馈组成迭代链路Cron Tasksfresh sessionschedule / skill / deliveryAgent RuntimeLLM + toolsmulti-turn rolloutTrajectoryShareGPT JSONLtool stats / metadataEnvironmenttask / sandbox / rewardevaluate / process / serveAtropos / Tinkerrollout groupsGRPO / LoRA / metricsImproved Agent Behaviorfine-tuned model / RL adapter / better tool policy

## 一、训练闭环的起点是可复现的任务执行

Agent 要进入训练闭环，第一步是把一次任务执行变成可复现对象。一次任务要有输入、可用工具、执行环境、过程记录、结果状态和评估信号。缺少其中任何一项，后面都只能得到一堆聊天记录，很难变成可用数据。

Hermes 的设计把这几件事拆开处理。运行时负责完成任务，Trajectory 负责保存过程，Environment 负责定义题目和奖励，Batch Runner 负责批量制造样本，RL 工具负责把环境接到训练服务。这个拆分让“使用 Agent”和“训练 Agent”之间有了共同的数据结构。

这条主线也决定了阅读 Hermes 的方式：训练能力从运行时结构里长出来。工具调用、沙盒状态和任务结果先被规范化，之后才有机会变成微调数据或强化学习样本。

从一次任务到训练样本，至少需要四个字段

1. **任务输入：** 用户问题、数据集 item、定时任务 prompt 或外部事件。

2. **执行过程：** 模型回复、工具调用、工具结果、失败与重试。

3. **环境状态：** 文件、终端、浏览器、容器、项目目录等可验证上下文。

4. **评分结果：** 成功标记、reward、测试输出、工具错误统计或人工评估。

## 二、Cron 把 Agent 任务变成持续运行的事件源

Cron 在 Hermes 里承担的是主动任务入口。它可以接收自然语言时间、间隔、标准 cron 表达式或指定时间戳，把一次 prompt 变成未来会自动执行的任务。任务可以带一个或多个 skill，可以指定工作目录，也可以把结果发回原始对话、文件或消息平台。

更重要的是，Cron 任务不是沿用原聊天窗口的上下文继续说话。每个 due job 会启动一个 fresh AIAgent session，加载附加 skill，再执行自包含 prompt。这个隔离很适合训练数据：它减少了“上一轮对话残留”对样本的污染，也要求任务描述必须足够完整。

```
cronjob(    action="create",    schedule="every 6h",    skills=["repo-auditor"],    workdir="/home/team/project",    prompt="检查未合并 PR、CI 状态和测试失败原因，输出工程风险摘要。",    deliver="wecom")
```

从训练闭环的角度看，Cron 的价值在于稳定地产生真实任务流。每日巡检、监控告警、资料摘要、代码仓库审计都可以成为长周期样本来源。它们来自持续发生的工作事件，比一次性 benchmark 题目更接近生产分布。

| Cron 机制 | 工程含义 | 对数据生成的帮助 |
| --- | --- | --- |
| fresh session | 每次任务独立运行，不继承聊天历史。 | 样本更干净，输入和输出边界更清晰。 |
| skills | 复用已经沉淀的工作流程。 | 让同类任务保持一致执行范式。 |
| workdir | 把任务绑定到项目目录和配置文件。 | 形成可复查的项目上下文。 |
| recursion guard | Cron run 内禁用 cronjob 工具。 | 避免样本里出现失控递归调度。 |

Cron 任务进入数据链路时，还要把失败当成一等记录处理。定时任务可能因为凭证失效、外部 API 限流、项目目录变化或工具后端异常而失败。失败轨迹不应该直接混入成功样本池，但也不应该简单丢掉；它们可以进入单独的 failure queue，用来训练错误恢复、工具降级和告警摘要。

更稳的做法是给 Cron 样本加上状态字段：success、retryable\_failure、terminal\_failure、needs\_human\_review。可重试失败先进入调度器重跑；不可重试失败保留 traceback、工具结果和最终说明；需要人工复查的样本暂缓进入训练集。这样 Cron 才能成为可靠的数据来源，而不是把生产噪声原样倒进训练文件。

## 三、Trajectory 把工具调用过程保存成训练材料

有了任务流之后，下一步是把过程保存下来。Hermes 使用 ShareGPT-compatible JSONL 保存 trajectory。Trajectory 可以理解成一次 Agent rollout 的完整轨迹：system、human、assistant、tool 这些消息按顺序排列，再附上 timestamp、model、completed、metadata、tool\_stats 等字段。

这个格式的好处在于它保留了工具使用上下文。普通聊天记录只看到用户和助手；Agent 训练更关心模型在什么时候决定调用工具、调用了什么、工具返回了什么、模型如何根据结果继续推理。工具轨迹一旦丢失，后续微调很容易只学到最终回答，学不到中间动作策略。

```
{  "conversations": [    {"from": "human", "value": "检查项目测试失败原因"},    {"from": "assistant", "value": "... terminal pytest ..."},    {"from": "tool", "value": "测试输出..."},    {"from": "assistant", "value": "失败原因是数据库迁移缺少字段。"}  ],  "completed": true,  "reward": 0.7,  "metadata": {"source": "cron", "status": "success"},  "tool_stats": {    "terminal": {"count": 1, "success": 1, "failure": 0}  }}
```

Batch Runner 会把大量 prompts 批量跑成 trajectories，并记录工具使用统计、错误计数、推理覆盖率和 checkpoint。它还会丢弃没有 reasoning 的样本，过滤幻觉工具名。这些过滤看似细节，实际是在保护训练集质量：迭代链路一旦混入大量无效轨迹，模型会学到错误的工具调用习惯。

Trajectory 保存的是过程，reward 和 metadata 则把这个过程放进可筛选的数据集里。离线 process 模式通常会把评分结果和环境信息写回同一条 JSONL 记录；在线 serve 模式则会把对话、reward、done 状态和 metadata 打包成 rollout response，交给训练系统继续计算优势和更新策略。

## 四、Environment 让任务具备可评分边界

Trajectory 解决“记录什么”，Environment 解决“怎样判断好坏”。Hermes 的 Environment Abstractions 把任务、数据集、prompt 构造、工具集合、沙盒后端和 reward 函数封装在同一个环境类里。一个环境至少要回答：下一道题是什么，如何变成用户消息，工具在什么沙盒里执行，结果怎样评分。

这一步让训练数据从“完成过的对话”变成“带分数的行为样本”。例如代码任务可以在同一个 Modal 或 Docker 沙盒里运行测试；文件任务可以检查目标文件是否生成；长周期策略任务可以用仿真结果计算 composite score。评分函数越贴近真实目标，trajectory 对训练越有用。

```
class MyEnv(HermesAgentBaseEnv):    name = "repo-fix-env"    async def get_next_item(self):        return self.dataset.next()    def format_prompt(self, item):        return item["issue_description"]    async def compute_reward(self, item, result, ctx):        test = ctx.terminal("pytest -q")        coverage = parse_coverage(ctx.terminal("coverage report"))        if test["exit_code"] != 0:            return {"reward": 0.0, "metadata": {"tests": "failed"}}        return {            "reward": 0.6 + 0.4 * coverage["line_rate"],            "metadata": {"tests": "passed", "coverage": coverage["line_rate"]},        }
```

Environment 的三个运行模式

1. **evaluate：** 跑 benchmark，计算指标，适合横向评测模型能力。

2. **process：** 跑 rollouts，保存带 reward 和 metadata 的 JSONL，适合生成 SFT 数据。

3. **serve：** 接入 Atropos API，环境接收任务、执行 rollout、计算奖励，再把 scored trajectories 送回训练系统。

## 五、Atropos 与 Tinker 接住在线 RL 链路

evaluate、process、serve 放在同一套环境框架下，带来的工程收益很直接。评测、SFT 数据生成和 RL 训练不需要各写一套任务逻辑。它们共享环境、工具解析、沙盒后端和奖励函数，只是在输出路径上不同。

process 模式更像离线数据工厂。它运行 agent rollouts，把完整对话、reward 和 metadata 写入 JSONL。团队可以用这些样本做监督微调，或者先人工抽检，筛掉奖励函数没有覆盖到的坏样本。

serve 模式则进入在线强化学习。Environment 作为环境服务接收 rollout 请求，取出 item、构造 prompt、调用 Hermes runtime、执行工具、计算 reward，再把 trajectory、reward、done 和 metadata 返回给 Atropos。Atropos 会把同一任务的多次 rollout 组织成 rollout group，用奖励差异估计不同轨迹的训练权重。

Tinker 处在训练执行层，负责 LoRA 训练、采样和优化步骤。优势计算可以理解成“这条轨迹比同组其他轨迹好多少”的归一化信号，GRPO/PPO 这类算法会用这个信号更新策略。Hermes 的 rl 工具把环境发现、配置、启动和监控暴露给 Agent，使训练流程也能被工具化编排。

serve 模式的数据流

1. Atropos 向 Environment 请求一个或多个待执行 item。

2. Environment 把 item 格式化成 prompt，并在 Hermes runtime 中执行 rollout。

3. Environment 用测试、规则、仿真或人工反馈计算 reward，并附上 metadata。

4. Atropos 汇总同组 rollouts，计算优势信号，再交给 Tinker 执行训练更新。

| 路径 | 产物 | 适合解决的问题 |
| --- | --- | --- |
| Batch Runner | ShareGPT trajectories、tool stats、reasoning coverage。 | 批量制造工具使用样本和评测样本。 |
| Environment process | 带 reward 和 metadata 的 scored trajectories。 | 生成可筛选的 SFT 数据。 |
| Environment serve | 发送给 Atropos 的 rollout groups。 | 做在线 RL、GRPO/PPO 训练和策略更新。 |
| Cron task | 真实周期任务输出和可审计运行记录。 | 把生产型任务变成持续样本来源。 |

## 六、奖励设计与样本过滤决定数据质量

运行时数据需要经过筛选和评分才能进入训练集。Agent 轨迹通常很长，工具结果很杂，任务成功也不总是二元结果。Hermes 提供了保存、批处理和环境接口，数据价值最终取决于 reward 函数和样本过滤。

reward 要尽量靠近任务真实目标：测试是否通过、文件是否生成、网页状态是否符合预期、错误是否被定位、风险是否被上报。对工程类 Agent 来说，奖励函数最好落在可执行验证上，模型裁判只适合补充主观质量判断。

| reward 形态 | 适用场景 | 风险 |
| --- | --- | --- |
| 二元奖励 | 测试通过 / 失败、文件存在 / 不存在。 | 信号稀疏，模型很难知道中间步骤哪里做对了。 |
| 连续奖励 | 测试通过率、覆盖率、错误减少比例、检索命中率。 | 容易奖励局部指标，忽略最终任务质量。 |
| 复合评分 | 工程任务、研究任务、长周期自动化任务。 | 权重设计复杂，需要人工抽检校准。 |

把运行轨迹用于训练前，至少做四类过滤

1. 去掉没有完成或被中断的样本，除非目标就是训练失败恢复。

2. 检查工具名、参数和返回格式，过滤幻觉工具调用。

3. 保留失败样本的错误原因，但不要把错误轨迹混进成功样本池。

4. 对长轨迹做压缩或摘要时，保护开头任务、关键工具调用和最终结果。

## 七、Cron 与 Environment 指向两种不同的数据来源

Cron 和 Environment 都能产生训练闭环里的样本，但它们的角色不同。Cron 更接近真实生产事件，优点是任务自然、长周期、带业务噪声；缺点是评分不一定直接。Environment 更接近可控实验台，优点是任务边界和 reward 清晰；缺点是容易脱离真实工作流。

一种更稳的组合方式是：先用 Cron 跑一周真实生产任务，例如仓库巡检、告警摘要和 PR 风险分析；再从 trajectory 中筛出高质量成功样本、可恢复失败样本和高频工具错误；最后把这些任务改写成 Environment item，用测试、规则或人工标签补上 reward，进入 process 或 serve 模式做对比实验。

持续的数据收集与训练迭代机制往往需要两者结合。Cron 提供真实任务分布，Environment 提供可验证训练场，Trajectory 把两边的过程统一成可处理格式。这样训练集既有真实复杂度，也有明确评分标准。

总结

1. Cron 让 Hermes 具备持续任务入口，fresh session 和 recursion guard 让任务样本边界更清楚。

2. Trajectory 把多轮对话、工具调用、工具返回和完成状态保存成 ShareGPT JSONL。

3. Environment 把任务、工具、沙盒和 reward 函数封装成可评测、可生成数据、可接入 RL 的统一接口。

4. Batch Runner 和 process 模式适合离线生成 SFT 数据，serve 模式适合接入 Atropos/Tinker 做在线 RL。

5. 训练闭环的质量取决于 reward 设计、样本过滤、失败样本管理和轨迹压缩策略，样本数量只是一部分。

Agent 平台的长期价值来自两件事，一件是当下完成任务，另一件是把完成任务的过程沉淀成下一轮能力提升的燃料。运行时、调度器、轨迹格式和环境框架连起来，才有可能形成持续改进的工程闭环。
