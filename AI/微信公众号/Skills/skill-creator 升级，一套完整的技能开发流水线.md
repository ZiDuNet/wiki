> 📎 来源: [AI工程化实战派](https://mp.weixin.qq.com/s?__biz=MzA4MDUzNjMzOQ==&mid=2447658837&idx=1&sn=a1f5427e057e2aee8961ab73fcbcdef6&chksm=8a2517e2b2219994e29be7735c136c4fe70799e77e5602c053a7e1f0b27e03734f60e4ce0c5e&mpshare=1&scene=1&srcid=0513FICvmeRt9rWBuiWJ2Xzd&sharer_shareinfo=66f887a551015e1ce253078b5be13b2a&sharer_shareinfo_first=66f887a551015e1ce253078b5be13b2a) | 时间: 2026-05-13 01:57

---

# 官方 Skill 创建工具升级了，一套完整的技能开发流水线

> Anthropic 官方的 skill-creator 最近更新了不少内容。从创建、测试、评估、迭代到打包发布，形成了一套完整的技能开发流水线。我之前写过几个自定义 Skill，这次把整个工具链跑了一遍，做个功能对比和实操笔记。

---

## 为什么关注这个？

之前写 Claude Code 的 Skill 基本靠手感。写个 SKILL.md，试试看能不能触发，效果不好就改。没有测试，没有对比，没有量化评估。

skill-creator 解决的正是这个问题。它把 Skill 开发从「写完了试试看」变成了「写测试用例 → 跑对比 → 看数据 → 改代码 → 再跑」的工程化流程。

---

## 一、skill-creator 是什么？

一句话概括：一个帮你创建、测试、评估和迭代 Claude Skill 的工具包。

它不是某个具体功能的 Skill，而是一个「制造 Skill 的 Skill」。你告诉它你想做什么，它帮你写出 SKILL.md，跑测试用例，对比有 Skill 和没 Skill 的效果，用可视化界面让你 review 结果，然后根据反馈改进。

整套工具包含：

- SKILL.md（核心指令，约 480 行）
- scripts/（7 个 Python 脚本）
- agents/（3 个专业子代理指令）
- eval-viewer/（评估结果可视化）
- assets/（评估集审核 HTML 模板）
- references/（JSON Schema 文档）

---

## 二、核心功能对比

### 和之前比，升级了什么？

| 能力 | 之前手写 Skill | 用 skill-creator |
| --- | --- | --- |
| 需求捕捉 | 自己写，凭经验 | 引导式问答，从对话历史提取 |
| 测试用例 | 手动试 1-2 个 | 系统化 2-3 个起步，可扩展 |
| 对比基线 | 没有 | with\_skill vs without\_skill |
| 量化评估 | 没有 | 断言检查 + 计时 + Token 统计 |
| 结果可视化 | 没有 | 浏览器 viewer，双标签页 |
| 迭代机制 | 手动改 | 结构化 iteration 目录，支持跨版本对比 |
| 描述优化 | 凭感觉 | 20 条测试 query 自动优化循环 |
| 盲评对比 | 没有 | 独立子代理 A/B 盲评 |
| 打包发布 | 手动复制 | 一键打包 。skill 文件 |

### 脚本工具清单

| 脚本 | 功能 | 何时用 |
| --- | --- | --- |
| ``` aggregate_benchmark.py ``` | 汇总 benchmark 数据，生成对比报告 | 所有测试跑完后 |
| ``` run_loop.py ``` | 描述优化自动循环，60% 训练 + 40% 测试 | 描述调优阶段 |
| ``` run_eval.py ``` | 单次评估运行 | 描述调优内部迭代 |
| ``` improve_description.py ``` | 基于结果改进描述 | 描述调优 |
| ``` package_skill.py ``` | 打包成 。skill 文件 | 最终发布 |
| ``` quick_validate.py ``` | 快速验证 Skill 格式 | 写完 SKILL.md 后 |
| ``` generate_review.py ``` | 启动评估结果 viewer | 测试完成后给人类 review |

### 子代理角色

| 代理 | 职责 |
| --- | --- |

grader 负责评估断言是否通过，给出证据。comparator 盲评两个输出，选更好的。analyzer 分析为什么一个版本赢了另一个。

---

## 三、完整实操流程

### 第一步：明确意图

告诉 skill-creator 你想做什么。比如「我想做一个把 CSV 数据转成数据可视化报告的 Skill」。

它会问你几个问题：

1. 这个 Skill 要让 Claude 做什么？
2. 什么时候触发？（用户说什么话、什么场景下）
3. 期望的输出格式是什么？
4. 要不要设测试用例？（客观可验证的 Skill 建议设，主观的比如写作风格可以跳过）

如果之前已经写过初稿，可以跳过这一步直接进入评估。

### 第二步：调研和编写

skill-creator 会主动问边界情况、输入输出格式、示例文件、成功标准。它会检查可用的 MCP 工具，如果有用得上的（搜文档、找类似 Skill、查最佳实践），会并行调研。

然后写出 SKILL.md 初稿。一个标准的 Skill 结构：

```
12345678
        skill-name/├── SKILL.md（必须）│   ├── YAML frontmatter（name + description）│   └── Markdown 指令└── 资源（可选）    ├── scripts/    - 可执行脚本    ├── references/ - 参考文档    └── assets/     - 模板、图标等
```

### 第三步：写测试用例

写出 2-3 个真实用户会说的测试 prompt，保存为

```
evals/evals.json
```

：

```
1234567891011
        {  "skill_name": "my-skill",  "evals": [    {      "id": 1,      "prompt": "帮我分析这份销售数据，做成图表",      "expected_output": "包含柱状图和折线图的 HTML 报告",      "files": ["sales_data.csv"]    }  ]}
```

### 第四步：跑对比测试

这是 skill-creator 最核心的部分。每个测试用例会同时跑两条线：

- with\_skill：带 Skill 的 Claude 执行
- baseline：不带 Skill 的 Claude 执行（创建新 Skill 时）或旧版本 Skill（改进已有 Skill 时）

所有并行启动，一起跑完。

测试过程中，skill-creator 会起草量化断言——每个测试用例检查什么、怎么算通过。

每次测试会记录：

- Token 消耗
- 运行时间
- 断言通过率

### 第五步：看结果

跑完后，启动 eval viewer：

```
1234
        python eval-viewer/generate_review.py \  /iteration-1 \  --skill-name "my-skill" \  --benchmark /iteration-1/benchmark.json
```

浏览器打开后有两个标签。Outputs 逐个看测试用例的输出，可以留反馈。Benchmark 展示量化对比，通过率、时间、Token 消耗。

### 第六步：迭代改进

根据人类反馈和量化数据改进 SKILL.md，然后跑下一轮。第二轮 viewer 会加上

```
--previous-workspace
```

，可以直接对比上一版。

重复直到满意。

### 第七步：描述优化

Skill 写好后，用描述优化循环提升触发准确率：

1. 生成 20 条测试 query（10 条应该触发 + 10 条不该触发）
2. 在 HTML 模板里审核这些 query，调整
3. 跑优化循环，自动迭代 5 轮
4. 选测试集分数最高的描述

### 第八步：打包

```
1
        python -m scripts.package_skill
```

生成

```
.skill
```

 文件，用户可以直接安装。

---

## 四、几个设计亮点

Skill 采用三级加载。元数据（name + description）始终在上下文，约 100 词。SKILL.md 正文在触发时才加载，理想情况不超过 500 行。资源文件按需加载，不限制大小。

这意味着 SKILL.md 本身要保持精简，大文件放到

```
references/
```

 里。

skill-creator 的设计哲学是给模型解释**为什么**重要，而不是用 ALL CAPS 下死命令。今天的 LLM 有很强的理论心智，给理由比下指令更有效。

如果 3 个测试用例里子代理都各自写了一个

```
create_docx.py
```

，这就是信号——Skill 应该把这个脚本打包进

```
scripts/
```

 里，以后就不用每次重新发明了。

skill-creator 还考虑了不同运行环境。Cowork 有子代理但没浏览器，用

```
--static
```

 生成 HTML 文件。Claude.ai 没子代理，手动跑测试，跳过量化基准。

---

## 五、注意事项

需要子代理才能跑完整流程。没有子代理的环境（Claude.ai）只能做定性测试，跳过定量基准和盲评。

测试用例质量决定一切。如果测试用例太简单，Claude 自己就能搞定，不会触发 Skill。测试用例要有一定复杂度，最好是多步骤任务。

描述优化的 20 条 query 要仔细审核。质量差的 query 会训练出差的描述。near-miss 类型的「不该触发」query 最有价值，它们测试的是边界情况，而不是明显无关的请求。

描述优化耗时较长。每条 query 跑 3 次取稳定触发率，20 条就是 60 次调用，加上 5 轮迭代，需要耐心。

SKILL.md 不要超过 500 行。超过的话需要分层，用 reference 文件分担内容。

---

## 总结

skill-creator 把 Skill 开发从「玄学」变成了「工程」。有测试、有对比、有量化指标、有迭代循环。

核心流程就四步：写 → 测 → 评 → 改。但每个环节都有工具支撑，不是靠手感。

如果你也在写自定义 Skill，建议试试这个工具链。尤其是描述优化那一步，跑完之后触发准确率确实有提升。

文档和源码：

- skill-creator 源码（Anthropic 官方仓库）
- Claude Code 文档 - Skills

如果你有 Skill 开发的好方法或踩坑经验，欢迎在评论区交流。

---

> **免责声明**：本文内容仅为个人学习分享，工具功能基于官方 SKILL.md 文档，实际功能以最新发布为准。skill-creator 为 Anthropic 官方项目。

---

感谢你的阅读。

如果这篇文章对你有帮助，欢迎：

- 点赞支持
- 分享给朋友
- 在评论区分享你的想法

关注「AI 工程化实战派」，不空谈虚概念，只输出务实干货。

期待和你的交流！

![](assets/img_d12b7144cd9b.jpg)

AI工程化实战派公众号二维码
