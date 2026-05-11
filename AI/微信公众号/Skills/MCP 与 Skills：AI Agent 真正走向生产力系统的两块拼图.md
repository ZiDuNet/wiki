> 📎 来源: [书声AI](https://mp.weixin.qq.com/s?__biz=MzYzODAyODk5Nw==&mid=2247483665&idx=1&sn=bb20978d4d6a5fbdef602c068684fbb2&chksm=f1973deeccd42077c79b62f4ce92ae0f4c7380caa517e1f13f3a3b313fca0f2d34c1faa3f2ce&mpshare=1&scene=1&srcid=0426i0lBvoItAtELkWlt13Rb&sharer_shareinfo=191a641e134fb38326ae80ae2ec2e361&sharer_shareinfo_first=191a641e134fb38326ae80ae2ec2e361) | 时间: 2026-04-26 18:58

---

# 过去一年，很多人谈 AI Agent，谈到最后都会落到一个问题上：

**大模型到底怎样才能真正“干活”？**

不是陪你聊天，不是写一段代码，不是回答一个知识问题，而是像一个可以接入真实世界的工作系统一样：能读文件、查数据库、调用 API、理解公司内部流程、遵守某种操作规范、按照稳定步骤完成任务，并且在不同工具、不同模型、不同客户端之间尽量可复用。

这里面有两个越来越重要的方向：

一个叫 **MCP，Model Context Protocol**。

另一个叫 **Agent Skills**，也可以简单理解为“给 Agent 打包技能”。

如果说过去的大模型主要是一个“会说话的大脑”，那么 MCP 和 Skills 解决的是两个更实际的问题：

**MCP 解决的是：Agent 怎么连接外部世界。**

**Skills 解决的是：Agent 怎么学会一套稳定的做事方法。**

这两个东西放在一起看，你会发现 AI Agent 的产品形态正在从“聊天框”变成一种新的软件架构。

---

## 一、为什么需要 MCP 和 Skills？

最早大家使用大模型，主要是直接在聊天框里输入问题：

“帮我写一个函数。”

“帮我总结这篇文章。”

“帮我翻译成英文。”

这种模式很强，但它有一个天然限制：**模型本身并不知道你的真实环境。**

它不知道你的文件在哪里，不知道你的数据库结构，不知道你的 Git 仓库状态，不知道你的公司内部 API，不知道某个任务应该遵守什么流程，也不知道这个任务完成后应该生成什么格式的结果。

所以后来出现了 tool calling。

你可以给模型提供一些工具，比如：

读取本地文件；

查询数据库；

调用天气 API；

执行 shell 命令；

操作浏览器；

创建日历事件；

发送邮件。

这一步让模型从“只会说”变成“可以做”。

但 tool calling 很快又遇到新的问题：

工具太多，怎么管理？

每个客户端都要重复接一遍工具吗？

工具的输入输出格式谁来规范？

一个工具更新了，客户端怎么知道？

远程工具和本地工具怎么统一？

权限、认证、生命周期、版本兼容怎么处理？

如果每个 AI 产品都自己发明一套工具协议，生态就会碎成一地。

这就是 MCP 出现的背景。

MCP 官方文档把它定义为一种围绕上下文交换的协议，它关注的是 AI 应用和外部上下文/能力之间如何通信，而不是规定 AI 应用怎样使用 LLM 或怎样管理上下文。MCP 的范围包括协议规范、不同语言 SDK、开发工具以及参考服务器实现。(Model Context Protocol[1])

也就是说，MCP 不是一个具体的 Agent 产品，而更像是 AI 时代的“连接协议”。

它想解决的是：

**外部能力如何以标准方式暴露给 AI 应用。**

而 Skills 解决的是另一个问题：

即使 Agent 有了工具，它也不一定知道“怎么正确使用”。

比如你给 Agent 一个 PDF 工具，它可能会提取文本、合并文件、填写表单。但在真实工作里，你通常需要的不只是“能调用工具”，而是：

处理 PDF 时先检查什么；

表格提取失败时怎么办；

生成结果时应该用什么命名规范；

遇到扫描件时是否需要 OCR；

公司内部文档应该怎么排版；

报告应该符合什么模板；

哪些命令允许执行，哪些不应该执行。

这就不是 MCP 的核心问题了。

这是“操作经验”和“流程知识”的问题。

Agent Skills 的官方介绍里说，Skills 是一种轻量、开放的格式，用于用专门知识和工作流扩展 AI Agent 的能力。一个 Skill 的核心就是一个包含 

```
SKILL.md
```

 的文件夹，里面至少有 metadata 和 instructions，也可以包含脚本、参考资料、模板和其他资源。(Agent Skills[2])

简单说：

**MCP 更像 USB-C 接口。**

**Skills 更像一本可执行的操作手册。**

一个负责连接，一个负责教会怎么做。

---

## 二、MCP 的核心：不是工具本身，而是工具协议

很多人第一次听 MCP，会以为它就是“让大模型调用工具”。

这个理解不算错，但太浅了。

MCP 真正重要的地方在于：它把“AI 应用”和“外部能力”之间的关系，抽象成一个标准的 client-server 架构。

在 MCP 架构里，有三个核心参与者：

**MCP Host**：AI 应用本身，比如 Claude Desktop、Claude Code、VS Code 这类宿主应用。

**MCP Client**：Host 内部用来连接某个 MCP Server 的组件。

**MCP Server**：提供上下文、工具、资源、提示词等能力的程序。

官方文档说明，MCP 采用 client-server 架构。一个 MCP Host 可以连接一个或多个 MCP Server；Host 会为每个 Server 创建一个 MCP Client，每个 Client 维护自己和对应 Server 的连接。(Model Context Protocol[3])

这个设计非常关键。

因为它意味着：

一个 AI 应用可以同时连接多个能力来源。

例如：

连接一个本地 filesystem MCP server，用来读写文件；

连接一个 GitHub MCP server，用来查 issue、PR、仓库内容；

连接一个 Sentry MCP server，用来分析错误日志；

连接一个数据库 MCP server，用来查询业务数据；

连接一个公司内部知识库 MCP server，用来读取文档。

从 Host 的视角看，这些能力不是零散的脚本，而是一组可以被发现、声明、调用、更新的标准化上下文服务。

这就是 MCP 的第一层价值：

**把外部能力从“硬编码插件”变成“可发现的服务”。**

---

## 三、MCP 的两层结构：Data Layer 和 Transport Layer

MCP 架构里有一个非常清晰的分层：

**Data Layer，数据层。**

**Transport Layer，传输层。**

官方文档说，MCP 由两层组成：数据层定义基于 JSON-RPC 的 client-server 通信协议，包括生命周期管理以及 tools、resources、prompts、notifications 等核心 primitives；传输层定义客户端和服务器之间的数据交换机制，包括连接建立、消息 framing 和授权等。(Model Context Protocol[4])

这个分层很像传统软件系统里的“协议语义”和“传输通道”分离。

数据层关心的是：

你要调用什么方法？

参数是什么？

返回结果是什么？

是否需要响应？

有哪些能力可以被发现？

初始化时如何协商能力？

传输层关心的是：

消息怎么送过去？

是本地进程通信，还是远程 HTTP？

认证怎么做？

连接如何建立？

是否支持流式返回？

MCP 当前支持两种主要传输机制：

一种是 **stdio transport**，用标准输入输出在本地进程之间通信，适合本地 MCP server。

另一种是 **Streamable HTTP transport**，通过 HTTP POST 发送 client-to-server 消息，也可以配合 Server-Sent Events 实现流式能力，适合远程 MCP server；官方文档还提到这种方式可以支持 bearer token、API key、自定义 header 等标准 HTTP 认证方式，并建议使用 OAuth 获取认证 token。(Model Context Protocol[5])

这背后的意义很大。

因为同一套数据层协议，可以跑在不同传输层之上。

你可以今天写一个本地 MCP server，通过 stdio 给 Claude Desktop 用；

明天把它改造成远程服务，通过 HTTP 给团队里的多个 AI 客户端用；

上层的工具发现、工具调用、资源读取语义可以尽量保持一致。

这就是协议的力量。

---

## 四、MCP 的核心 primitives：Tools、Resources、Prompts

理解 MCP，一定要理解 primitives。

MCP 不是只定义了 tool calling，它还定义了几类可以暴露给 AI 应用的核心能力。

官方文档把 server 可以暴露的核心 primitives 分为三类：

**Tools**：AI 应用可以调用的可执行函数，比如文件操作、API 调用、数据库查询。

**Resources**：给 AI 应用提供上下文的数据源，比如文件内容、数据库记录、API 响应。

**Prompts**：可复用的交互模板，比如系统提示词、few-shot examples。(Model Context Protocol[6])

这三个东西看起来简单，但它们对应的是 Agent 工作流里的三种不同需求。

Tools 是“行动能力”。

例如：

查天气；

创建 Jira ticket；

执行 SQL；

读取 Git diff；

调用部署 API；

向 Slack 发消息。

Resources 是“上下文能力”。

例如：

当前项目 README；

数据库 schema；

某个 issue 的完整讨论；

某个设计文档；

用户上传的文件；

某个服务的日志片段。

Prompts 是“交互模式能力”。

例如：

代码审查模板；

故障排查模板；

SQL 分析模板；

产品需求拆解模板；

客户支持回复模板。

一个成熟的 MCP server 不一定只暴露 tools。

它也可以同时暴露：

数据库查询工具；

数据库 schema resource；

SQL 编写示例 prompt。

这样 Agent 不只是“能查数据库”，而是更接近“知道该怎样和这个数据库工作”。

MCP 还规定了 discovery 机制。每类 primitive 都有对应的 list、get/read 或 call 之类方法。比如客户端可以先通过 

```
tools/list
```

 发现工具，再通过 

```
tools/call
```

 执行具体工具。官方文档也强调，这种设计允许工具列表是动态的。(Model Context Protocol[7])

这点很重要。

过去我们写 AI 工具调用，经常是启动时把 tools 写死：

```
[
```

但真实系统里，工具能力可能变化：

用户登录状态变了；

权限变了；

某个插件安装了；

某个服务不可用；

某个项目切换了；

当前目录不同，可用命令不同；

团队管理员禁用了某些操作。

MCP 的 list/discovery 机制，使工具能力可以被动态发现，而不是永远静态写死。

---

## 五、MCP 的生命周期：初始化、能力协商、工具发现、工具调用

MCP 不是“上来就调用工具”。

它是一个有生命周期的协议。

官方文档说明，MCP 是 stateful protocol，需要生命周期管理；生命周期管理的目的，是协商 client 和 server 双方支持的能力。初始化阶段会进行协议版本协商、能力发现以及身份信息交换。(Model Context Protocol[8])

典型过程大概是：

第一步，Client 向 Server 发送 

```
initialize
```

 请求。

这个请求里包含：

协议版本；

client 支持的能力；

client 信息，比如 name、version。

第二步，Server 返回自己的能力。

比如它支持 tools，支持 resources，是否支持 tools list changed notification。

第三步，Client 发送 initialized notification，表示初始化完成。

第四步，Client 可以发送 

```
tools/list
```

，获取当前 server 暴露的工具列表。

第五步，当 LLM 决定调用某个工具时，AI 应用拦截这个 tool call，把它路由到对应 MCP server，通过 

```
tools/call
```

 执行。

第六步，Server 返回结构化结果，AI 应用再把结果放回模型上下文里，让模型继续推理和回复。

官方文档里的例子显示，

```
tools/list
```

 响应中的每个 tool 会包含 

```
name
```

、

```
title
```

、

```
description
```

、

```
inputSchema
```

 等字段；其中 

```
inputSchema
```

 使用 JSON Schema 描述输入参数，方便类型校验和文档化。(Model Context Protocol[9])

这带来的好处是：

LLM 不需要凭空猜工具怎么用。

Host 可以把工具 schema 提供给模型。

模型生成工具调用参数后，客户端或服务端可以做验证。

工具返回结果后，也可以用结构化方式进入上下文。

更进一步，MCP 还支持 notifications。

比如当 server 的工具列表发生变化时，server 可以发送 

```
notifications/tools/list_changed
```

，客户端收到后重新请求 

```
tools/list
```

，更新自己的工具注册表。官方文档指出，通知不需要响应，因为它遵循 JSON-RPC 2.0 notification 语义；这可以避免客户端轮询，并保持能力列表的实时一致。(Model Context Protocol[10])

这说明 MCP 并不是一个简单的“函数调用包装器”。

它更像一个面向 Agent 的能力总线。

---

## 六、Skills 的核心：把经验打包成可复用目录

如果 MCP 解决了“Agent 怎么接工具”，那 Skills 解决的是“Agent 怎么获得稳定的操作方法”。

很多人低估了这一点。

因为在真实工作里，失败往往不是因为模型完全不能调用工具，而是因为它不知道：

什么时候该调用；

调用前要检查什么；

调用后要验证什么；

出错时怎么处理；

输出结果应符合什么格式；

这个团队有什么约定；

这个项目有哪些坑；

这个任务有哪些边界条件。

这类知识很难只靠工具 schema 表达。

工具 schema 只能告诉模型：

这个函数叫什么；

参数是什么；

返回什么。

但它很难表达：

“处理 PDF 前先检查是否是扫描件。”

“修改代码前先读 CONTRIBUTING.md。”

“生成 release note 时按我们团队固定格式。”

“合并 MR 前必须确认 pipeline 通过。”

“做英文 stand-up update 时使用简洁、礼貌、非夸张的语气。”

这正是 Skills 的价值。

Agent Skills 的官方规范规定，一个 skill 是一个目录，至少包含一个 

```
SKILL.md
```

 文件；目录里也可以包含 

```
scripts/
```

、

```
references/
```

、

```
assets/
```

 等可选目录。(Agent Skills[11])

典型结构是：

```
my-skill/
```

其中 

```
SKILL.md
```

 是核心。

它包含两部分：

第一部分是 YAML frontmatter，用来描述 metadata。

第二部分是 Markdown body，用来写具体操作指令。

规范要求 

```
SKILL.md
```

 必须包含 YAML frontmatter，然后跟 Markdown 内容。frontmatter 中 

```
name
```

 和 

```
description
```

 是必填字段，

```
license
```

、

```
compatibility
```

、

```
metadata
```

、

```
allowed-tools
```

 是可选字段；其中 

```
allowed-tools
```

 目前还是实验性字段。(Agent Skills[12])

一个最小 Skill 可以长这样：

```
---
```

这不是一个 API。

这更像是给 Agent 的“任务说明书”。

但它比普通 prompt 更强，因为它是：

文件化的；

可版本控制的；

可分发的；

可复用的；

可被 Agent 按需加载的；

可以绑定脚本、模板、参考资料。

这使它从“提示词片段”升级成了一种工程化资产。

---

## 七、Skills 的 progressive disclosure：控制上下文成本

Agent Skills 里最关键的设计之一，是 progressive disclosure。

官方文档说明，Agent 会渐进式加载 Skills：启动时只加载每个 Skill 的 

```
name
```

 和 

```
description
```

，用于判断是否相关；当任务匹配某个 Skill 的描述时，才把完整 

```
SKILL.md
```

 指令读入上下文；执行时再按需运行脚本或加载引用文件。这样可以在保留大量技能的同时，只占用很小的上下文空间。(Agent Skills[13])

这个设计非常现实。

因为大模型上下文不是无限的。

如果你有 100 个 skills，每个 skill 都有几千字说明，启动时全部塞给模型，马上就会产生几个问题：

上下文爆炸；

模型注意力分散；

成本上升；

延迟变高；

无关规则互相干扰；

真正重要的任务指令反而被淹没。

Progressive disclosure 的思路是：

先让模型知道“有哪些技能”。

但不立刻加载全部细节。

只有当任务触发某个 skill 时，再读取具体说明。

这类似于人类工作中的“目录 + 手册”模式。

你不需要把公司所有 SOP 都背下来。

你只需要知道：

有一个“发版流程 SOP”；

有一个“客户故障排查 SOP”；

有一个“微信公众号排版规范”；

有一个“PDF 处理规范”。

当任务真的发生时，再打开那份文档。

Agent Skills 把这个模式标准化了。

官方规范还建议，完整 

```
SKILL.md
```

 body 在 Skill 被激活后才加载；较长内容应拆分到 referenced files 里，并且建议主 

```
SKILL.md
```

 保持在 500 行以内。(Agent Skills[14])

这对工程化 Agent 非常重要。

因为 Agent 的能力不是靠一个超级长的 system prompt 堆出来的。

真正可维护的方式是：

把知识拆成多个技能；

每个技能只负责一个清晰任务；

技能描述写得足够具体，方便 Agent 判断何时使用；

详细资料放 references；

可执行逻辑放 scripts；

模板和样例放 assets。

这才像一个可以长期维护的 Agent 能力库。

---

## 八、MCP 与 Skills 的区别：一个是“连接器”，一个是“方法论”

现在我们可以清晰地区分 MCP 和 Skills。

MCP 是协议层。

它关心：

Client 怎么连接 Server；

Server 怎么声明能力；

工具怎么被发现；

工具怎么被调用；

资源怎么被读取；

提示词怎么被获取；

通知怎么发送；

本地和远程传输怎么统一；

认证和生命周期怎么处理。

Skills 是知识封装层。

它关心：

Agent 在某类任务里应该怎么做；

有哪些步骤；

有哪些边界情况；

有哪些参考资料；

有哪些脚本可以辅助；

输出格式是什么；

什么工具可以预先批准；

什么时候应该加载更多资料。

所以 MCP 和 Skills 不是竞争关系。

它们更像上下两层。

举个例子：

你要做一个“公司内部 release assistant”。

MCP 层可以提供：

GitLab MCP server：读取 MR、pipeline、commit、issue；

Slack MCP server：读取发布讨论、发送通知；

Jira MCP server：读取 ticket 状态；

内部文档 MCP server：读取 release checklist；

CI/CD MCP server：触发构建或查询结果。

Skills 层可以提供：

```
release-note-writing
```

：告诉 Agent 怎么写 release note；

```
merge-request-review
```

：告诉 Agent 合并前检查哪些条件；

```
standup-update
```

：告诉 Agent 怎么写内部进展更新；

```
customer-facing-announcement
```

：告诉 Agent 如何写面向客户的版本说明；

```
incident-summary
```

：告诉 Agent 如何总结故障和修复过程。

MCP 提供外部世界的接口。

Skills 提供做事的章法。

没有 MCP，Agent 只能靠用户复制粘贴信息，无法稳定接入真实系统。

没有 Skills，Agent 即使接入真实系统，也可能做事风格混乱、流程不稳定、结果不可审计。

二者结合，才更接近真正的生产力 Agent。

---

## 九、为什么 Skills 可能比你想象得更重要？

很多开发者天然更关注 MCP，因为 MCP 更“技术”。

协议、JSON-RPC、Server、Client、Transport、OAuth、Tool Schema，这些都很工程化。

Skills 看起来像“写 Markdown”。

但越接近真实生产场景，你越会发现：

**Agent 的核心竞争力，不只是能调用多少工具，而是能不能稳定复现高质量工作流。**

举个简单例子。

你让 Agent “帮我处理一个 PDF”。

只给它 PDF 工具，它可能会做出一个能用但不稳定的结果。

但如果你有一个 PDF skill，里面写清楚：

先判断 PDF 是文本型还是扫描型；

文本型优先直接提取；

扫描型再考虑 OCR；

遇到表格时输出 CSV 和 Markdown 两版；

处理合同类文档时保留页码引用；

生成摘要时不要丢失金额、日期、责任主体；

最终结果要包括“发现的问题”和“无法确认的内容”。

这时 Agent 的行为会稳定很多。

再比如代码审查。

只给 Agent Git 工具和文件读取工具，它可以 review。

但如果你有一个 code-review skill，规定：

先看变更范围；

再看测试覆盖；

再看错误处理；

再看性能影响；

再看安全边界；

最后按 blocking / non-blocking / suggestion 分类输出。

这就不只是“调用工具”，而是“复用专家经验”。

这也是为什么 Skills 适合沉淀团队知识。

对于个人开发者，它可以沉淀自己的工作习惯。

对于公司，它可以沉淀内部 SOP。

对于开源项目，它可以沉淀贡献流程。

对于咨询公司，它可以沉淀交付方法论。

对于垂直产品，它可以沉淀行业经验。

未来很多 Agent 产品的护城河，可能不在于“我接了多少 API”，而在于：

**我沉淀了多少高质量、可复用、可执行的 Skills。**

---

## 十、一个更具体的架构想象：MCP + Skills + LLM Pool

如果我们从产品架构角度看，一个比较合理的 Agent 系统可以分成几层：

最底层是外部系统：

文件系统；

数据库；

GitLab/GitHub；

Slack/飞书/钉钉；

浏览器；

内部 API；

云服务；

知识库；

CI/CD；

业务系统。

再上一层是 MCP Servers。

每个 MCP Server 负责把某类外部系统以标准方式暴露出来：

filesystem server；

git server；

database server；

browser automation server；

company-docs server；

monitoring server；

ticketing server。

再上一层是 Agent Runtime。

它负责：

管理 MCP Client 连接；

执行 initialize；

做 capability negotiation；

维护 tool registry；

把 LLM 的 tool call 路由到正确 server；

接收 tool result；

处理 notifications；

管理权限和审计。

再上一层是 Skills Registry。

它负责：

存放不同 skills；

根据 name 和 description 做技能发现；

按需加载 SKILL.md；

按需读取 references；

按需执行 scripts；

管理版本；

管理团队共享技能。

再上一层是 LLM Pool。

不同任务可以选择不同模型：

便宜模型做分类和初筛；

强模型做复杂规划；

代码模型做实现；

长上下文模型做文档分析；

本地模型做隐私敏感任务；

海外 API 模型做高质量英文输出。

最上层才是用户界面：

聊天界面；

IDE 插件；

桌面应用；

企业内部工作台；

命令行工具；

自动化任务系统。

这样一看，MCP 和 Skills 都不是孤立概念。

它们分别占据 Agent 系统里的两个关键位置：

MCP 是能力接入层。

Skills 是能力组织层。

LLM 是推理与决策层。

Agent Runtime 是调度层。

UI 是交互层。

这套结构一旦成型，AI Agent 就不再是一个“prompt 工程玩具”，而更像一种新的应用运行时。

---

## 十一、MCP 和 Skills 对开发者意味着什么？

对开发者来说，这两个方向会带来几个变化。

第一，未来很多工具不再只是提供 REST API，而是可能同时提供 MCP Server。

就像过去一个 SaaS 产品会提供 API、SDK、Webhook。

未来它可能还会提供：

“Install our MCP server, then your AI agent can use our product.”

这会成为 AI-native 产品的重要入口。

第二，内部工具会更容易被 Agent 使用。

很多公司内部系统没有必要做完整 UI，也没有必要给每个 AI 客户端单独写插件。

只要把关键能力包装成 MCP Server，多个 Agent 客户端都可以接入。

第三，Prompt 会从零散文本变成工程资产。

过去团队内部可能有很多提示词：

写日报的 prompt；

写 PRD 的 prompt；

做代码 review 的 prompt；

做客户回复的 prompt；

做数据分析的 prompt。

但它们往往散落在 Notion、飞书文档、聊天记录里。

Skills 把它们变成一个标准目录，可以放进 Git，可以 review，可以版本管理，可以测试，可以随着团队流程演化。

第四，Agent 产品的竞争会从“模型能力”转向“系统能力”。

当所有人都能调用强模型时，差异化就会来自：

谁能接入更多真实系统；

谁的权限控制更好；

谁的工作流更稳定；

谁的 Skills 更专业；

谁能把工具、知识、流程、审计整合起来。

这对独立开发者也是机会。

你不一定要训练模型。

你可以做：

某个垂直领域 MCP Server；

某类高质量 Skills 包；

某个 Agent Runtime；

某个企业内部 Agent 平台；

某个开源项目的 AI 助手；

某个 SaaS 的 MCP 接入层。

AI 时代的软件创业，不一定是“重新做一个 ChatGPT”。

更现实的机会是：

**把已有软件世界变成 Agent 可操作的世界。**

---

## 十二、MCP 和 Skills 的风险：别把 Agent 变成失控的自动化脚本

当然，MCP 和 Skills 也不是银弹。

MCP 让 Agent 更容易调用外部能力，这也意味着风险变大。

如果 Agent 可以读文件、写文件、调用 API、执行命令、操作数据库，那么权限边界必须非常清晰。

哪些工具只读？

哪些工具可写？

哪些操作需要用户确认？

哪些环境禁止执行？

远程 MCP Server 如何认证？

token 如何保存？

日志如何审计？

工具返回的数据是否会泄露给模型？

这些都是生产环境绕不开的问题。

Skills 也有类似问题。

一个 Skill 本质上是给 Agent 的指令包。

如果 Skill 里包含不安全的步骤，Agent 可能会忠实执行。

如果 Skill 允许某些脚本执行，但脚本没有处理边界情况，也可能造成错误。

如果 Skill 的 description 写得太宽泛，Agent 可能在不该使用的时候激活它。

如果多个 Skills 之间规则冲突，Agent 的行为可能变得不可预测。

所以 MCP 和 Skills 的落地，需要配套：

权限模型；

沙箱；

审批机制；

日志审计；

版本控制；

测试评估；

失败回滚；

最小权限原则；

人类确认节点。

尤其是企业场景，不能因为“Agent 很聪明”就跳过传统工程里的安全治理。

越是强大的 Agent，越需要明确边界。

---

## 十三、一个判断：Agent 的未来不是“一个超级助手”，而是“一套可组合系统”

我认为 MCP 和 Skills 共同指向一个趋势：

**AI Agent 的未来，不是一个无所不能的超级聊天机器人，而是一套可组合的软件系统。**

这个系统里：

模型负责理解、规划、生成、选择；

MCP 负责连接外部能力；

Skills 负责沉淀工作方法；

Runtime 负责调度和执行；

权限系统负责边界；

日志系统负责可审计；

评估系统负责质量控制；

人类负责目标设定和关键决策。

这和传统软件最大的区别在于：

传统软件的流程大多是开发者提前写死的。

Agent 系统的流程则是由模型在运行时根据上下文动态组装的。

但这种“动态”不能是混乱的。

它需要协议化的工具接入，也需要工程化的技能沉淀。

MCP 和 Skills，一个偏底层协议，一个偏上层工作流，正好构成了 Agent 工程化的两块拼图。

MCP 让 Agent 有手有脚。

Skills 让 Agent 有经验、有规矩、有章法。

---

## 结语：真正的 Agent 不是会聊天，而是会接入、会执行、会复用经验

过去我们评价大模型，常常问：

它聪不聪明？

会不会写代码？

回答准不准？

上下文多长？

但如果从生产力角度看，未来更重要的问题会变成：

它能不能接入我的真实系统？

它能不能理解我的工作流程？

它能不能安全地调用工具？

它能不能稳定复现专家经验？

它能不能在团队之间共享能力？

它能不能被版本管理、测试和审计？

MCP 和 Skills 的意义就在这里。

MCP 把“外部能力”协议化。

Skills 把“操作经验”文件化。

两者结合，Agent 才可能从“一个聪明的聊天窗口”，变成“一个可维护、可扩展、可治理的生产力系统”。

这也是我认为接下来开发者值得重点关注的方向：

不是只学怎么写 prompt。

也不是只学怎么调 API。

而是要理解：

**如何为 Agent 构建工具协议，如何为 Agent 沉淀技能系统，如何让 AI 真正进入软件工程和企业流程。**

真正的 AI Agent，不是一个更会说话的机器人。

它更像一个新型操作系统上的进程：

能感知上下文，能调用工具，能加载技能，能执行任务，也能被约束、被观察、被改进。

而 MCP 和 Skills，就是这个新型 Agent 操作系统里最值得关注的两个基础模块。
