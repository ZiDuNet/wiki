---
tags: [synthesis, Skills, 精选推荐]
sources:
  - 分享6个宝藏Skills.md
  - 10 个顶级 Claude Code Skills，装上就删不掉！附真实使用场景和效果对比.md
  - 假期结束，打工人上线：5 个做 PPT 的 AI 工具skill，按场景选就够了.md
  - Skills商店来了：5w+人在用的热门Skills，我试了一遍.md
  - AI大神开源的宝藏技能合集.md
  - 5个让Hermes-AI脱胎换颈的skills用过就回不去了.md
  - 每日skill系列之项目经理工作流.md
  - AI时代高效开发的skill技能.md
  - 47个产品经理的skills这1个要单独评测否则再好的skill也会退化.md
  - 写 SKILL.md 总是卡住？这 5 Skill 设计模式能救你.md
  - 太多 Skills 管理麻烦？不妨试试这款开源的客户端工具.md
  - Harness 实践：让 Agent 自动制作知识讲解视频.md
created: 2026-05-10
updated: 2026-05-10
---

# Skills 精选

从 530+ 篇微信公众号文章中提炼的高价值 Skill 推荐，按使用场景分类，每个都经过社区实测验证。

---

## 一、开发工程类

### 1. Superpowers（必装）

**安装：** `npx skills add obra/superpowers`
**Star：** 42,000+
**核心价值：** 把 Claude 从"写代码工具"升级为"工程教练"，覆盖规划、TDD、调试、代码审查、并行开发等 20+ 场景

包含子 Skills：

| Skill | 用途 | 适用场景 |
|-------|------|----------|
| `brainstorming` | 动手前先头脑风暴 | 新功能、架构决策 |
| `writing-plans` | 把复杂任务拆成可执行计划 | 多文件功能开发 |
| `executing-plans` | 按计划精准执行 | 计划落地 |
| `test-driven-development` | TDD 工作流 | 核心模块高覆盖 |
| `systematic-debugging` | 结构化调试 | 线上 bug、诡异问题 |
| `requesting-code-review` | 5 个 Agent 并行审查 | 推 PR 前 |
| `dispatching-parallel-agents` | 多任务并行 | 跨模块批量改动 |
| `verification-before-completion` | 完工前检查清单 | 任何"完成"声明前 |
| `using-git-worktrees` | 分支隔离 | 并行功能开发 |
| `receiving-code-review` | 接收 code review 反馈 | 修改代码前先看建议 |

### 2. Blueprint

**核心价值：** 一键生成高质量 Plan，比原生 Plan Mode 更注重 grounded questions 和可执行计划
**适用场景：** 大型重构、多步软件开发、模糊大任务拆解
**特点：** 充当 "Manager + Specialist" 桥接，提升成功率约 3 倍

### 3. Excalidraw Diagram

**安装：** `npx skills add excalidraw-diagram`
**核心价值：** 自动生成架构图、流程图
**适用场景：** 需要图示的技术方案、架构文档

### 4. Skill-Graphs

**核心价值：** 生成知识图谱和关系图
**适用场景：** 项目文档、知识体系可视化

---

## 二、UI/设计类

### 5. UI-UX-Pro-Max（强烈推荐）

**安装：** `npx skills add nextlevelbuilder/ui-ux-pro-max-skill`
**核心价值：** 让 AI 像专业设计师思考，避免"AI slop"（千篇一律的灰色卡片布局）
**特点：** 67 种风格、96 种配色、56 种字体搭配、25 种图表、13 种技术栈支持
**适用场景：** Landing Page、UI 原型、跨平台一致性设计

### 6. Frontend Design

**核心价值：** 从提示生成生产级 HTML/CSS/React/Tailwind 界面
**支持导出：** HTML/PDF/PPTX
**适用场景：** 快速原型、Vibe Coding

---

## 三、PPT/演示类

### 7. guizang-ppt-skill（演示首选）

**GitHub：** `op7418/guizang-ppt-skill`
**核心价值：** 生成单文件横向滑动杂志风格 HTML 演示稿
**特点：** 10 种布局、5 套主题、WebGL 英雄背景、字体分级
**适用场景：** 线下分享、产品发布、demo day、需要高视觉冲击力的演示

### 8. html-ppt-skill（浏览器演示）

**GitHub：** `lewislulu/html-ppt-skill`
**核心价值：** HTML5 幻灯片方案，浏览器即演示环境
**特点：** 单文件 HTML、离线可用、深色模式、演讲者视图、打印支持
**适用场景：** 内部分享、培训材料、技术演示
**限制：** 如果需要 .pptx 格式则不适用

### 9. huashu-slides（文档转演示）

