---
title: "OpenClaw 和 Hermes直接画CAD，一天2.5k Star — text-to-cad开源了"
type: source-summary
tags: ["text-to-cad", "OpenClaw", "Hermes", "CAD"]
sources: [OpenClaw 和 Hermes直接画CAD，一天2.5k Star — text-to-cad开源了.md]
created: 2026-05-17
updated: 2026-05-17
author: 量子智元
category: OpenClaw
---

# OpenClaw 和 Hermes直接画CAD，一天2.5k Star — text-to-cad开源了

> 📎 来源: 微信公众号 | 量子智元 | 2026-05-17

上个月我遇到一个挺尴尬的事。同事指着屏幕上一张零件截图问我："这个法兰盘，外径多少，孔位怎么分布的？"我张嘴比划了半天，最后打开SolidWorks重新画了一遍给他看。明明脑子里是完整的三维造型，传到另一个人那里就变成了一堆说不清的数字和手势。 设计协作的痛点从来不是"画不出来"，而是"讲不明白"。直到我试了 text-to-cad 这个项目——准确说，是它背后的那套逻辑，让我突然意识到一件事：我们可能一直搞错了方向。AI辅助设计的终点不是"帮人画得更快"，而是让机器能像读代码一样读懂几何。 大多数人对AI做CAD的想象是这样的：你描述一个零件，AI像Midjourney一样"生成"一张图出来。但 text-to-cad 不是这么做的。它的底层是 build123d 这个Python库加上OpenCASCADE几何内核。你给AI一句"生成一个100x60x20mm的矩形块，四角打M6通孔，顶部边缘倒角2mm"——AI不是在脑海里渲染一幅画面，而是在背后写了一串Python代码。...

## 涉及实体

[[OpenClaw]], [[text-to-cad]]

## 涉及概念

[[Text-to-CAD]], [[text-to-cad]]
