> 📎 来源: [极空间私有云](https://mp.weixin.qq.com/s?__biz=MjM5OTM5NTEzNw==&mid=2247571617&idx=1&sn=6829652aa1896eeda1ede8dea4a82c16&chksm=a66b0827301b815110c714aa8a69b723283280bf6848d545223c988485bdf1af4f0b1cdba48b&mpshare=1&scene=1&srcid=0504mEoPAyXTGWyyvHUsi6xf&sharer_shareinfo=2a3e3a54fd0c60feae6556411462c14f&sharer_shareinfo_first=2a3e3a54fd0c60feae6556411462c14f) | 时间: 2026-05-04 20:46

---

各位极友，我是小极君 🎬

谁不想靠 AI 做短剧、赚大钱？但之前的漫剧工具要么烧 token，要么门槛高。今天给大家挖到一个**开源 AI 短剧制作平台 —— ArcReel**。从小说到剧本、角色设计、分镜图，再到视频生成，全流程打通。更关键的是：配合火山引擎的**每日免费额度**，每天能免费 20 张 Seedream 图片 + 4 个 Seedance 视频（5s/个），入门成本几乎为零。

而且还内置了 OpenClaw Skill，让小龙虾也能帮你自动跑视频任务。跟着@可爱的小cherry 一步步教你部署到极空间，开启你的“AI 短剧工作室”。👇👇

**/****/ 风险****提示**

**///**

1. 极空间仅提供支持创建Docker镜像的环境，软件功能与注意事项详见该软件内具体使用规则。
2. 本文仅代表作者观点，使用第三方解决方案，均非官方正式方案，可能会产生相关风险，请自行斟酌。

小伙伴们，之前 cherry 介绍了不少的 AI 漫剧/短剧内容，有用 MiniMax token 额度制作的，有用成熟的短剧平台制作的。

但是唯独没有介绍的，就是白嫖制作 AI 漫剧。

今天给大家介绍一个我认为效果很不错的开源 AI 短剧制作平台 —— ArcReel，采用 AGPL-3.0 license 协议。

该项目支持

```
从小说到视频、说书模式
```

。 是一个 AI Agent 驱动的开源视频生成工作台 — 打通 小说→角色/场景/道具设计→剧本→分镜图→视频，跨镜头角色与场景一致。

而且提供了内置的 OpenClaw Skill ，支持一键接入 OpenClaw ，可以让小龙虾进行视频创作。

![](assets/img_709404d5b91c.png)

先说说免费豆包模型。（其实也可以从豆包APP使用**Seedance**2.0，但是没有平台一致性的保证）

火山引擎里，目前可以开通指定模型每天 200W tokens 的活动。

本教程使用最核心的两个模型，分别是 Seedance-1.5-Pro（视频）、Seedream-4.5（图片）

虽然这俩不是目前的顶级旗舰模型，但是对于 AI 短剧制作入场和初体验，已经完全完全足够了。

开通方法也很简单，注册火山引擎之后，点击左侧的开通管理，先把所有模型一键开通。新账号有 400W 的 **Seedance**-1.5-Pro tokens，以及 200 张 Seedream-4.5 图片额度。

![](assets/img_1a3d6752c6eb.png)

接着点击上方的【领取免费资源包】活动，点击右侧【立即参与】，在字节模型里开通上述提到的两个模型。

每天可以领取的 

```
Doubao-Seedance-2.0-pro
```

（200W），

```
Doubao-Seedance-1.5-pro
```

（200W），

```
Doubao-Seedream-4.5
```

 （20张图片）三个额度。

1 个 5s 视频大约 50W 

```
Seedance-1.5-pro
```

 的用量，相当于每天 4 个视频。

![](assets/img_68c3a8cbf245.png)

---

# **一、ArcReel 制作视频**

## **1.基础配置**

ArcReel 不同于普通的 AI 短剧工作流。

它的底层采用了 Claude Code ，由 Agent + 工作流的双重模式来进行整体创作。

所以在正式启动之前，我们需要配置 Claude Code 以及生图、生视频的模型。

Claude Code 不需要登录账号，仅需要 Anthropic 兼容的 API 就可以接入。

这里推荐使用量大管饱的 MiniMax Token Plan，本身就是 Anthropic 格式的。

![](assets/img_4d5da8e7431e.png)

在 ****设置**** —— ****智能体**** 中，密钥填写你生成的 

```
token
```

，

```
ANTHROPIC_BASE_URL
```

 为 

```
https://api.minimaxi.com/anthropic
```

，所有默认都填写 

```
MiniMax-M2.7
```

。

![](assets/img_da7a1998dab6.png)

接着回到前面的火山引擎，在左侧点击 API Key 管理，创建并复制你的 API Key。

![](assets/img_be9cd648b001.png)

在设置里的第二个供应商里，选择火山方式，填入你的 API Key，然后选择模型。

![](assets/img_0df10458de81.png)

其它还支持 Google、**Grok**、OpenAI 等模型，还有自定义模型端点。

比如我一直在说的阿里百炼平台，90 天的 Wan 以及各种生图模型，免费用量都很不错。

![](assets/img_8f7880e3ac73.png)

最后，切换到模型选择页面。这里配置文本、图片、视频的默认模型。直接按照文章开头里提到的几个来配置就可以。

这个只是默认模型，实际在创作的时候又可以再次选择，所以不是很重要。

![](assets/img_3e576460436d.png)

## **2.制作流程**

完成配置，我们点击顶部的创建项目就可以启动一个工作流。

这里的说书+画面，指的就是我们常用的旁白多的模式。而动画就是普通的 AI 视频。

下面这个分镜生成模式比较重要。宫格生视频，就是一次性生成一张图片里进行宫格区分，同一个提示词可以创建更统一的画面。

![](assets/img_7fe907706dec.png)

ArcReel 内置了大量的 AI 真人/ AI 漫剧风格，这个风格会内置到 ClaudeCode 生成剧本的流程中去，所以很重要。

基于 Doubao-Seedance-1.5-pro 的模型，推荐大家不要选择太复杂或者训练量太少的模型，尽量选择动画、羊毛毡、真人这些训练成熟的风格。

![](assets/img_efee4a69e84a.png)

![](assets/img_fd53baa8b15a.png)

来了，正式的制作环节来了。这是我目前体验下来 ArcReel 最有特色的部分。

可以看到屏幕最左侧，是当前的资产库，里面提供了剧本、场景、道具、人物图片，剧情分集等信息；中间是创作进度条和实际画布，可以看到项目进度；右侧则是和Claude Code 的对话框，通过聊天由 Claude Code 来协助我们推进视频制作。

![](assets/img_306072c7d9fe.png)

首先我们先上传一段话或者小说，ArcReel 会调用文本模型对剧情进行解析，生成一个项目概览。

这个时候直接和 Agent 对话，让它根据项目概述创建人物、场景的提示词信息。创建完成之后，Agent 会进行下一步提醒，建议你进行角色、场景创作。

当然，你也可以根据提示词判断是否要修改。如果没问题，就直接下一步创建。

![](assets/img_efbf9d91cadb.png)

也可以输入 

```
/技能
```

 来调用服务。系统内置了生成分镜、视频、工作流编排器、批量生产资产、合并视频等专门的脚本。

![](assets/img_f91e11cbd491.png)

我统一让 Agent 帮我创建的分集、角色、场景。这里有个小技巧，创建了分集之后，可以让 Agent 先创建最小单集的角色，避免剧本错误导致的免费额度浪费。

![](assets/img_4761c6bb274e.png)

场景也是一样，有具体的描述、大图、细节图。如果你觉得 Agent 生成的不够好，也可以直接复制提示词到其它平台生图，然后在资产库里导入使用。

![](assets/img_1a67dafd7556.png)

每一个步骤完成后，ArcReel 都会详细的记录费用明细、任务进度，在右上角点开就可以看，一目了然。

![](assets/img_b75a48eca6c8.png)

![](assets/img_b39fdebb19e9.png)

调几次分镜，觉得差不多了，直接制作视频。额度就是我刚才说的，5s 大概 50w tokens 左右。

![](assets/img_4163e34877fa.png)

最后，所有的视频都创作完成后。输入指令 

```
/合并视频
```

 ，最终的成稿会输出到 NAS 

```
~/项目地址/projects/项目地址/output
```

 目录下。

![](assets/img_881dcfc21f45.png)

## **3.接入 Openclaw**

要接入 OpenClaw，建议大家在局域网环境下打开 ArcReel。因为极空间客户端走的是 

```
127.0.0.1
```

，实际访问不通的。

回到项目首页，点击右上角的小龙虾图标，这里就是 ArcReel 的 Skills。

里面有一键部署指令（容器内部），点击后就可以打开极空间的文本管理器查看到具体的配置信息。

![](assets/img_5d31fdf12432.png)

然后点击获取 API 令牌，等 OpenClaw 学习完成之后，把令牌复制给它去跑流程。

![](assets/img_bc2f481aad43.png)

OpenClaw 的学习特别快。链接之后，可以看到一共有六个 API 端点，最核心的就是和 Agent 对话来推进制作。

![](assets/img_0088e8c1fce9.png)

具体的效果就不演示了，我个人感觉还是很不错的。内容详细，推进自然。

![](assets/img_0bcc06ae917f.png)

# **二、极空间私有云部署 ArcReel**

打开极空间的 docker 应用，创建一个 compose 项目，然后依次填入下面两个文件。

![](assets/img_f8479c8500d5.png)

🔻 

```
docker-compose.yaml
```

 配置

```
services:  arcreel:    image: ghcr.io/arcreel/arcreel:main    ports:      - "31241:1241"  # 这里左边修改为你想要的端口    env_file: ./.env    volumes:      - ./.env:/app/.env      - ./projects:/app/projects      - ./vertex_keys:/app/vertex_keys      - ./claude_data:/root/.claude    restart: unless-stopped    healthcheck:      test: ["CMD", "curl", "-f", "http://localhost:1241/health"]      interval: 30s      timeout: 5s      retries: 3
```

🔻

```
.env
```

 配置

```
# ============================================================# Authentication / 认证配置# ============================================================# 登录用户名（默认: admin）AUTH_USERNAME=admin# 登录密码（留空则首次启动时自动生成并回写到此文件）AUTH_PASSWORD=# JWT 签名密钥（留空则自动生成，但重启后 token 失效需重新登录）AUTH_TOKEN_SECRET=# ============================================================# Database Configuration / 数据库配置# ============================================================# 默认使用 SQLite（开发/单机）# SQLite:     sqlite+aiosqlite:///./projects/.arcreel.db# PostgreSQL: postgresql+asyncpg://user:pass@host:5432/arcreel# DATABASE_URL=sqlite+aiosqlite:///./projects/.arcreel.db# ============================================================# Logging / 日志配置# ============================================================# 日志级别（默认: INFO，可选: DEBUG, WARNING, ERROR）# LOG_LEVEL=INFO# ============================================================# Video Provider / 视频供应商# ============================================================# 全局默认视频供应商 (gemini | seedance)# DEFAULT_VIDEO_PROVIDER=seedance# ============================================================# Seedance (Volcengine Ark) / Seedance (火山方舟) 配置# ============================================================# Volcengine Ark API key / 火山方舟 API key# ARK_API_KEY=# 项目文件服务公网地址（Seedance 图片上传需要公网访问）# FILE_SERVICE_BASE_URL=
```

部署完成之后，在极空间个人空间里重新打开 

```
.env
```

 文件，这里会回填 

```
AUTH_PASSWORD
```

 就是你的登录密码。

![](assets/img_2ed6ee703a2e.png)

最后创建一个极空间的远程访问服务，添加到桌面快捷方式。随时随地都可以打开进行 AI 短剧制作。

![](assets/img_a10d77e7c5a6.png)

---

# **总结**

世上无难事，只怕有心人。

虽然每天只有 15~20s 的视频制作，但毕竟这是 Seedance-1.5-Pro 模型，某些风格下的制作效果还是相当不错的。

先用 LLMs、生图做好剧情、分镜、宫格图，然后让 OpenClaw 每天晚上跑个定时任务去执行视频制作，你也不用管。

哪天想起来上去看一下最新的状态，遇到有问题的直接现场修复，一个礼拜就可以跑 2 分钟的小短篇，对于 AI 视频初学者理解、调试 AI 视频效果实在是太好了。

![](assets/img_ff7a35de5569.webp)

![](assets/img_784f7a0a8071.gif)

![](assets/img_121c8e073628.gif)
