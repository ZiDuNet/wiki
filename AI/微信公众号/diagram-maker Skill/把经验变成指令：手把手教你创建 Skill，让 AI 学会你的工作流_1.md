> 📎 来源: [椰卷卷](https://mp.weixin.qq.com/s?__biz=MzI1ODQ1NTc3Mg==&mid=2247483991&idx=1&sn=fa997d3cbed0d844b3fd58ccd81f7113&chksm=ebf48c6e4887b89078e1af0b37e081961602c85e1c72696432c83f4c1eddbacda9c754c32c71&mpshare=1&scene=1&srcid=0529DMgrpOzxct1WqmAxkclY&sharer_shareinfo=949a76bb2ab7a518cdc7f3deb9744f47&sharer_shareinfo_first=949a76bb2ab7a518cdc7f3deb9744f47) | 时间: 2026-05-29 12:41

---

> `本篇将带你从零开始创建/蒸馏一个Skill，用于自动化重复性任务。`

> 阅读时间：约 5 分钟

在正式开始之前，有一个重要认知：**Skill 不是某个工具独有的概念**。

`无论你使用什么 AI 工具`

`（openclaw/ClaudeCode/Codex/Opencode）`

`都可以通过类似 Skill 的方式来封装重复性任务：`

`
`

`Skill 的本质：将如何做某件事的经验，封装成可复用的结构化指令。`

`
`

`所以，本教程的核心知识是通用的——学会之后，你可以迁移到任何支持自定义指令的 AI 工具中。`

`
`

> 下文以 **Claude Code** 为例进行演示，但原理适用于所有支持Skills的工具。

---

## 01Skill的核心价值

## 其实在Skill火到现在，无论是蒸馏还是自创，Skill本身的核心价值在于**将行业知识、业务逻辑与 AI 能力深度融合**，实现 “任务拆解 - 自主执行 - 结果闭环 - 自我进化” 的全流程提效。

## 例如以下是一些Skill常用场景：

| 类型 | 示例命令 | 用途 |
| --- | --- | --- |
| 内容生成 | `/写公众号` | 按固定格式生成内容 |
| 格式转换 | `/转Markdown、pdf` | 将其他格式转为Markdown、pdf |
| 质量检查 | `/检查项目信息一致性、准确性` | 自动检查常见问题 |
| 数据处理 | `/整理数据` | 按规则处理数据 |
| 代码辅助 | `/对接API文档` | 让agent通过API文档成功调用工具/模型/应用 |

## 02Skill 文件放在哪里？

对于ClaudeCode，Skill 文件有两种存放位置：

```
方式一：项目级 Skill（推荐）
```

```
方式二：用户级 Skill（全局）
```

```
对于其他Agent（openclaw/codex……），你需要去找到它们在你电脑路径的根目录，进行存放，例如：
```

```

```

```
Codex: '.codex/skills/'
```

```

```

## 03实战：用 Skill-creator 创建 Skill（蒸馏你的写作风格）

最高效的方式不是从零手写 Skill，而是**让 AI 帮你分析和封装**。`

下面来个狠活，教你来自动提炼你的公众号写作风格，并生成专属的写作 Skill

（belike：直接蒸馏我自己……）

#### Step 1: 用Skill-creator创建Skill

这里虽然是可以我们直接用和AI进行自然语言对话创建skill，但是我还是强烈推荐Anthropic官方推出的skill-creator进行skill创建（稳定、好用、强！）

**安装 Skill-Creator**

方法一：对话安装

告诉你的ClaudeCode，安装skill-creator

方法二：手动安装

从 GitHub下载：

https://github.com/anthropics/skills/tree/main/skills/skill-creator

将 skill-creator 文件夹复制到.claude/skills/目录下(或者你的AI Agent的skill文件夹中)

`
`

#### Step 2: 用Skill-creator创建Skill

现在，我们来实战演示：假设你想创建一个「模仿你公众号风格」的写作 Skill。

**操作步骤**：

1️⃣在ClaudeCode/skill-creator或直接描述需求

```
eg.我想创建一个椰卷卷风格的公众号写作skill
```

`
`

`2️⃣提供你的写作样本（给AI足够多的文章内容），然后说：`

```
我的过往公众号文章在：（提供你电脑的本地存放路径；
```

```
AI Agent会分析你的文章，提取：
```

- `你的开头套路（比如"先讲个故事..."）`
- `你的段落长度偏好（短句为主？长短结合？）`
- `你的过渡词习惯（"说白了...""换句话说..."）`
- `你的结尾方式（金句收尾？提问互动？）`

3️⃣自动生成 .claude/skills/skill-公众号写作助手.md

#### Step 3: 使用生成的 Skill

创建完成后，你只需要：

```
我想用椰卷卷公众号写作风格写一篇文章主题：
```

04进阶：优化生成的 Skill

```

```

自动生成的 Skill 可能效果不能一次达到你心中预期的效果，但你可以进一步优化：

`1️⃣手动添加参数支持`
`文章类型、语气风格、文章长度、写作重点`

```
# 公众号写作助手
```

```

```

```
2️⃣设定自动更新规则
```

```
# 公众号写作助手
```

```

```

```
好啦，教程就结束了，来创建你的第一个Skill吧！
```

```

```

---

```
📚 往期推荐超干货教程① Claude Code + CC Switch + Trae IDE 完整配置教程（小白也能看懂）② Claude Code + Obsidian 教程：让 AI 住进你的笔记里③  飞书OpenClaw配置经验：从安装到避坑④  告别命令行恐惧！用AI对话5分钟装软件，说人话就行
```

```
就喜欢说点不一样的① 我为什么越听播客越焦虑② 不是，那个天天挂在老板嘴边的小龙虾到底是什么③ 现在害怕【AI写作】，或许就像电脑时代害怕【复制粘贴】
```

```
J 人的自我管理
```

```
① 当我用Obsidian搭了人生管理系统
```
