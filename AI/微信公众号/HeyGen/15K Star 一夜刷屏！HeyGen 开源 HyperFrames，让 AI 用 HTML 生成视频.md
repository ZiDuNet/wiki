> 📎 来源: [MinimaxClaw](https://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg1Nw==&mid=2247484042&idx=1&sn=7ff6ad8200d8eebe90bbe07cec102f04&chksm=a72bac0aa5f71b740c6adb0f319c4f41c5ccb906632ddb8eace4849db962b4fc3ab170c0dee4&mpshare=1&scene=1&srcid=0520YbnUHKFepKA4liyXQBDq&sharer_shareinfo=6c3fae90a423dc04938f1d7e140acfee&sharer_shareinfo_first=6c3fae90a423dc04938f1d7e140acfee) | 时间: 2026-05-20 04:23

---

发现一个项目突然狂揽 1.5 万 Star。点进去一看，是 HeyGen 开源的视频渲染框架，名字叫 HyperFrames。它做的事一句话就能说清楚：写 HTML 代码，直接出视频。而且它从设计第一天起，就是给 AI 智能体用的，不是给人用手拖拽的那种剪辑工具。

这思路有点意思。我一晚上没睡，把它文档翻了一遍。

# 01

**HyperFrames 是干嘛的**

HyperFrames 是一个视频渲染引擎。你把网页动画写好，它能一帧一帧地给你渲成 MP4。

它和 After Effects 这类工具最大的区别是：HyperFrames 的“项目文件”就是一份 HTML。你用 HTML 搭画面，用 Tailwind CSS 控制样式，用 GSAP、Lottie、Three.js 这些库做动画，然后一行命令渲染。整个过程不需要 GUI，也不需要时间轴拖来拖去。

说白了，这是一个“写代码出视频”的管线。以前可能要前端工程师 + 动效师 + 剪辑师协作的活儿，现在一个人写前端动画，就能把最终视频跑出来。

# 02

**最牛的设计：它是为 AI 智能体量身定做的**

如果说光是 HTML 渲染视频，市面也有一些实验性项目。HyperFrames 真正让我眼前一亮的地方，是它打包了一套完整的“技能”（skills），专门喂给 Claude Code、Cursor、Gemini CLI、Codex 这些 AI 编程智能体。

你都不用亲自写 HTML。直接告诉 AI 你想要什么画面，智能体会自动调用 HyperFrames 的规范，生成一段带 GSAP 动画的 HTML，然后你一条命令渲染出视频。

我试了一下在 Claude Code 里装它的 skill。装完以后，终端里多了几个斜杠命令：

```
/hyperframes
```

 写画面，

```
/hyperframes-cli
```

 走预览和渲染流程，

```
/gsap
```

 专门处理时间线动画。而且它把 Tailwind v4 在浏览器运行时的写法、GSAP 的时间线结构、各个动画库的适配器都约束好了，AI 写出来的代码基本就是可渲染的。这个设计真挺聪明。

相当于它给了 AI 一个“视频语言”。模型理解了怎么用 HTML 去讲故事，而不是凭空猜视频怎么剪。

# 03

**快速上手：两行命令跑起来**

想自己玩一下的话，装它的 skill 是最快的。

```
npx skills add heygen-com/hyperframes
```

这行命令会把你正在用的 AI 编程智能体（Claude Code、Cursor 之类）教会怎么写 HyperFrames 画面。之后在对话里描述视频内容就行。

如果不用 AI 手写，也可以直接跑它的脚手架：

```
npx hyperframes init my-video
```

初始化一个项目，然后写 HTML，最后：

```
npx hyperframes render
```

视频就出来了。

我随手让 Claude Code 生成了一段 10 秒的产品宣传片段，从提示词到渲染完成，前后不超过 5 分钟。虽然不是大片级别，但节奏和转场已经有了短视频的雏形。

# 04

**为什么我觉得这个方向选得很准**

视频生产一直是个重活儿。剪映、CapCut 这些工具把门槛降到了移动端，但仍然需要人去一点点操作。现在 AI 智能体的能力正在从“写代码”向“操控世界”延伸，HyperFrames 等于给智能体在视频领域开了一条直达通路。

未来可能出现这种场景：一个自动化的运营智能体，直接读取产品数据，生成一条适配不同尺寸的推广视频，渲染、发布一气呵成，中间不用人碰一下。HeyGen 本身做数字人视频就已经很成熟了，现在把底层渲染能力开源，背后的逻辑很清晰——让开发者社区一起搭这个“AI 视频工厂”。

开源地址：https://github.com/heygen-com/hyperframes

# 05

**点击下方卡片，关注MinimaxClaw**

**[OpenAI 悄悄开源 CLI，一天就 365 Star，终端党的春天来了？](https://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg1Nw==&mid=2247484038&idx=1&sn=93a06ff78d21ad93843c8c2d450583f2&scene=21#wechat_redirect)**

**[49 万 Star！从零造轮子，这个 GitHub 仓库太香了](https://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg1Nw==&mid=2247484018&idx=1&sn=da016a5c6f93b0d1b8a0ef98aee4d803&scene=21#wechat_redirect)**
