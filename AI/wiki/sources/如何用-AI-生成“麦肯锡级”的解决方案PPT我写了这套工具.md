---
tags: [AI技术, PPT, Prompt, Skill]
source: "等等想一想"
created: 2026-05-01
updated: 2026-05-10
category: AI技术
---

# 如何用 AI 生成“麦肯锡级”的解决方案PPT？我写了这套工具

> 来源: [等等想一想](https://mp.weixin.qq.com/s?__biz=MzE5ODAxMTI0Mw==&mid=2247483785&idx=1&sn=166f2fc20e3e74a83778e9ecbc9297d9&chksm=97c3b377e83a65a33f7ccc3fc8afee03f9570a7231dd39a0778e8d72847267ba6fb1f1e00023&mpshare=1&scene=1&srcid=0501FVY3lkvKjmUjVzfHlBlM&sharer_shareinfo=15ce4315c6ea7f9fb24e6573b36c1f2b&sharer_shareinfo_first=15ce4315c6ea7f9fb24e6573b36c1f2b) | 2026-05-01

## 摘要

做售前方案的人，有一半的工作时间花在 PPT 上。
另一半花在改 PPT 上。
见过不少制造业数字化方案，里面真正能拿去见客户的，说实话，比例不高。不是说内容不行——内容往往是够的，但内容到了 PPT 里，就变形了。
去年我开始琢磨能不能用 AI 把这件事提效。不是觉得 AI 多神奇，纯粹是这件事太重复了，不应该每次都从头来。
【通过我这套AI工具生成的咨询风格解决方案 PPT】
最早我试过直接让 AI 生成 PPTX。
跑了十几次之后放弃了。
PPTX 本身是个很复杂的格式。你看到的一页幻灯片，底下是一堆 XML、坐标、图层关系。AI 直接写这东西，出来的结果"看着差不多"，但你一改就知道：文字其实是图片，图表其实是截图，表格里的数字改一个，格式就散了。
做售前的人都知道，方案 PPT 到了客户现场是要改的。客户会指着某页说"这个数据换成我们的"，销售会在最后一晚说"把第三页那段加到第五页"。如果你的 PPT 改不了，那它就是废纸。
所以后来我换了一条路：不直接生成 PPTX，先生成 HTML，再转。
HTML 和 CSS 至少是可读的。结构清楚，规则能写死，AI 输出的稳定性比直接...

## 相关实体

[[OpenClaw]]
[[html-ppt-skill]]

## 相关概念

[[PPT制作]]
[[PPT设计]]
[[Skill开发]]
