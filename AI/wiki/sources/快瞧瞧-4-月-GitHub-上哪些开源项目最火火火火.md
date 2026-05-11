---
tags: [GitHub, Agent, Claude, 飞书, PPT, Prompt, API, Python]
source: "逛逛GitHub"
created: 2026-05-02
updated: 2026-05-10
category: GitHub
---

# 快瞧瞧 4 月 GitHub 上哪些开源项目最火火火火？

> 来源: [逛逛GitHub](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247533406&idx=1&sn=5cf3e7d5020d2d474cde1a8c35fb127a&chksm=f8ae92a3872170d99bc6a53ab2e1ca934ab25c6db5abd7c3d2798c667c8f3039c5f66fe86909&mpshare=1&scene=1&srcid=0502UpEAVwQEjfW7MqPEzWKQ&sharer_shareinfo=5e2d88838308073459f8d18976993f9e&sharer_shareinfo_first=5e2d88838308073459f8d18976993f9e) | 2026-05-02

## 摘要

01
**一个 Rust 写的省 token 神器**
如果你平时用 Claude Code，可能没注意到一个事情：每次执行 git status、npm test 这些命令的时候，AI 工具会把所有输出都塞进上下文窗口。
一次 git status 就能吃掉约 2000 个 token，跑一次测试更是上万。
这些冗余输出挤占了模型的推理空间，上下文窗口过早溢出，API 费用也跟着涨。
RTK 就是专门解决这个问题的。
它是一个用 Rust 写的 CLI 代理工具，拦截并压缩这些命令的输出，平均压缩率能达到 80-90%。
支持超过 100 种命令的智能过滤，覆盖 git、测试框架、构建工具、Docker、AWS 等场景。
它的原理是通过 Hook 机制自动改写命令，比如把 git status 变成 rtk git status，对 AI 来说完全透明，你什么都不用改。
单个二进制文件，零依赖，开销低于 10ms，已经支持 Claude Code、Cursor、Gemini CLI、Codex 等 12 种 AI 工具。
对于重度使用 AI Coding 工具的开发者来说，这个工具能...

## 相关实体

[[Claude-Code]], [[Claude]], [[Cursor]], [[Docker]], [[Excel]], [[Gemini]], [[GitHub]], [[Hermes]], [[Llama]], [[Markdown]], [[OpenAI]], [[Python]], [[Qwen]], [[微信]], [[钉钉]], [[飞书]]

## 相关概念

[[AI-Agent]], [[CICD]], [[Function-Calling]], [[代码审查]], [[代码生成]], [[多模态]], [[自进化系统]], [[记忆系统]]
