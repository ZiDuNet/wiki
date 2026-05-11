> 📎 来源: [AIGC聊聊智晓](https://mp.weixin.qq.com/s?__biz=MzUyMjQ2ODg5Mg==&mid=2247484119&idx=1&sn=a77155000fad2d3fccfd059246cd4b0c&chksm=f88bae1f3cd96be44627e789d773b287e00fa073ed4b06273ce4fdc1434f8203137d0e90e7d9&mpshare=1&scene=1&srcid=0424MpiqVotDes0yU2uMgJhb&sharer_shareinfo=d02b390447897fab6dbac2cf4190a850&sharer_shareinfo_first=d02b390447897fab6dbac2cf4190a850) | 时间: 2026-04-24 15:15

---

`# 自动选择风格和布局
/baoyu-xhs-images posts/ai-future/article.md

# 指定风格（notion 极简风）
/baoyu-xhs-images posts/ai-future/article.md --style notion

# 指定布局（知识卡片风格）
/baoyu-xhs-images posts/ai-future/article.md --layout dense

# 覆盖配色（马卡龙色）
/baoyu-xhs-images posts/ai-future/article.md --palette macaron

# 非交互模式（定时任务用）
/baoyu-xhs-images posts/ai-future/article.md --yes --preset knowledge-card
`

**12种风格**：cute（默认可爱风）、fresh（小清新）、warm（暖调）、bold（大胆）、minimal（极简）、retro（复古）、pop（波普）、notion（Notion风）、chalkboard（黑板风）、study-notes（学习笔记）、screen-print（丝网印刷）、sketch-notes（手绘草图）

**6种布局**：sparse（封面/金句）、balanced（常规内容）、dense（知识卡片）、list（清单/排行）、comparison（对比）、flow（流程/时间线）

### 专业信息图：21种布局 × 17种风格

做 PPT 汇报、产品介绍、行业分析最头疼的是什么？找模板。

baoyu-infographic 让你用一行命令生成专业级信息图。21 种布局覆盖几乎所有场景：

17 种视觉风格从手绘纸艺（craft-handmade）到赛博霓虹（cyberpunk-neon），从乐高积木（lego-brick）到宜家说明书（ikea-manual），应有尽有。

```
# 根据内容自动推荐/baoyu-infographic path/to/content.md# 指定布局和风格/baoyu-infographic path/to/content.md --layout funnel --style corporate-memphis# 指定比例/baoyu-infographic path/to/content.md --aspect portrait
```

### SVG 图表：Claude 直接手写代码

这是我个人最喜欢的一个技能。

baoyu-diagram 不同于那些调用图像生成 API 的工具——它让 Claude **直接手写 SVG 代码**。这意味着：

```
# 流程图/baoyu-diagram "JWT 认证流程" --type flowchart# 时序图（谁和谁通信）/baoyu-diagram "OAuth 2.0 流程" --type sequence# 架构图/baoyu-diagram "Kubernetes 架构" --type structural# 输出到文件/baoyu-diagram "微服务架构" --lang zh --out docs/arch.svg
```

### PPT 幻灯片：自动生成 + 自动合并

再也不用对着空白 PPT 模板发呆：

```
# 从 Markdown 文章生成幻灯片/baoyu-slide-deck path/to/article.md --slides 15# 指定风格（蓝图风/白板风/企业风/像素风...）/baoyu-slide-deck path/to/article.md --style corporate# 指定受众/baoyu-slide-deck path/to/article.md --audience executives# 仅生成大纲（先看结构再生成图片）/baoyu-slide-deck path/to/article.md --outline-only
```

生成后自动合并为 `.pptx` 和 `.pdf`，直接拿去演示。

### 微信公众号发布：API 模式，快到飞起

终于不用手动复制粘贴了！

```
# 贴图模式（多图配短文）/baoyu-post-to-wechat 贴图 --markdown article.md --images ./photos/# 文章模式（完整富文本）/baoyu-post-to-wechat 文章 --markdown article.md --theme grace# API 方式发布（需配置 AppID/AppSecret）# 或浏览器方式（扫码登录，无需配置）
```

支持多账号管理，一个配置管理多个公众号。

---

## 安装方式

### 方式一：通过 ClawHub 安装（推荐）

每个技能都可以独立安装：

```
clawhub install baoyu-xhs-imagesclawhub install baoyu-infographicclawhub install baoyu-diagram# ...按需安装
```

### 方式二：通过 Claude Code Marketplace

在 Claude Code 中运行：

```
/plugin marketplace add JimLiu/baoyu-skills
```

然后在插件市场选择安装即可。

### 方式三：直接告诉 AI

> 请帮我安装 github.com/JimLiu/baoyu-skills 中的 Skills

---

## 为什么推荐这个项目？

**第一，视觉内容质量高。** 不同于简单的 AI 图像生成，这些技能有精心设计的设计系统和风格规范，生成的图片有统一的视觉语言，不是随机堆砌。

**第二，覆盖全链路。** 从内容创作 → 配图生成 → 排版美化 → 多平台发布，一条龙搞定。尤其是 SVG 图表和 PPT 生成，解决了创作者最耗时的问题。

**第三，更新活跃。** 14.7k Stars，11 小时前还在更新，说明作者在认真维护，不是一个「摆烂」的仓库。

**第四，完全开源免费。** MIT-0 协议，发布到 ClawHub 的技能可以免费使用。

---

## 结语

baoyu-skills 是那种「用了就回不去」的工具。它不替代你的创作工作，而是把那些繁琐的、重复的、机械的工作自动化——让你把精力放在真正有价值的部分：内容本身。

GitHub 地址：github.com/JimLiu/baoyu-skills[1]

有兴趣的朋友可以 clone 下来试试，有问题可以在 GitHub 提 Issue。

---

### 引用链接
