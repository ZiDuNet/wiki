---
tags: [GPT-5.5, Claude, PPT, Prompt, OpenAI]
source: "AI的岔路口"
created: 2026-04-29
updated: 2026-05-10
category: GPT-5.5
---

# AI 做 PPT，别再一次性生成了

> 来源: [AI的岔路口](https://mp.weixin.qq.com/s?__biz=MzI5NTg2OTk2Ng==&mid=2247485446&idx=1&sn=ea7890e47b0b99043faa58803021b66f&chksm=ed7145587f81dbe1d41fd5ae3b43da62876e00ea6611ddc5e075d7131617d947de362d755d76&mpshare=1&scene=1&srcid=042967ghLAdyjuud4RVATW0D&sharer_shareinfo=3086a3f874c546ce4b54ee8f3a7e2f2f&sharer_shareinfo_first=3086a3f874c546ce4b54ee8f3a7e2f2f) | 2026-04-29

## 摘要

我以前一直不太相信 OpenAI 模型能稳定做出漂亮的演示文稿。
原因很简单：它们经常把一页幻灯片塞得太满，文字、图表和装饰元素互相挤在一起。看上去很努力，但真拿去汇报，还是得人手工返工。
这次我换了一个流程：先让 GPT-5.5 只负责内容，再让 GPT Image 2 负责视觉设计。结果比我预期好很多。
关键不在某个神奇提示词，而在工作顺序。
先内容。
再设计。
在这次实验之前，我对几类工具的分工很明确。
NotebookLM 适合低风险场景。你上传材料，再给一段提示词，它能一次性做出一套演示文稿。但单页布局很难精细控制，后面虽然可以继续用提示词改，结果仍然有随机性。
Google Slides 更适合逐页处理。它能创建单页，也能增强单页，但很难一次性给你一整套打磨好的 deck。
Claude Cowork 是我过去几个月的主力。它能按照品牌色、字体和图片做出专业、干净的幻灯片，适合内部汇报和客户会议。限制也明显：设计通常偏简洁优雅，复杂视觉不太够，而且没有原生图像生成器。
ChatGPT 和 Codex 以前在这件事上最不稳定。常见问题就是布局拥挤、元素重叠、单页文字过多。
我...

## 相关实体

[[ChatGPT]], [[Claude]], [[GPT-5]], [[OpenAI]]

## 相关概念

[[数据可视化]]
