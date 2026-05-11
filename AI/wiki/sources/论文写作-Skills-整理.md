---
tags: ["AI办公", "Agent开发", "自动化工作流", "GitHub开源项目", "PPT制作"]
sources: ["微信公众号/Skills/论文写作 Skills 整理.md"]
created: 2026-04-23
updated: 2026-05-10
---

# 1. 创建技能目录mkdir -p ~/.claude/skills# 2. 安装核心技能cd ~/.claude/skills# luwill/research-skillsgit clone https://github.com/luwill/research-skills.gitcp -r research-skills/research-proposal .cp -r research-skills/paper-slide-deck .cp -r research-skills/medical-imaging-review .# lishix520/academic-paper-skillsgit clone https://github.com/lishix520/academic-paper-skills.gitcp -r academic-paper-skills/strategist .cp -r academic-paper-skills/composer .# K-Dense-AI/claude-scientific-skillsgit clone https://github.com/K-Dense-AI/claude-scientific-skills.gitcp -r claude-scientific-skills/scientific-skills/scientific-writing .# ndpvt-web/latex-document-skillgit clone https://github.com/ndpvt-web/latex-document-skill.gitcp -r latex-document-skill/skills/* .# 清理rm -rf research-skills academic-paper-skills claude-scientific-skills latex-document-skill

**Source:** 阳哥书房
**Category:** Skills
**Date ingested:** 2026-05-10
**Type:** article

## Summary

今年准备要论文了，整理了下论文写作相关的 Skills，希望能用得上。

## Entities Mentioned

- [[Claude-Code]] — Anthropic 的命令行 AI 编程工具，支持 Skills 系统
- [[Superpowers]] — Jesse Vincent 的软件工程最佳实践 Skills 框架
- [[Anthropic]] — Claude 系列模型的开发商，Agent Skills 标准的提出者
- [[GitHub]] — 代码托管平台，Skills 主要分发渠道
- [[skills-sh]] — Skills 发现和分发平台 skills.sh

## Concepts Covered

- [[Agent开发]]
- [[PPT制作]]
- [[AI办公]]
- [[GitHub开源项目]]
- [[自动化工作流]]
- [[论文写作]]
- [[科研工具]]
- [[分阶段流程]]