**GitHub：** `alchaincyf/huashu-skills`
**核心价值：** 已有文档（Word/Markdown/会议纪要）直接转成正式 PPT
**适用场景：** 方案转演示、白皮书变幻灯片、培训稿转 PPT

### 10. PPT Master（真 PPT 格式）

**核心价值：** 生成真正可编辑的 .pptx 文件（不是 HTML）
**适用场景：** 必须交付 PowerPoint 格式的企业场景

---

## 四、内容创作类

### 11. baoyu-skills（内容全家桶，强烈推荐）

**GitHub：** `baoyu-ai/baoyu-skills`
**Star：** 13,000+
**核心价值：** 覆盖公众号运营全流程的 Skill 集合

| 子 Skill | 功能 |
|----------|------|
| `baoyu-imagine` | 多模型 AI 绘图（OpenAI/Google/MiniMax/阿里云） |
| `baoyu-cover-image` | 封面图生成，5 维度自动匹配 |
| `baoyu-post-to-wechat` | 文章一键发布到公众号 |
| `baoyu-image-cards` | 信息图卡片制作 |
| `baoyu-infographic` | 专业信息图 |
| `baoyu-slide-deck` | PPT 制作 |
| `baoyu-comic` | 知识漫画 |
| `baoyu-markdown-to-html` | 格式转换 |
| `baoyu-translate` | 专业长文本翻译（术语一致性） |
| `baoyu-youtube-transcript` | YouTube 字幕下载 |
| `baoyu-x-to-markdown` | 推特内容转文章素材 |

### 12. 卡兹克写作 Skill

**GitHub：** `KKKKhazix/khazix-skills`
**核心价值：** 三年公众号运营方法论蒸馏而成，一键进入写作模式
**适用场景：** 公众号写作、内容创作
**配合使用：** Nano Banana Pro（Gemini 3 Pro 图像生成）

### 13. Remotion Best Practices

**GitHub：** `remotion-dev/skills`
**核心价值：** 用代码做视频的最佳实践
**适用场景：** 代码驱动的视频制作

---

## 五、研究/信息类

### 14. last30days-skill

**核心价值：** 跨 Reddit/X/YouTube/HN/GitHub/TikTok 等抓取最近 30 天热门内容
**特点：** v3 引擎支持智能实体解析、集群合并、跨源比较
**适用场景：** 会议前了解人物/公司动态、热点事件追踪、竞品分析
**使用：** `/last30days [topic]`

### 15. Self-Improving-Agent

**安装：** `npx skills add charon-fan/agent-playbook --skill self-improving-agent`
**核心价值：** 跨会话长期记忆，AI 会记住你的偏好并自我进化
**适用场景：** 长期协作项目、个性化 AI 助手

### 16. SwarmVault（LLM Wiki 知识库）

**安装：** `npx claude-code-skills install swarmvault`
**核心价值：** 基于 Karpathy LLM Wiki 模式的本地知识库
**适用场景：** 个人知识管理、知识库搭建与维护

---

## 六、项目管理类

### 17. PM-Skills（产品经理方法论）

**GitHub：** `热门Skill研究：pm-skills`
**核心价值：** 把顶级 PM 方法论装进 AI
**适用场景：** 需求分析、产品规划、用户故事

### 18. SuperAgent（企业级）

**Star：** 57K
**核心价值：** AI 员工操作系统，支持多角色协作
**适用场景：** 企业级多 Agent 管理

---

## 七、工具/效率类

### 19. aweskill（Skills 管理器）

**核心价值：** 让 AI Agent 自己管理 Skills 的安装和更新
**适用场景：** Skills 太多管不过来时

### 20. acquire-codebase-knowledge

**核心价值：** 快速理解不熟悉的项目代码库
**适用场景：** 接手新项目、Code Review

---

## 安装速查

```bash
# 通用安装命令
npx skills add <GitHub用户名/仓库名>

# 通过 claude-code-skills 目录安装
npx claude-code-skills install <skill名称>

# 在 Claude Code 中使用 /plugins 浏览安装
```

**Skills 搜索平台：** https://skills.sh/

---

## 相关页面

- [[Skills生态全景]] — Skills 完整生态分析
- [[Skill设计模式]] — 如何设计好一个 Skill
- [[Harness框架]] — Skill 的运行载体
- [[Claude-Code]] — Skills 的主要运行环境
- [[Hermes-Agent]] — Skills 的另一个运行环境
- [[OpenClaw]] — 开源 Agent 框架
- [[MCP]] — Model Context Protocol
- [[Superpowers]] — 最受欢迎的 Skill 合集
- [[baoyu-skills]] — 内容创作全家桶
- [[PPT制作]] — PPT 相关 Skill 对比
