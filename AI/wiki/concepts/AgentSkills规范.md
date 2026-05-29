---
type: concept
created: 2026-05-29
updated: 2026-05-29
---

# AgentSkills规范

AI Agent 技能的标准化规范，实现跨平台 Skill 兼容。

## 定义

AgentSkills 是一套 AI Agent 技能编写和组织的标准规范，使得 Skill 可以无缝接入不同的 AI 编码助手平台。

## 核心要素

- **SKILL.md** — 入口文件，定义触发条件、工具表、步骤与提示词映射
- **prompts/** — 分步模板，Agent 按步骤读取执行
- **tools/** — 工具集，支持特定功能实现
- **标准化结构** — 目录组织、文件命名规范

## 支持平台

- [[Claude Code]] — `.claude/skills/` 目录
- [[Cursor]] — skills 路径 + Settings → Rules
- [[OpenClaw]] — 兼容 AgentSkills 规范
- [[Codex]] — 支持 AgentSkills
- 其他遵循规范的 AI Agent 平台

## 代表项目

- [[patent-disclosure-skill]] — 716 Star，中国专利交底书自动化
- [[agent-skills]] — 37.9k Star，AI Agent 工程纪律

## 规范价值

1. **跨平台兼容** — 一套 Skill 多平台使用
2. **标准化交付** — 统一的目录结构和文件命名
3. **可复用** — Skill 可分享、可复用、可组合
4. **可维护** — 清晰的组织结构便于维护更新

## Skill 安装方式

```
# Claude Code
git clone https://github.com/user/skill-name.git ~/.claude/skills/skill-name

# Cursor
放到 skills 路径，重启后在 Settings → Rules 确认

# SkillHub
npx skills add skill-name
```

## 相关概念

- [[Agent Skills]]
- [[技术交底书自动化]]
- [[Skill生态]]

## 相关实体

- [[patent-disclosure-skill]]
- [[agent-skills]]
- [[Claude Code]]
- [[Cursor]]
- [[OpenClaw]]
- [[SkillHub]]

## 来源文章

- [[ai帮我写专利交底书这个716星技能做到了]]
- [[37.9k-Star-agent-skills-AI-Agent-工程纪律]]