---
tags: [Hermes, Agent, GitHub, PPT, Prompt, API, Python, Skill]
source: "i龙虾"
created: 2026-05-02
updated: 2026-05-10
category: Hermes
---

# Hermes 开源了 ComfyUI Skill，以后出图、出视频直接说就行了

> 来源: [i龙虾](https://mp.weixin.qq.com/s?__biz=MzI3MTk5OTc3Ng==&mid=2247484534&idx=1&sn=9b455db401a84278a8f199bf0f697481&chksm=eae47c502c650aa5b7400baa89c310e85b208f0ce97daaea8c4f5cf687338f549d6a112e666f&mpshare=1&scene=1&srcid=0502iKLGlSNZGB0yie5mEQo5&sharer_shareinfo=ebb71da9bfc9e58f570b330689b945c1&sharer_shareinfo_first=ebb71da9bfc9e58f570b330689b945c1) | 2026-05-02

## 摘要

前两天 Nous Research 悄悄往 hermes-agent 仓库里塞了一个 ComfyUI Skill，ComfyUI 是生图、生视频的利器，堪称多媒体工作流中的“乐高”，但也正因如此，上手难度很高。而有了 ComfyUI Skill 之后，只需一句话就能在本地出图、出视频，更重要的是，还能用自然语言完成复杂的工作流。
Hermes 的 ComfyUI Skill 把 Agent 和 ComfyUI 之间的整个交互链路都封装好了。
**生命周期管理方面**，Agent 用 `comfy-cli` 负责 ComfyUI 的安装、启动、自定义节点管理。你不需要手动跑 `python main.py`，也不需要手动 `pip install` 缺失的节点依赖——说一声，Agent 搞定。
**执行层面**，Skill 直接走 ComfyUI 的 REST + WebSocket API，不是截图、不是 UI 操作，是真正的接口调用。工作流 JSON 加载进去，参数注入进去，生成结果拿出来。
**工作流管理方面**，你可以把任意复杂的工作流 JSON 导入进来，Skill 会自动解析...

## 相关实体

[[ComfyUI]], [[Hermes]], [[LoRA]], [[OpenClaw]], [[Python]]

## 相关概念

[[工作流自动化]]
