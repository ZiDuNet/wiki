# lanshu-awesome-ai-video-kit

> 做企业 AI 视频项目逼出来的开源工具包 · 431 prompt · 15 模型 · 7 Claude Skill · 16 篇方法论

- **GitHub**: https://github.com/cclank/lanshu-awesome-ai-video-kit
- **作者**: @lanshu (cclank)
- **License**: MIT
- **版本**: v0.9.0 (2026-05)

## 一句话介绍

企业级 AI 视频制作工具包，431 条实测 Prompt 覆盖 15 个模型（11 商业 + 4 开源），含 16 篇方法论 SOP、7 个 Claude Code Skill、3 个 Web 工具，GitHub Action 每周自动巡检 32 个端点。

## 核心数据

| 资源 | 数量 | 说明 |
|------|------|------|
| 实测 Prompt | 431 条 | 321 条单模型最佳实践 + 110 条跨模型对照矩阵 |
| AI 视频模型 | 15 个 | 11 商业旗舰 + 4 开源 |
| 方法论 SOP | 16 篇 | 基础公式 → 导演级写作框架 |
| Claude Code Skill | 7 个 | 一行命令安装 |
| Web 工具 | 3 个 | 零依赖单文件 HTML，开箱即用 |
| 监控端点 | 32 个 | 每周一自动巡检 |

## 覆盖的 15 个模型

**商业模型 (11)**: Seedance 2.0 ⭐、Kling 3.0、Veo 3.1、Sora 2 (⚠️已停服)、HappyHorse 1.0、Runway Gen-4.5、Pika 2.5、Hailuo 02、Hunyuan Video 1.5、Wan 2.7、即梦 AI

**开源模型 (4)**: LTX-Video 0.9.7、Mochi 1、CogVideoX、Higgsfield Soul

## 7 个 Claude Code Skill

| Skill | 功能 |
|-------|------|
| ★ model-selector | 15 模型购物顾问，推荐 1-3 个模型 |
| ★ prompt-translator | 跨模型 Prompt 转换（110 条基准） |
| seedance-prompter | Seedance 8 要素结构化 prompt |
| seedance-storyboard | 剧情拆分镜 |
| seedance-debugger | Prompt 诊断 + 修复 |
| happyhorse-prompter | 紧凑短片 prompt |
| kling-prompter | 可灵三套写法 |

## 快速上手

```bash
git clone https://github.com/cclank/lanshu-awesome-ai-video-kit
cd lanshu-awesome-ai-video-kit
python3 serve.py 8000
# 浏览器打开 http://localhost:8000/
```

## 项目亮点

- 每条 Prompt 带 `source` 字段链接官方文档，来源可追溯
- GitHub Action 每周一巡检 32 个端点，版本变化自动开 Issue
- 每个模型按官方公式独立收录，不做大杂烩
- 16 篇方法论从入门到导演级完整路径
- 3 个 Web 工具：Prompt Browser、Cross-Model Matrix、Markdown Viewer

## 来源

- 微信公众号文章：[这个GitHub开源工具包，把15个AI视频模型一网打尽了](https://mp.weixin.qq.com/s/58rswsiOQUAdyMYPMSFL3g)
