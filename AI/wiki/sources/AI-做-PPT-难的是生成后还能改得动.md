---
title: "AI 做 PPT 不难，难的是生成后还能改得动"
type: source-summary
created: 2026-05-25
updated: 2026-05-25
sources: ["AI 做 PPT 不难，难的是生成后还能改得动.md"]
tags: [PPT, AI生成, HTML, SVG, Claude, Design-System]
---

# AI 做 PPT 不难，难的是生成后还能改得动

## Summary

AI 生成 PPT 这件事已经不难，真正稀奇的难题是：生成之后能不能修改编辑和交付。SlideMind 的核心思路是放弃图片路线，改走 HTML+SVG，在设计系统约束下让 LLM 生成内容，最终通过双层映射（文字→原生文本框，SVG→截图保真）导出可编辑 PPTX。

## Key Claims

1. 核心判断：AI 生成的 PPT 如果只能看不能改，本质上是一张截图，不是一份交付物
2. 图片路线的本质是把质量押在模型单次生成效果上，随机性高、不可控；HTML+SVG 路线押在设计系统约束上
3. HTML+SVG 审美上限 80% 靠 CSS 和组件系统，20% 靠模型填内容
4. 四层约束体系：CSS 变量（6个）→ 布局类型（12种）→ 组件 class → SVG 图表（11种，硬规则）
5. 模板试跑机制（先跑2页锚点确认视觉方向，再批量展开）解决"直接批量生成风险高"问题
6. 五大工程坑：Playwright 截图 flaky、LLM 输出截断、推理模型 token 预算被吃完、Prompt 文件引用≠代码加载、HTTP Client 超时丢失
7. BroadcastChannel 实现演讲者模式和观众窗口像素级一致的翻页同步

## Entities Mentioned

- [[SlideMind]] — 作者做的 HTML+SVG PPT 生成工具
- [[html-ppt-skill]] — HTML PPT 生成 Skill 参考项目
- [[guizang-ppt-skill]] — 设计系统约束 PPT Skill 参考项目
- [[python-pptx]] — PPTX 文字元素处理的 Python 库
- [[Playwright]] — HTML 渲染截图工具

## Concepts

- [[HTML-SVG-PPT路线]] — 放弃图片生成，改用 HTML+SVG 结构化输出
- [[设计系统约束]] — CSS 变量/布局类型/组件 class 四层硬约束替代自由 prompt
- [[PPT-模板试跑]] — 先跑锚点页确认视觉方向再批量展开的机制
- [[AI-可编辑性]] — AI 输出的"最终成品"vs"协作中间态"的设计哲学区分
- [[BroadcastChannel]] — 浏览器窗口间消息同步协议

## Notable Quotes

> "AI 生成的 PPT，如果只能看、不能改，本质上是一张截图，不是一份交付物。"

> "自由生成负责惊艳，约束系统负责落地。"

> "Prompt 文件之间的'引用'只是人类可读的文档约定，代码必须显式拼接才能生效。"

> "当底层是 HTML 时，很多'传统 PPT 软件自带的能力'，你都可以用 Web 技术重新拿回来。"

## Limitations / Bias

- HTML+SVG 路线视觉上限依赖设计系统质量，设计系统建设需要前期投入
- 复杂 SVG 图表（架构图、服务器拓扑）需要较大 max_tokens（文中提到 3000-8000 token）
- 推理模型使用 reasoning 时，max_tokens 需设为预期输出长度的 4 倍
- 实测 8 页完整 pipeline 耗时 63 分钟（DeepSeek flash 模型），速度是当前瓶颈
