> 📎 来源: [JOSS实验室](https://mp.weixin.qq.com/s?__biz=MzkwMDI4NDQzMg==&mid=2247483782&idx=1&sn=6baa4826a3f19db6c5cba5829450e7af&chksm=c1469a1c4e9406069fde0d99a36b46b8dd8665655135fc24e6af97450a2e34d333c4497c9134&mpshare=1&scene=1&srcid=05164u51CLPD0WxuasWf9s8B&sharer_shareinfo=b73f28b7421a743fc3c0484a0be25eb9&sharer_shareinfo_first=b73f28b7421a743fc3c0484a0be25eb9) | 时间: 2026-05-16 17:04

---

**mmx-cli** 是 MiniMax 官方推出的命令行工具，核心理念：一句话，帮你的 AI Agent 助手用上 MiniMax 的全部多模态能力。

**它能做什么？**

- 视频生成 — Hailuo 2.3，文字描述转视频
- 音乐生成 — Music 2.6，支持歌词和纯音乐
- 图片生成 — Image 01，文生图，支持批量
- 语音合成 — Speech 2.8，多音色 TTS
- 文本对话 — 多轮对话、流式输出
- 视觉理解 — 图理解，描述图片内容
- 网络检索 — 内置搜索能力

**安装只需三步**

第一步，全局安装 CLI：

```
npm install -g mmx-cli
```

第二步，登录并配置 API Key（Token Plan 用户）：

```
mmx auth login --api-key 你的Key
```

第三步，安装官方 SKILL（Agent 用户推荐）：

```
npx skills add MiniMax-AI/cli -y -g
```

验证是否成功：

```
mmx quota
```

**基本用法**

生成图片：

```
mmx image "赛博朋克风格的城市夜景，16:9"
```

生成视频：

```
mmx video generate --prompt "夕阳下，一只猫坐在窗边望向远方"
```

语音合成：

```
mmx speech synthesize --text "欢迎使用 MiniMax" --out voice.mp3
```

音乐生成：

```
mmx music generate --prompt "轻快爵士风格，主题是夏天的海边"
```

**AI Agent 集成**

如果你的 AI 助手是 OpenClaw、Claude Code、Cursor、MaxClaw 等，加装 SKILL 后 Agent 可以直接调用 mmx 的能力，不需要写代码。

把以下提示词发给你的 Agent 即可完成安装：

```
请帮我接入 MiniMax CLI（https://github.com/MiniMax-AI/cli），按以下三步完成安装与配置：

1. 全局安装 CLI：执行 npm install -g mmx-cli
2. 登录并配置 API Key：执行 mmx auth login --api-key 你的Key
3. 安装官方 SKILL：执行 npx skills add MiniMax-AI/cli -y -g

完成后请执行 mmx quota 查看我的 Token Plan 余额，确认整体配置生效。
```

**Token Plan 配额说明**

不同模态消耗不同配额，具体见 MiniMax 官方定价页面。常用配额：

- Image-01：每周 50 张
- Music-2.6：每周 100 首
- Speech-HD：每周 4,000 次
- Hailuo 视频：按次计费

**常见问题**

**登录后仍报 401？**

大概率是 region 没匹配成功。手动指定：

```
mmx config set --key region --value cn    # 国内版
mmx config set --key region --value global  # 海外版
```

确认状态：

```
mmx auth status
```

**总结**

mmx-cli 把 MiniMax 的多模态能力打包成命令行工具，适合：

- 需要 AI 能力的开发者（直接调 CLI）
- 使用 AI Agent 的用户（SKILL 集成）
- 需要自动化图文视频内容的工作流

一句话：让 AI 助手拥有视频、音乐、图片、语音的全套能力。
