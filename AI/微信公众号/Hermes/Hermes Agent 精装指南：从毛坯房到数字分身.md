> 📎 来源: [kingram](https://mp.weixin.qq.com/s?__biz=MzU3OTc2NzMyMQ==&mid=2247484485&idx=1&sn=7df8d0de1555b356db43624be9ff2af0&chksm=fc00000ab337ebf6ba6918c9538c7944925bf5e26a8a37062133c5e70c4c428c4b64625bc3d7&mpshare=1&scene=1&srcid=0429EME9NEQAixNG03HyjVNL&sharer_shareinfo=e19195344b45b78f44fb9a8ce915014a&sharer_shareinfo_first=e19195344b45b78f44fb9a8ce915014a) | 时间: 2026-04-29 03:28

---

# Hermes Agent 精装指南：从毛坯房到数字分身

> **工欲善其事，必先利其器。** 很多人低估了 Hermes，不是因为它不强，而是因为大多数人用到的，只是**毛坯版**。

---

## 一个残酷的真相

**毛坯版 Hermes** = 一个聪明的临时工，干完活就忘，下次重来。

**精装版 Hermes** = 一个有记忆、有工具、有感官、还能持续进化的**数字分身**。

两者的差距，不是 prompt 写得好不好，而是你有没有把它从一个聊天模型，真正配置成一个 **Agent**。

---

## 第一步：先告诉它"你是谁"

很多人一上来就想装搜索、装抓取、装语音。

**顺序反了。**

Agent 最先要补的不是工具，是**身份**。

没有身份，它每次都像临时工。没有长期记忆，它每次都像金鱼。

### 怎么做：写 SOUL.md

本质上是在定义：

- 你是谁
- 你的风格是什么
- 你的工作方法是什么
- 你希望 Agent 以什么角色协助你

### 捷径：agency-agents-zh

不想从零写？直接用现成模板库：

**GitHub：** https://github.com/jnMetaCode/agency-agents-zh[1]

里面有大量中文角色模板，覆盖：

- 工程、设计、营销
- 产品、游戏、安全
- 金融、HR 等多个部门

**它的价值不只是人设。** 很多角色里已经包含了：

- 专业流程
- 任务结构
- 输出格式
- 可交付成果

**你是在给 Hermes 装一个职业脑子。**

---

## 第二步：把默认 MEMORY 换成 Hindsight

这一步，是 Hermes 从"能用"到"好用"的关键。

默认 MEMORY.md 的问题不是没有记忆，而是记忆方式太轻了——更像偶尔记一笔，不是持续建档。

### Hindsight 的价值

如果按官方向导接入 Hindsight，它会自动从对话里提取：

- 实体
- 事实
- 关系
- 时间戳

然后**建立知识图谱**，并且在每次调用模型前，把相关记忆**自动注入 system prompt**。

这才是真正意义上的**长期记忆系统**。

### 配置步骤

```
1. 运行：hermes memory setup2. 选择 Hindsight3. 控制台注册并生成 API Key：   https://ui.hindsight.vectorize.io/connect4. 验证：hermes memory status
```

配置成功后，你能看到：

- Hindsight 已激活
- bank\_id
- auto-recall
- auto-retain 等状态

---

## 第三步：让它真正"读懂"互联网

很多人以为 AI 上网能力就是搜索。

**搜索只负责"找到"。**

真正好用的 Agent 还要能：

- 抓网页
- 读文档
- 过反爬
- 做批量提取
- 模拟浏览器行为

这部分你可以理解成**给 Hermes 装眼睛**。

### 推荐工具链

| 工具 | 适用场景 |
| --- | --- |
| **Jina Reader** | 单页抓取，轻量直接够快 |
| **Crawl4 AI** | 批量深度抓取，网站级信息抽取 |
| **Scrapling** | 复杂页面、反爬场景 |
| **CamoFox** | 隐身浏览器，模拟真实用户行为 |

> CamoFox 和 Scrapling 比较贴近 Hermes 工具链思路。Jina Reader 和 Crawl4 AI 可通过 Skill 或自定义调用集成。

这一步补完，**Hermes 开始真的会"读"**。

---

## 第四步：从聊天工具变成研究工具

如果说抓取解决的是"看见"，那搜索和文档处理解决的就是：

**怎么快速把信息变成可用材料。**

### 推荐组合

| 工具 | 作用 |
| --- | --- |
| **Tavily** | AI 工作流的主力搜索 |
| **DuckDuckGo** | 兜底搜索，零成本简单稳 |
| **Pandoc** | 格式转换神器，文档工作流必备 |
| **Marker** | PDF 转 Markdown 增强，喂给 Agent 时体验好很多 |

**这套装好之后：**

- 搜索更稳
- 文档可读性更强
- 格式转换更顺
- PDF 处理不再痛苦

**意义在于：** 它不只是帮你找资料，是在帮你把资料变成模型能真正吃进去的东西。

---

## 第五步：让它不只会"打字"

很多人低估了表达能力工具链。

一个真正完整的 Agent，不该只会输出文字。它还应该能：

**听、说、画**

### 推荐工具

| 工具 | 能力 |
| --- | --- |
| **Whisper** | 语音识别，多语言支持很强 |
| **Edge TTS** | 语音合成，低成本 TTS |
| **Fal.ai** | 图像生成入口 |
| **FLUX Skill** | 高质量出图 |

这一步装完，Hermes 就不再只是一个聊天窗口。

而是开始具备**多模态表达能力**：

- 听语音做整理
- 把文字转成音频
- 生成配图
- 直接做内容生产链路

**对内容创作者尤其有用。**

---

## 第六步：效率与成本控制

Hermes 最大的问题之一，不是模型不够强，而是**成本控制和上下文管理**。

Agent 一旦频繁调工具、跑终端、读长文档，Token 很容易失控。

这部分不是锦上添花，而是**决定你能不能长期用下去**。

### 1. Tokscale：看清 Token 花到哪了

想知道：

- 总共用了多少 Token
- Hermes 用了多少
- 哪个模型最贵
- 近 7 天趋势

Tokscale 让你第一次真正看见，Token 到底是怎么被吃掉的。

### 2. hermes-hudui：Web UI 级别的成本拆解

想看得更细？按**模型、组件、技能、会话、工具调用**来拆解 Token 成本。

```
git clone https://github.com/joeynyc/hermes-hudui.gitcd hermes-hudui./install.shhermes-hudui# 浏览器打开：http://localhost:xxxx
```

**它不是看用了多少，而是看浪费在哪。**

### 3. RTK：终端输出压缩器

如果你经常让 Hermes 跑：

```
lsgit statusgit diffcargo test
```

你会很快发现，**终端输出是 Token 黑洞**。

RTK 的思路很简单：**不是减少动作，而是减少无效输出。**

```
# 安装brew install rtk# 或curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh# 初始化rtk init -g# 常用命令rtk ls .rtk git statusrtk git diffrtk cargo testrtk read http://main.rsrtk gain --graph
```

### 4. Hermes-agent-self-evolution：让它自己优化自己

**进阶玩法。** 核心不是装更多功能，而是让 Hermes 通过自动化方法，持续优化自己的：

- System Prompt
- Skill
- 工具描述
- 行为策略

**项目地址：** https://github.com/NousResearch/hermes-agent-self-evolution[2]

这类工具更适合已经把 Hermes 用熟的人，因为它解决的是：**Hermes 怎么越用越强。**

### 5. Skill 扩展：别自己重复造轮子

Hermes 真正的上限，很多时候在生态。

如果你愿意把 Skill 体系接起来，很多场景根本不用从零造：

- 跨平台自动化
- 内容处理
- 工作流增强

**这一步本质上是在把一个 Agent，变成一个平台。**

---

## 最后一步：配一个资源总入口

很多人装了一堆东西，最后反而更乱。

**工具多 ≠ 生态清晰**

给 Hermes 配一个资源总入口：

- **awesome-hermes-agent** — 资源目录
- **hermes-ecosystem** — 能力地图

它们是让你知道：

- 生态里到底有什么
- 哪些值得装
- 哪些只是看起来很热闹

---

## 写在最后

很多人以为 Hermes 的差别，只是会不会调 prompt。

**真正拉开差距的，不是对话技巧。**

是你有没有把它从一个聊天模型，真正配置成一个 Agent。

|  | 毛坯版 Hermes | 精装版 Hermes |
| --- | --- | --- |
| 记忆 | 金鱼，干完就忘 | 知识图谱，自动召回 |
| 上网 | 只会搜索 | 会抓、会读、会过反爬 |
| 表达 | 只会打字 | 能听、能说、能画 |
| 成本 | Token 黑洞 | 可控、可视、可优化 |
| 进化 | 一成不变 | 自我迭代，越用越强 |

**毛坯版 Hermes，更像一个新生儿。****精装版 Hermes，才开始像一个真正能长期协作的数字搭子。**

所以这不叫优化。

这是**知识库的切换**。

---

*如果这篇对你有启发，欢迎转发给还在用"毛坯房"的朋友。*

*精装一下，你会发现新世界。*

### 引用链接

[1]*https://github.com/jnMetaCode/agency-agents-zh*

[2]*https://github.com/NousResearch/hermes-agent-self-evolution*
