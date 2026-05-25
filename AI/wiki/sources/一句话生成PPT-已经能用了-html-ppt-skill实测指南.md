---
tags: [html-ppt-skill, PPT, AI生成, HTML幻灯片, 静态网站]
sources: [AI生成PPT方案/一句话生成PPT，已经能用了：html-ppt-skill实测指南.md]
created: 2026-05-25
updated: 2026-05-25
---

# 一句话生成PPT，已经能用了：html-ppt-skill实测指南

**来源：** AI生成PPT方案/一句话生成PPT，已经能用了：html-ppt-skill实测指南.md
**摄入日期：** 2026-05-25
**类型：** 实测指南

## 摘要

本文实测 html-ppt-skill 在 Windows 环境下的安装和使用。当前覆盖场景已不算窄：技术分享、融资路演、小红书图文都能落地。核心价值是把 PPT 从人工排版对象推进成 AI 可调度的视觉输出能力。输出为普通 HTML/CSS/JS，零额外编译流程，对 AI Agent 友好。

## 核心观点

- **核心价值**：PPT 从人工操作对象变成 AI 可直接调度的能力模块，把"怎么做一页 PPT"变成"这一页要不要这样表达"
- **36套主题 + 31种布局 + 14套deck模板 + 47种动画效果**
- **输出格式**：普通 HTML/CSS/JS，无额外编译流程，浏览器是最成熟跨平台视觉输出系统
- **AI Agent 接口感**：用户丢进来一句需求，系统先吐出第一版，再由人做判断和细修
- **三组测试验证**：技术分享deck（cyberpunk主题）、Pitch Deck（融资路演）、小红书图文（9张白底柔和风）
- **安装要点**：离线包安装、本地压缩包比在线克隆更稳、Windows路径适配、生成结果统一复制到桌面
- **适合三类人**：需要快速出技术分享稿、把文字提纲变完整deck、做多页图文内容的人

## html-ppt-skill 结构

- `assets/`：字体、基础样式、主题和运行时脚本
- `templates/`：布局模板和完整 deck 模板
- `references/`：主题说明、模板说明和写作约束
- `scripts/render.sh`：HTML 渲染成 PNG

## 触发示例

- "做一份 8 页技术分享 slides，用 cyberpunk 主题"
- "turn this outline into a pitch deck"
- "做一个小红书图文，9 张，白底柔和风"

## 测试成果

| 测试 | 模板 | 主题 | 成果 |
| --- | --- | --- | --- |
| 技术分享deck | tech-sharing | cyberpunk-neon | 8页 HTML |
| Pitch Deck | pitch-deck | pitch-deck-vc | 完整路演 deck |
| 小红书图文 | xhs-post | xiaohongshu-white | 9张白底图文 |

## 涉及实体

- [[html-ppt-skill]] — GitHub 开源项目，HTML 格式 PPT 生成技能
- [[WorkBuddy]] — 腾讯 AI Agent，html-ppt-skill 可作为 Skill 被调用
- [[Claude Code]] — AI 编程工具，可通过 MCP 调用 html-ppt-skill

## 涉及概念

- [[AI生成PPT]] — 从人工排版到 AI 调度的转变
- [[HTML幻灯片]] — 用 HTML/CSS/JS 替代传统 PPT 格式
- [[AIGC工作流]] — AI 直接输出可预览的视觉产物
- [[Software-3.0]] — Karpathy 提出的自然语言承担编程接口角色

## 相关链接

- GitHub：https://github.com/lewislulu/html-ppt-skill