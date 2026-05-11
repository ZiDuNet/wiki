---
tags: [Claude, GitHub, API, Skill]
source: "程序员锋仔"
created: 2026-04-21
updated: 2026-05-10
category: Claude
---

# 1. 克隆并链接到Claude Code的技能目录git clone https://github.com/browser-use/video-usecd video-useln -s "$(pwd)" ~/.claude/skills/video-use# 2. 安装依赖pip install -e .brew install ffmpeg # 必需brew install yt-dlp # 可选，用于下载在线资源# 3. 添加你的ElevenLabs API密钥cp .env.example .env$EDITOR .env # ELEVENLABSAPIKEY=...

> 来源: [程序员锋仔](https://mp.weixin.qq.com/s?__biz=MzYzMTA2MDY0Mg==&mid=2247488605&idx=1&sn=06adaa8781e56f094c3c139ea1749798&chksm=f19c0eefd0e1494102130de2801c42dd56eb48c0785ac249878a1ce203c816d56d900e20159a&mpshare=1&scene=1&srcid=0421hZMxcCEBNMPSwZLXm7jp&sharer_shareinfo=f38c36132b18acf8c35e128735675ebf&sharer_shareinfo_first=f38c36132b18acf8c35e128735675ebf) | 2026-04-21

## 摘要

你是否曾想过，如果有一个AI能理解你的视频内容，自动去除冗余，优化音画，甚至添加字幕和动画，那该多好？今天，我要向你介绍一个改变游戏规则的开源项目——  **video-use**  。这个工具让你只需与Claude Code对话，就能将一堆原始素材变成一部专业级的视频作品。
video-use是一个100%开源的视频编辑工具，它通过AI智能处理视频内容，无需复杂的预设和菜单，适用于各种类型的视频内容：
• 自动去除填充词（"嗯"、"啊"、不完整的句子）和镜头间的空白
• 自动调色（电影感暖色调、中性高对比度或自定义ffmpeg滤镜链）
• 每个剪辑点添加30ms音频渐变，避免突兀的爆音
• 烧录字幕（默认为2词大写块，完全可自定义）
• 通过Manim、Remotion或PIL生成动画覆盖层
• 自我评估渲染输出，确保每个剪辑点都完美
• 在project.md中保持会话记忆，下次继续未完成的工作
使用video-use非常简单，只需三个步骤：
然后，将Claude Code指向你的原始素材文件夹：
在会话中，只需简单地说：
Claude会盘点所有素材，提出剪辑策略，等待你的确认，然...

## 相关实体

[[Claude-Code]], [[Claude]], [[GitHub]]

## 相关概念

[[内容创作]]
