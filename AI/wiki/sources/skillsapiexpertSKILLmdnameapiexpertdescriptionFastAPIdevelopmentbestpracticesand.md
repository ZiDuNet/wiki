---
tags: [Skills, Agent, Claude, GitHub, Prompt, API, Python, Skill]
source: "悟鸣AI"
created: 2026-05-07
updated: 2026-05-10
category: Skills
---

# skills/api-expert/SKILL.md---name:api-expertdescription:FastAPIdevelopmentbestpracticesandconventions.Usewhenbuilding,reviewing,ordebuggingFastAPIapplications,RESTAPIs,orPydanticmodels.metadata:pattern:tool-wrapperdomain:fastapi---YouareanexpertinFastAPIdevelopment.Applytheseconventionstotheuser'scodeorquestion.## Core ConventionsLoad'references/conventions.md'forthecompletelistofFastAPIbestpractices.## When Reviewing Code1.Loadtheconventionsreference2.Checktheuser'scodeagainsteachconvention3.Foreachviolation,citethespecificruleandsuggestthefix## When Writing Code1.Loadtheconventionsreference2.Followeveryconventionexactly3.Addtypeannotationstoallfunctionsignatures4.UseAnnotatedstylefordependencyinjection

> 来源: [悟鸣AI](https://mp.weixin.qq.com/s?__biz=Mzg3NzI0MzAyNA==&mid=2247492815&idx=1&sn=0dccd0f6f990aadf43d069d167ca4ca9&chksm=cec241841eb3dbd43c5852d2bd3c8f2b1e34d0e066bfa6dcfb7903c9686e94eccd298be9fa88&mpshare=1&scene=1&srcid=050719D3n1igJxej3p3dI9qe&sharer_shareinfo=da5d4f729330c2c81828d40a3cba3c76&sharer_shareinfo_first=da5d4f729330c2c81828d40a3cba3c76) | 2026-05-07

## 摘要

大家好，我是悟鸣。
写
的时候，很多人会卡在格式上：YAML 怎么写、目录怎么建、规范怎么跟。但其实 30 多个 agent 工具（Claude Code、Gemini CLI、Cursor……）都已经统一了布局，格式这事基本不用操心了。
真正头疼的，是内容怎么设计。
规范只告诉你 skill 怎么打包，但里面的逻辑怎么组织？完全没说。一个封装 FastAPI 规范的 skill，跟一个四步文档流水线，运行逻辑差了十万八千里，但
文件看起来一模一样。
看完整个生态圈，从 Anthropic 的仓库到 Vercel 和 Google 的内部指南，发现大家都在用这 **5 种设计模式**。
下面一个个展开，每种都附了可运行的 ADK 代码：
- **Tool Wrapper**：让 agent 瞬间成为任何库的专家
- **Generator**：按模板产出结构化文档
- **Reviewer**：按严重程度给代码打分
- **Inversion**：agent 先采访你，再动手
- **Pipeline**：带检查点的多步工作流
Tool Wrapper 的作用很简单：让你的 agent...

## 相关实体

[[Anthropic]], [[Claude-Code]], [[Claude]], [[Cursor]], [[Gemini]], [[GitHub]], [[Python]], [[Vercel]]

## 相关概念

[[代码审查]], [[设计模式]]
