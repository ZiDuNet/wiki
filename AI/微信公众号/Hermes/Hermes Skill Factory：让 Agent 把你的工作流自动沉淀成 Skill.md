> 📎 来源: [AI 趋势方向](https://mp.weixin.qq.com/s?__biz=MzU5MTkyMzY4NQ==&mid=2247483704&idx=1&sn=f3129d78a0db853567a138d79e38e064&chksm=ff7b8348a36115ab9f16f3c6fc249f60652ab9e491607d5c340aa8a65914ee0dc285ed0c96ad&mpshare=1&scene=1&srcid=05094mzd2FR3ObezOGHTtOtd&sharer_shareinfo=4a57dbf64cafcacce920639efcdea2a5&sharer_shareinfo_first=4a57dbf64cafcacce920639efcdea2a5) | 时间: 2026-05-09 15:37

---

Hermes Skill Factory：让 Agent 把你的工作流自动沉淀成 Skill

很多人用 AI Agent 的方式，其实还停留在“每次重新教一遍”。

今天让它帮你搭 Python 环境。

明天让它帮你修测试。

后天让它帮你开 PR。

流程明明差不多，但每次都要重新解释：

- 先做什么
- 再验证什么
- 出错怎么排
- 哪些坑别踩
- 最后怎么收尾

这就是 Agent 使用里一个很真实的浪费：

你解决过的问题，没有自动变成下次可复用的能力。

hermes-skill-factory 这个项目，解决的就是这件事。

它不是一个普通 skill。

它是一个“制造 skill 的 skill”。

项目地址：

https://github.com/Romanescu11/hermes-skill-factory

---

# 01

# 它是什么？

一句话：

Skill Factory 是给 Hermes Agent 用的元技能：它观察你的工作流，然后把可复用流程自动生成 Hermes Skill。

它面向的是 Nous Research 的 Hermes Agent，要求 Hermes Agent v2026.3+。

它的核心思路很简单：

Every workflow you repeat is a skill waiting to be born.

每一个你重复做的工作流，都是一个等待诞生的 skill。

比如你经常这样做：

创建 Python 虚拟环境

安装依赖

运行测试

修失败

再次验证

以前这只是一次对话里的操作过程。

对话结束，它就散了。

Skill Factory 想做的是：

把这些过程识别出来，整理成 SKILL.md，必要时再生成一个 plugin.py，让下次可以直接复用。

---

# 02

# 为什么这个方向值得看？

因为 AI Agent 真正有价值的地方，不只是“这次帮你做完”。

更重要的是：

它能不能把这次做事的方法沉淀下来，下次做得更快、更稳。

现在很多 Agent 的问题是：

- 会干活，但不会长期积累流程
- 能解决一次问题，但下次还要重新讲
- 过程藏在聊天记录里，不容易复用
- 好的 prompt、步骤、检查项，没有变成工具
- 团队经验没有沉淀成标准作业流

Hermes 本身有 skills 机制，可以把流程写成可复用能力。

但现实问题是：

大部分人不会主动写 skill。

不是不知道有用，而是麻烦。

你得回忆刚才怎么做的。

你得整理步骤。

你得写触发条件。

你得补质量检查。

你还得放到正确目录。

所以 Skill Factory 的价值点就出来了：

它把“工作流沉淀”从手工整理，变成半自动生成。

这对高频使用 Agent 的人很重要。

---

# 03

# 它不是自动保存一堆垃圾，而是先观察、再提案

Skill Factory 的设计里有一个关键点：

它不是看到什么都自动保存。

它分三步：

1. Passive Observation 被动观察

2. Proposal 提案

3. Generation 生成

第一阶段：被动观察

你正常使用 Hermes。

Skill Factory 在背后观察：

- 重复动作
- 3 步以上的完整工作流
- 经常一起使用的工具组合
- 用户口头提示，比如“我每次都要这样做”
- 调试里的固定套路
- 某个领域里的稳定处理方法

它不会打断你。

它更像一个在旁边看你工作的助理，等发现有价值的模式，再提醒你：

这个流程值得沉淀成 skill。

第二阶段：提案

当它检测到模式，或者你手动触发：

/skill-factory propose

它会给出类似这样的提案：

🏭 SKILL FACTORY — New Skill Detected

I noticed you repeatedly set up a Python environment,

installed dependencies, and ran tests in the same order.

Proposed Skill: python-env-setup

Category: software-development

Description: Reproducible Python project setup workflow

What it captures:

1. Create venv and activate

2. Upgrade pip and install dependencies

3. Run pytest to verify environment

Generate:

[A] SKILL.md

[B] plugin.py

[C] Both

[D] Skip

也就是说，它会先问你。

你可以选：

A：只生成 SKILL.md

B：只生成 plugin.py

C：两个都生成

D：跳过

这点很合理。

因为不是所有重复动作都值得沉淀。

自动保存一堆低质量 skill，只会污染系统。

第三阶段：生成

你确认之后，它会写文件：

~/.hermes/skills///SKILL.md

~/.hermes/plugins/.py

一个是 AI 能理解的流程说明。

一个是可以直接触发的 slash command 插件脚手架。

---

# 04

# 它到底会生成什么？

Skill Factory 主要生成两类东西。

1）SKILL.md：给 Agent 看的流程说明

生成的 SKILL.md 会符合 Hermes 的 skill 格式。

典型结构包括：

---

name: Python Env Setup

category: software-development

description: Reproducible Python project setup

tags: [python, venv, testing]

---

# Python Env Setup

## When to Activate

## Workflow

### Phase 1: Environment

1. python -m venv .venv

2. source .venv/bin/activate

3. pip install dependencies

## Quality Checklist

## Examples

## Anti-patterns

## Integration

这个文件的价值是：

下次 Agent 遇到类似任务时，不需要重新从零理解你的习惯。

它知道：

- 什么情况下应该激活这个 skill
- 标准步骤是什么
- 做完前要检查什么
- 哪些反模式要避免
- 有哪些真实例子可以参考

这就是程序化记忆。

不是普通聊天记录，而是能被 Agent 主动复用的操作规程。

---

2）plugin.py：给用户直接触发的命令

除了 SKILL.md，它还可以生成一个 Hermes 插件脚手架。

例如：

def register(hermes):

@hermes.command(

name="python-env-setup",

description="Reproducible Python project setup",

usage="/python-env-setup [args]"

)

async def run\_skill(ctx, args=""):

# Step 1: Create venv

# Step 2: Install deps

# Step 3: Run tests

...

这意味着你不只是有一份流程文档，还可以有一个命令入口：

/python-env-setup

当然要注意：

生成的 plugin.py 更像脚手架，不一定是最终可直接生产使用的完整代码。

项目文档里也明确提到，生成后需要你继续编辑：

- 补实际实现逻辑
- 加错误处理
- 调整步骤细节
- 适配你的 Hermes 版本和插件 API

这点很重要，别把它理解成“自动生成完就万事大吉”。

---

# 05

# 安装方式

项目提供一键安装脚本。

要求：

Hermes Agent v2026.3+

安装：

git clone https://github.com/Romanescu11/hermes-skill-factory

cd hermes-skill-factory

bash install.sh

也可以手动安装。

安装 meta-skill：

mkdir -p ~/.hermes/skills/meta/skill-factory

cp skills/skill-factory/SKILL.md ~/.hermes/skills/meta/skill-factory/

安装 plugin：

cp plugins/skill\_factory.py ~/.hermes/plugins/

然后激活：

hermes skills reload

hermes skills enable skill-factory

---

# 06

# 常用命令

安装之后，可以用这些命令：

/skill-factory propose

分析当前会话，立即提出一个最值得沉淀的 skill。

/skill-factory list

列出当前会话生成过的 skills。

/skill-factory status

查看当前追踪了多少模式。

/skill-factory queue

查看排队等待提案的模式。

/skill-factory save

用自定义名字保存上一个提案。

/skill-factory clear

清空当前会话日志。

你也可以直接自然语言告诉 Hermes：

Save this as a skill

Remember how to do this

Turn this workflow into a reusable skill

这对非命令行用户更友好。

---

# 07

# 它的仓库结构也很清楚

项目结构大概是这样：

hermes-skill-factory/

├── skills/

│ └── skill-factory/

│ └── SKILL.md

├── plugins/

│ └── skill\_factory.py

├── templates/

│ ├── SKILL\_TEMPLATE.md

│ └── PLUGIN\_TEMPLATE.py

├── examples/

│ └── generated/

│ └── git-pr-workflow/

│ └── SKILL.md

├── docs/

│ └── how-it-works.md

└── install.sh

这里面最关键的是两块：

skills/skill-factory/SKILL.md

plugins/skill\_factory.py

一个负责“让 Hermes 知道怎么观察和生成 skill”。

一个负责提供 /skill-factory 这些命令和文件生成能力。

---

# 08

# 一个具体例子：把 PR 流程沉淀成 skill

仓库里有一个示例：git-pr-workflow。

它把一次完整 PR 流程拆成几个阶段：

Phase 1：Branch & Commit Hygiene

Phase 2：CI Pre-flight

Phase 3：PR Description

里面会要求你：

- git status 检查工作区

- git log origin/main..HEAD --oneline 检查提交

- squash / reword 噪声 commit

- 运行测试和 linter

- push 分支

- 写清楚 PR 的 What / Why / How to Test

- 分配 reviewer

这就是典型适合变成 skill 的流程。

因为它不是一次性的。

只要你经常做 PR，就会重复遇到：

- commit 乱

- 测试没跑

- PR 描述太水

- reviewer 不知道怎么看

- CI 红了才发现

把这套流程做成 skill，下次 Agent 就可以按标准流程帮你准备 PR。

这比每次说一句“帮我开个 PR”靠谱得多。

---

# 09

# 它真正有价值的场景

我认为 Skill Factory 适合这几类场景。

1）调试流程沉淀

比如你经常做：

复现 bug

查看日志

提出假设

做最小验证

修复

回归测试

写总结

这就非常适合变成 skill。

下次 Agent 修 bug 时，不会一上来乱改，而是按你的调试纪律走。

2）项目初始化流程

比如：

创建虚拟环境

安装依赖

配置 env

运行测试

检查格式化

启动服务

验证 endpoint

这类流程重复率很高，沉淀成 skill 很划算。

3）PR / Review 流程

比如：

查看 diff

跑测试

查敏感信息

写 PR 描述

补验证记录

生成 review checklist

这些流程一旦标准化，团队协作质量会明显提高。

4）内容生产流程

对自媒体也有用。

比如：

读取 GitHub README

提炼项目定位

写公众号正文

补标题

补封面文案

补社群转发语

补评论区引导

这类流程也可以沉淀成 skill。

以后写同类文章，就不是“重新想结构”，而是按标准链路执行。

5）部署和运维流程

比如：

检查配置

备份数据

执行部署

看进程状态

看日志

跑健康检查

确认回滚方案

这种高风险流程更应该 skill 化。

因为它要求稳定、可验证、少犯错。

---

# 10

# 但它也有边界

这个项目值得看，但不要过度神化。

第一，自动生成不是最终质量

Skill Factory 生成的是起点。

真正好用的 skill，还是要人修：

- 触发条件要清楚

- 步骤要具体

- 质量检查要落地

- 反模式要写明

- 示例要贴近真实工作流

如果完全不审，就容易生成一堆看似有用、实际很泛的 skill。

第二，plugin.py 需要二次实现

生成的插件更多是 scaffold。

要真正变成稳定命令，还需要补代码、补异常处理、补版本兼容。

第三，隐私和敏感信息要注意

它会观察工作流。

如果你的会话里涉及：

- token

- password

- 私有路径

- 客户信息

- 内部业务数据

生成 skill 前要审一遍，避免把敏感信息写进 SKILL.md 或插件里。

第四，当前更适合重度 Hermes 用户

如果你只是偶尔用一次 Agent，这个工具可能显得重。

但如果你每天都在用 Hermes 做开发、调试、发文、运维、策略研究，那它很有价值。

---

# 11

# 我对这个项目的判断

Hermes Skill Factory 最有意思的地方，不是“自动生成一个 markdown 文件”。

而是它代表了 Agent 使用方式的一种升级：

从一次性对话

变成可复用流程

从聊天记录

变成程序化记忆

从人工重复解释

变成自动提案沉淀

从经验散落

变成 Skill 库

这和普通 prompt 模板不一样。

prompt 模板通常是静态的。

而 Skill Factory 的方向是从真实工作流里提炼模板。

也就是说，你不是先拍脑袋写 SOP。

你是先真实做事，然后让系统帮你发现：

哪些流程值得固化。

这很符合 AI Agent 未来的发展方向。

Agent 不能只会执行。

它还得能把执行过程变成经验。

经验再变成 skill。

skill 再反过来提升下一次执行。

这才是复利。

所以我会把 hermes-skill-factory 看成一个很有启发性的 Hermes 生态项目：

它不是帮你多做一次事，而是帮你把“做事的方法”留下来。
