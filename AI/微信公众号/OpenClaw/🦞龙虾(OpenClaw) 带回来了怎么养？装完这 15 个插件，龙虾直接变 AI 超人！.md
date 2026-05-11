> 📎 来源: [码上炼AI](https://mp.weixin.qq.com/s?__biz=Mzk3NTA2NzIwMA==&mid=2247484041&idx=1&sn=60b9731c020a78d5c13911d6d68ee81f&chksm=c5e5a26b43686ac27fccafbc9a98faef75a8c1e695ec12908a4e8fd255ea1e3a5e782a827545&mpshare=1&scene=1&srcid=04209gQYa5dhr6AmwSbbB8Z6&sharer_shareinfo=a81d1875057703fa7fc311d6ebde86b0&sharer_shareinfo_first=a81d1875057703fa7fc311d6ebde86b0) | 时间: 2026-04-20 20:27

---

OpenClaw🦞 就像一台手机，SKILL 就是上面装的 APP。每装一个，AI 就多一项本事。所有 SKILL 都能在 clawhub.ai 免费找到，一键安装，想用哪个装哪个。本文将带你安装15个重要的skill，让你的龙虾🦞助手更聪明地为你服务。

---

## 下面将这 15 个 skill 按照类别分为新手入门套装、文档处理、AI创作、开发者效率、安全保障以及日历管理六个类别进行介绍。

### 新手入门套装

#### 01. find-skills｜技能搜索助手

**什么时候用**：不知道有什么插件可用时

跟 AI 说"我想管理日程"、"有没有能搜 Reddit 的插件"，它会自动去 ClawHub 搜索匹配的 SKILL，给出安装建议。相当于给 AI 装了个"应用商店搜索"功能，不用自己翻目录。

**适合谁**：刚接触 OpenClaw，不知道从何入手的新手

```
clawhub install find-skills
```

🔗 clawhub.ai/steipete/find-skills

---

#### 02. summarize｜内容摘要生成器

**什么时候用**：遇到长文/长视频不想看完时

丢给它一个链接——不管是公众号文章、YouTube 视频、PDF 文档还是音频文件，它能快速输出核心要点摘要。

**我的用法**：先让它总结，判断值得细读再深入阅读，省时间。

**支持格式**：网页链接、PDF、音频、视频、图片（OCR）

```
clawhub install summarize
```

🔗 clawhub.ai/steipete/summarize

---

#### 03. openai-whisper｜本地语音转文字

**什么时候用**：会议录音整理、视频字幕提取

基于 OpenAI Whisper 的本地部署版本，音频/视频里的语音直接转成文字稿。完全本地运行，不上传数据，不需要 API 费用。

**我常用它**：整理采访录音和会议记录，准确率很高，方言也能识别个七七八八。

**支持格式**：mp3、wav、m4a、mp4、mov 等主流格式

```
clawhub install openai-whisper
```

🔗 clawhub.ai/steipete/openai-whisper

---

#### 04. memory-setup｜持久记忆配置

**什么时候用**：希望 AI 记住你的偏好和习惯

原生 AI 每次对话都是"失忆状态"，这个 SKILL 帮它配置长期记忆系统——你的工作习惯、常用术语、历史决策、重要偏好，它都能记住。

配置之后，AI 从"每次初见"变成"老搭档"，越用越顺手。

**记忆内容**：工作习惯、专业术语、决策偏好、重要日期等

```
clawhub install memory-setup
```

🔗 clawhub.ai/jrbobbyhansen-pixel/memory-setup

---

#### 05. proactive-agent｜主动代理助手

**什么时候用**：希望 AI 主动提醒而不是被动等待

默认 AI 是你问它才答。装上这个，它学会主动预判——定时巡检、重要事项提前提醒、上下文意外中断能自动恢复。

从"问答工具"升级成"主动助理"，就差这个插件。

**主动能力**：定时巡检、主动提醒、上下文恢复、习惯学习

```
clawhub install proactive-agent
```

🔗 clawhub.ai/halthelobster/proactive-agent

---

### 📁 文档处理三剑客

#### 06. nano-pdf｜PDF 编辑工具

**什么时候用**：需要修改 PDF 内容时

跟 AI 说"把第 3 页标题改成 XXX"、"在第 2 页加一段说明"，它直接帮你改好。PDF 不再是只读文件，不需要打开 Adobe Acrobat 记复杂操作。

**核心功能**：文字修改、页面增删、页面提取、多文件合并

```
clawhub install nano-pdf
```

🔗 clawhub.ai/steipete/nano-pdf

---

#### 07. markdown-converter｜格式转换神器

**什么时候用**：收到各种格式文件需要统一处理时

Word、Excel、PPT、PDF、HTML、图片、音频……各种格式一键转成 Markdown，方便 AI 统一处理。不管收到什么格式的文件，都能直接"喂"给 AI 分析。

**转换能力**：

- 办公文档：DOCX、XLSX、PPTX → Markdown
- 网页内容：HTML → Markdown
- 多媒体：图片 OCR、音频转写 → Markdown
- ```
  clawhub install markdown-converter
  ```

🔗 clawhub.ai/steipete/markdown-converter

---

#### 08. video-frames｜视频帧提取

**什么时候用**：做视频内容分析或素材剪辑时

基于 ffmpeg，从视频里提取关键帧或指定片段。做内容分析不用一帧帧截图，做素材剪辑能快速拿到关键画面。

```
clawhub install video-frames
```

🔗 clawhub.ai/steipete/video-frames

**常用命令**：

```
/video-frames tutorial.mp4 --interval 10s    # 每 10 秒提取一帧/video-frames meeting.mp4 --extract-keyframes # 提取关键帧
```

---

### 🎨 AI 创作三剑客

#### 09. nano-banana-pro｜AI 绘画工具

**什么时候用**：需要快速生成图片时

描述你想要的画面，AI 直接生成，支持 1K/2K/4K 多种分辨率。也能基于现有图片二次创作——换背景、加文字、改风格都可以。

不用单独买 Midjourney 订阅，在对话框里就能出图，适合快速出概念图。

**支持功能**：文生图、图生图、图片编辑、风格迁移

```
clawhub install nano-banana-pro
```

🔗 clawhub.ai/steipete/nano-banana-pro

---

#### 10. humanizer｜AI 文本润色

**什么时候用**：AI 生成的文章"AI 味"太重时

专门识别并替换 AI 写作套话——"值得注意的是"、"综上所述"、"不仅……而且……"这类表达，换成更自然的说法。

**我写公众号文章的习惯**：AI 出初稿 → humanizer 过一遍 → 人工微调，效率高很多。

**检测范围**：AI 套话、过度正式表达、重复句式、生硬过渡词

```
clawhub install humanizer
```

🔗 clawhub.ai/biostartechnology/humanizer

---

#### 11. self-improving｜自我进化系统

**什么时候用**：希望 AI 从错误中学习

AI 犯错被你纠正后，自动记录这次经验，建立分层记忆库。下次遇到类似问题，不再犯同样错误。不是靠你反复教，它自己会"长记性"。

**进化机制**：错误记录 → 经验存储 → 自动复习 → 应用优化

```
clawhub install self-improving
```

🔗 clawhub.ai/ivangdavila/self-improving

---

### 💼 开发者效率包

#### 12. github｜开发者助手

**什么时候用**：程序员管理 GitHub 项目时

搜开源项目、查 Issue、看 PR 状态、检查 CI/CD 进度——全在聊天框里完成。开发者不用在浏览器和 IDE 之间来回切换。

**支持操作**：仓库搜索、Issue/PR 管理、CI 状态查询、通知管理

```
clawhub install github
```

🔗 clawhub.ai/steipete/github

---

#### 13. obsidian｜知识库打通

**什么时候用**：用 Obsidian 做知识管理时

如果你用 Obsidian 记笔记，这个 SKILL 让 AI 直接访问你的 Vault——搜索笔记、创建文档、更新内容都能通过对话完成。

"帮我找去年记的关于机器学习的笔记"，它真能找到并总结给你。

**支持功能**：笔记搜索、文档创建/更新、关系图查看、双向链接管理

```
clawhub install obsidian
```

🔗 clawhub.ai/steipete/obsidian

---

### 🔒 安全保障

#### 14. skill-vetter｜安全审查工具

**什么时候用**：安装陌生 SKILL 前

装来路不明的插件前，先让它审查一遍——检查权限配置、分析代码行为、识别潜在风险。相当于给 SKILL 做"背景调查"。

**审查项目**：权限配置、代码行为、网络请求、风险评级

```
clawhub install skill-vetter
```

🔗 clawhub.ai/spclaudehome/skill-vetter

---

### 📅 日历管理

#### 15. macos-calendar｜macOS 日历管理

**什么时候用**：管理 macOS 本地日历（Apple Calendar）

通过 AppleScript 直接操作 macOS 日历应用，纯本地运行，无需联网。

**支持功能**：

- 列出所有日历（区分只读/可写）
- 创建事件（支持标题、时间、时长、提醒、重复事件）

**限制**：目前不支持查询/修改/删除已有事件

```
clawhub install macos-calendar
```

🔗 github.com/lucaperret/agent-skills

---

## 快速上手

安装好的 Skills 无需额外配置，**直接在对话中调用**即可。以下是每个 Skill 的使用示例：

### 新手入门套装

| Skill | 你可以这样说 |
| --- | --- |
| **find-skills** | "我想管理日程，有什么推荐的 skill？" |
| **summarize** | "帮我总结这篇文章：https://example.com/article" |
| **openai-whisper** | "把这个会议录音转成文字：/path/to/recording.mp3" |
| **memory-setup** | "记住我的工作时间是每天 9 点到 6 点" |
| **proactive-agent** | "有重要事情记得主动提醒我" |

### 文档处理三剑客

| Skill | 你可以这样说 |
| --- | --- |
| **nano-pdf** | "把这份 PDF 第 3 页的标题改成'新标题'" |
| **markdown-converter** | "把这个 Word 文档转成 Markdown" |
| **video-frames** | "从这个视频每 10 秒提取一帧：/path/to/video.mp4" |

### AI 创作三剑客

| Skill | 你可以这样说 |
| --- | --- |
| **nano-banana-pro** | "画一只在太空中的猫，4K 分辨率" |
| **humanizer** | "把这段文字润色一下，去掉 AI 味" |
| **self-improving** | （自动工作，无需手动调用） |

### 开发者效率包

| Skill | 你可以这样说 |
| --- | --- |
| **github** | "帮我搜索 GitHub 上最火的 Python 项目" |
| **obsidian** | "帮我找去年记的关于机器学习的笔记" |

### 安全保障

| Skill | 你可以这样说 |
| --- | --- |
| **skill-vetter** | "帮我审查一下 xxx skill 是否安全" |

### 📅 日历管理

| Skill | 你可以这样说 |
| --- | --- |
| **macos-calendar** | "列出我的日历" / "明天下午 3 点创建一个会议" |

> **注意**：macos-calendar 目前支持**列出日历**和**创建事件**，暂不支持查询/修改/删除已有事件。

---

## ⚠️ 注意事项

1. 1. **权限审查**：陌生 SKILL 先用 skill-vetter 审查
2. 2. **依赖检查**：部分 SKILL 需要额外依赖（ffmpeg、node 等）
3. 3. **API 配置**：GitHub、AI 绘画等 SKILL 需要配置 API Key 或 Token
4. 4. **版本兼容**：确保 OpenClaw 版本与 SKILL 兼容
5. 5. **隐私边界**：Obsidian、记忆类等访问本地文件的 SKILL 注意权限范围

---
