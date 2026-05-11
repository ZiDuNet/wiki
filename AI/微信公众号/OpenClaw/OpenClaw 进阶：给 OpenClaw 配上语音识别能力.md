> 📎 来源: [檀勤忠](https://mp.weixin.qq.com/s?__biz=MzYyMzE2MzQ5MQ==&mid=2247484037&idx=1&sn=5dc2f16f6888549f0dbba688ec5d07d9&chksm=fe063845979fe2cc5ced6b2f0725f265f92386c7ccfa449783b485111ff283363241211672b0&mpshare=1&scene=1&srcid=0421G147jQDKfLG4jbk8QHqv&sharer_shareinfo=206156c758528f7ee88d88e34729d0d5&sharer_shareinfo_first=206156c758528f7ee88d88e34729d0d5) | 时间: 2026-04-21 20:28

---

OPENCLAW 进阶系列

让你的 AI 助手能听懂语音

基于 SenseVoice 的实时语音识别实战

今天，我们要更进一步 —— 让 AI 听懂 用户说的话。

 本文将详细介绍如何集成 **SenseVoice**（阿里开源的多语言语音识别模型），为你的 OpenClaw 工作流添加语音识别能力。

一、ASR 项目选型对比

 在选择语音识别方案之前，让我们对比五个主流的 ASR（自动语音识别）项目：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 项目 | 厂商 | 开源 | 中文支持 | 实时性 |
| SenseVoice | 阿里 | 完全开源 | 极佳 | 实时 |
| Whisper | OpenAI | 开源 | 良好 | 较慢 |
| FunASR | 阿里 | 开源 | 极佳 | 实时 |
| DeepSpeech | Mozilla | 开源 | 一般 | 实时 |
| 讯飞语音 | 科大讯飞 | 商业 | 极佳 | 实时 |

为什么选 SenseVoice？

✓**多语言支持** — 支持中文、英文、粤语、日语、韩语等 50+ 语言

✓**自动检测** — 无需预先指定语言类型

✓**极速识别** — 本地部署，实时转写，支持流式识别

✓**开源免费** — 完全开源，可本地部署，支持商业用途

✓**精准度高** — 在多个基准测试中达到 SOTA 水平

二、架构设计

 完整的语音处理流程：

 用户语音(QQBot) → SILK格式转换 → SenseVoice识别 → OpenClaw处理

三、实战部署

**1. 环境准备**

 pip install funasr modelscope

 python -c "from modelscope import snapshot\_download; snapshot\_download('iic/SenseVoiceSmall', local\_dir='./sensevoice')"

**2. 核心代码**

 from funasr import AutoModel

 model = AutoModel(model="./sensevoice")
 result = model.generate(input="audio.wav")

四、性能基准测试

|  |  |  |  |
| --- | --- | --- | --- |
| 项目 | WER(错误率) | RTF(实时率) | 内存占用 |
| SenseVoice-Small | 4.2% | 0.05 | 1.2GB |
| Whisper-base | 8.5% | 0.8 | 1.0GB |
| FunASR | 3.8% | 0.03 | 1.5GB |

*说明：WER 越低越好，RTF 越低越好（<1 表示实时）*

五、总结

 通过集成 SenseVoice，我们让 OpenClaw/OpenCode 具备了：

✓**听懂用户** — 实时语音识别

✓**多语言支持** — 50+ 语言自动识别

✓**自然交互** — 语音对话，解放双手

✓**场景丰富** — 会议记录、语音指令、实时翻译

**完整的人机语音交互闭环：**
听 — SenseVoice 语音识别
想 — OpenClaw AI 处理
说 — TTS 语音合成

— 本文代码已开源，欢迎 Star 和 PR —

作者: 老坛 | 更新时间: 2026-04-06
