> 📎 来源: [墨与端](https://mp.weixin.qq.com/s?__biz=MzYyNDI3NTg1Nw==&mid=2247484093&idx=1&sn=baa468510be96f76b641bc0f585ad34f&chksm=f1a6dcfae7fcbd2c56ee6e6f407031ea66b50f8268e4fb687aa9a7ade49c9586a00c8258e9c9&mpshare=1&scene=1&srcid=0425MHxxWoQQqPPLnMolV7AA&sharer_shareinfo=5cb50d4bb6ae5ca7bd381cdad5e50a87&sharer_shareinfo_first=5cb50d4bb6ae5ca7bd381cdad5e50a87) | 时间: 2026-04-25 20:13

---

前几天有读者问我：你的龙虾（OpenClaw）能自动剪视频吗？

我说能，但要看装什么 Skill。

他一愣：什么是 Skill？

好问题。今天就来说说这件事，以及我最近挖到的一个 GitHub 上超全的 Skill 宝库。

### 先说 Skill 是什么

你可以把 Skill 理解为 OpenClaw 的"插件"。

OpenClaw 本身是个通用的 AI 助手，会聊天、会读文件、会写代码。但你要让它干点专业的事——比如剪视频、发公众号、管日历——光靠它自己不够，得给它装对应的 Skill。

装上 Skill 的 OpenClaw，就像手机装上了专业 App。基础版只能打电话，装了地图 App 才能导航，装了美团才能点外卖。

**Skill 就是 AI 助手的外挂能力包。**

### 我挖到的这个宝库

在 GitHub 上有一个叫 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) 的项目，目前 **46,959 颗星**，收录了 **5,400+** 个经过筛选的 Skill，分为 30 个大类。

官方 ClawHub 上一共有 13,729 个社区技能，这个列表帮你过滤掉了垃圾内容、重复项、低质量描述和可疑项目，最后剩下 5,211 个精挑细选的可用 Skill。

说它是 OpenClaw 的"技能商店"不为过。

### 视频剪辑相关的，有这几个能打

从列表里筛出视频相关的，直接能用的：

**🎬 ai-video-gen**

端到端 AI 视频生成 Skill。输入一段文字，它自动：

1. 调用 DALL-E 3 / Stable Diffusion 生成图片帧

2. 调用 LumaAI / Runway 把图片合成视频

3. 调用 OpenAI TTS / ElevenLabs 生成配音

4. 调用 FFmpeg 把画面和音频组装成最终 MP4

一条命令，文本进去，视频出来。

不过这个 Skill 被 OpenClaw 官方标记为"Suspicious"（可疑），原因是第三方 Skill 没有经过完整审计。安装前建议自己看看源码，确认没问题再用。

**🎞️ ai-video-remix**

本地素材 AI 混剪。你本地有一堆视频片段，告诉它主题和风格，它自动选片段、拼接、加转场，出一套混剪成品。

**📥 download-tools**

YouTube 和微信视频下载工具。素材不会自己飞来，先下到本地，才能喂给剪辑 Skill。

**🎙️ elevenlabs-tts**

高质量语音合成。18 种角色、32 种语言，配音用它比系统 TTS 自然很多。

### 怎么装

最简单的方式——把仓库链接直接发给 OpenClaw，让它自己处理：

```
帮我安装 ai-video-gen 这个 Skill
```

它会自动识别、安装、配置环境变量，一条龙搞定。

或者用命令行：

```
clawhub install ai-video-gen
openclaw skills install ai-video-gen
```

手动安装的话，把 Skill 文件夹丢到

```
~/.openclaw/skills/
```

 目录下即可。

### 重点说说 ai-video-gen 的实际流程

举个工作流例子：

你告诉 OpenClaw："帮我生成一个 10 秒的科技风开场视频，配上旁白说'欢迎来到未来'。"

它会这样执行：

1. **生成图片帧** → 调用 DALL-E 3 根据提示词出图

2. **合成视频** → 调用 LumaAI Dream Machine 把图片变成视频片段

3. **生成配音** → 调用 ElevenLabs 合成旁白音频

4. **组装输出** → FFmpeg 合并音视频，输出最终 MP4

整个过程你就在旁边看着它干活，不需要打开任何软件，不需要手动操作。

### 但我要泼一盆冷水

这些 Skill 目前有几个现实问题：

**质量不稳定。** AI 生成视频的能力还没那么成熟，出来的效果有时候会比较"假"，离商用水平还有距离。

**成本不低。** LumaAI、Runway、ElevenLabs 都是付费服务，跑一个视频可能要几块钱。不适合大批量生产。

**中文支持一般。** 配音 TTS 对中文的支持目前不如英文，部分 Skill 的中文效果比较机械。

**第三方 Skill 有风险。** 刚才说了，不是每个 Skill 都经过完整审计。装之前看一眼源码，有条件的跑一下 VirusTotal，是对自己负责。

### 我的判断

这些视频 Skill 目前更适合：探索尝鲜、验证创意方向、做内部演示素材。

真正要生产内容，OpenStoryline 的路线更成熟——它是先有素材再有 AI 加工，而不是纯 AI 从零生成。

两者可以结合：用 download-tools 下素材 → OpenStoryline 剪辑精修 → elevenlabs-tts 配音。

一条完整的 AI 视频流水线。

工具在进化，速度比我们想象的快。

\*作者：AI小2\*
